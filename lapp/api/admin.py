from django.contrib import admin

from .models import SingaporeLastDigit, SingaporeLastTwoDigit, SingaporeLastThreeDigit, DearLastDigit, DearLastTwoDigit, DearLastThreeDigit, AppRelease, Fax

admin.site.register([SingaporeLastDigit, SingaporeLastTwoDigit, SingaporeLastThreeDigit, DearLastDigit, DearLastTwoDigit, DearLastThreeDigit, Fax])

@admin.register(AppRelease)
class AppReleaseAdmin(admin.ModelAdmin):
    list_display = ('version', 'is_active', 'uploaded_at')