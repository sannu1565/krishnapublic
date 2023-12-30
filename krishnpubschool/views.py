from django.shortcuts import render
from .models import feedback
from .models import adform
from .models import ragister
from django.http import HttpResponse


# Create your views here.
def index(request):
        return render(request,'index.html')
def about(request):
        return render(request,'about.html')           
def admission(request):
        return render(request,'admission.html')

def signup(request):
        return render(request,'signup.html')

def login(request):
        return render(request,'login.html')

def enquiryForm(request): 
                n='' 
                if request.method=="POST":
                                firstname = request.POST.get('firstname')
                                lastname = request.POST.get('lastname')
                                mobile_no = request.POST.get('mobile_no')
                                type = request.POST.get('type')
                                textcomment = request.POST.get('textcomment')
                                form = feedback(firstname=firstname,lastname=lastname,mobile_no=mobile_no,type=type,textcomment=textcomment)
                                
                                form.save()
                                n='YOUR ENQUIRYFORM SUCCESSFULLY SUBMITTED'
                                return render(request,'index.html',{'n': n})


def sign(request):
        p=''             
        if request.method=="POST":
                        username = request.POST.get('username')
                        email= request.POST.get('email')
                        password = request.POST.get('password')
                        if ragister.objects.filter(email=email).exists(): 
                                return HttpResponse('USER ALREADY EXISTS')
                        
                        else:
                        # passr= request.POST.get('passr')
                                user= ragister(username=username,email=email,password=password)
                                user.save()
                                p='USER SIGNUP SUCCESSFULLY CREATED'
                                return render(request,'signup.html',{'p':p})




def admissions(request):
                a=''
                if request.method=="POST":
                        firstname = request.POST.get('firstname')
                        lastname = request.POST.get('lastname')
                        fathername = request.POST.get('fathername')
                        mothername = request.POST.get('mothername')
                        mobile=request.POST.get('mobile')
                        types=request.POST.get('types')
                        addform= adform(firstname=firstname,lastname=lastname,fathername=fathername , mothername=mothername ,mobile=mobile,types=types)
                        addform.save()
                        a='YOUR ADMISSION FORM IS SUBMITEDPLEASE VISIT FOR VARIFICATION'
                        return render(request,'admission.html',{'a':a})


                # Import your model class

# def admission(request):
#     if request.method == "POST":
#                 firstname = request.POST.get('firstname')
#                 lastname = request.POST.get('lastname')
#                 fathername = request.POST.get('fathername')
#                 mothername = request.POST.get('mothername')
#                 mobile = request.POST.get('mobile')

#                 enrollment = admission(firstname=firstname, lastname=lastname, fathername=fathername, mothername=mothername, mobile=mobile)
#                 enrollment.save()
#                 return render(request, 'admission.html')

    # Handle the case when the request method is not POST
   # Adjust this line as needed

                # if admissions.objects.filter(mobile=mobile).exists(): 
                #         return HttpResponse('user alrady exist')
                
                # else:
                #         admissions.objects.create(firstname=fristname,lastname=lastname,fathername=fathername,mothername=mothername,mobile=mobile,)
                # return HttpResponse('you are successfully admission')
              





