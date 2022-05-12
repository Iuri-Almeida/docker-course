FROM node

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY app.js .

EXPOSE 3000

ENTRYPOINT ["node", "app.js"]