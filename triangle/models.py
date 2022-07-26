from django.db import models


class FirstForms(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_field = models.EmailField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class FirstModelLog(models.Model):
    path = models.CharField(max_length=30)
    method = models.CharField(max_length=30)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.path
