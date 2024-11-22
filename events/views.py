from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def event_register(request, event_id):
    event = Event.objects.get(id=event_id)
    
    if request.method == 'POST':
        # Register the user for the event
        student = request.user.student  # Assuming the user has a related student model
        EventRegistration.objects.create(event=event, student=student)
        
        # Show a success message
        messages.success(request, f'You have successfully registered for {event.name}!')
        return redirect('event_register', event_id=event_id)

    return render(request, 'event_register.html', {'event': event})
def event(request):
    return render(request,'event.html')