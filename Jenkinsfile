pipeline {

    agent any

    stages {

        stage('Checkout Source Code') {

            steps {

                git branch: 'main',
                    url: 'https://github.com/sairevoori8/CapstoneProject_Automation_Testing.git'
            }
        }

        stage('Install Dependencies') {

            steps {

                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {

            steps {

                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {

                    bat 'python -m pytest --alluredir=reports/allure-results'
                }
            }
        }
    }

    post {

        always {

            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'reports/allure-results']]
            )
        }
    }
}