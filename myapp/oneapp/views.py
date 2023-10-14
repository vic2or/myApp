from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def counter(request):
    word= request.POST['word']
    amount_of_words= len(word.split())


    return render(request, 'counter.html', {'amount':amount_of_words})