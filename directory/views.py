from django.shortcuts import render
from .models import Hotel, Policy, Service, RoomType, LocalAttraction

def welcome(request):
    hotel = Hotel.objects.first()
    return render(request, 'directory/welcome.html', {'hotel': hotel})

def policies(request):
    policies = Policy.objects.all()
    return render(request, 'directory/policies.html', {
        'general_policies': policies.filter(category='GEN'),
        'safety_policies': policies.filter(category='SAF'),
        'service_policies': policies.filter(category='SER'),
    })

def services(request):
    services = Service.objects.all()
    return render(request, 'directory/services.html', {
        'services': services,
        '24h_services': services.filter(available_24h=True)
    })

def attractions(request):
    return render(request, 'directory/attractions.html', {
        'attractions': LocalAttraction.objects.all()
    })


def room_info(request):
    room_types = RoomType.objects.prefetch_related('amenities').all()
    return render(request, 'directory/room_info.html', {
        'room_types': room_types
    })