from kombu import Queue, Exchange

# 消息代理, 队列本身. 也称为消息中间件   注意，celery4版本后，CELERY_BROKER_URL改为BROKER_URL
# BROKER_URL = "amqp://guest:guest@localhost:5672/vhost"
BROKER_URL = "pyamqp://admin:123456@127.0.0.1:5672/myvhost"
# 指定结果的接受地址
# CELERY_RESULT_BACKEND = "redis://root:sea@localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
# 指定任务序列化方式
CELERY_TASK_SERIALIZER = "msgpack"
# 指定结果序列化方式
CELERY_RESULT_SERIALIZER = "json"
# 任务过期时间,celery任务执行结果的超时时间
CELERY_TASK_RESULT_EXPIRES = 60*60*24
# 指定任务接受的序列化类型.
CELERY_ACCEPT_CONTENT = ["json", "msgpack"]

# 创建exchange
default_exchange = Exchange('default', type='direct')
upload_task_exchange = Exchange('upload_task', type='direct')

# 定义默认的QUEUE, EXCHANGE和ROUTING_KEY
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'

# 创建CELERY_QUEUES
CELERY_QUEUES = (
    Queue("default", default_exchange,  routing_key="default"),
    Queue("upload",  upload_task_exchange,  routing_key="upload_task"),
)


# 定义路由
CELERY_ROUTES = (
    {
        'celery_service.tasks.add': {
            'queue': 'default',
            'routing_key': 'default'
        }
    },
    {
        'celery_service.tasks.upload_file': {
            'queue': 'upload',
            'routing_key': 'upload_task'
        }
    }
)
