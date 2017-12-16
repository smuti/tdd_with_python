# Aim of this project

Book: ** TDD with Python Harry J.W. Percival ** 

Main aim is to apply Test Driven Development on a web project. In that project we will learn: 

- TDD methodology
- Functional Testing Fundamentals
- Integration Testing Fundamentals
- Unit Testing Fundamentals
- Python Django Framework
- HTML :)
- JavaScript
- Docker
- Makefile

# Major Functionalities for Web App(can be updated according to needs)

1- I have heard about a cool new online to-do app. I go to checkout its home page

2- I notice the page title and header mention to-do lists
		
3- I am invited to enter a to-do item straight away
		
4- I type "Buy peacock feathers" into text box. When I hit enter, the page updates, and now the page lists, "1: Buy peacock feathers" as an item in a to-do list

5- There is still a text box inviting me to add another item. I enter "Use peacock feathers to make a fly". The page updates again, and now shows both items in my list

6- I wonder whether site remembers my list. Then I see that the site has generated a unique URL for mine -- there is some explanatory text to that effect. I visit that URL - my to-do list is still there

# Setting up the development environment

## Required Software Installations

- Python3
- Firefox Web Browser
- [Git VCS](http://git-scm.com)
- pip3 (Python package management tool)
- Python Packages
	- Django 1.7, `sudo pip3 install django==1.7`
	- Selenium, `sudo pip3 install --upgrade selenium`
- Any IDE you like

## Getting Django Up and Running

`$ django-admin.py startproject superlists`
`$ python3 manage.py runserver`

Open a browser and type localhost:8000 as url.