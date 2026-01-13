from django.urls import path
from .views import SingaporeLastDigitAPI, SingaporeLastTwoDigitAPI, SingaporeLastThreeDigitAPI, DearLastTwoDigitAPI, DearLastDigitAPI, DearLastThreeDigitAPI, AppVersionCheckAPI, FaxViewAPI

urlpatterns = [
    path('singapore/last-digit/', SingaporeLastDigitAPI.as_view()),
    path('singapore/last-two-digit/', SingaporeLastTwoDigitAPI.as_view()),
    path('singapore/last-three-digit/', SingaporeLastThreeDigitAPI.as_view()),

    path('dear/last-digit/', DearLastDigitAPI.as_view()),
    path('dear/last-two-digit/', DearLastTwoDigitAPI.as_view()),
    path('dear/last-three-digit/', DearLastThreeDigitAPI.as_view()),
    path('version/', AppVersionCheckAPI.as_view()),
    path('today-fax/', FaxViewAPI.as_view()),
]