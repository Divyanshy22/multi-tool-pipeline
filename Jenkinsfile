pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python Deps') {
            steps {
                sh 'python3 -m pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Quality Checks') {
            parallel {
                stage('Python Lint') {
                    steps {
                        sh 'python3 -m pylint app.py'
                    }
                }
                stage('Terraform Validate') {
                    steps {
                        sh 'terraform init -backend=false'
                        sh 'terraform validate'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Both Python lint and Terraform validate passed.'
        }
        failure {
            echo 'One or more quality checks failed — check console output above.'
        }
    }
}
