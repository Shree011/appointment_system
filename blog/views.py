from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog.models import Appointment, Blog, DocAppointments, PatAppointments
from signup.models import Profile
# Create your views here.
def docAppointments(request):
    userType = request.session.get('userType')
    username = request.user
    appointments = DocAppointments.objects.filter(docuser=username)
    #patAppoin = PatAppointments.objects.filter(appointment=appointments)
    context = {
        'userType' : userType,
        'username' : username,
        'appointments' : appointments,
        #'patAppoin' : patAppoin
    }
    #print(patAppoin)
    return render(request, 'blog/docAppointments.html', context)

def appointment(request):
    patuser = request.user
    docuser = request.POST.get('username')
    docuser = User.objects.get(username=docuser)
    req_spec = request.POST.get('req_spec')
    doa = request.POST.get('DOA')
    sta = request.POST.get('STA')

    appoin = Appointment(req_spec=req_spec, doa=doa, sta=sta)
    appoin.save()
    docAppoin = DocAppointments(docuser=docuser, appointment=appoin)
    docAppoin.save()
    patAppoin = PatAppointments(patuser=patuser, appointment=appoin)
    patAppoin.save()
    print('ok')
    print(docuser, req_spec, doa, sta, patuser)
    messages.info(request, 'Appointment saved successfully')
    return redirect('allDoctors')

def alldocs(request):
    userType = request.session.get('userType')
    username = request.user
    doctors = Profile.objects.all()
    context = {
        'doctors' : doctors,
        'userType' : userType,
        'username' : username
    }
    return render(request, 'blog/allDoctors.html', context)

def postBlog(request):
    userType = request.session.get('userType')
    username = request.user
    context = {
        'userType' : userType,
        'username' : username
    }
    
    #print(username)
    if request.method == 'POST':
        caption = request.POST.get('caption')
        img = request.FILES['img']
        #print(caption)
        print(img)
        #now = datetime.now()
        #print(now)
        blog = Blog(img=img, caption=caption, userId=username)
        blog.save()
        messages.info(request, 'record saved')
    return render(request, 'blog/postBlog.html', context)

def homepage(request):
    userType = request.session.get('userType')
    username = request.user
    if userType == 'Patient':
        blogs = Blog.objects.filter()
    elif userType == 'Doctor':
        blogs = Blog.objects.filter(userId=username)
    else:
        return redirect('/signup/logout')
    print(userType)  
    #print(blogs[0])
    context = {
        'userType' : userType,
        'username' : username,
        'blogs' : blogs
    }
    return render(request, 'blog/homepage.html', context)