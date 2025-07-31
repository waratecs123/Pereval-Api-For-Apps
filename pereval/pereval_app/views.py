from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from pereval.pereval_app.serializers import PerevalSerializer


# Create your views here.
class SubmitDataView(APIView):
    def post(self, request):
        selializer = PerevalSerializer(data=request.data)
        if selializer.is_valid():
            try:
                pereval = selializer.save()
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': None,
                    'id': pereval.id
                })
            except Exception as e:
                return Response({
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': str(e),
                    'id': None
                }, status=500)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': selializer.errors,
            'id': None
        }, status=400)