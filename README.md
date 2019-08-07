# tornado-celery

## celery
```
celery -A celery_service.tasks worker -Q default -l info  --pool=eventlet
celery -A celery_service.tasks worker -Q upload -l info  --pool=eventlet

```