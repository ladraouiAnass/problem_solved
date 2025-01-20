import os
import json
from django.conf import settings
from django.apps import AppConfig
from django.core.management import call_command

global_config = {}

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        global global_config

        json_file_path = os.path.join(str(settings.BASE_DIR) + "/files", 'millennium-falcon.json')
        try:
            with open(json_file_path, 'r') as file:
                global_config = json.load(file)
                print("JSON file loaded successfully:", global_config)
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return

        routes_db_path = global_config.get("routes_db")
        if routes_db_path:
            db_full_path = os.path.join(str(settings.BASE_DIR)+"/databases", routes_db_path)
            if os.path.exists(db_full_path):
                settings.DATABASES['default'] = {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': db_full_path,
                    'TIME_ZONE': settings.TIME_ZONE,  
                    'CONN_HEALTH_CHECKS': False,
                    'CONN_MAX_AGE':None,
                    'AUTOCOMMIT': True,
                    'ATOMIC_REQUESTS': False, 
                    'OPTIONS': {
                        'timeout': 20,  
                    },
                }
                print(f"Database configured to use: {db_full_path}")
            else:
                print(f"Database file does not exist: {db_full_path}")
        else:
            print("No database path specified in the JSON file.")
 


