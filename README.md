# 🚀 CI/CD Deployment of Flask Backend and Express Frontend using Jenkins on AWS EC2

---

## 📌 Project Overview
This project demonstrates the deployment of a Flask backend and an Express frontend on a single AWS EC2 instance using a fully automated CI/CD pipeline with Jenkins.

Every push to GitHub automatically triggers Jenkins using Webhooks, which pulls the latest code, installs dependencies, and restarts the applications.

---

## 🔗 GitHub Repositories

- 🐍 Flask Backend: https://github.com/naresh-mishra/jenkins-backend  
- 🌐 Express Frontend: https://github.com/naresh-mishra/jenkins-frontend  

---

## 🏗️ Architecture Diagram

GitHub (Backend Repo: jenkins-backend)
GitHub (Frontend Repo: jenkins-frontend)
                │
                ▼
        GitHub Webhook Trigger
                │
                ▼
        Jenkins CI/CD Server
                │
                ▼
     AWS EC2 Instance (Ubuntu Server)
        ├── Flask Backend (Port 5000)
        └── Express Frontend (Port 3000)

---

## ☁️ EC2 Instance Setup

### Step 1: Connect to EC2
```bash id="ec2connect"
ssh -i key.pem ubuntu@<EC2-Public-IP>

### Step 2:Update system and install dependencies
sudo apt update -y
sudo apt install git -y
sudo apt install python3 python3-pip -y

curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs -y

sudo npm install -g pm2

### Flask Backend Deployment
Clone Repository
git clone https://github.com/naresh-mishra/jenkins-backend.git
cd jenkins-backend
Install Dependencies
pip3 install -r requirements.txt
Run Flask App
pm2 start app.py --interpreter python3 --name flask-app
http://<EC2-Public-IP>:5000

### Express Frontend Deployment
Clone Repository
git clone https://github.com/naresh-mishra/jenkins-frontend.git
cd jenkins-frontend
Install Dependencies
npm install
Run Express App
pm2 start server.js --name express-app
Access Express App
http://<EC2-Public-IP>:3000

### Jenkins CI/CD Setup
Step 1: Install Jenkins
sudo apt install openjdk-11-jdk -y

wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -

sudo sh -c 'echo deb http://pkg.jenkins.io/debian binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt update
sudo apt install jenkins -y

sudo systemctl start jenkins
sudo systemctl enable jenkins
Step 2: Access Jenkins
http://<EC2-Public-IP>:8080

### CI/CD Workflow
Developer pushes code to GitHub repositories
GitHub Webhook triggers Jenkins automatically
Jenkins pulls latest code
Installs required dependencies (pip/npm)
Restarts applications using PM2
Updated application is deployed automatically

### GitHub Webhook Setup

Add webhook in both repositories:

http://<EC2-Public-IP>:8080/github-webhook/

Trigger:

Push events

### Final Output URLs
🐍 Flask Backend → http://<EC2-Public-IP>:5000
🌐 Express Frontend → http://<EC2-Public-IP>:3000

### Final Result

✔ Flask backend deployed successfully
✔ Express frontend deployed successfully
✔ Jenkins CI/CD pipeline working
✔ Automatic deployment using GitHub Webhooks
✔ End-to-end DevOps pipeline implemented successfully
⚙️ Jenkins Server → http://<EC2-Public-IP>:8080
