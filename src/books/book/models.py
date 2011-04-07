from django.db import models
from django.contrib.auth.models import User
import string

class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
    
class Tag(models.Model):
    description = models.SlugField(max_length=50)
    
    def __unicode__(self):
        return FormatSlug(self.description)
    
class Genre(models.Model):
    description = models.SlugField(max_length=50)
    
    def __unicode__(self):
        return FormatSlug(self.description)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    publisher = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=5, blank=True)
    publishYear = models.CharField(max_length=4, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    deweyDecimal = models.CharField(max_length=10, blank=True)
    amazonURL = models.URLField(blank=True)
    gutenbergURL = models.URLField(blank=True)
    googleBooksURL = models.URLField(blank=True)
    abeBooksURL = models.URLField(blank=True)
    
    def __unicode__(self):
        str = r''
        str += self.title
        str += " by "
        str += self.author.__unicode__()
        return str
    
class ISBN(models.Model):
    isbn = models.CharField(max_length=16)
    book = models.ForeignKey(Book)
    
    def __unicode__(self):
        return self.isbn
    
class Suggestion(models.Model):
    userFrom = models.ForeignKey(User, related_name="userFrom")
    userTo = models.ForeignKey(User, related_name="userTo")
    book = models.ForeignKey(Book)
    message = models.TextField(blank=True)
    
    def __unicode__(self):
        str = r''
        str += self.userFrom
        str += r" recommends "
        str += self.book
        str += r" to "
        str += self.userTo
        return str
    
class Review(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    review = models.TextField()
    
    def __unicode__(self):
        str = r''
        str += self.user
        str += r"'s review of "
        str += self.book
        return str
    
class Rating(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.IntegerField()
    
    def __unicode__(self):
        str = r''
        str += self.user
        str += r"'s rating for "
        str += self.book
        return str
        
def FormatSlug(slug):
    str = string.replace(slug, "_", " ")
    return string.capwords(str)