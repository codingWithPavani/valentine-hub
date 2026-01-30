from django.shortcuts import render, redirect
from .models import ValentineCard
from django.contrib.auth.decorators import login_required

@login_required
def create_card(request):
    if request.method == 'POST':
        card = ValentineCard.objects.create(
            user=request.user,
            sender_name=request.POST['sender'],
            receiver_name=request.POST['receiver'],
            message=request.POST['message']
        )
        return redirect(f'/cards/view/{card.id}/')

    return render(request, 'create_card.html')

@login_required
def view_card(request, card_id):
    card = ValentineCard.objects.get(id=card_id)
    return render(request, 'view_card.html', {'card': card})
