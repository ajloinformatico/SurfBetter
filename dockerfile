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
# Containers run nginx with global directives
ENTRYPOINT ["nginx", "-g", "daemon off;"]

# Flask
FROM python:3
# Create api directory
RUN mkdir /api
# Set work directory
WORKDIR /api
# Copy API data
COPY /api /api
# Run Api dependency
RUN pip3 install -r /api/apirequirements.txt
# Expose port
# EXPOSE 5000
# Run flask
# RUN python3 /api/main.py
# Set gunicorn server ["./gunicorn.sh"]

# ENTRYPOINT ["./gunicorn.sh"]



