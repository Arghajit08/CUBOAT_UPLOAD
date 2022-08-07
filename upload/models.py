from django.db import models

# Create your models here.
class Upload(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author1 = models.CharField(max_length=100, default='')
    author2 = models.CharField(max_length=100, default='')
    author3 = models.CharField(max_length=100, default='')
    publication_link = models.CharField(max_length=100)

    def __str__(self):
        return self.title
