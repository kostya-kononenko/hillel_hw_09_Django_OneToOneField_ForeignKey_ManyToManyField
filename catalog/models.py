from django.db import models


class Products(models.Model):
    name_products = models.CharField("Products name", max_length=25)

    def __str__(self):
        return self.name_products


class Clients(models.Model):
    name = models.CharField("Client name", max_length=25)
    client_city = models.ForeignKey("City", on_delete=models.CASCADE)
    products = models.ManyToManyField("Products")

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField("City name", max_length=25)
    provider = models.OneToOneField("Provider", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name_provider = models.CharField("Provider name", max_length=25)

    def __str__(self):
        return self.name_provider
