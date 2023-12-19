from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import MeetingRoom, Booking
from .forms import RegistrationForm, UserProfileForm#, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def home(request):
  return render(request, 'booking/home.html')


def register(request):
  if request.method == 'POST':
    user_form = RegistrationForm(request.POST)
    profile_form = UserProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      profile = profile_form.save(commit=False)
      profile.user = user
      profile.save()
      login(request, user)
      return redirect('home')
  else:
    user_form = RegistrationForm()
    profile_form = UserProfileForm()
  return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('home')
  else:
    form = AuthenticationForm()
  return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
  logout(request)
  return redirect('home')

##### ROOM_LIST view
#@login_required
def room_list(request):
  current_time = timezone.now()
  rooms = MeetingRoom.objects.all()
  room_availablety = {}

  for room in rooms:
    upcoming_bookings = Booking.objects.filter(meeting_room=room, start_time__gte=current_time).order_by("start_time")
    room_availablety[room] = upcoming_bookings

  return render(request, "booking/room_list.html",  {"rooms": rooms})


##### BOOK_ROOM view
@login_required
def book_room(request, room_id):
  room = MeetingRoom.objects.get(pk=room_id)

  if request.method == "POST":
    form = BookingForm(request.POST)
    if form.is_valid():
      booking = form.save(commit=False)
      booking.meeting_room = room
      booking.user = request.user
      booking.save()
      return redirect("room_list")
  else:
    form = BookingForm()

  return render(request, "booking/book_room.html", {"room": room, "form": form})


##### DELETE RESERVATION
def delete_booking(request, booking_id):
  booking = get_object_or_404(Booking, pk=booking_id)
  booking.delete()
  return redirect("room_list")


##### EDIT RESERVATION
def edit_booking(request, booking_id):
  booking = get_object_or_404(Booking, pk=booking_id)

  if request.method == "POST":
    form = BookingForm(request.POST, instance=booking)
    if form.is_valid():
      form.save()
      return redirect("room_list")
  else:
    form = BookingForm(instance=booking)
  
  return render(request, "booking/booking_room.html", {"form": form})



