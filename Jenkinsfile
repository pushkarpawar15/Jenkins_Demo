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
                sh "chmod u+x Test1.py"
                sh "python3 Test1.py"
                sh "chmod u+x Test2.py"
                sh "python3 Test2.py"
            }
        }
        stage('Test Code Failure') {
            steps {
                sh "chmod u+x Test3.py"
                sh "python3 Test3.py"
                sh "chmod u+x Test4.py"
                sh "python3 Test4.py"
            }
        }
    } 
}
