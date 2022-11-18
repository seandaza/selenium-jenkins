pipeline {
    agent {
        docker {
            image 'joyzoursky/python-chromedriver:3.9'

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
   