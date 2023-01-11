# takehome-technodreams

Backend code to takehome challenge

### Backend Service
- Dev: [api-clag.onrender.com](https://api-clag.onrender.com)

### Starting services locally

To simply start the project locally, run:

    source venv/bin/activate
    docker-compose up [services]

Some things to note:

- dependencies do not need to be installed locally when starting the services this way (without volumes).
- environmental variables used by `docker-compose` should be in a .env file in the root of the docker/main directory.
- `[services]` is a list of space-separated service names to start, for example:


      docker-compose up django database

    This starts the `django` and `database` (not necessarily in that order). Skipping service names implies that docker should start all services.

### Development
To start the project with volumes, enabling live updates in the containers, you need to install the dependencies for any service you wish to start by running `pip install -r requirements.txt` in the root of that service's directory. Then do:

    docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml --env-file=.env up api database redis celery

### Note:
Don't forget to include `.env` file required by docker-compose before starting the services.
DEBUG=True
ENV=LOCAL
DJANGO_SECRET_KEY=leadsmanship
DB_USER=leads
POSTGRES_PASSWORD=leads
DB_HOST=database
DB_NAME=leads
DB_PASSWORD=leads
DB_USER=leads
POSTGRES_USER=leads
POSTGRES_DB=leads
DB_PORT=5432