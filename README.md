# Student-Resume-Builder

We have tried to create a resume builder website to the best of our knowledge. Firstly the user gets an option to register or login and then he/she can begin with the journey of building a resume. After the user has been authenticated, he/she would be redirected to the dashboard which has options like - Create/Edit your Resume, View your Resume, Switch your Resume Template and Logout. The user needs to fill in his/her details and then choose one out of the three templates. One of the templates is a pro-template which has a razorpay payment-gateway integrated with it and would demand the user to pay Rupees 500. The resume would be stored in the database along with other details of the user which can be accessed as and when required.

Steps to set-up the project on your system-

## Fork and clone this repository

```git clone ```

## Change Directory

```cd studentResumeBuilder```

## Set up the .env file and settings.py

Create a .env file mentioning <br />
DEBUG=True <br />
PASSWORD="your_mysql_password"

Go to settings.py and change the username. 
Create a MySQL database named 'studentResumeBuilder' in your system.

## Install Dependencies
Install the required dependencies including razorpay, python-decouple, pymysql, mysqlclient, etc.

## Run the Migrate Command
Go to the terminal and run the following commands :

```python manage.py makemigrations``` <br />
```python manage.py migrate``` <br />
```python manage.py runserver``` <br />


## Happy Resume Building!
