from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    authorName = models.CharField(max_length=200)
    
class Tag(models.Model):
    description = models.CharField(50)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    publisher = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    language = models.CharField(max_length=5)
    publishYear = models.CharField(max_length=4)
    deweyDecimal = models.CharField(max_length=10)
    amazonURL = models.CharField(max_length=500)
    gutenbergURL = models.CharField(max_length=500)
    googleBooksURL = models.CharField(max_length=500)
    abeBooksURL = models.CharField(max_length=500)