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
    stage('test') {
      steps {
        sh 'python3 flask_hello/run.py &'
        sh 'curl -I http://localhost:5555/'
      }
    }
  }
}