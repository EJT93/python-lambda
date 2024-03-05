pipeline {
    agent any
    stages {
        stage('Zip Python Code') {
            steps {
                script {
                    sh 'zip -r my_lambda_function.zip my_python_code_folder'
                }
            }
        }
        stage('Upload to S3') {
            steps {
                script {
                    // Assuming AWS CLI is installed and configured on Jenkins agent
                    sh 'aws s3 cp my_lambda_function.zip s3://my-lambda-code-bucket/'
                }
            }
        }
        stage('Update Lambda Function') {
            steps {
                script {
                    // Update the Lambda function's code
                    sh 'aws lambda update-function-code --function-name myLambdaFunction --s3-bucket my-lambda-code-bucket --s3-key my_lambda_function.zip'
                }
            }
        }
    }
}
