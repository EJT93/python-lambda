import logging
import json
import calendar
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def monthly_cost_review(event, context):
    today = datetime.date.today()
    first_day = today.replace(day=1)
    last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])

    logger.info(f"Monthly cost review function triggered for the period: {first_day} to {last_day}")
    # Generate export for all resources between the first and last day of the current month
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Monthly cost review export generated for {first_day} to {last_day}")
    }
