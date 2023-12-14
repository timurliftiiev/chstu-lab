pipeline {
    agent any

    stages {
        stage('Build and run Docker') {
            steps {
                script {
                    sh 'docker build -t jenkins-image /var/jenkins_home'
                    sh 'docker run --name jenkins-container -d jenkins-image'
                }
            }
        }

        stage('Build RPM Package') {
            steps {
                script {
                    sh 'docker exec deep-container rpmdev-setuptree'
                    sh 'docker exec deep-container wget https://github.com/timurliftiiev/chstu-lab/archive/main.zip'
                    sh 'docker exec deep-container unzip main.zip'
                    sh 'docker exec deep-container mv chstu-lab/rpm/count-files.spec ~/rpmbuild/SPECS/'
                    sh 'docker exec deep-container mv chstu-lab/count-files.sh ~/rpmbuild/SPECS/'
                    sh 'docker exec deep-container mv main.zip ~/rpmbuild/SOURCES/'
                    sh 'docker exec deep-container rpmbuild -bs --define "dist .generic" ~/rpmbuild/SPECS/count-files.spec'
                    sh 'docker exec deep-container rpmbuild --rebuild ~/rpmbuild/SRPMS/count-files-1.0-1.generic.src.rpm'
                }
            }
        }

        stage('Install RPM Package') {
            steps {
                script {
                    // Install RPM package inside the container
                    sh 'docker exec deep-container rpm -ivh ~/rpmbuild/RPMS/noarch/count-files-1.0-1.el7.noarch.rpm'
                    sh 'docker exec deep-container count-files chstu-lab'
                }
            }
        }

        stage('Stop Docker') {
            steps {
                script {
                    sh 'docker stop jenkins-container'
                    sh 'docker rm jenkins-container'
                    sh 'docker rmi jenkins-image'
                }
            }
        }
    }
}
