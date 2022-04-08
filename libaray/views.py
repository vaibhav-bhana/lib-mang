from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.views.generic import View
from .models import  CustomUser,book
User = get_user_model()




def registers(request):
    if request.method=="POST" :
        username=request.POST.get("username")
        email =request.POST.get("email")
        password=request.POST.get("password")
        cpassword=request.POST.get("confirmpassword")
        if password != cpassword:
              return render(request, 'libaray/register.html', {"msg": "password not match"})
       
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect("/")
    return render(request,"libaray/register.html")

def login(request):
    if request.method=="POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
                    request.session['uid'] = request.POST['email']
                    use=User.objects.get(email=request.POST['email'])
                    staff=use.is_superuser
                    if staff == True:
                         return redirect('home')
                    else:
                        return redirect('index')       
            
          
    return render(request, 'libaray/login.html')



class home(View):
    def get(self, request, pk=None):
        bk=book.objects.all()
        return render(request,"libaray/index.html",{"all":bk})
    def post(self,request):
        boo = request.POST.get('book')

        author = request.POST.get('author')
        user=book(bookname=boo,author=author)
        user.save()
        return redirect("home")
    def put(self,pk,request):
        print(pk)
        return HttpResponse("hy")




def edit(request,pk):
    bk=book.objects.get(id=pk)
    bkn=bk.bookname
    bka=bk.author
    if request.method=="POST":
        boo = request.POST.get('book')
        aut = request.POST.get('author')
        bk.bookname=boo
        bk.author=aut
        bk.save()
        return redirect("/home")  
    return render(request,"libaray/edit.html",{"bka":bka,"bkn":bkn})



def delete(request,pk):
    print(pk)
    customer = book.objects.get(id=pk)
    customer.delete()
    return redirect("/home") 
        


        

  


def index(request):
    if request.session.has_key('uid'):
        a=book.objects.all()
     
        return render(request,"libaray/home.html",{"book":a})


def Logout(request):
    del request.session['uid']
    return redirect('/')



# # Create your views here.
# class Register(View):
#     def get(self,request):
#          return render(request,"app/auth-register.html")

#     def post(self,request):
#         username= request.POST["username"]
#         email= request.POST["email"]
#         password= request.POST["password"]
#         conf_password = request.POST["conf-password"]
#         mobile = request.POST["mobile number"]
#         myuser = User.objects.create_user(username,email,password)
#         myuser.mobile=mobile
#         myuser.save()
         
#         return redirect("auth-login.html")


# class LoginView(View):
#     def get(self, request):
#          return render(request,"app/auth-login.html")

#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
       
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             use=User.objects.get(username=username)
#             sub=use.subscriber
#             if sub==True:
#                 login(request, user)
#                 return redirect("/index")
#             else:
#                   messages.error(request,"your subscription is expire")
#                   return redirect("/")


#         else:
#             messages.error(request,"invalid credential")
#             return redirect("/")
