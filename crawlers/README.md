![Screenshot](img/snoospider_bot2.png)

## 📝 Description

This application creates a telegram bot who scrap subredddits, fetching threads with more than 5k upvotes.</br>
It is part of a challenge proposed by idwall</br></br>

<center><table class="center" border="0" style="border: 1px solid transparent">
 <tr valign="top"><td>    
    <b>Table of contents:</b></br>
    <a href="#packages">1 Packages</a></br>
    <a href="#Software">2 Software required</a></br>
    <a href="#BuildingApp">3 Application setup</a> </br>
    <a href="#BuildingApp_1">3.1 Cloning the project</a> </br>
    <a href="#BuildingApp_2">3.2 Creating a telegram bot</a></br> 
    <a href="#BuildingApp_3">3.3 Running locally through Docker</a></br>
    <a href="#BuildingApp_3_1">3.3.1 Creating images and running containers</a></br>
    <a href="#BuildingApp_4">3.4 Heroku Deployment</a></br>
    <a href="#BuildingApp_4_1">3.4.1 Creating a new app in heroku</a></br>
    <a href="#BuildingApp_4_2">3.4.2 Deploying through Heroku</a></br> 
    <a href="#Using">4 Using the bot in a chat</a></br> 
    <a href="#tests">5 running tests</a>
    </td>
    <td><img src="img/using_snoospiderbot.gif"></td>
 </tr>
</table></center>

### 1 📦 Packages<a id="Packages"></a>
The packages used in this project were:
- **requests**: gets the page content as html 
- **beautiful Soup**: allows the navigation and extraction of relevant page contents
- **python-telegram-bot**: framework that implements telegram API to handle requests through pooling or webhook (was used pooling in this project)
- **Flask**: the docker container run in a heroku service using a free account who shutdown with 30 min of innactivity, was used flask to route a resource that can wake up the service easily
- **Gunicorn**: process incoming HTTP requests `concurrently`. the built-in Flask web server has `blocking` behavior and stops to answer while scraping is being executed
- **PyTest**: allows to run tests in the project</br>

Package versions used and dependencies are listed at ``requirements.txt`` 


### 2 💿 softwares required<a id="Software"></a>
In order to use this app you'll need:
- [python3](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## 3.1⚙️Application Setup<a id="BuildingApp"></a>

### 3.2 Cloning the project<a id="BuildingApp_1"></a>

Clone project:
```
$ git clone https://github.com/glauberdmo/desafios.git
```
and uses /crawlers/ as root for the next steps

### 3.3 📲Creating a telegram bot<a id="BuildingApp_2"></a>
Firstly, create a bot through the telegram app by talking to the @botfather, if you don't know how to do that please follow the [official documentation](https://core.telegram.org/bots#3-how-do-i-create-a-bot).</br>
You will need to go through this step to get his token with telegram API


### 3.4 🐳 Running locally through Docker<a id="BuildingApp_3"></a>

#### 3.4.1 Creating images and running containers<a id="BuildingApp_3_1"></a>
to create a new docker img, follow this cmds [(or create a pipeline and a app inside)](https://devcenter.heroku.com/articles/heroku-cli-commands#heroku-pipelines-add-pipeline):
```
docker build --tag telegram-bot .
docker run -e TOKEN=TELEGRAM_API_TOKEN_HERE -dp 80:80 telegram-bot
```
<b>note</b>: Heroku is not compatible with docker compose.</br>
Access your [localhost](https://localhost:80) to start the bot


### 3.4.2 Heroku Deployment<a id="BuildingApp_4"></a>
#### 3.5 Creating a new app in heroku<a id="BuildingApp_4_1"></a>
**you can skip this section if wants to run it locally through docker or use other container based service**
```
$ heroku apps:create [APP]
```
and define this enviroment vars:

```
$ heroku config:set TOKEN=TELEGRAM_API_TOKEN_HERE
```

#### 3.6 Deploying through Heroku<a id="BuildingApp_4_2"></a>
First you need go to ``Dockerfile`` and change ``80`` -> ``$PORT`` in row 11. Heroku define one port by dyno and needs to control it dynamically.</br>
in your bash:

```
heroku container:push web -a telegram-bot-challenge
```
The last cmd calls the docker to create a new image and pushes it to heroku service. We need to create a new image to consider the PORT we changed. If you know some way to improve it, open a issue!
Makes the deployment
```
heroku container:release web -a telegram-bot-challenge
```
Access your app website to wake up the bot.

## 4 🕹 Using the bot in a chat<a id="Using"></a>
To use the bot, send a message command following this format: 
```
/npf | /nadaprafazer subrredit_name1 subrredit_name2 ...
```
the subrredits names can be separated with any symbol, except "_"</br>

## 5 👁‍🗨 Running tests<a id="tests"></a>
It uses pytests to run the tests.</br>
In /crawler/ run:
```
pytest -s -v
```


