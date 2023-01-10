##!/usr/bin/env sh
#set -x
#
#echo "ENV:" $ENV
#
#run_local_migrations () {
#    python manage.py makemigrations
#}
#
#run_local_migrations
#
#if [ "$ENV" = "LOCAL" ]; then
#    run_local_migrations
#    gunicorn leads.wsgi -b 0.0.0.0:8000 --reload
#elif [ "$ENV" = "DEV" ]; then
#    gunicorn leads.wsgi -b 0.0.0.0:$PORT
#else
#    run_local_migrations
#    gunicorn leads.wsgi --reload -b 0.0.0.0:$PORT
#fi
