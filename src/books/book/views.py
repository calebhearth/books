from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from books.book.models import Book, Tag, Genre, Suggestion
from django.forms import ModelForm

class BookForm(ModelForm):
    class Meta:
        model = Book

class SuggestForm(ModelForm):
    class Meta:
        model = Suggestion

def index(request):
    return render_to_response('index.html')
    
#def book(request, book_id):
#    try:
#        book = Book.objects.get(pk=book_id)
#        tags = book.tags
#        genres = book.genres
#        
#    except (Book.DoesNotExist):
#        raise Http404
#    return render_to_response('book.html', {
#                                'book' : book,
#                                'tags' : tags,
#                                'genres' : genres,
#                            })

def book(request, book_id):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # do stuff with the data in form.cleaned_data
            return HttpResponseRedirect('/')
    else:
        try:
            book = Book.objects.get(pk=book_id)
            tags = book.tags
            genres = book.genres
            form = BookForm(book)
        except:
            raise Http404
    return render_to_response('book.html', {
                                'form' : form,
                                'tags' : tags,
                                'genres' : genres,
                                'book' : book,
                            })
    
def tag(request, tag_slug):
    try:
        tag = Tag.objects.get(description=tag_slug)
        books = Book.objects.filter(tags__description__icontains=tag_slug)
    except(Tag.DoesNotExist):
        #tag = tag_slug
        #return render_to_response('tag.html' {'tag' : tag})
        raise Http404
    return render_to_response('tag.html', {
                                'tag' : tag,
                                'books' : books,
                            })
    
def genre(request, genre_slug):
    try:
        genre = Genre.objects.get(description=genre_slug)
        books = Book.objects.filter(genres__description__icontains=genre_slug)
    except(Genre.DoesNotExist):
        #genre = genre_slug
        #return render_to_response('genre.html' {'genre' : genre})
        raise Http404
    return render_to_response('genre.html', {
                                'genre' : genre,
                                'books' : books,
                            })
    
#def contact(request):
#    if request.method == 'POST': # If the form has been submitted...
#        form = ContactForm(request.POST) # A form bound to the POST data
#        if form.is_valid(): # All validation rules pass
#            # Process the data in form.cleaned_data
#            # ...
#            return HttpResponseRedirect('/thanks/') # Redirect after POST
#    else:
#        form = ContactForm() # An unbound form
#
#    return render_to_response('contact.html', {
#        'form': form,
#    })
    
def suggest(request, book_id=0):
    if request.method == 'Post':
        form = SuggestForm(request.POST)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
        else:
            return HttpResponseRedirect('/worked/')
    else:
        form = SuggestForm()
        
    return render_to_response('suggest.html', {
                                'form' : form,
                                              },
                                context_instance=RequestContext(request),
                            )
        
    