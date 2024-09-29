# AccuKnox QA Engineer Practical Assessment

## Project Overview

This repository contains the implementation for the QA Engineer Practical Assessment at AccuKnox. The application consists of a frontend and backend service deployed on a local Kubernetes cluster.

## Setup Instructions

1. **Prerequisites**:

   - Minikube
   - kubectl
   - Python 3.x
   - Pip
   - WSL (Windows Subsystem for Linux) ((if needed))

2. **Deploy the Application**:

   - Clone the repository:

     git clone https://github.com/SudarsanRamachandran/qa-assesment.git
     cd /qa-assesment/

   - Start Minikube:

     minikube start

     To start minikube, if docker desktop is supported on your machine, then you can directly use the command "minikube start".

     else

   i. Install wsl using the command wsl --install
   ii. After your computer restarts, open the installed Linux distribution (e.g., Ubuntu) from the Start menu.
   iii. Set up your username and password for the Linux environment.
   iv. Update the packages using the command "sudo apt update && sudo apt upgrade -y"
   v. Install the prerequisites using the command "sudo apt install -y minikube kubectl python3 python3-pip"
   vi. To verify that everything is set up correctly, run the following commands :
   kubectl version --client
   minikube status
   python3 --version
   vii. Now since all looks good, run "miinikube start"

   - Apply the deployment and service configurations:

     cd deployment
     kubectl apply -f backend-deployment.yaml
     kubectl apply -f frontend-deployment.yaml

3. **Run Tests**:

   - Ensure that the frontend service is accessible:

     curl http://192.168.49.2:30001

   - Run the test script:

     python3 test_frontend.py

## Problem Statement 2

### Objectives

In this section, two objectives have been implemented using Python:

1.  **Application Health Checker**: This script checks the uptime of an application and determines if it is functioning correctly.

### Setup Instructions

**Run Application Health Checker**:

Open your terminal and run the command "python3 system_health_monitor.py"
It provides a log file named 'sytem_health.log' after running it successfully.

2. **Log File Analyzer**: This script analyzes web server logs for common patterns such as the number of 404 errors and the most requested pages.

### Setup Instructions

**Run Log File Analyzer**:
Open your terminal and run the command "python3 log_file_analyzer.py"

Note: I have created a 'access.log' with sample entries to test. You can modify them to check the log_file which needs to be analyzed.

### Note

Ensure to have the required permissions and your Python environment is properly set up to run these scripts. Adjust file paths as necessary based on your setup.
