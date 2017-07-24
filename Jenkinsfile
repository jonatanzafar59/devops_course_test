pipeline {
  agent {
    node {
      label 'docker-slave'
    }
    
  }
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r flask_hello/requirements.txt'
      }
    }
  }
}