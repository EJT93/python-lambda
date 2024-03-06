pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-2' // Specify your AWS region
        S3_BUCKET = 'lambda-code-and-logs' // Specify your S3 bucket name
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: '0bcb9385-f23a-4c61-abd5-8e07356c3802', url: 'git@github.com:EJT93/python-lambda.git'
                git 'https://github.com/EJT93/python-lambda.git'
            }
        }

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
