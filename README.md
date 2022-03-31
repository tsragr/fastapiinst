# fastapiinst
```
su
apt update; apt upgrade -y; apt install -y curl; curl -sSL https://get.docker.com/ | sh; curl -L https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
mkdir fastapi
cd fastapi
git init
git clone https://github.com/tsragr/fastapiinst.git
docker-compose build
docker-compose up -d
```
After go ahead http://0.0.0.0:8000/docs
