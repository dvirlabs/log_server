pipeline {
    agent any
    
    stages {
        stage('Execute SSH command') {
            steps {
                script {
                    // Define SSH credentials
                    def remote = [:]
                    remote.name = 'log_server'
                    remote.host = '192.168.1.30'
                    remote.user = 'root'
                    remote.password = 'Aa123456'
                    remote.allowAnyHosts = true // This allows connections to hosts with non-trusted keys

                    // Execute SSH command
                    sshCommand remote: remote, command: 'echo "word" > /tmp/file.txt'
                }
            }
        }
    }
}