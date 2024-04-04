pipeline {
    agent any
    triggers { githubPush() } 
    environment {
        registry = "asademo.azurecr.io"
        imageName = "${registry}/${env.BUILD_ID}" // Using Jenkins build ID, adjust if you want a custom name
        registryCredential = 'azure ACR' // ID of your ACR credentials stored in Jenkins
        appServicePublishProfile = 'AzureAppService_PublishProfile_43b8c52a9f9c46609eba4113bd48ed2c'
    }
        stage('Build and Push Image') {
            steps {
                script {
                    docker.withRegistry("https://${registry}", registryCredential) {
                        def image = docker.build(imageName, "./") 
                        image.push()
                    } 
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    withCredentials([string(credentialsId: appServicePublishProfile, variable: 'AZURE_CREDENTIALS')]) {
                        sh 'az webapp deployment container config --enable-cd true'
                        sh 'az webapp config container set --name jenkinsmaster --slot production --resource-group <resource_group_name> --docker-custom-image-name ${imageName}'
                    }
                }
            }
        }
    }

