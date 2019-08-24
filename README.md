# Freedy

![freedy](https://i.imgur.com/Z0P5UVL.jpg)

## What is Freedy?
Freedy is a free and simple RSS/ Atom reader for the browser, written in Python with Flask. Using Bootstrap as a mobile-first web framework, we were able to create a nice looking webapp for every kind of device.

## Features
- Looks great on tablets, phones etc. thanks to Bootstrap.
- Compatible with RSS and Atom feeds.
- Add as many feeds as you like!
- Amount of the recent posts shown of each feed can be configured.
- ... and of course the simple deployment via Docker ;)

## Usage
You basically just need to clone the repo, setup the virtualenv for the project and then run the flask/gunicorn server. Do not forget to enter your Atom/RSS feeds in the urls.txt file (one line for every entry).

We also recommend using a reverse proxy (eg. nginx) in front of the app for security reasons.

```bash
git clone https://github.com/konstantingoretzki/freedy && cd freedy/

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

pip install gunicorn

exec gunicorn -b :5000 --access-logfile - --error-logfile - freedy:app
```

## Docker deployment
Take a look at our [freedy-docker](https://github.com/konstantingoretzki/freedy-docker) repo for some instructions.




