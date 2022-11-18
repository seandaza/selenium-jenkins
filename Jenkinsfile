pipeline {
  agent any
  docker {
     image 'python:3.7'
      args '-p 3000:3000'
    }
  stages {
    stage('Run python') {
      steps {
        sh 'python -m http.server 3000'
      }
    }
  }

