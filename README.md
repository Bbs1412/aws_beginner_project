<img src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/amazonwebservices-original-wordmark.svg" alt="AWS" width="60" align="left">

# `Beginner Project`

- This is the project developed as part of the AWS course. The project is a simple Travel Guide application that gives information about various travel destinations.
- It utilizes various AWS services under free-tier limits, making it beginner-friendly.
- We faced a lot of challenges during development and deployment, so we've documented everything in detail to help others who might run into similar issues.
- Also, there are two versions of this project, it will be described in detail below.


# Index:
- [Project Details](#-project-details)
    - [Aim](#aim)
    - [Features](#features)
    - [Architecture](#architecture)
    - [Warning](#warning)
    - [Tech Stack](#-tech-stack)
    - [Another Version](#another-version)
- [Steps to run](#-steps-to-run)
- [To make changes](#%EF%B8%8F-to-make-changes)
- [Steps to deploy](#-steps-to-deploy)
- [Important Instructions](#%EF%B8%8F-important-instructions)
- [Cleanup](#-cleanup)
- [Contributions](#-contributions)
- [License](#%EF%B8%8F-license)
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
<image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/architecture.png" alt="Project Architecture Diagram" style="width: 550px;">

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
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/html5-plain.svg" alt="HTML-icon" height=45></td>
            <td>HTML/CSS/JS</td>
            <td>Pretty obvious beginner-friendly web technologies for building the frontend.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/flask-original-wordmark.svg" alt="Flask-icon" height=50></td>
            <td>Flask</td>
            <td>A lightweight Python web framework to serve the web application.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/sqlite-original.svg" alt="SQLite-icon" height=45></td>
            <td>SQLite-3</td>
            <td>A simple file based database for storing travel destination data.</td>
        </tr>
        <tr>
            <th colspan="3">AWS Services</th>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/EC2.svg" alt="AWS-icon" height=45></td>
            <td>AWS EC2</td>
            <td>For hosting the web application.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/Elastic Block Store.svg" alt="EBS-icon" height=45></td>
            <td>AWS EBS</td>
            <td>For persistent instance storage.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/Simple Storage Service.svg" alt="S3-icon" height=45></td>
            <td>AWS S3</td>
            <td>For hosting the static website assets.</td>
        </tr>
        <tr>
            <th colspan="3">(Optional) You can add these services easily</th>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/RDS.svg" alt="RDS-icon" height=45></td>
            <td>AWS IAM</td>
            <td>For managing access to AWS services with roles and policies.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/CloudWatch.svg" alt="CloudWatch-icon" height=45></td>
            <td>AWS CloudWatch</td>
            <td>For monitoring instance performance and logs.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/CloudTrail.svg" alt="CloudTrail-icon" height=45></td>
            <td>AWS CloudTrail</td>
            <td>For tracking user activity and API usage.</td>
        </tr>
        <tr>
            <td><image src="./Docs/Budgets.svg" alt="Budgets-icon" height=45></td>
            <td>AWS Budgets</td>
            <td>For setting up cost and usage budgets to avoid unexpected charges.</td>
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


# 🚀 Steps to run:
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


# 🌐 Steps to deploy:

> [!CAUTION]
> Avoid doing anything un-necessary in the AWS console, unless you know what you are doing.  
> It can lead to unexpected charges on your AWS account.  
> Don't forget to stop or terminate the resources after you are done with the project.  
> More details are here in [Important Instructions](#-important-instructions) and [Cleanup](#-cleanup) sections.

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

> [!TIP]
> AWS resources can be used across various regions.
> Make sure that you always select the same region for all the resources you create, to avoid any issues later. (Regions are visible in the top right corner of the AWS console.)
> Default region is `us-east-1`, so you can use that for all the resources.


## Set Up S3 Bucket (Optional):
- In the project code files, static assets are served from the EC2 instance itself.
- Optionally, you can use S3 to serve the static assets.
- Make the below mentioned changes first:
    - Uncomment the S3 bucket code in the [`static/script.js`](static/script.js#L39) and [`templates/place_detail.html`](templates/place_detail.html#L49).
    - Fill in the S3 URL in the [`app.py`](app.py).
    - Commit new changes to github.
- Now, you can follow these steps to create S3 bucket and upload the static assets with public access:
    1. Go to the [AWS Console](https://console.aws.amazon.com/) and log in to your AWS account.
    1. Navigate to the S3 service. (You can search for "S3" in the search bar.)
    1. Click on "Create bucket".
    1. Name you bucket something like `travel-guide-project` (or any unique name) 
    1. Keeping other settings to their defaults, scroll down to ***Block Public Access settings for this bucket*** section and uncheck the **Block all public access** option. Acknowledge the warning and click on **Create bucket** button.
    1. If name is already taken, you can try with a different name.
    
- Add `Bucket Policy` to allow public access to the bucket:
    1. Click on the bucket name you just created.
    1. Go to the **Permissions** tab.
    1. Scroll down to the **Bucket policy** section and click on **Edit**.
    1. Add the following policy, replacing `travel-guide-project` with your actual bucket name:
        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::travel-guide-project/*"
                }
            ]
        }
        ```
    1. Click on **Save changes**.
    
- Test the bucket:
    1. Go to the bucket you just created.
    1. Click on the **Upload** button and upload some test image file to the bucket.
    1. Once uploaded, click on the file name to view its details.
    1. On the page, you will see the **Object URL**. This is the public URL of the file you just uploaded.
    1. Try checking file url on another browser or in incognito mode. It should be accessible publicly.

- Now, you can add all the assets from [static/images](static/images) directory to the S3 bucket using same file upload method.



# 🧹 Cleanup:

## S3 Bucket:
1. To delete the S3 bucket, go to the S3 service in the AWS console.
1. First you need to clear all the objects in the bucket before deleting it.
1. Click on the bucket name you created, then go to the **Objects** tab.
1. Select all the objects in the bucket and press **Delete** button.
1. Follow any extra steps on the screen to confirm deletion of objects.
1. Now go back to the **Buckets** tab, select the bucket you want to delete, and click on the **Delete** button.
1. Confirm the deletion by typing the bucket name when prompted.



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