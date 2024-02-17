pipeline {
    agent any

    stages {
        stage('SSH Command') {
            steps {
                script {
                    sshCommand remote: [
                        host: '192.168.1.30',
                        user: 'root',
                        password: 'Aa123456',
                        allowAnyHosts: true // Optional: Allow connections to hosts with non-trusted keys
                    ], command: 'echo "word" > /tmp/file.txt'
                }
            }
        }
    }
}