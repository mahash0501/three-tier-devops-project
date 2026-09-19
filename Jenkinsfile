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
            docker build -t three-tier-backend:$GIT_COMMIT ./backend
        '''
    }
}
       stage('Trivy Scan') {
    steps {
        sh '''
            trivy image --severity HIGH,CRITICAL three-tier-backend:$GIT_COMMIT
        '''
    }
}

      stage('Docker Push') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USERNAME',
            passwordVariable: 'DOCKER_PASSWORD'
        )]) {
            sh '''
                echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                docker tag three-tier-backend:$GIT_COMMIT $DOCKER_USERNAME/three-tier-backend:$GIT_COMMIT
                docker push $DOCKER_USERNAME/three-tier-backend:$GIT_COMMIT
                docker logout
            '''
        }
    }
}
    stage('Update Helm Image Tag') {
        steps {
            sh '''
                sed -i "/repository: ashh501\\/three-tier-backend/{n;s/tag:.*/tag: $GIT_COMMIT/;}" helm/three-tier-app/values.yaml
                echo "Updated backend image tag:"
                grep -A2 "repository: ashh501/three-tier-backend" helm/three-tier-app/values.yaml
               '''
      }
    }   
  }
}
