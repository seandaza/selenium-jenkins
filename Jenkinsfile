pipeline {
  agent any
  stages {
    stage('Run python') {
      steps {
        sh 'apt-get update'
        sh 'apt-get install python3-pip'
        sh 'pip3 --version'
      }
    }
  }
}