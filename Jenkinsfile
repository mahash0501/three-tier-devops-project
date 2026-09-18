pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
    steps {
        sh '''
            cd backend
            python3 -m pytest
        '''
    }
   }
    }
}
