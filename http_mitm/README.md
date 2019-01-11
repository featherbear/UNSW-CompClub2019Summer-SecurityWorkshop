# HTTP vs HTTPS / MITM Demo
---

> This demo explores the importance of HTTPS when dealing with confidential data in website.  

## Teaching Material
[Slides](https://docs.google.com/presentation/d/1ykIUm1xAKMforvTPeqvXMdC4DZlnWOg604ekaybhiOs/edit?usp=sharing)  

### Overview
Students are shown the lack of security over HTTP sites, by being able to see their credentials transmitted over a network in plain-text.  

User accounts are able to be compromised even if credentials are encrpyted (ie MD5).  

Performing the same tasks over HTTPS yields a change in results, where packet analysis no longer reveals the password

### Tools
* Server computer (w/ nodejs)
* Client computer
* [Wireshark](https://www.wireshark.org) / [Fiddler](https://www.telerik.com/fiddler) / network packet analyser

---
## Setup
### Generate SSL Certificate
```bash
cd ssl
openssl req -nodes -new -x509 -keyout server.key -out server.cert
```

### Install NodeJS Modules
`npm install`

---
## Run
`node server.js`
