from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupuser(request):

    #{'form':UserCreationForm()} >>> key:value
    # UserCreationForm() is a function
    # return render(request, 'todo/signup.html', {'form':UserCreationForm()}) 

    if request.method == 'GET':
        return render(request, 'todo/signup.html', { 'form' : UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            return redirect('currenttodos')
        else:
            #Tell the user taht passwords do not match
            return render(
                request, 
                'todo/signup.html', 
                {
                    'form':UserCreationForm(),
                }
            )

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')

