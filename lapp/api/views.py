from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SingaporeLastDigit, SingaporeLastTwoDigit, SingaporeLastThreeDigit, DearLastDigit, DearLastTwoDigit, DearLastThreeDigit, AppRelease, Fax

from .serializers import SingaporeLastDigitSerializer, SingaporeLastTwoDigitSerializer, SingaporeLastThreeDigitSerializer, DearLastDigitSerializer, DearLastTwoDigitSerializer, DearLastThreeDigitSerializer,FaxSerializer

class SingaporeLastDigitAPI(APIView):
    def get(self, request):
        data = SingaporeLastDigit.objects.all()
        serializer = SingaporeLastDigitSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SingaporeLastDigitSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SingaporeLastTwoDigitAPI(APIView):
    def get(self, request):
        data = SingaporeLastTwoDigit.objects.all()
        serializer = SingaporeLastTwoDigitSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serialzer = SingaporeLastTwoDigitSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SingaporeLastThreeDigitAPI(APIView):
    def get(self, request):
        data = SingaporeLastThreeDigit.objects.all()
        serializer = SingaporeLastThreeDigitSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SingaporeLastThreeDigitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DearLastDigitAPI(APIView):
    def get(self, request):
        data = DearLastDigit.objects.all()
        serializer = DearLastDigitSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DearLastDigitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DearLastTwoDigitAPI(APIView):
    def get(self, request):
        data = DearLastTwoDigit.objects.all()
        serializer = DearLastTwoDigitSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DearLastTwoDigitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DearLastThreeDigitAPI(APIView):
    def get(self, request):
        data = DearLastThreeDigit.objects.all()
        serializer = DearLastThreeDigitSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DearLastThreeDigitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppVersionCheckAPI(APIView):
    def get(self, request):
        apk = AppRelease.objects.filter(is_active=True).order_by('-version_code').first()

        if not apk:
            return Response({"error": "No APK available"}, status=status.HTTP_404_NOT_FOUND)

        # This creates the direct download link
        full_url = request.build_absolute_uri(apk.apk_file.url)

        return Response({
            "min_version_code": apk.version_code,
            "version_name": apk.version,
            "apk_url": full_url,      # For your Website
            "update_url": full_url,   # For your Android Force Update
        })

from datetime import date
class FaxViewAPI(APIView):
    def get(self, request):
        fax = Fax.objects.filter(date=date.today()).first()

        if not fax:
            return Response({"detail": "No fax for today"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "date": fax.date,
            "image": fax.image.url
        })