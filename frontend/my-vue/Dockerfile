# Base image
FROM node:lts-alpine as build-stage

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy project files and build the project
COPY . .
RUN npm run build

# Production stage
FROM nginx:stable-alpine as production-stage

# Copy built app to nginx server root
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]