#!/bin/bash
celery -A celery_service.tasks worker -Q celery -E --loglevel=${CELERY_LOGLEVEL} --pool=eventlet
