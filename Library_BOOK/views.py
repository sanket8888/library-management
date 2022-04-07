from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')


# View for Add Books
def add_books(request):


    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        publisher = request.POST['publisher']
        language = request.POST['language']
        copies = request.POST['copies']
        book = BookDB(title=title, author=author, publisher=publisher, language=language, copies=copies)
        if book is not None:
            book.save()
            return redirect("view")
            # print(book.title)
        return HttpResponse('Not Added !!!!')
    return render(request, 'BOOK_temp/create_book.html')


# View for Display books
def view_books(request):
    all_books = BookDB.objects.all()
    cntx = {"books":all_books}
    return render(request,'BOOK_temp/view_book.html',cntx)

def delete_books(request, id):

    delete_book = BookDB.objects.get(id=id)
    delete_book.delete()
    # return redirect("view")
    all_books = BookDB.objects.all()
    cntx = {"books":all_books}
    return render(request,'BOOK_temp/view_book.html',cntx)

# View for Updation
def upd_books(request,id):
    if request.method == "GET":
        book = BookDB.objects.get(id=id)
        c = {"book":book}
        return render(request,'BOOK_temp/create_book.html',c)
    if request.method == "POST":
        book = BookDB.objects.get(id=id)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publisher = request.POST['publisher']
        book.language = request.POST['language']
        book.copies = request.POST['copies']
        book.save()
        return redirect("view")
    return render(request, 'BOOK_temp/create_book.html')




