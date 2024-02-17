pipeline {
    agent any

    stages {
        stage('SSH Command') {
            steps {
                script {
                    sshagent(credentials: ['123456']) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no root@192.168.1.30 'echo "word" > /tmp/file.txt'
                        '''
                    }
                }
            }
        }
    }
}