pipeline {
  agent {
    node {
      label 'docker-slave'
    }
    
  }
  stages {
    stage('') {
      steps {
        sh 'echo "radio"'
        sh 'hostname'
        sh 'whoami'
        sh 'sleep 15'
      }
    }
  }
}