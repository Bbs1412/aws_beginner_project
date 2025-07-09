<img src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/amazonwebservices-original-wordmark.svg" alt="AWS" width="60" align="left">

# `Beginner Project`

- This is the project developed as part of the AWS course. The project is a simple Travel Guide application that gives information about various travel destinations.
- It utilizes various AWS services under free-tier limits, making it beginner-friendly.
- We faced a lot of challenges during development and deployment, so we've documented everything in detail to help others who might run into similar issues.
- Also, there are two versions of this project, it will be described in detail below.


# Index:
- [AWS Beginner Project](#aws-beginner-project)
- [Project Details](#-project-details)
    - [Aim](#aim)
    - [Features](#features)
    - [Architecture](#architecture)
    - [Warning](#warning)
    - [Tech Stack](#-tech-stack)
    - [Another Version](#another-version)
- [Steps to run](#-steps-to-run)
- [To make changes](#-to-make-changes)
- [Steps to deploy](#-steps-to-deploy)
- [Important Instructions](#-important-instructions)
- [Contributions](#-contributions)
- [License](#-license)
- [Contact](#-contact)


# 🎯 Project Details:
## Aim:
- Build a simple Travel Guide app that provides destination info using AWS services.
- Demonstrate how to easily deploy a project using common AWS components.

## Features:
- Responsive web UI that works well on different screen sizes.
- Dynamic page rendering with data pulled from a database.
- Clean, user-friendly interface using just HTML, CSS, and JavaScript.
- Option to use either S3 or EBS for storing image assets.

## Architecture:
<image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/architecture.png" alt="Project Architecture Diagram" width="550">

## Warning:
- The project is not meant for real-world use or as an impactful solution. Its main purpose is to demonstrate how different AWS services can be used together in a beginner-friendly setup.
- So, following strict best practices or writing production-ready code wasn't the main focus.

## 🧑‍💻 Tech Stack:

<!-- 
https://aws-icons.com/?
https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-plain.svg
-->

<table>
    <thead>
        <tr>
            <th>🖼️</th>
            <th>Tech </th>
            <th>Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//html5-plain.svg" alt="HTML-icon" height=45></td>
            <td>HTML/CSS/JS</td>
            <td>Pretty obvious beginner-friendly web technologies for building the frontend.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//flask-original-wordmark.svg" alt="Flask-icon" height=50></td>
            <td>Flask</td>
            <td>A lightweight Python web framework to serve the web application.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//sqlite-original.svg" alt="SQLite-icon" height=45></td>
            <td>SQLite-3</td>
            <td>A simple file based database for storing travel destination data.</td>
        </tr>
        <tr>
            <th colspan="3">AWS Services</th>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//EC2.svg" alt="AWS-icon" height=45></td>
            <td>AWS EC2</td>
            <td>For hosting the web application.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//Elastic Block Store.svg" alt="EBS-icon" height=45></td>
            <td>AWS EBS</td>
            <td>For persistent instance storage.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//Simple Storage Service.svg" alt="S3-icon" height=45></td>
            <td>AWS S3</td>
            <td>For hosting the static website assets.</td>
        </tr>
        <tr>
            <th colspan="3">(Optional) You can add these services easily</th>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//RDS.svg" alt="RDS-icon" height=45></td>
            <td>AWS IAM</td>
            <td>For managing access to AWS services with roles and policies.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//CloudWatch.svg" alt="CloudWatch-icon" height=45></td>
            <td>AWS CloudWatch</td>
            <td>For monitoring instance performance and logs.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs//CloudTrail.svg" alt="CloudTrail-icon" height=45></td>
            <td>AWS CloudTrail</td>
            <td>For tracking user activity and API usage.</td>
        </tr>
</table>


## Another Version:
- There’s a more advanced version of this project that includes additional AWS services:
    | Service | Description |
    | --- | --- |
    | **AWS RDS** | Replaces SQLite with a managed database. |
    | **AWS Translate** | Translates destination descriptions to multiple languages. |
    | **AWS Cognito** | Adds user authentication (register/login). |
    | **AWS SNS** | Sends OTPs and notifications to users. |
    | **AWS Bedrock** | Will be added later for AI features. |

- You can check that version of the project: [![AWS Advanced Project](https://img.shields.io/badge/Bbs1412/-AWS_Advanced_Project-ff8800.svg?logo=github)](https://github.com/Bbs1412/aws_advanced_project)


# 🛠️ Steps to run:
To run the project locally on your device first, follow these steps:

1. Create fork of the repository:
    - Click on the `Fork` button at the top right corner of this page to create a copy of the repository in your GitHub account.
    - This will also help to easily deploy the project on AWS later.
    - Now, you have your own copy of the project repository in your GitHub account.

1. Clone the repository from your GitHub account:
    ```bash
    # Replace the <your-username> with your GitHub username
    git clone https://github.com/<your-username>/aws_beginner_project
    cd aws_beginner_project
    ```

1. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    ```

1. Activate the virtual environment:
    ```bash
    # Linux:
    source venv/bin/activate  
    # Windows:
    venv\Scripts\activate
    ```

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    After this, all the dependencies will be installed in your virtual environment.

1. Create the SQLite database:
    ```bash
    python sq_db_entries.py
    ```
    This will run the script to create the SQLite database file `lite.db` and fill it with some initial data. 

1. Run the Flask application:
    ```bash
    python app.py
    ```

1. Now, server is live and project can be accessed at [`http://localhost:5000/`](http://localhost:5000/) in your browser.


# 🛠️ To make changes:
- To make changes in UI, html files in ***templates/*** and, scripts and styles in ***static/*** directories can be modified. 

- The script [`sq_db.py`](sq_db.py) is used to create the SQLite database file. It provides all the necessary functions to insert the new data into the database.

- To update the locations, you can modify data in [`sq_db_entries.py`](sq_db_entries.py) file. This file is used to create the initial database entries and can be modified to add or update or remove locations.

- Make sure that file names and corresponding data in the database are consistent, so that the images can be loaded correctly.


# 🚀 Steps to deploy:

> [!CAUTION]
> Avoid doing anything un-necessary in the AWS console, unless you know what you are doing.  
> It can lead to unexpected charges on your AWS account.  
> Don't forget to stop or terminate the resources after you are done with the project.  
> More details are here in [Important Instructions](#-important-instructions) section. 

## Update the project files:
1. Assuming that you have already created a fork of the repository and cloned it to your local machine.

1. If you have made any changes to the code, make sure to commit and push those changes to GitHub (to your own version of the project):
    ```bash
    # make sure you are in the project directory `aws_beginner_project`
    git add .
    git commit -m "Update project files"
    git push origin main
    ```

1. After you make any new changes, make sure to `add > commit > push` them to your GitHub repository.

1. If you get any errors or issues, ChatGPT is always a good friend to help you out 😅.



# 🤝 Contributions:

<table>
    <tbody>
    <tr>
        <td> 
            <img src="https://avatars.githubusercontent.com/Bbs1412" alt="Bhushan Songire" width="100" height="100">
        </td>
        <td> 
            <img src="https://avatars.githubusercontent.com/primegen-git" alt="Ujjawal Kumar" width="100" height="100">
        </td>
    </tr>
    <tr>
        <td> 
            <a href="https://github.com/Bbs1412">Bhushan Songire</a>
        </td>
        <td> 
            <a href="https://github.com/primegen-git">Ujjawal Kumar</a>
        </td>
    </tr>
</table>

- If you want to contribute to this project, please feel free to fork the repository and create a pull request.


# ⚖️ License:
- Project is licensed under the GNU General Public License v3.0 (GPL-3.0).
- See the [LICENSE](LICENSE) file for details.
- You are allowed to use code with **same license** and **proper attribution to the original author(s)**.


# 📧 Contact:
- **Email :** [bhushanbsongire@gmail.com](mailto:bhushanbsongire@gmail.com)
- **Email :** Ujjawal