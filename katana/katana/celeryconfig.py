import os

broker_url = os.environ.get('BROKER_URL')
result_backend = os.environ.get('RESULT_BACKEND_URL') #"redis://localhost/1"

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

imports = (
    'katana.tasks.math',
)

task_routes = {
    'katana.tasks.math.add': {
        'queue': 'low-priority',
        'serializer': 'json',
    }
}

#result_expires = 60 Default is 1 day
result_persistent = True
