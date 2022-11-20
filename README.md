# Rooznegar, an online news survey

In today's world, Due to the huge volume of news in different news sources, tracking news from these sources is a time-consuming task and due to the difference in the way news is displayed on different news websites, it causes the user to be slow or confused in following the news. It should also be mentioned that users are usually interested in checking and comparing news from several sources; Therefore, it is important to have a platform for presenting news from different news sources at once and a display format.

`Rosnegar` program is an online Farsi newsletter that was created to solve this problem. This program collects news from several Irianian online news outlets, including including Islamic Republic of Iran Radio and Television, Tasnim, Rasa, Rozno, and Students of Iran (ISNA) and then categorizes these news using artificial intelligence technology into appropriate topics for each news item. It has tried to make it easier for users to follow the news.

## Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install)
- [X] Vue CLI 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3 - [instructions](https://wiki.python.org/moin/BeginnersGuide)
- [X] Pipenv - [instructions](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)

## Setup
First run command below to install dependencies and setting up:
```
$ yarn install
$ pipenv install
$ pipenv shell
$ pip install jdatetime
$ pip install convert_numbers
$ python manage.py migrate
```

## Running Development Servers
You can run development servers by commands below (you will need `three` shells) :

### `Shell No.1`
Shell No.1 will keep the scrapers up and running and also refetching the news every 2 hours autometically (be patient so the program fetches all news, it will take some minutes up to your internet conection speed):
```
./run.sh
```
### `Shell No.2`
Running the backend:
```
$ python manage.py runserver
```
### `Shell No.3`
Running the frontend (in the first run it will take some few minutes to insert all news to database, after loading page fades away, refresh youe brower tab) :
```
$ yarn serve
```

The Vue application will be served from [`localhost:8080`](http://localhost:8080/) and the Django API
and static files will be served from [`localhost:8000`](http://localhost:8000/).

The dual dev server setup allows you to take advantage of
webpack's development server with hot module replacement.
Proxy config in [`vue.config.js`](/vue.config.js) is used to route the requests
back to django's API on port 8000.

If you would rather run a single dev server, you can run Django's
development server only on `:8000`, and you have to build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python manage.py runserver
```

### Program features
* Ability to view all the news announcements with tags related to each news
* Display the full text of the news by clicking on the read more option
* Display the news history and provide a link to the news source
* Display the subject detected by the artificial intelligence model
* Displaying all Persian pages
* Ability to load more news by reaching the bottom of the page
* Refetching the news almost every 2 hours
        

### Technologies used:
* Django as backend
* Django REST framework
* Django Whitenoise for static files
* Vue CLI 3 as frontend
* Vue Router for routing
* Vuex as state management pattern
* Scrapy as web scraper
* Beautiful soup as web scraper
* Bash scripting for keep scrapers running
* Sqlite3 as database
* SVM classifier as AI model classifier
* Bulma as CSS framework

(I should mention that I used [gtalarico](https://github.com/gtalarico/django-vue-template) vue + django template for this project.)
