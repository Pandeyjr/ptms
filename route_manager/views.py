# route_manager/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RouteManagerLoginForm
from .models import Route
from django.http import JsonResponse
from .models import Route
from django.shortcuts import render, redirect
from .models import Route

def route_manager_login(request):
    if request.method == "POST":
        form = RouteManagerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('route_manager_home')  # Redirect to a route management dashboard
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = RouteManagerLoginForm()

    return render(request, 'route_manager/login.html', {'form': form})

def route_manager_home(request):
    # Only accessible if logged in as route manager
    if not request.user.is_authenticated:
        return redirect('route_manager_login')

    routes = Route.objects.all()
    return render(request, 'route_manager/home.html', {'routes': routes})

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Route
import json

@csrf_exempt
def create_route(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Create new route
        route = Route.objects.create(
            name=data['name'],
            starting_point=data['starting_point'],
            destination=data['destination'],
            start_lat=data['start_lat'],
            start_lon=data['start_lon'],
            end_lat=data['end_lat'],
            end_lon=data['end_lon'],
        )

        # Return success response with created route data
        return JsonResponse({'success': True, 'route': {
            'name': route.name,
            'starting_point': route.starting_point,
            'destination': route.destination
        }})
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)


def get_route(request, route_id):
    route = Route.objects.get(id=route_id)
    route_data = {
        'start_lat': route.start_lat,
        'start_lon': route.start_lon,
        'end_lat': route.end_lat,
        'end_lon': route.end_lon,
        'name': route.name,
        'starting_point': route.starting_point,
        'destination': route.destination,
    }
    return JsonResponse({'route': route_data})



def assign_route_to_driver(request, bus_id):
    # Logic to assign route to bus driver
    if request.method == "POST":
        route_id = request.POST.get("route_id")
        bus = Bus.objects.get(id=bus_id)
        route = Route.objects.get(id=route_id)
        bus.route = route
        bus.save()
        return redirect('bus_details', bus_id=bus.id)  # Redirect to bus details
    routes = Route.objects.all()
    return render(request, 'route_manager/assign_route.html', {'routes': routes})
