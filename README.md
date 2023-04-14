# Hospital Administration System

## What is this?

As part of our final project for IT6006: Secure Web Applicaiton Development with Server-Side Scripting we were tasked to build an enterprise-level applicaiton using Django. Our group decided to build a administration system for a Hospital. 

## Who worked on this?

| Name | Position |
| --- | ----------- |
| Inna Klishunova | Project Manager |
| Benjamin Charles Olds | Back-End Engineer |
| Gurjeet Kaur | Front-End Engineer |
| Shane Hislop | Database Engineer |
| Hyunwoo Jung | System Designer |
| Neelam Ranjit | System Designer |

## How do I use this?

* Pull the files or download an official release. 
* Create a new superuser in django, by copying the below code and following the prompts. 

`py manage.py createsuperuser`

* Make migrations, and migrate. 

`py manage.py migrate`

`py manage.py makemigrations`

## Common Bugs and How to Fix Them? 

### Operational Error

This is caused when the data model is altered and Django struggles to make changes, whilst this shouldn't happen with a completed Data Model, during development this did occur with associating ForeignKeys to pre-existing models. Note the following fix can reset the database to its primary form and remove data including any users permanently and should be a last resort. 

1. Delete db.sqlite3
2. Delete __pycache__
3. Delete migrations folders
4. Run the following commands

`py manage.py migrate --run-syncdb
`

`py manage.py makemigrations`

`py manage.py createsuperuser`
