## Setup

### Requirements
* Docker: https://docs.docker.com/engine/install/ (Login required)
* Docker Compose: https://docs.docker.com/compose/install/

## Usage

* Docker image and scaffolding for running a webdriver on an M1 Macbook Pro.

#### Navigate to root folder and run the following commands:
```
chmod u+x ./scripts/*
./scripts/deploy
```

## Notes 

#### Troubleshooting:
If you get the following error message:
```
selenium.common.exceptions.WebDriverException: Message: Reached error page: about:neterror?e=netTimeout&u=https%3A...&c=UTF-8&d=The%20server%20at%%20is%20taking%20too%20long%20to%20respond.
```
Try:
```
./scripts/reset
```

## Useful commands:

#### Build container and run scraper:
```
./scripts/deploy
```

#### Run scraper:
```
./scripts/run
```

#### Open shell into container:
```
./scripts/shell
```

#### Refresh container (i.e., docker-compose stop + docker-compoes up):
```
./scripts/refresh
```

#### Reset container (i.e., remove and re-build container):
```
./scripts/reset
```
