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
                sh "chmod u+x Prog.py"
                sh "./Prog.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
