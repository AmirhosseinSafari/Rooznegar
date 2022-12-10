# Rooznegar, an online news survey

In today's world, Due to the huge volume of news in different news sources, tracking news from these sources is a time-consuming task and due to the difference in the way news is displayed on different news websites, it causes the user to be slow or confused in following the news. It should also be mentioned that users are usually interested in checking and comparing news from several sources; Therefore, it is important to have a platform for presenting news from different news sources at once and a display format.

`Rosnegar` program is an online Farsi newsletter that was created to solve this problem. This program collects news from several Irianian online news outlets, including including Islamic Republic of Iran Radio and Television, Tasnim, Rasa, Rozno, and Students of Iran (ISNA) and then categorizes these news using artificial intelligence technology into appropriate topics for each news item. It has tried to make it easier for users to follow the news.

## File structure and content of them
| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/api`               | Backend API of news                        |
| `/backend`           | Django Project & Backend Config            |
| `/backend_news`      | News model & AI model & web scraper        |
| `/backend_news/newsman`      | Fetching news from other news websites (web scraping) |
| `/src`               | Vue App                                    |
| `/src/main.js`       | JS Application Entry Point                 |
| `/public/index.html` | Html Application Entry Point               |
| `/public/static`     | Static Assets                              |
| `/dist/`             | Bundled Assets Output (generated at `yarn build`) |

```bash
.
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── app.json
├── backend
│   ├── settings
│   │   ├── dev.py
│   │   ├── __init__.py
│   │   ├── prod.py
│   ├── urls.py
│   └── wsgi.py
├── backend_news
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_news_creation_time.py
│   │   ├── 0003_auto_20220816_0805.py
│   │   ├── 0004_auto_20220816_0812.py
│   │   ├── 0005_auto_20220817_0424.py
│   │   ├── 0006_auto_20220818_2245.py
│   │   ├── 0007_news_body.py
│   │   ├── 0008_news_source.py
│   │   └── __init__.py
│   ├── models.py
│   ├── my_dumped_classifier.pkl
│   ├── newsman
│   │   ├── 100_news.json
│   │   ├── dataExtracter.py
│   │   ├── lastNewsUpdate.txt
│   │   ├── news.json
│   │   ├── newsman
│   │   │   ├── __init__.py
│   │   │   ├── items.py
│   │   │   ├── middlewares.py
│   │   │   ├── pipelines.py
│   │   │   ├── settings.py
│   │   │   └── spiders
│   │   │       ├── __init__.py
│   │   │       ├── news_spider.py
│   │   └── scrapy.cfg
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── dist
│   ├── index.html
│   └── static
│       ├── css
│       │   ├── app.a44d0384.css
│       │   └── chunk-vendors.0ea4d1d3.css
│       ├── favicon.ico
│       └── js
│           ├── app.4a38c89b.js
│           ├── app.4a38c89b.js.map
│           ├── chunk-vendors.41368f00.js
│           └── chunk-vendors.41368f00.js.map
├── LICENSE
├── manage.py
├── node_modules
├── package.json
├── package-lock.json
├── Pipfile
├── Pipfile.lock
├── Procfile
├── public
│   ├── index.html
│   └── static
│       └── favicon.ico
├── README.md
├── requirements.txt
├── run.sh
├── src
│   ├── App.vue
│   ├── assets
│   │   ├── logo-django.png
│   │   ├── logo-vue.png
│   │   └── Spinner-0.9s-250px.gif
│   ├── components
│   │   ├── Loading.vue
│   │   ├── NewsObject.vue
│   │   └── News.vue
│   ├── main.js
│   ├── router.js
│   ├── services
│   │   ├── api.js
│   │   └── newsService.js
│   └── store
│       ├── index.js
│       └── modules
│           └── news.js
├── vue.config.js
└── yarn.lock
```



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
