pipeline {
    agent any

    stages {
        stage('SSH Command') {
            steps {
                script {
                    sshagent(['your_ssh_credentials_id']) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no root@192.168.1.30 'echo "word" > /tmp/file.txt'
                        '''
                    }
                }
            }
        }
    }
}