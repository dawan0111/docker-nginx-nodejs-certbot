FROM node:16
USER node

RUN mkdir /home/node/.npm-global
ENV PATH=/home/node/.npm-global/bin:$PATH
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global

RUN npm install yarn -g
WORKDIR /usr/src/app
COPY --chown=node . .

RUN yarn
EXPOSE 3000
ENV PORT 3000
CMD ["yarn", "build:start"]