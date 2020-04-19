
from rest_framework.views import APIView
from django.http import JsonResponse

class TemplateDRF(APIView):

    def get(self, req):
        return JsonResponse({'data': 'Template DRF app'})
