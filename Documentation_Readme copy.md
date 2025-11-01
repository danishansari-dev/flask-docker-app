# **DevOps Assignment - 5**

**Name:** Mohammad Danish Ansari
**Roll Number:** 22BDS039


## **TASK 1**: Multi-Container Application (Flask + MySQL)

## 1. Objective

To create and deploy a multi-container application consisting of a Python Flask web application and a MySQL database using Docker Compose, demonstrating container orchestration and inter-container communication.


## 2. Project Structure

The project consists of the following directory structure:

```
flask-mysql-app/
├── docker-compose.yml
└── flask-app/
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

**GitHub Repository:** [Your GitHub Link Here]

## 3. Built all container images using Docker Compose.
```
docker-compose up --build
```
![alt text](<Screenshot 01.png>)
![alt text](<Screenshot 1.png>)

## 4. Verified successful creation and running of containers.

![alt text](<Screenshot 4.png>)

## 5. Browser showing running application.
![alt text](<Screenshot 2.png>)

![alt text](<Screenshot 3.png>)
![alt text](<Screenshot 5.png>)
## 6. Conclusion
Successfully implemented a multi-container application demonstrating Docker Compose capabilities for orchestrating interconnected services. Both Flask web application and MySQL database containers communicate seamlessly over a custom network, with data persistence implemented through Docker volumes. The application is fully functional and accessible at http://127.0.0.1:5000/


# **TASK 2:** CI/CD Pipeline (Auto-Deploy from GitHub)

### What Are We Building?

An automatic system that:

1. You push code to GitHub
2. Jenkins automatically detects the change
3. Jenkins builds a Docker image
4. Jenkins pushes it to Docker Hub (like Google Drive for Docker images)
5. Jenkins runs your application automatically[^4][^3]

It's like having a robot assistant that deploys your code!

### Step-by-Step Instructions

#### Step 1: Create a GitHub Account (If You Don't Have One)

1. Go to `github.com`
2. Click "Sign up"
3. Create a free account
4. Verify your email

#### Step 2: Create a New Repository on GitHub

1. Log into GitHub
2. Click the **"+"** button (top right) → **"New repository"**
3. Repository name: `flask-docker-app`
4. Make it **Public**
5. Check "Add a README file"
6. Click **"Create repository"**[^4]

#### Step 3: Install Git on Windows (If Not Already Installed)

1. Download from: `https://git-scm.com/download/win`
2. Install with default options
3. Open Command Prompt and verify:

```
git --version
```


#### Step 4: Create Your Flask App Locally

1. Create a new folder on Desktop: `flask-docker-app`
2. Inside this folder, create these files:

**File 1: `app.py`**

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my Flask CI/CD App!",
        "version": "1.0",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**File 2: `requirements.txt`**

```
flask
```

**File 3: `Dockerfile`**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```


#### Step 5: Push Your Code to GitHub

1. Open Command Prompt in your `flask-docker-app` folder:

```
cd Desktop\flask-docker-app
```

2. Initialize Git:

```
git init
git add .
git commit -m "Initial commit"
```

3. Connect to your GitHub repository (replace with YOUR username):

```
git remote add origin https://github.com/YOUR-USERNAME/flask-docker-app.git
git branch -M main
git push -u origin main
```

4. If asked, enter your GitHub username and password (or token)

**Verify**: Refresh your GitHub repository page - you should see all your files!

#### Step 6: Create Docker Hub Account

1. Go to `hub.docker.com`
2. Sign up for a free account
3. Remember your username and password - you'll need them later!

#### Step 7: Configure Jenkins

1. **Open Jenkins** in your browser:

```
http://localhost:8080
```

2. If this is your first time:
    - Find the password: Open Command Prompt and run:

```
type "C:\Program Files\Jenkins\secrets\initialAdminPassword"
```

    - Copy the password
    - Paste it in Jenkins
    - Click "Install suggested plugins" and wait
    - Create your admin account[^3]

#### Step 8: Install Required Jenkins Plugins

1. In Jenkins, click **"Manage Jenkins"** (left sidebar)
2. Click **"Manage Plugins"**
3. Click **"Available plugins"** tab
4. Search and install these plugins (check the box and click "Install without restart"):
    - **Git plugin**
    - **GitHub Integration Plugin**
    - **Docker Pipeline**[^3]
5. Wait for installation to complete

#### Step 9: Add Docker Hub Credentials to Jenkins

1. In Jenkins, go to **"Manage Jenkins"** → **"Manage Credentials"**
2. Click **"(global)"** → **"Add Credentials"**
3. Fill in:
    - Kind: **Username with password**
    - Username: Your Docker Hub username
    - Password: Your Docker Hub password
    - ID: `dockerhub-credentials` (exactly this!)
    - Description: Docker Hub Login
4. Click **"Create"**[^4]

#### Step 10: Create Jenkins Job

1. On Jenkins homepage, click **"New Item"**
2. Enter name: `flask-app-pipeline`
3. Select **"Freestyle project"**
4. Click **OK**[^4]

#### Step 11: Configure the Job

**Section A: Source Code Management**

1. In the job configuration page, scroll to **"Source Code Management"**
2. Select **"Git"**
3. Repository URL: `https://github.com/YOUR-USERNAME/flask-docker-app.git` (replace with yours)
4. Branch: `*/main`[^4]

