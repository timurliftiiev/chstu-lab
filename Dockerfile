# Use the official Jenkins master image
FROM jenkins/jenkins:2.361.1-lts-centos7

USER jenkins

# Expose ports for web UI and agent communication
EXPOSE 8080
EXPOSE 50000

# Command to start Jenkins master
CMD ["/usr/local/bin/jenkins.sh"]
