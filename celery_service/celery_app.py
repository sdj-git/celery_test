from celery import Celery


celery_app = Celery('celery_service', include=["celery_service.tasks"])
celery_app.config_from_object("celery_service.celery_config")


if __name__ == '__main__':
    celery_app.start()
