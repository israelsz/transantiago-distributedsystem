FROM node:14.20-alpine
WORKDIR /app
COPY package*.json ./

RUN apk add --update \
        git \
    && npm i 
    
#RUN npm audit fix    

COPY . .
RUN npm run generate

### New Stage ###
FROM nginx:1.15.11-alpine  

RUN apk add --no-cache bash 

# Copy the Statics files from the app to the nginx container
COPY --from=0 /app/dist /usr/share/nginx/html

COPY default.conf /etc/nginx/conf.d/default.conf

RUN cp /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.orig && \
    sed -i 's/listen[[:space:]]*80;/listen 9000;/g' /etc/nginx/conf.d/default.conf

EXPOSE 9000

CMD ["nginx", "-g", "daemon off;"]