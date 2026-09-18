pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    cd backend
                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    cd backend
                    venv/bin/python -m pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t three-tier-backend:ci ./backend
                '''
            }
        }
       stage('Trivy Scan') {
         steps {
           sh '''
            trivy image --severity HIGH,CRITICAL three-tier-backend:ci
              '''
    }
   }
  }
}
