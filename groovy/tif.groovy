pipeline {
    agent any

    stages {

        stage("build") {
            steps {
                script {
                    def remoteHost = '192.168.1.30'
                    def remoteUser = 'root'
                    def remotePassword = 'Aa123456'

                    // SSH command to be executed on the remote server
                    def command = 'echo "Hello from Jenkins" > /tmp/tif-groovy.txt'

                    // Execute SSH command
                    // sshCommand remote: [
                    //     host: remoteHost,
                    //     user: remoteUser,
                    //     password: remotePassword,
                    //     allowAnyHosts: true // Allow connecting to any host (not recommended for production)
                    // ], command: command

                    sh(script: """
                        sshpass -p ${remotePassword} ssh -o StrictHostKeyChecking=no ${remoteUser}@${remoteHost} '${command}'
                    """)
                }
            }
        }

    }

}