pipeline {
    agent any

    stages {

        stage("build") {
            steps {
                 sshagent (credentials: ['123456']) {
                        sh 'ssh -o StrictHostKeyChecking=no -l root 192.168.1.30'
                        sh 'echo tif > /tmp/tif.txt'
                    }
            }
        }

    }

}
