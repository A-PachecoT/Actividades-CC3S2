# Official image of Node.js v14
FROM node:14

# Stablishing working directory
WORKDIR /app

# Copying package.json and package-lock.json
COPY package*.json ./

# Installing dependencies
RUN npm install

# Copying source code
COPY . .

# Expose port 3000, 3001, 9090
EXPOSE 3000 3001 9090

# Setting the environment variable
ENV PORT=3000

# Running the server
CMD [ "node", "src/server.js" ]