FROM node:18-alpine
RUN npm install -g npm
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 5173 8080 8000
CMD ["npm", "run", "dev"]