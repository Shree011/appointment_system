import profile
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from signup.models import Address, Profile

# Create your views here.
def logout_view(request):
    logout(request)
    try:
        del request.session['userType']
    except KeyError:
        pass
    return redirect('loginn')


def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userType = request.POST.get('userType')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            checkuser = Address.objects.filter(userId_id=user.id)
            #print(checkuser[0].user)
            if checkuser.exists():
                if checkuser[0].user == userType:
                    login(request, user)
                    request.session['userType'] = userType
                else:
                    messages.info(request, 'this username does not exists for this type of user')
                    return redirect('loginn')
                return redirect('')
        else:
            messages.info(request, 'Username or Password is incorrect !!')
            return redirect('loginn')
                
    return render(request, 'signup/loginn.html')

def signupUser(request):
    userType = request.session.get('signupUsername')
    context = {
        'userType' : userType
    }
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.info(request, 'password confirmation failed')
            return redirect('signupUser')

        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
        except:
            user = None
            pass
        #print(user)
        #print(type(user))
        if user is not None:
            messages.info(request, 'enter diffrent username')
            return redirect('signupUser')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_user(username, email, password1, first_name=first_name, last_name=last_name)
        #auth_id = userr.id
        #print(userr.id)
        #userr.save()
        
        #take id from auth table and insert it in doc/pat table along with its values
        

        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        
        addr = Address(phone=phone, address=address, city=city, state=state, pincode=pincode, userId=user, user=userType)
        addr.save()
        if userType == 'Doctor':
            profile_photo = request.FILES['profile_photo']
            profile = Profile(profile_photo=profile_photo, user=user)
            profile.save()
            
        messages.info(request,'data saved successfully')
        del request.session['signupUsername']
        return redirect('loginn')
    return render(request, 'signup/signupUser.html', context)

def userSignupSession(request, pkey):
    print(pkey)
    if pkey == 'd':
        pkey = 'Doctor'
    else:
        pkey = 'Patient'
    request.session['signupUsername'] = pkey
    #userType = request.session.get('signupUsername')
    #print(userType)
    return redirect('signupUser')

def signup(request):
    return render(request, 'signup/signup.html')
