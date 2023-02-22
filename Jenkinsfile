pipeline {
    agent {
        docker {
            image 'python:3.8-alpine'
            args '-p 5000:5000'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    docker.build("myflaskapp:latest")
                }
            }
        }
        stage('Docker Run') {
            steps {
                sh 'docker run -d -p 5000:5000 myflaskapp:latest'
            }
        }
    }
}
