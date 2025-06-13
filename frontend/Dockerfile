# frontend/Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package.json tsconfig.json ./
COPY pages ./pages
COPY components ./components
COPY styles ./styles

RUN npm install

EXPOSE 3000

CMD ["npm", "run", "dev"]
