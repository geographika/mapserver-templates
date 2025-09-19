# Install Digital Ocean doctl - see https://docs.digitalocean.com/reference/doctl/how-to/install/

start "C:\Program Files\Docker\Docker\Docker Desktop.exe"
cd D:\GitHub\mapserver-templates\docker

docker build `
    --tag "geographika-mapserver:mapserver-homepage" `
    --target=runner `
    --build-arg=MAPSERVER_BRANCH=mapserver-homepage `
    --build-arg=MAPSERVER_REPO=https://github.com/geographika/mapserver `
    .

# to get any latest changes from github
docker build --no-cache `
    --tag "geographika-mapserver:mapserver-homepage" `
    --target=runner `
    --build-arg=MAPSERVER_BRANCH=mapserver-homepage `
    --build-arg=MAPSERVER_REPO=https://github.com/geographika/mapserver `
    .

# test - but when using bash the mapserv exe won't start so we can't connect using a port

docker run -it `
    --name mapserver-homepage `
    geographika-mapserver:mapserver-homepage bash

docker start mapserver-homepage
docker exec -it mapserver-homepage bash

# within the image
mapserv -v


docker run -it `
    --name mapserver-homepage `
    -p 8080:8080 `
    geographika-mapserver:mapserver-homepage

# copy file to container for testing

# docker cp D:\MapServer\VS2022\mapserver\msautotest\config\index.conf mapserver-homepage:/usr/local/share/mapserver/config/index.conf
# docker cp D:\MapServer\VS2022\mapserver\msautotest\config\index_wms.map mapserver-homepage:/usr/local/share/mapserver/config/index_wms.map

#  msSaveImage(): Unable to access file. Failed to create output file (/usr/local/share/mapserver/config/Kitchensink Demo Mapfile175812282169.png

http://localhost:8080/?map=/etc/mapserver/mapfiles/test.map&service=WFS&request=GetCapabilities
http://localhost:8080/server-status-remote

doctl auth init
# generate new temporary token
doctl registry login

# tag (need to run this after each change)
docker tag geographika-mapserver:mapserver-homepage registry.digitalocean.com/geographika/geographika-mapserver:mapserver-homepage

# any updates pushed cause the app to rebuild
docker push registry.digitalocean.com/geographika/geographika-mapserver:mapserver-homepage
