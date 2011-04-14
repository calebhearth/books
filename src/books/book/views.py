from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from books.book.models import Book, Tag, Genre, Suggestion, SuggestionMessage
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, ModelChoiceField, CharField, Textarea

class BookForm(ModelForm):
    class Meta:
        model = Book

class SuggestForm(ModelForm):
    #userTo = ModelChoiceField(User, label="Suggest to")
    suggestionMessage = CharField(widget=Textarea, label = "Message")
    class Meta:
        model = Suggestion
        exclude = ('userFrom', 'book')
    
    
def index(request):
    return render_to_response('index.html')

def css(request, css_id):
    if css_id == "screen":
        return render_to_response('screen.css')
    else: 
        raise Http404

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
    
#todo: process data, 
# show book title in template (why isn't the {% book %} syntax working with template inheritance?
def suggest(request, book_id=0):
    if request.method == 'Post':
        form = SuggestForm(request.POST)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            newSuggestion = form.save(commit=False)
            newSuggestion.book = request.POST('book')
            newSuggestion.userFrom = request.POST('user')
            newSuggestion.userTo = request.POST('')
            newSuggestion.save()
            newMessage = SuggestionMessage(
                           user = request.POST('user'),
                           text = form.cleaned_date['suggestion'],
                           suggestion = newSuggestion)
            newMessage.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
        else:
            return HttpResponseRedirect('/worked/')
    else:
        form = SuggestForm()
        book = Book.objects.get(id=book_id)
        
    return render_to_response('suggest.html', {
                                'form' : form,
                                'book' : book,
                                              },
                                context_instance=RequestContext(request),
                            )
    
def login(request):
    if request.method == 'Post':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                #return a 'disabled account' error message
                return HttpResponseRedirect('/disabled_account/')
        else:
            return render_to_response('login.html', {
                                         'failed_login' : True,
                                         'form' : AuthenticationForm()
                                                    },
                                        context_instance=RequestContext(request),
                                     )
    else:
        return render_to_response('login.html', {
                                        'failed_login' : False,
                                        'form' : AuthenticationForm()
                                                    },
                                        context_instance=RequestContext(request),
                                     )
        
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    