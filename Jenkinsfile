pipeline {
    agent none
      stages {
          
        stage('SCM Checkout') {
            steps {  
                  git branch: 'main', url: 'https://github.com/jachetblix/hello_world_jenkins.git'      
            }
        }
        stage('Build') {
            steps {
                sh 'python3 main.py'
            }
        }
    }
}
