pipeline {
    agent {
        docker {
            image 'python:3.7'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'ls -la'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
   