**Section B: Build Triggers**

1. Scroll to **"Build Triggers"**
2. Check **"GitHub hook trigger for GITScm polling"**[^4]

**Section C: Build Steps**

1. Scroll to **"Build"**
2. Click **"Add build step"** → **"Execute Windows batch command"**
3. Paste this script (REPLACE `your-dockerhub-username` with YOUR Docker Hub username):
```batch
@echo off
echo Starting build process...

REM Variables (CHANGE THIS!)
set IMAGE_NAME=your-dockerhub-username/flask-app
set CONTAINER_NAME=flask-app-container

REM Stop and remove old container if exists
docker stop %CONTAINER_NAME% 2>nul
docker rm %CONTAINER_NAME% 2>nul

REM Build Docker image
echo Building Docker image...
docker build -t %IMAGE_NAME%:latest .

REM Login to Docker Hub (using saved credentials)
echo Logging into Docker Hub...
docker login -u your-dockerhub-username -p your-dockerhub-password

REM Push to Docker Hub
echo Pushing image to Docker Hub...
docker push %IMAGE_NAME%:latest

REM Run the container
echo Running container...
docker run -d -p 5000:5000 --name %CONTAINER_NAME% %IMAGE_NAME%:latest

echo Deployment complete!
docker ps
```

**Important**: Replace:

- `your-dockerhub-username` with your actual Docker Hub username (3 places)
- `your-dockerhub-password` with your actual Docker Hub password

4. Click **"Save"** at the bottom[^3]

#### Step 12: Test Jenkins Build Manually

