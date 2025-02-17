<a href="https://www.gitpod.io#gh-light-mode-only">
  <img src="https://github.com/gitpod-io/gitpod/assets/55068936/01a00b23-e1f5-4650-a629-89db8e300708" style="width: 256px">
</a>
<a href="https://www.gitpod.io#gh-dark-mode-only">
  <img src="https://github.com/gitpod-io/gitpod/assets/55068936/ff437ec6-adda-4814-9e92-fff44cfd00ad" style="width: 256px">
</a>

# Always ready-to-code 🍊
Gitpod is the developer platform for on-demand Cloud Development Environments (CDEs). Say goodbye to slow onboarding and unmanageable dev environments. Gitpod removes pain and frustration from your developer experience, helps you deliver software faster, and makes you more secure and compliant. 

## Why Gitpod?
Here are some of the reasons devops, security, and finance teams love Gitpod:

👩🏻‍💻 Faster developer onboarding  
⚙️ Eliminate software dependency issues  
🤝 Collaborate async or in real time  
☁️ Utilize the compute power of the cloud  
💰 Save money on hardware and virtual infrastructure  
🔐 Secure and protect your code and dev environments

## Gitpod Demo
This repo contains a simple voting application that can be launched in Docker compose. You can try it yourself right now! Simply click the link below to launch a new Gitpod workspace where you can play with the voting application in any web browser. No extra software is required, all you need is a free Gitpod account:

https://gitpod.io/#https://github.com/gitpod-demos/voting-app

## Architecture

![Architecture diagram](architecture.excalidraw.png)

* A front-end web app in [Python](/vote) which lets you vote between two options
* A [Redis](https://hub.docker.com/_/redis/) which collects new votes
* A [.NET](/worker/) worker which consumes votes and stores them in…
* A [Postgres](https://hub.docker.com/_/postgres/) database backed by a Docker volume
* A [Node.js](/result) web app which shows the results of the voting in real time

You can also use the [Gitpod browser extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki) to launch a workspace from *any* Github repo of your choice!
