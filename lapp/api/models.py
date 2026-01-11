from django.db import models

class SingaporeLastDigit(models.Model):
    date = models.CharField(max_length=20)
    mor = models.CharField(max_length=1)
    day = models.CharField(max_length=1)
    evn = models.CharField(max_length=1)

    def __str__(self):
        return self.date

class SingaporeLastTwoDigit(models.Model):
    date = models.CharField(max_length=20)
    mor = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    evn = models.CharField(max_length=2)

    def __str__(self):
        return self.date

class SingaporeLastThreeDigit(models.Model):
    date = models.CharField(max_length=20)
    mor = models.CharField(max_length=3)
    day = models.CharField(max_length=3)
    evn = models.CharField(max_length=3)

    def __str__(self):
        return self.date

class DearLastDigit(models.Model):
    date = models.CharField(max_length=20)
    mor = models.CharField(max_length=1)
    day = models.CharField(max_length=1)
    evn = models.CharField(max_length=1)

    def __str__(self):
        return self.date

class DearLastTwoDigit(models.Model):
    date = models.CharField(max_length=20)
    mor = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    evn = models.CharField(max_length=2)

    def __str__(self):
        return self.date

class DearLastThreeDigit(models.Model):
    date = models.CharField(max_length=20)
    mor = models.CharField(max_length=3)
    day = models.CharField(max_length=3)
    evn = models.CharField(max_length=3)

    def __str__(self):
        return self.date

class AppRelease(models.Model):
    version = models.CharField(max_length=20)
    apk_file = models.FileField(upload_to='apks/')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"App v{self.version}"