from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import person_info_form, auth_user
from .models import person_info
from django.contrib.auth import authenticate, login
from django.db.models import Q


# Create your views here.

def home(request):
    lovar1 = { 'Academic Year' : 'flush-headingOne',
                'Institution': 'flush-headingTwo', 
                'General Science': 'flush-headingThree',
                'Mechanical': 'flush-headingFour', 
                'Electrical': 'flush-headingFive', 
                'Civil': 'flush-headingSix', 
                'Computer': 'flush-headingSeven', 
                'E&TC': 'flush-headingEight', 
                'Polytechnic': 'flush-headingNine', 
                'Mechanical Poly': 'flush-headingTen', 
                'Electrical Poly': 'flush-headingEleven', 
                'Civil Poly': 'flush-headingTwelve'}
    lovar2 = ['2019-20', '2020-21', '2021-22', '2022-23']
    lovar3 = ['Office','Lab assistant','Library','Examination','Sports']
    lovar4 = ['Machanical','Electrical','Civil','Computer','E&TC']
    lovar5 = ['Second Year','Third Year','Final Year']
    lovar6 = ['Machanical','Electrical','Civil']
    lovar7 = ['Second Year','Third Year']
    dict = {'lovar1' : lovar1, 'lovar2' : lovar2, 'lovar3' : lovar3, 'lovar4' : lovar4, 
            'lovar5' : lovar5, 'lovar6' : lovar6, 'lovar7' : lovar7}
    return render(request, 'Registration/layout.html', context= dict)

def insert (request):
    course = request.POST['course']
    dept_token = request.POST['dept_token']
    action_text = request.POST['action_text']
    role_info = {'course':course, 'dept_token': dept_token, 'action_text': action_text}
    if action_text == 'Register':         
        form = person_info_form()
        return render(request, 'Registration/data_fields.html', context={'form':form , 'role_info':role_info })
    elif action_text == 'Login':
        form = auth_user()
        return render(request, 'Registration/data_fields.html', context={'form':form , 'role_info':role_info})
        

def person_data_save(request):
    if request.method == 'POST':
        form = person_info_form(request.POST)        
        if form.is_valid():
            form.save()                    
        auth_form = auth_user()            
    return render(request, 'Registration/signup.html' , context={'form':form , 'auth_form': auth_form} )



def create_user(request):    
    if request.method == 'POST':               
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            myuser = User.objects.create_user(username, email, password1)
            myuser.first_name =  request.POST['fname']
            myuser.last_name = request.POST['lname']
            myuser.save()         
    return render(request,'Registration/layout.html' )


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)        
        if user is not None:
            f_name = user.first_name
            l_name = user.last_name
            full_name = {'fname' :f_name, 'lname' : l_name }
            login(request, user)            
            form = person_info.objects.get(Q(fname=f_name) & Q(lname=l_name))            
            print(form)
        elif user is None:
            print('user id password do not match')
    return render(request, 'Registration/signin.html', context={'form':form , 'full_name' : full_name})


def project_help(request):
    return render(request, 'Registration/help.html')
