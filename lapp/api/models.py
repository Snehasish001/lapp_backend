from django.db import models

class BaseDailyDigit(models.Model):
    date = models.DateField(unique=True)
    mor = models.CharField(max_length=3, default='-')
    day = models.CharField(max_length=3, default='-')
    evn = models.CharField(max_length=3, default='-')

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.date)


class SingaporeLastDigit(BaseDailyDigit):
    mor = models.CharField(max_length=1, default='-')
    day = models.CharField(max_length=1, default='-')
    evn = models.CharField(max_length=1, default='-')


class SingaporeLastTwoDigit(BaseDailyDigit):
    mor = models.CharField(max_length=2, default='-')
    day = models.CharField(max_length=2, default='-')
    evn = models.CharField(max_length=2, default='-')


class SingaporeLastThreeDigit(BaseDailyDigit):
    pass



class DearLastDigit(BaseDailyDigit):
    mor = models.CharField(max_length=1, default='-')
    day = models.CharField(max_length=1, default='-')
    evn = models.CharField(max_length=1, default='-')


class DearLastTwoDigit(BaseDailyDigit):
    mor = models.CharField(max_length=2, default='-')
    day = models.CharField(max_length=2, default='-')
    evn = models.CharField(max_length=2, default='-')


class DearLastThreeDigit(BaseDailyDigit):
    pass


class Fax(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    image = models.ImageField(upload_to="fax/")

    def __str__(self):
        return f"Fax for {self.date}"


class AppRelease(models.Model):
    version = models.CharField(max_length=20)
    apk_file = models.FileField(upload_to='apks/')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"App v{self.version}"
    