pipeline {
  agent any
  stages {
    stage('Run python') {
      steps {
        sh 'apt update'
        sh 'apt install python3-pip'
        sh 'pip3 --version'
      }
    }
  }
}