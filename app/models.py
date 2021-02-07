from django.db import models

class Policy(models.Model):
    id = models.AutoField
    provider = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    is_recurring = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.provider+' - '+self.product


class Category(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.name

