FROM node:16
ARG USER_ID=node

USER $USER_ID

RUN mkdir /home/$USER_ID/.npm-global
ENV PATH=/home/$USER_ID/.npm-global/bin:$PATH
ENV NPM_CONFIG_PREFIX=/home/$USER_ID/.npm-global

RUN npm install yarn --global
RUN mkdir -p /home/$USER_ID/app
WORKDIR /home/$USER_ID/app
COPY --chown=$USER_ID . .

RUN yarn
EXPOSE 3000
ENV PORT 3000
CMD ["yarn", "build:start"]