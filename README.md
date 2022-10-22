# Random Memer

Flask API to return random programming meme images scrapped from [Memedroid](https://www.memedroid.com/memes/tag/programming).

To use just send a GET request to [https://random-memer.herokuapp.com/](https://random-memer.herokuapp.com/)

You can also use this with `img` tag in your website and it will display a random meme everytime the website is loaded

```html
<img src='https://random-memer.herokuapp.com/' title="Meme" alt="Please refresh the page if the meme doesn't show up.">
```

### Usage Notes:

* The API is deployed on Heroku free dyno which provides certain number of free compute hours per month, so app might stop working at the end of the month. You can deploy your own instance of the app on Heroku for free and use that.
* The API is deployed on the free dyno provided by Heroku, which shuts-down if there is no request to it for some time, so sometimes it might take some time to load the image from the URL.

