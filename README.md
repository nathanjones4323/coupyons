<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="./logo.png" alt="Project logo"></a>
</p>

<h3 align="center">Grocery Coupon Clipper</h3>

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 Clips all of the Digital Coupons for your go to grocery chain.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## 🧐 About <a name = "about"></a>

Scanning through coupons in your grocery store's app is so boring and time consuming. Everyone likes to save money, but the time spent finding coupons is not worth the $10 or less you might save on your trip to the grocery store. This bot will clip all of the digital coupons under your account, so you can just shop for your regular list and save money *passively*. 

> :warning: **Right now the bot only works for Albertsons**

## 🏁 Getting Started <a name = "getting_started"></a>

TODO

### Prerequisites

Docker ([Docker Desktop comes with Docker](https://www.docker.com/products/docker-desktop/))

## Running the App <a name = "usage"></a>

Replace the following environment variables in `main.py` with your login credentials:

`os.environ["albertsons_email_1"]`
`os.environ["albertsons_password_1"]`
`os.environ["albertsons_email_2"]`
`os.environ["albertsons_password_2"]`

If you have more than 2 accounts you want to clip coupons for, you can simply add them the the `usernames` and `passwords` list in order.

Clone the repoisitory
```
git clone {repo}
```

Navigate to the app's directory
```
cd && cd coupyons
```

Run the following in your terminal:
```
docker-compose up -d
```

> :warning: If you need to rebuild and run the container run this command
```
docker-compose up --force-recreate --build -d && docker image prune -f
```