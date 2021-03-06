<p align="center"><img src ="https://imghost.io/images/2017/11/12/logo.png" /></p>


*Debt-o-mator is my first Python 3/Django project. It's used for managing debts of registered users.
It helps to control who is in debt and to which user the debtor needs to give money back.*


## Prerequisites

You need Python 3 installed and Django framework.  
How to get them?:

```
https://www.python.org/downloads/
https://docs.djangoproject.com/en/1.11/topics/install/
```

### Setting up

**These commands are based for Linux, but they can be same or similar when using other OS.**
  
  
When you dowloaded a project, you need to go to main directory of project ("Debt-o-mator"). 

After reaching that directory you need to use this command for making a migration.  
In our case:

```
$ python manage.py makemigrations
```

After that you need to do a migration. By that you will create a sqlite3 database:

```
$ python manage.py migrate --run-syncdb
```

Next we need to import data from fixture to make categories available:

```
$ python manage.py loaddata accounts/migrations/fixtures/category.json
```

You also need to create superuser/admin for using administration panel:

```
$ python manage.py createsuperuser
```

Finally we can run the server:

```
$ python manage.py runserver
```


## Using in browser

Default address to connect to the website:

```
http://127.0.0.1:8000
```

At the start when no one is signed in you can have access only for Sign in or Sign up screen.


### Sign in

Simply put Username and Password of the existing user to the appropriate fields.


### Sign up

If you are on Sign in screen click Sign up button below. Fill up fields according to the instructions showed on screen.


### Creating a debt

When you are signed in you have option to Create a debt and Check debts. Click Create a debt button.
Choose who is a debtor, who should receive money, for what, category, amount and click Add debt.


### User informations

Check debts button is used for it.
It will show you all records connected with your username, total amount of debts and total amount of debts for exact user.
Deleting a record is only available for person which appears in "Whom to pay off?".


### Administration panel

You can add/edit/delete debts, categories and users.  
Of cource only for users with superuser permissions.
  
Administration panel is achievable at this link:

```
http://127.0.0.1:8000/admin
```

## Screenshots

![alt text](https://imghost.io/images/2017/12/02/ZrzutekranuDeepin_wybierz-obszar_20171202125112.png)
![alt text](https://imghost.io/images/2017/12/02/ZrzutekranuDeepin_wybierz-obszar_20171202125402.png)
![alt text](https://imghost.io/images/2017/12/02/ZrzutekranuDeepin_wybierz-obszar_20171202125439.png)
![alt text](https://imghost.io/images/2017/12/02/ZrzutekranuDeepin_wybierz-obszar_20171202125921.png)
![alt text](https://imghost.io/images/2017/12/02/ZrzutekranuDeepin_wybierz-obszar_20171202125953.png)

## Tools used in project

* [Antergos 17.10](https://antergos.com) - System used to make this project
* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Python 3.6](https://www.python.org) - Python
* [Django](https://www.djangoproject.com) - Python's framework for web development
* [Skeleton-Plus](https://github.com/oldaniel/skeleton-plus) - boilerplate for changing site appearance
