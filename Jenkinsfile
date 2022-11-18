pipeline {
  agent any
  stages {
    stage('Run python') {
      steps {
        sh 'python3 -m venv venv'
        sh 'source venv/bin/activate'
        sh 'pip install -r requirements.txt'
        sh 'python3 main.py'
        }
      }
    }
  }
}