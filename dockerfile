# Node image on builder
FROM node:10 AS builder
# Set work directory
WORKDIR /app
# Copy project into ../front
COPY /front .
# Install and build project
RUN yarn install && yarn add react-token-auth
# Dont know wy it continue fall
RUN yarn build

# Nginx
FROM nginx:alpine
# SET WORKING DIRECTORY for Nginx
WORKDIR /usr/share/nginx/html
# Remove default nginx statics
RUN rm -rf ./*
# Copy static assets from builder
COPY --from=builder /app/build .
# Copy conf to nginx
COPY default.conf /etc/nginx/conf.d/default.conf
# Containers run nginx with global directives
ENTRYPOINT ["nginx", "-g", "daemon off;"]



