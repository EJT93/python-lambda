import logging
import json
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def weekly_cost_review(event, context):
    today = datetime.date.today()
    last_sunday = today - datetime.timedelta(days=today.weekday() + 1)  # Last Sunday
    next_saturday = last_sunday + datetime.timedelta(days=6)  # Next Saturday

    logger.info(f"Weekly cost review function triggered for the period: {last_sunday} to {next_saturday}")
    # Generate export for all resources between last Sunday and next Saturday
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Weekly cost review export generated for {last_sunday} to {next_saturday}")
    }
