from django.shortcuts import render, redirect
from .models import Wish
from .forms import WishForm

def wishes_wall(request):
    wishes = Wish.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = WishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wishes_wall')
    else:
        form = WishForm()

    return render(request, 'confessions/wishes_wall.html', {
        'wishes': wishes,
        'form': form
    })
