# build and push PNT3 to Docker Hub
docker build -t sneakerhax/pnt3 -f ./Dockerfile .
docker push sneakerhax/pnt3:latest