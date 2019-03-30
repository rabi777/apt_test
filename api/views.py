from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Counter


class DataListApiView(APIView):
    def get(self, request):
        ar = ['a', 'b', 'c', 'd', 'e', 'f']
        try:
            get_count = Counter.objects.get(id=1)
            count = get_count.data_request
            get_count.data_request = count + 1
            get_count.save()
            obj = Counter.objects.get(id=1).data_request
            print(obj)
        except:
            Counter.objects.create()
            obj = 1

        data = {
            'data': ar,
            'counter': obj
        }
        return Response(data)


class DataListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'api/data_list.html')
