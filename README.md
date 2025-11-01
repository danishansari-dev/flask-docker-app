# CI/CD Pipeline (Jenkins + Docker + GitHub)

Name: `Mohammad Danish Ansari`  
Roll Number: 22BDS039

## 1. Objective

To design and implement an automated CI/CD pipeline that integrates Docker, GitHub, and Jenkins to automatically build, test, and deploy a Flask application whenever code is pushed to the GitHub repository.

***

## 2. Project Structure

The project consists of the following directory structure:

```
flask-docker-app/
├── Dockerfile
├── requirements.txt
├── app.py
└── README.md
```

**GitHub Repository:** [https://github.com/danishansari-dev/flask-docker-app](https://github.com/danishansari-dev/flask-docker-app)

**Docker Hub Repository:** [https://hub.docker.com/r/danish491/flask-docker-app](https://hub.docker.com/r/danish491/flask-docker-app)

## 4. Pushed Code to GitHub Repository

Initialized Git repository and pushed all files to GitHub:

```bash
git init
git add .
git commit -m "Initial commit for CI/CD task"
git remote add origin https://github.com/danishansari-dev/flask-docker-app.git
git push -u origin main
```

**Screenshot: GitHub repository showing all files**
![alt text](https://raw.githubusercontent.com/danishansari-dev/Documentation/refs/heads/main/Screenshots/Screenshot%202.png)

## 5. Configured Docker Hub Credentials in Jenkins

Added Docker Hub credentials to Jenkins for automated image pushing:

- Navigated to Manage Jenkins → Manage Credentials
- Added Username with password credentials
- ID: `dockerhub-creds`

**Screenshot: Jenkins credentials page**

![alt text](<Screenshots/Screenshot 5.png>)

***

## 6. Created Jenkins Pipeline Job

Created a new Freestyle project in Jenkins named `flask-app-pipeline` with:

- Git repository configuration
- GitHub webhook trigger
- Windows batch build script

**Screenshot: Jenkins job configuration - Source Code Management**

![alt text](https://raw.githubusercontent.com/danishansari-dev/Documentation/refs/heads/main/Screenshots/Screenshot%204.png)

### Screenshot: Jenkins job configuration - Build Triggers

![alt text](https://raw.githubusercontent.com/danishansari-dev/Documentation/refs/heads/main/Screenshots/Screenshot%206.png)

### Screenshot: Jenkins job configuration - Build Steps (batch script)

![alt text](<Screenshots/Screenshot 07 Build Steps Script1.png>)
![alt text](<Screenshots/Screenshot 07 Build Steps Script2.png>)

***

## 7. Manual Build Test - Latest Execution

Executed manual build by clicking "Build Now" to verify pipeline configuration.

The pipeline performs the following steps:

1. Builds Docker image
2. Tests the image locally
3. Attempts to push to Docker Hub
4. Deploys container on port 5000

### Screenshot: Jenkins console output showing successful build

![alt text](<Screenshots/Screenshot 08 Manual Build Console Output1.png>)
![alt text](<Screenshots/Screenshot 08 Manual Build Console Output2.png>)

### Screenshot: Jenkins build history showing Build Success

![Screenshot 09 Build History.png](<Screenshots/Screenshot 09 Build History.png>)

***

## 8. Verified Deployed Application

Opened browser and tested the Flask application endpoints:

- `http://localhost:5000` - Home page

**Screenshot: Browser showing Flask app running (version 1.0)**
![alt text](<Screenshots/Screenshot 10 App Running v1.0.png>)

**Screenshot: Docker ps command showing running container**
![alt text](<Screenshots/Screenshot 11 Docker PS Output.png>)

***

## 9. Configured GitHub Webhook

Set up GitHub webhook to automatically trigger Jenkins builds on code push:

- Used ngrok to expose local Jenkins to internet
- Configured webhook URL: `https://[ngrok-url]/github-webhook/`
- Selected "Just the push event" trigger
- Verified webhook with green checkmark

### Screenshot: GitHub webhook configuration page

![alt text](<Screenshots/Screenshot 12 Webhook Configuration.png>)

### Screenshot: GitHub webhook showing green checkmark (successful delivery)

![alt text](<Screenshots/Screenshot 13 Webhook Green Checkmark.png>)

***

## 10. Made Code Changes to Test Automatic Deployment

Modified `app.py` to update version and message:

```python
"message": "Flask CI/CD Pipeline - AUTO DEPLOY TEST v2.0! 🚀",
"version": "2.0",
```

Committed and pushed changes to GitHub:

```bash
git add .
git commit -m "Test automatic deployment - version 2.0"
git push origin main
```

### Screenshot: Git push command for version 2.0

![alt text](<Screenshots/Screenshot 14 Git Push v2.0.png>)

***

## 11. Automatic Build Triggered by GitHub Webhook

Jenkins automatically detected the GitHub push and triggered a new build without manual intervention.

### Screenshot: Console output of automatic build showing SUCCESS

![alt text](<Screenshots/Screenshot 16 Automatic Build Console.png>)

***

## 12. Verified Updated Application Deployment

Refreshed browser to confirm automatic deployment of updated version.

### Screenshot: Browser showing updated app with version 2.0

![alt text](<Screenshots/Screenshot 17 App Running v2.0.png>)

***

## 13. Build History and Pipeline Execution

Jenkins build history showing multiple successful builds:

- Manual builds (started by user)
- Automatic builds (triggered by GitHub push)

### Screenshot: Jenkins build history showing multiple builds

![alt text](<Screenshots/Screenshot 18 Multiple Builds History.png>)

***

## 15. CI/CD Pipeline Workflow Diagram

The complete automated workflow:

```
Developer → Code Change → Git Push → GitHub
                                        ↓
                                   Webhook Trigger
                                        ↓
                                     Jenkins
                                        ↓
                    ┌──────────────────┴──────────────────┐
                    ↓                  ↓                   ↓
              Pull Code         Build Image         Test Image
                    ↓                  ↓                   ↓
                    └──────────────────┼───────────────────┘
                                       ↓
                              Push to Docker Hub (optional)
                                       ↓
                              Deploy Container
                                       ↓
                          Application Running (Port 5000)
```

## 21. Conclusion

Successfully implemented a fully automated CI/CD pipeline integrating Jenkins, Docker, and GitHub. The pipeline automatically detects code changes via GitHub webhooks, builds Docker images, tests the application, and deploys containers without manual intervention. This demonstrates modern DevOps practices including continuous integration, continuous deployment, containerization, and automated testing.

**Key Achievements:**

- ✅ Automated build and deployment workflow
- ✅ GitHub webhook integration working successfully
- ✅ Docker containerization implemented
- ✅ Multiple successful build cycles completed
- ✅ Automatic deployment verified with version updates

The pipeline is production-ready and demonstrates enterprise-level CI/CD practices. All endpoints accessible at **<http://localhost:5000>**
