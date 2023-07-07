from django.db import models

# Create your models here.


class User(models.Model):
    firstName1 = models.CharField(max_length=200)
    lastName1 = models.CharField(max_length=200, null=True)
    number1 = models.IntegerField(default=1)
    firstName2 = models.CharField(max_length=200)
    lastName2 = models.CharField(max_length=200, null=True)
    number2 = models.IntegerField(default=1)
    product = models.IntegerField(default=1)

    def __str__(self):
        return self.firstName1 + ' ' + self.firstName2 + ' ' + str(self.product)
