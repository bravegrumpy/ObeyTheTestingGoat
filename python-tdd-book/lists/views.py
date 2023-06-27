from django.http import HttpResponse
from lists.models import Item

from django.shortcuts import render

# Create your views here.


def home_page(request):
    item = Item()
    # TODO: FIXME: This adds an empty entry for every desired entry.
    item.text = request.POST.get('item_text', '')
    item.save()

    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', '')
    })
