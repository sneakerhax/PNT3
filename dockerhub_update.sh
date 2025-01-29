# build and push PNT3 to Docker Hub
docker buildx build --platform linux/amd64 -t sneakerhax/pnt3 -f ./Dockerfile . --push
# docker push sneakerhax/pnt3:latest