pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-2' // Specify your AWS region
        S3_BUCKET = 'lambda-code-and-logs' // Specify your S3 bucket name
    }

    stages {
        stage('Zip Files') {
            steps {
                sh 'zip weekly-cost-review.zip weekly-cost-review.py'
                sh 'zip monthly-cost-review.zip monthly-cost-review.py'
            }
        }

        stage('Upload to S3') {
            steps {
                    // Upload the first zip file
                    sh 'aws s3 cp weekly-cost-review.zip s3://${S3_BUCKET}/weekly-cost-review.zip'
                    
                    // Upload the second zip file
                    sh 'aws s3 cp monthly-cost-review.zip s3://${S3_BUCKET}/monthly-cost-review.zip'
            }
        }
    }
}
