# SpendWise

------------------------------------
### put main image here

You can view the site here [here](https://.herokuapp.com/). 

-----

## Table of Contents
--------------------------------------

- [Description](#description)
- [Design](#design)
- [Agile Development](#agile-development)
- [Features](#features)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
-
- [Author ](#author)

------
<br>

## Description
<br>
SpendWise is a website designed to help users track their spending and stay within their budget. With this app, users can easily add expenses as they occur, and the app will automatically calculate the total amount spent.

The user can also set an initial budget and the app will automatically deduct your expenses from your budget, giving you an up-to-date picture of your spending.

To use the app, users start by specifying an initial budget. They can then add expenses by entering the amount spent, along with a description of the expense. The app will subtract the total amount of the expenses from the total budget, so users can easily see how much they have left to spend.

The app is designed to be user-friendly, with a simple interface that makes it easy to enter and track expenses.

Overall, the expenses tracker app is a useful tool for anyone who wants to stay on top of their finances and make sure they are staying within their budget.

 heroku link to web


<br>

---

<br>

## Design/UX

<br>


#### Structure of the app

<br>

The app is designed to have a natural flow, with the main focus on basic crud functionality. All the pages include a header with navagation links to login/logout/sign up and navagation links to all the pages. The website includes a footer at the bottom of each page with links to social media.

-----


<br>

#### Wireframe

<br>

I used Balsamiq to build a wireframes for the website before I began developement. I decided on a relatively simple design so I could focus more on the backend of the project.

<br>

- Wireframe for the Home page

<br>



![alt text](/static/css/images/homewire.JPG)

-------------

<br>

- Wireframe for the Expenses page

<br>



![alt text](/static/css/images/expensewire.JPG)

-------------


<br>
<br>

## Agile Development

<br>


I used the Agile methodology for my project, which emphasizes collaboration, flexibility, and customer satisfaction. One of the key tools used in Agile development is user stories.

I created and managed user stories for my website project using github issues. I defined user stories for the features and functions. 

To map my user stories to GitHub project for my website, I created a GitHub repository for my project and used the GitHub project feature to track the user stories. I linked each user story to a GitHub issue and used a label to indicate priority.


<br>


---
### User Stories

<br>


<br>

I wrote these users stories and used github projects feature to track them

- Epic 1: User Register
	*  Sign-up - As a site user I can sign-up so that I use the website
	*  User Login - As a site user I can login into my account so that use the website
    *  User Logout - As a site user I can logout of my account so that stop using website features

- Epic 2: Expenses CRUD
	*  See expenses - As a site user I can see my expenses that were added so that track my spending
	*  Add expenses - As a site user I add new expenses so that I can keep track of all expenses
	*  Update expenses - As a site user I can edit an expense so that I make changes to my expenses
	*  Delete expenses - As a site user I can delete an expense so that I delete an expense that I dont want

<br>



![alt text](/static/css/images/userboard.JPG)

<br>

------

<br>



## Features
<br>

### Home Page

<br>

The home page gives the user information about the website. It allows them to register/login/logout and navagate to the Expenses page.

![alt text](/static/css/images/homes.JPG)

<br>

---------
<br>

### Expenses Page

<br>

THe expenses page allows users to create, add, update and delete expenses. They can adjust their total budget and see the expenses total subtracted from it. It also allows them to register/login/logout and navagate to the Home page

![alt text](/static/css/images/expenses.JPG)

<br>

---------

<br>

### Nav Bar

The nav bar allows site users to signup/login/register and visit each page.


![alt text](/static/css/images/nav.JPG)

---------

<br>

### Footer

<br>

The footer provides site users with links to social media.


![alt text](/static/css/images/footer.JPG)

<br>

---------

<br>

### User Register

<br>

This feature allows new users to register an account on the website. Users will need to provide two basic pieces of information which is their username and password to create an account. Once registered, they will be able to log in to your website and access the features that are available to registered users.

![alt text](/static/css/images/registerpage.JPG)

<br>

---------

<br>

### User Login 

<br>

This feature allows users who have already registered an account to log in to the website. Users will need to enter their username and password to access their account. Once logged in, they will be able to view their expenses, add new expenses, and use the budget calculator.
![alt text](/static/css/images/loginpage.JPG)

<br>

-----------

<br>

### User Logout

<br>

User logout: This feature allows users to log out of their account when they are finished using your website. Logging out ensures that their account remains secure and that no one else can access their expenses.
![alt text](/static/css/images/logoutpage.JPG)

<br>

---------------

<br>

### Budget calculator

<br>

This feature allows users to set a budget for a specific period, such as a month or a week, and track their expenses against that budget. Users can input their budget and their expenses will be subtracted from it. The calculator shows how much of their budget is left to spend
![alt text](/static/css/images/budgetformpage.JPG)
![alt text](/static/css/images/budgetdisplay.JPG)

<br>

----------

<br>

### Read Expenses

<br>

This feature allows users to view their existing expenses. Users can see a list of all their expenses on a single page.This feature helps users keep track of their spending and identify areas where they might need to cut back.
![alt text](/static/css/images/readexpenses.JPG)

<br>

------

<br>

### Create Expenses

<br>

This feature allows users to add new expenses to their account. Users can input details such as the date, amount and namen of each expense. This feature makes it easy for users to record their spending.
![alt text](/static/css/images/createxpense.JPG)

<br>

---------

<br>

### Update Expenses

<br>


This feature allows users to edit or update their existing expenses. Users can modify the details of an expense such as the date, amount, category, or description. This feature is useful when users make a mistake or need to make changes to their expenses.
![alt text](/static/css/images/editexpense.JPG)

<br>

------

<br>

### Delete Expenses

<br>
This feature allows users to remove an expense from their account. Users can delete an expense they no longer need, such as an expense that was entered in error or a duplicate expense. This feature helps users keep their expense records organized and up to date
![alt text](/static/css/images/deleteexpense.JPG)

<br>
<br>

------------

<br>





## Testing

The testing strategy for the website can be found here [Testing.md](https://github.com/Thomas-Longworth/Expense-tracker/blob/main/TESTING.md)










-----
## Technologies used


- HTML5: Usedfor the structure of the website.

- CSS: To style the website

- JavaScript: Used to add interactiviy to website.

- Python: Used to program django.

- Django: This was the main framework for the website..

- ElephantSQL: Used to host PostgreSQL database.

- Balsamiq: Used to design the websites wireframe.

### Packages used
![alt text](/static/css/images/pack.JPG)

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Expensed](https://dashboard.heroku.com/apps/expensed)

### Project Deployment

I deployed my project to Herou using the following steps:

- Login to [Heroku](https://www.heroku.com/).
- On the Heroku website, navagate to "Create New App".
- Name the project.
- This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
- Navagage to the Resources Tab and add 'Heroku Postgres' to the Add ons.
- Go to the settings tab, and copy the DATABASE_URL to the Config vars.
- Create an env.py file in the djagno repository. Import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. It should look like this: os.environ["DATABASE_URL"] = "Pasted URL".
- In the env.py file, create a secret key. It should look like this: os.environ["SECRET_KEY"] = " Your Secret key ".
- Copy your secret key and paste it into a Heroku config var. Use SECRET_KEY as the var key.
- Copy and paste the following into your projects settings.py file : from pathlib import Path, import os, import dj_database_url,if os,path.isfile("env.py"):import env.
- Remove djangos insecure key and replace it with: SECRET_KEY = os.environ.get('Your secret key').
- Comment out the database section the setting.py file. Replace it with: DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} .
- Add DISABLE_COLLECTSTATIC to Heroku Config Vars. Set the value to 1.
- Link the file to the templates directory in Heroku. Under the BASE_DIR line, insert the following  { TEMPLATES_DIR = os.path.join(BASE_DIR,'templates') }.
- Change the templates directory to TEMPLATES_DIR. It should look like this 'DIRS': [TEMPLATES_DIR].
- Add Heroku Hostname to ALLOWED_HOSTS. It should look like this:  ALLOWED_HOSTS =["ProjectName.herokuapp.com", "localhost"].
- Create 3 new folders on top level directory: media, static, templates.
- In the Settings.py file - add the STATIC files settings - storagepath, the url, directory path, root path, media url and default file storage path.
-  Make a new file call Procfile. Add the following code: web: gunicorn ProjectName.wsgi
- Add, commit and push all changes to Github.
- Navigate to the deployment tab in Heroku. Link your github repo to Heroku and deploy the branch manually. View the build log for any errors. It will dipslay a link to the live site.


### Forking the project

 
- Sign/regester in to Github and go to my repository at https://github.com/Thomas-Longworth/Expense-tracker .
- Navagage the Fork button at the top right of the page and select it.
- The fork is now created and copied to your repositories.


### Cloning the project
  
- Sign/regester in to Github and go to my repository at https://github.com/Thomas-Longworth/Expense-tracker .
- Select the green ‘code’ button.
- Choose which clone option you want(HTTPS, SSH or Github CLI). 
- Copy the url.
- Open git bash
- Type ‘git clone’ and then paste the URL you copied. Press Enter.

|




## Credits


- The images used on the website pexels.com, freely available images.
- The footer social media Icons were generated from font awesome and I took inspiration from Code Institutes love running project.

- I used Code institute's walthrough projects "Hello Django" and "I think, therefore I blog" to learn the Django fundamentals