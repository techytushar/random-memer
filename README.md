# Random Memer

Flask API to return random programming meme images scrapped from [Memedroid](https://www.memedroid.com/memes/tag/programming).

### Usage Notes:

Just add `img` tag in your website / README file and it will display a random meme everytime the website is loaded

```html
<img src='URL' title="Meme" alt="Please refresh the page if the meme doesn't show up.">
```

> **Deprecation Note:** The previous Heroku app link has stopped working due to Heroku [discontinuing its free tier services](https://blog.heroku.com/next-chapter). Deploy your own instance of the app using the links below and use them. 

## How to deploy

## Use [Railway](https://railway.app) (500 hours)

> **Note**
No delay

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/Hp9Kv4?referralCode=dUt24_)

* Sign in with GitHub to Deploy

* URL will produce after finish building

---

## Use [Replit](https://replit.com/) (unlimited hours)
> **Warning**
response delay of up to 30 seconds for the first request that comes in after a period of inactivity

<p align="left">
<a href="https://repl.it/github/trinib/random-memer">
  <img alt="Run on Repl.it" src="https://repl.it/badge/github/Ashutosh00710/github-readme-activity-graph" style="height: 50px; width: 200px;" />
</a></p>

* Click Import from GitHub Button

* Run `pip install gunicorn==20.0.4` and `pip install lxml` in console on the right

* Add line `app.run(host='0.0.0.0', port=80)` at the end of 'app.py' file

* Click the $\color{white} \colorbox{Green} {RUN}$ button on top, the console will run, wait to finish and output URL on the right under "Webview"

---

## Use [Render](https://render.com/) (750 hours)<br>
> **Warning**
response delay of up to 30 seconds for the first request that comes in after a period of inactivity

* Sign in https://dashboard.render.com/select-repo?type=static

* Enter in **Public Git repository** https://github.com/techytushar/random-memer and  click 'continue'

* Enter a name and add `gunicorn app:app` in **Start Command** option 

* Click 'Create Web Service' and wait until "==> Build successful 🎉" and server is Live

* Click URL link at top left (https://appname-xxxx.onrender.com)

---
