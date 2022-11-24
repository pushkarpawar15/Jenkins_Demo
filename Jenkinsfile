pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/pushkarpawar15/Jenkins_Demo'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x multiply.py"
                sh "python3 multiply.py"
            }
        }
    stage('Test Code Success') {
            steps {
                sh "chmod u+x Test.py"
                sh "python3 Test.py"
            }
        }
    stage('Test Code Fail') {
            steps {
                sh "chmod u+x Test1.py"
                sh "python3 Test1.py"
            }
        }
    } 
}
