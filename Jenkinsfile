pipeline {
    agent any
    stages {
        stage('Build') {
            steps {

                sh 'pip3 install -r requirements.txt'
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
