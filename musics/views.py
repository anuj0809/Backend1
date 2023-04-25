from django.shortcuts import render, redirect
from .forms import MusicForm
from .models import Music
from users.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url="/user/login/")
def upload_music(request):
    errors = []
    if request.method == "POST":
        music = Music()
        music.title = request.POST['title']
        music.uploaded_by = request.user
        music.upload_mode = request.POST['upload_mode']
        music.file = request.FILES['music-file']
        music.save()

        if music.upload_mode == "protected":
            shared_with_emails = request.POST['shared-with'].split(',')
            shared_with_users = []
            for email in shared_with_emails:
                try:
                    shared_with_users.append(User.objects.get(email=email))
                except User.DoesNotExist:
                    errors.append("User with email {} does not exist".format(user))
            music.shared_with.set(shared_with_users)
            music.save()
        return redirect(to='home')

    context = {}
    context['errors'] = errors    
    return render(request, "musics/upload_music.html",context)



@login_required(login_url="/user/login/")
def home(request):
    context = {}
    my_uploads = Music.objects.filter(uploaded_by=request.user)
    context['my_uploads'] = my_uploads

    shared_with_me = Music.objects.filter(shared_with=request.user)
    context['shared_with_me'] = shared_with_me

    others_uploads = Music.objects.filter(upload_mode='public').exclude(uploaded_by=request.user)
    context['others_uploads'] = others_uploads
    return render(request,'users/home.html',context)
