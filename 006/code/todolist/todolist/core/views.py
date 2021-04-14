from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404

from .models import TodoItems


def index(request):
    return render(request, 'index.html',
                  context={'todo_items': TodoItems.objects.all()})


def insert(request):
    new_item_text = request.POST.get('text')
    if new_item_text:
        TodoItems.objects.create(text=new_item_text, done=False)
        return HttpResponse(status=200)


def remove(request):
    item_id = request.POST.get('id')
    if item_id:
        get_object_or_404(TodoItems, id=item_id).delete()
        return HttpResponse(status=200)


def check(request):
    item_id = request.POST.get('id')
    if item_id:
        item = get_object_or_404(TodoItems, id=item_id)
        item.done = not item.done
        item.save()

        return HttpResponse(status=200)