1. On your job page, click **"Build Now"** (left sidebar)
2. Watch the build progress - a new build will appear under "Build History"
3. Click on the build number (e.g., \#1)
4. Click **"Console Output"** to see what's happening
5. Wait until you see "BUILD SUCCESS" or "Finished: SUCCESS"
6. **Test your app**: Open browser and go to:

```
http://localhost:5000
```

You should see your Flask app!

**Take Screenshot**: Console Output showing success

#### Step 13: Set Up GitHub Webhook (Auto-Trigger)

Now we'll make GitHub automatically tell Jenkins when you push code.[^3][^4]

**Problem on Windows**: Jenkins on localhost can't receive messages from GitHub. We need to expose Jenkins to the internet temporarily.

**Solution: Use ngrok (Free tool)**

1. Download ngrok: `https://ngrok.com/download`
2. Extract the zip file
3. Open Command Prompt in the ngrok folder
4. Run:

```
ngrok http 8080
```

5. You'll see something like:

```
Forwarding   https://abcd1234.ngrok.io -> http://localhost:8080
```

6. **Copy the `https://abcd1234.ngrok.io` URL** (yours will be different!)

**Configure GitHub Webhook:**

1. Go to your GitHub repository page
2. Click **"Settings"** (top right)
3. Click **"Webhooks"** (left sidebar)
4. Click **"Add webhook"**
5. Fill in:
    - **Payload URL**: `https://abcd1234.ngrok.io/github-webhook/` (use YOUR ngrok URL + `/github-webhook/`)
    - **Content type**: `application/json`
    - **Which events**: Select "Just the push event"
    - **Active**: ✓ Checked
6. Click **"Add webhook"**[^3][^4]
7. **Take Screenshot**: Webhook page showing green checkmark

**Note**: Keep the Command Prompt with ngrok running! If you close it, the webhook stops working.

#### Step 14: Test Automatic Deployment!

1. Open your `app.py` file in Notepad
2. Change the message to:

```python
"message": "Welcome to my UPDATED Flask CI/CD App!",
```

3. Save the file
4. Push to GitHub:

```
cd Desktop\flask-docker-app
git add .
git commit -m "Updated welcome message"
git push origin main
```

5. **Watch Jenkins** (refresh the page) - A new build should start automatically!
6. Wait for build to finish
7. Test the app:

```
http://localhost:5000
```

You should see the UPDATED message!

**Take Screenshot**:

- Jenkins build history showing automatic build
- Browser with updated message

***

## What to Submit for Your Assignment

### Task 1 Submission:

1. ✓ All files in a zip: `docker-compose.yml`, `Dockerfile`, `app.py`, `requirements.txt`
2. ✓ Screenshot: `docker-compose up` running
3. ✓ Screenshot: `docker ps` showing both containers
4. ✓ Screenshot: Browser showing `http://localhost:5000/users`
5. ✓ Screenshot: Browser showing `http://localhost:5000/health`

### Task 2 Submission:

1. ✓ GitHub repository link
2. ✓ Screenshot: GitHub repository with all files
3. ✓ Screenshot: Jenkins job configuration page
4. ✓ Screenshot: Jenkins build history (showing successful builds)
5. ✓ Screenshot: Jenkins console output (showing success)
6. ✓ Screenshot: GitHub webhook configuration (green checkmark)
7. ✓ Screenshot: Docker Hub showing your pushed image
8. ✓ Screenshot: Browser showing your running Flask app

***

## Troubleshooting Common Issues

### "Docker is not running"

- Open Docker Desktop from Start menu
- Wait for the whale icon to appear in system tray


### "Port 5000 is already in use"

- Change the port in `docker-compose.yml` from `5000:5000` to `5001:5000`
- Access via `http://localhost:5001`


### "Cannot connect to database"

- Wait 30 seconds after running `docker-compose up`
- MySQL takes time to initialize


### Jenkins build fails

- Check Console Output in Jenkins
- Make sure Docker Desktop is running
- Verify your Docker Hub credentials are correct


### Webhook not working

- Make sure ngrok is running
- Verify the webhook URL has `/github-webhook/` at the end
- Check webhook delivery in GitHub Settings → Webhooks

***

## Key Concepts Explained Simply

**Docker**: Think of it as creating mini-computers (containers) inside your computer[^1]

**Docker Compose**: A tool to create multiple containers at once and connect them[^1]

**Flask**: A simple Python framework to build websites

**MySQL**: A database to store information

**Jenkins**: A robot that automatically builds and deploys your code[^3]

**GitHub**: Where you store your code online

**Docker Hub**: Where you store your Docker images (like Google Drive for containers)[^4]

**Webhook**: A way for GitHub to tell Jenkins "Hey, new code just arrived!"[^3]

**CI/CD Pipeline**: An automated system that takes your code from GitHub to running on a server[^4][^3]

This assignment teaches you the basics of modern software deployment! You're doing great![^1][^3][^4]
<span style="display:none">[^10][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://betterstack.com/community/guides/scaling-docker/docker-compose-getting-started/

[^2]: https://www.geeksforgeeks.org/devops/docker-compose-for-windows-tips-and-tricks/

[^3]: https://dzone.com/articles/adding-a-github-webhook-in-your-jenkins-pipeline

[^4]: https://www.blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project

[^5]: https://github.com/KartikShrikantHegde/Docker-Flask-MySQL

[^6]: https://stackoverflow.com/questions/60283947/how-to-dockerize-my-flask-web-app-with-mysql-databasecannot-connect-mysql-and-c

[^7]: https://docs.docker.com/compose/gettingstarted/

[^8]: https://www.youtube.com/watch?v=KQUiICpM_u0

[^9]: https://www.docker.com/101-tutorial/

[^10]: https://dev.to/idsulik/a-beginners-guide-to-docker-compose-for-developers-55dm

