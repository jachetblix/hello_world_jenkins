pipeline {
    agent any
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
// pipeline {
//     agent any
//     stages {
//         stage('Run Python Script') {
//             steps {
//                 sh 'python3 /Users/artyomegorov/Desktop/hello_world_jenkins/main.py'
//             }
//         }
//     }
// }