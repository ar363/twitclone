# Twitclone

A website with features similar to twitter

Built with:
 - [Django](https://www.djangoproject.com/)
 - [Turbo from Hotwire](https://turbo.hotwired.dev/)
 - [TailwindCSS](https://tailwindcss.com/)


## Demo
https://quackquack.pythonanywhere.com/

## Requirements
 - Python3 (for django)
 - Nodejs LTS (for tailwind)


## Usage

Install the requirements

```
pip install -r requirements.txt
python manage.py tailwind install
```


Run Tailwind build
```
python manage.py tailwind start
```


Run Django server
```
python manage.py runserver
```

## Features:
 - Fully secure cookie auth with CSRF protection
 - Authentication with password, google or github
 - User with profile picture, full name and username
 - Smooth, PWA like feel with Turbo
 - Clean UI with TailwindCSS
 - Search option to find by user/tweet


## Todo:
 - add reply and retweet features
 - add like option
 - add user profile view
 - add option to delete tweets/users
 - restrict pfp image upload size limit
 - add user follow/unfollow options
 - add user block ability

