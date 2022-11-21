pipeline {
    agent any
    stages {
        stage('Chrome') {
            steps {
                sh 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
                sh 'dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install'
            }
        }
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
   