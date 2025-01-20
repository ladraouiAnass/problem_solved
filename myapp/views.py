from django.shortcuts import render
from .apps import global_config
from django.conf import settings
from .operations import get_graph, proba
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random,os
import json

@csrf_exempt
def calculate_percentage(request):
    
    if request.method == 'POST':
        try:
            print(f"Request body: {request.body.decode('utf-8')}")
            data = json.loads(request.body)
            graph, _ = get_graph()
            percentage = proba(graph, current=global_config["departure"], end= global_config["arrival"], day=0, autonomy=global_config["autonomy"], k=0, max_autonomy=global_config["autonomy"], countdown=data["countdown"], bounty_hunters = data["bounty_hunters"])
            return JsonResponse({'number': (1-percentage)*100})
        except json.JSONDecodeError:
            print("Error: Invalid JSON received.")
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)






@csrf_exempt
def cli_view(request):
    """
    View to dynamically load two JSON files (empire.json and falcon.json),
    update the global configuration (global_config), and change the database
    settings based on the 'database' key in falcon.json.

    Expects a POST request with two JSON files in the request body:
      - empire.json
      - falcon.json
    """
    global global_config

    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed."}, status=405)

    try:
        # Parse the JSON body
        body = json.loads(request.body)

        # Check for the required JSON files
        empire_json = body.get("empire")
        falcon_json = body.get("falcon")

        if not empire_json or not falcon_json:
            return JsonResponse({"error": "Both 'empire.json' and 'falcon.json' are required in the request body."}, status=400)

        # Validate the presence of the 'database' key in falcon.json
        database_path = falcon_json.get("routes_db")
        if not database_path:
            return JsonResponse({"error": "'database' key is required in 'falcon.json'."}, status=400)

        # Build the full path to the database file
        db_full_path = os.path.join(str(settings.BASE_DIR) + "/databases", database_path)

        # Check if the database file exists
        if not os.path.exists(db_full_path):
            return JsonResponse({"error": f"Database file does not exist: {db_full_path}"}, status=400)

        # Dynamically update the database settings
        settings.DATABASES['default'] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': db_full_path,
            'TIME_ZONE': settings.TIME_ZONE,
            'CONN_HEALTH_CHECKS': False,
            'CONN_MAX_AGE': None,
            'AUTOCOMMIT': True,
            'ATOMIC_REQUESTS': False,
            'OPTIONS': {
                'timeout': 20,
            },
        }

        print(f"Request body: {request.body.decode('utf-8')}")
        data= empire_json
        global_config = falcon_json
        graph, _ = get_graph()
        percentage = proba(graph, current=global_config["departure"], end= global_config["arrival"], day=0, autonomy=global_config["autonomy"], k=0, max_autonomy=global_config["autonomy"], countdown=data["countdown"], bounty_hunters = data["bounty_hunters"])
        return JsonResponse({'success': (1-percentage)*100})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body."}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)




def home(request):
    return render(request, 'home.html')

