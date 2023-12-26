from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def profile(request):
    user = request.user
    profile_obj = user.profile
    return render(request, "profile.html", {"profile": profile_obj})
