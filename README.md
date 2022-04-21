# HearthStone Api App
## About
Uses oauth to auth api calls to hearthstone cards API. 
Returns json that is rendered into a template as tables.

## Development
### Requirements:
- Install python3.9+ & pip
- Install Docker
- (optional) Install python virutalenv in the app directory `python -m venv venv/`
- (optional) Activate python venv `. venv/bin/activate`
- Install the requirements.txt dependecies.  `pip install -r requirements.txt`

## Deployment:
### Requirements
- Install Docker
- https://develop.battle.net/documentation/guides/getting-started

### Building image
`docker build . -t hearthstone-api-app`

### Running container
`docker run -it -d -p 8080:8080 --env CLIENT_ID=<clientid> --env CLIEND_SECRET=<secret> hearthstone-api-app`

### Environment variables
Environment variables for hearthstone API clientId and clientSecret. 
*CLIENT_ID
*CLIENT_SECRET

## Running the application
Make a get request to the api endpoint such as `curl localhost:8080/get/warlock`.
Api returns a json of stats. 
