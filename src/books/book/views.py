from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from books.book.models import Book, Tag, Genre

def index(request):
    return render_to_response('index.html')
    
def book(request, book_id):
    try:
        b = Book.objects.get(pk=book_id)
        tags = Tag.objects.get(book=b)
        genres = Genre.objects.get(book=b)
        
    except (Book.DoesNotExist):
        raise Http404
    return render_to_response('book.html', {
                                'book' : b,
                                'tags' : tags,
                                'genres' : genres,
                            })