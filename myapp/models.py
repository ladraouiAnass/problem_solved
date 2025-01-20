from django.db import models

class ROUTES(models.Model):
    ORIGIN = models.CharField(max_length=255)
    DESTINATION = models.CharField(max_length=255)
    TRAVEL_TIME = models.IntegerField()
    
    def get_routes():
        try:
            routes_queryset = ROUTES.objects.values_list('ORIGIN', 'DESTINATION', 'TRAVEL_TIME')
            routes_list = [list(route) for route in routes_queryset]
            print(f"ROUTES loaded into global list: {routes_list}")
        except Exception as e:
            print(f"Error loading ROUTES: {e}")
            routes_list = []  
        return routes_list
    
    class Meta:
        db_table = 'ROUTES'  # Explicitly specify the table name