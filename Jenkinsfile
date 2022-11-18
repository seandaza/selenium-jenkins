pipeline {
    agent {
        docker {
            image '15174814/scrapy:scrapy'

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
   