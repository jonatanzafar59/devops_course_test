pipeline {
  agent {
    node {
      label 'docker-slave'
    }
    
  }
  stages {
    stage('build') {
      steps {
        sh 'cd flask_hello/'
        sh 'pip3 install -r requirements.txt'
      }
    }
  }
}