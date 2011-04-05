from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    authorName = models.CharField(max_length=200)
    
    
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
    
class ISBN(models.Model):
    isbn = models.CharField(max_length=16)
    book = models.ForeignKey(Book)
    
class Tag(models.Model):
    description = models.CharField(50)
    book = models.ForeignKey(Book)
    
class Genre(models.Model):
    description = models.CharField(50)
    book = models.ForeignKey(Book)
    
class Suggestion(models.Model):
    userFrom = models.ForeignKey(User, related_name="userFrom")
    userTo = models.ForeignKey(User, related_name="userTo")
    book = models.ForeignKey(Book)
    message = models.CharField(max_length=1000)
    
class Review(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    review = models.CharField(max_length=1000)
    
class Rating(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.IntegerField()
    