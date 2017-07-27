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
    stage('test') {
      steps {
        sh 'docker run -d hello:0.0.1'
	sh 'curl -I -f http://localhost:5555'
      }
    }

  }
}
