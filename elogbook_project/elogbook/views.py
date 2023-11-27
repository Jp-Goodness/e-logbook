from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Week, Day, Activity
from .forms import ActivityForm

@login_required
def dashboard(request):
    # Your dashboard logic here
    pass

@login_required
def select_week(request):
    # Logic to display weeks and days, handle form submissions
    pass

@login_required
def activity_detail(request, day_id):
    # Logic to display and handle activity details
    pass

@login_required
def assess_activity(request, activity_id):
    # Logic to assess an activity
    pass
