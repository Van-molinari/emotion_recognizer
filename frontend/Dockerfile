FROM node:18.17.1

WORKDIR /usr/app

COPY app/package.json ./

RUN npm install

COPY app .

EXPOSE 5173

CMD [ "npm", "run", "dev", "--", "--host" ]