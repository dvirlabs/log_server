pipeline {
    agent any

    stages {

        stage("build") {
            steps {
                 sshagent (credentials: ['123456']) {
                        sh 'sudo ssh -o StrictHostKeyChecking=no -i /tmp/tif root@192.168.1.30'
                        sh 'echo tif > /tmp/tif.txt'
                    }
            }
        }

    }

}
