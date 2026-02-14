from django.shortcuts import render, redirect
from .models import Memory
from django.contrib.auth.decorators import login_required

@login_required
def memory_wall(request):
    memories = Memory.objects.filter(user=request.user)
    return render(request, 'memorywall/memory_wall.html', {'memories': memories})


@login_required
def add_memory(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES.get('image')

        Memory.objects.create(
            user=request.user,
            title=title,
            description=description,
            image=image
        )

        return redirect('memory_wall')

    return render(request, 'memorywall/add_memory.html')
