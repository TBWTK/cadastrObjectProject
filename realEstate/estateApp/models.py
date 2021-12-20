from django.db import models


class Status(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Estate(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    estate = models.ForeignKey(Estate, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} {self.surname}"


class LandPlot(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    description = models.FileField(upload_to='files/')
