from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    creation_date = models.DateTimeField(verbose_name="creation date", auto_now_add=True)
    modification_date = models.DateTimeField(verbose_name="modification date", auto_now=True)


    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    creation_date = models.DateTimeField(verbose_name="creation date", auto_now_add=True)
    modification_date = models.DateTimeField(verbose_name="modification date", auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
