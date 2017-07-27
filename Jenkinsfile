pipeline {
  agent {
    node {
      label 'dockercli-slave'
    }
    
  }
  stages {
    stage('build') {
      steps {
        sh 'docker build -t hello:0.0.1 .'
      }
    }
  }
}
