from rest_framework import serializers
from .models import SingaporeLastDigit, SingaporeLastTwoDigit, SingaporeLastThreeDigit, DearLastDigit, DearLastTwoDigit, DearLastThreeDigit, Fax

class SingaporeLastDigitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingaporeLastDigit
        fields = ['date', 'mor', 'day', 'evn']

class SingaporeLastTwoDigitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingaporeLastTwoDigit
        fields = ['date', 'mor', 'day', 'evn']

class SingaporeLastThreeDigitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingaporeLastThreeDigit
        fields = ['date', 'mor', 'day', 'evn']

class DearLastDigitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DearLastDigit
        fields = ['date', 'mor', 'day', 'evn']

class DearLastTwoDigitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DearLastTwoDigit
        fields = ['date', 'mor', 'day', 'evn']

class DearLastThreeDigitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DearLastThreeDigit
        fields = ['date', 'mor', 'day', 'evn']

class FaxSerializer(serializers.ModelSerializer):
    date = serializers.DateField(read_only = True)
    class Meta:
        model = Fax
        fields = ['date' ,'image']



