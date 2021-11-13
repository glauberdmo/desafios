![Screenshot](img/snoospider_bot.png)

## 📝 Description

This application creates a telegram bot who scrap subredddits fetching threads with too many upvotes.</br>

### Packages
The packages used in this project were:
- **requests**: gets the page content as html 
- **beautiful Soup**: allows the navigation and extraction of relevant page contents
- **python-telegram-bot**: framework that implements telegram API to handle requests through pooling or webhook
- **Flask**: the docker container run in a heroku service using a free account who shutdown with 30 min of innactivity, was used flask to route a resource that can wake up the service easily
- **Gunicorn**: process incoming HTTP requests `concurrently`. the built-in Flask web server has `blocking` behavior and stops to answer while scraping is being executed

Package versions used and dependencies are listed ``requirements.txt`` 

### softwares
To use this app is needed:
- [python3](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Building app

### Clone project

Clone project:
```
$ git clone https://github.com/glauberdmo/desafios.git
```
and uses /crawlers/ as root for the next steps

### Create a telegram bot
First create a bot through telegram app talking with @botfather, if you don't know how to do that follow the [official documentation](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
you will need to make this step to get his token with telegram API

### Creates a new app in heroku:
**you can skip this section if wants to run it locally through docker or use other container based service**
```
$ heroku apps:create [APP]
```
and define this enviroment vars:

```
$ heroku config:set TOKEN=TELEGRAM_API_TOKEN_HERE
```

### Creating image and running through Docker:
to create a new docker img, follow this cmds [(or create a pipeline and a app inside)](https://devcenter.heroku.com/articles/heroku-cli-commands#heroku-pipelines-add-pipeline):
```
docker build --tag telegram-bot .
docker run -e TOKEN=TELEGRAM_API_TOKEN_HERE -dp 80:80 telegram-bot
```
note: Heroku are not compatible with docker compose
Access your [localhost](https://localhost:80) to start the bot

### Deploying through Heroku
First you need go to ``Dockerfile`` and change ``80`` -> ``$PORT`` in row 11. Heroku define one port by dyno and needs to control it dynamically.
in your bash:

```
heroku container:push web -a telegram-bot-challenge
```
The last cmd calls the docker to create a new image and push to heroku service. We need to create a new image because the PORT change. If you know some way to improve it, open a issue!
Makes the deployment
```
heroku container:release web -a telegram-bot-challenge
```
Access his web

## 📝 Using bot
To use the bot, send a message command follow this format: 
```
/npf | /nadaprafazer subrredit_name1 subrredit_name2 ...
```
the subrredits names can be separated with any symbol, except "_"


![Screenshot](img/using_snoospiderbot.gif)

Use /npf
```bash
go install github.com/create-go-app/cli/v3/cmd/cgapp@latest
```

Also, macOS and GNU/Linux users available way to install via [Homebrew](https://brew.sh/):

```bash
# Tap a new formula:
brew tap create-go-app/cli
# Installation:
brew install create-go-app/cli/cgapp
```

Let's create a new project via **interactive console UI** (or **CUI** for short) in current folder:

```bash
cgapp create
```

Next, open the generated Ansible inventory file (called `hosts.ini`) and fill in the variables according to your server configuration. And you're ready to **automatically deploy** this project:

```bash
cgapp deploy
```

That's all you need to know to start! 🎉

### 🐳 Docker-way to quick start

If you don't want to install Create Go App CLI to your system, you feel free to using our official [Docker image](https://hub.docker.com/r/koddr/cgapp) and run CLI from isolated container:

```bash
docker run --rm -it -v ${PWD}:${PWD} -w ${PWD} koddr/cgapp:latest [COMMAND]
```

> 🔔 Please note: the `deploy` command is currently **unavailable** in this image.
## 📖 Project Wiki

The best way to better explore all the features of the **Create Go App CLI** is to read the project [Wiki](https://github.com/create-go-app/cli/wiki) and take part in [Discussions](https://github.com/create-go-app/cli/discussions) and/or [Issues](https://github.com/create-go-app/cli/issues). Yes, the most frequently asked questions (_FAQ_) are also [here](https://github.com/create-go-app/cli/wiki/FAQ).

## ⚙️ Commands & Options

### `create`

CLI command for create a new project with the interactive console UI.

```bash
cgapp create [OPTION]
```

| Option | Description                                              | Type   | Default | Required? |
| ------ | -------------------------------------------------------- | ------ | ------- | --------- |
| `-t`   | Enables to define custom backend and frontend templates. | `bool` | `false` | No        |

![cgapp_create](https://user-images.githubusercontent.com/11155743/116796937-38160080-aae9-11eb-8e21-fb1be2750aa4.gif)

- 📺 Full demo video: https://recordit.co/OQAwkZBrjN
- 📖 Docs: https://github.com/create-go-app/cli/wiki/Command-create

### `deploy`

CLI command for deploy Docker containers with your project via Ansible to the remote server.

> 🔔 Make sure that you have [Python 3.8+](https://www.python.org/downloads/) and [Ansible 2.9+](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-specific-operating-systems) installed on your computer.
```bash
cgapp deploy [OPTION]
```

| Option | Description                                                                                            | Type   | Default | Required? |
| ------ | ------------------------------------------------------------------------------------------------------ | ------ | ------- | --------- |
| `-k`   | Prompt you to provide the remote user sudo password (_a standard Ansible `--ask-become-pass` option_). | `bool` | `false` | No        |

![cgapp_deploy](https://user-images.githubusercontent.com/11155743/116796941-3c421e00-aae9-11eb-9575-d72550814d7a.gif)

- 📺 Full demo video: https://recordit.co/ishTf0Au1x
- 📖 Docs: https://github.com/create-go-app/cli/wiki/Command-deploy

## 📝 Production-ready project templates

### Backend

- Backend template with Golang built-in [net/http](https://golang.org/pkg/net/http/) package:
  - [`net/http`](https://github.com/create-go-app/net_http-go-template) — simple REST API with CRUD and JWT auth.
- Backend template with [Fiber](https://github.com/gofiber/fiber):
  - [`fiber`](https://github.com/create-go-app/fiber-go-template) — complex REST API with CRUD, JWT auth with renew token, DB and cache.

### Frontend

- Pure JavaScript frontend template:
  - `vanilla` — generated template with pure JavaScript app.
  - `vanilla-ts` — generated template with pure TypeScript app.
- Frontend template with [React](https://reactjs.org/):
  - `react` — generated template with a common React app.
  - `react-ts` — generated template with a TypeScript version of the React app.
- Frontend template with [Preact](https://preactjs.com/):
  - `preact` — generated template with a common Preact app.
  - `preact-ts` — generated template with a TypeScript version of the Preact app.
- Frontend template with [Vue.js](https://vuejs.org/):
  - `vue` — generated template with a common Vue.js app.
  - `vue-ts` — generated template with a TypeScript version of the Vue.js app.
- Frontend template with [Svelte](https://svelte.dev/):
  - `svelte` — generated template with a common Svelte app.
  - `svelte-ts` — generated template with a TypeScript version of the Svelte app.
- Frontend template with [Lit](https://lit.dev/) web components:
  - `lit-element` — generated template with a common Lit app.
  - `lit-element-ts` — generated template a TypeScript version of the Lit app.

> ☝️ Frontend part will be generate using awesome tool [Vite.js](https://vitejs.dev/) under the hood. So, you'll always get the latest version of `React`, `Preact`, `Vue`, `Svelte`, `Lit` or pure JavaScript/TypeScript templates for your project!
>
> Please make sure that you have `npm` version `7` or higher installed to create the frontend part of the project correctly. If you run the `cgapp create` command using our [Docker image](https://hub.docker.com/r/koddr/cgapp), `npm` of the correct version is **already** included.
## 🚚 Pre-configured Ansible roles

### Web/Proxy server

- Roles for run Docker container with [Traefik Proxy](https://traefik.io/traefik/):
  - `traefik` — configured Traefik container with a simple ACME challenge via CA server.
  - `traefik-acme-dns` — configured Traefik container with a complex ACME challenge via DNS provider.
- Roles for run Docker container with [Nginx](https://nginx.org):
  - `nginx` — pure Nginx container with "the best practice" configuration.

> ✌️ Since Create Go App CLI `v2.0.0`, we're recommend to use **Traefik Proxy** as default proxy server for your projects. The main reason: this proxy provides _automatic_ SSL certificates from Let's Encrypt out of the box. Also, Traefik was built on the Docker ecosystem and has a _really good looking_ and _useful_ Web UI.
### Database

- Roles for run Docker container with [PostgreSQL](https://postgresql.org/):
  - `postgres` — configured PostgreSQL container with apply migrations for backend.

### Cache (key-value storage)

- Roles for run Docker container with [Redis](https://redis.io/):
  - `redis` — configured Redis container for backend.

## ⭐️ Project assistance

If you want to say **thank you** or/and support active development of `Create Go App CLI`:

- Add a [GitHub Star](https://github.com/create-go-app/cli) to the project.
- Tweet about project [on your Twitter](https://twitter.com/intent/tweet?text=%E2%9C%A8%20Create%20a%20new%20production-ready%20project%20with%20%23Golang%20backend%2C%20%23JavaScript%20or%20%23TypeScript%20frontend%2C%20%23Docker%20and%20%23Ansible%20deploy%20automation%20by%20running%20one%20command.%20%0A%0AFocus%20on%20writing%20code%20and%20thinking%20of%20business-logic%21%0AThe%20CLI%20will%20take%20care%20of%20the%20rest.%0A%0Ahttps%3A%2F%2Fgithub.com%2Fcreate-go-app%2Fcli).
- Write interesting articles about project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or personal blog.
- Join DigitalOcean at our [referral link](https://m.do.co/c/b41859fa9b6e) (your profit is **$100** and we get $25).

<a href="https://www.producthunt.com/posts/create-go-app?utm_source=badge-review&utm_medium=badge&utm_souce=badge-create-go-app#discussion-body" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/review.svg?post_id=316086&theme=light" alt="Create Go App - Create a new production-ready project by one CLI command | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

Together, we can make this project **better** every day! 😘

## ⚠️ License

`Create Go App CLI` is free and open-source software licensed under the [Apache 2.0 License](https://github.com/create-go-app/cli/blob/master/LICENSE). Official [logo](https://github.com/create-go-app/cli/wiki/Logo) was created by [Vic Shóstak](https://shostak.dev/) and distributed under [Creative Commons](https://creativecommons.org/licenses/by-sa/4.0/) license (CC BY-SA 4.0 International).