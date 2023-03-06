from http.client import responses
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .postgres import select 


@api_view(['GET'])
def select_one(request):
    
    try:
        data = JSONParser().parse(request)
        #coluna = list(data.keys())[0]
        email = list(data.items())  
        email = email[0][1]      
        return JsonResponse(select(email), status=201, safe=False)

    except Exception as ex:
        response = {
            "error": str(ex.args[0])
        }
        return JsonResponse(response, status=400)
