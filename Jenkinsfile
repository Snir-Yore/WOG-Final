pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install selenium'
                sh 'docker-compose build'
            }
        }

        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                dir('test') {
                    sh 'e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose push'
            }
        }
    }
}
