from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Account,MyAccountManager
from account.forms import RegistrationForm, AccountAuthenticationForm,UpdatePassword, AccountUpdateForm
from django.contrib.auth.decorators import login_required

from Quiz.models import CustomizeQuiz,Tquestion,Myself,Slide,Department_or_branch


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.hashers import make_password

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect("Quiz:Mquiz")
        else:
            try:
                new_password1 = request.POST['new_password1']
                new_password2 = request.POST['new_password2']
                if (new_password1 != new_password2):
                    messages.error(request, 'New and Confirm password is not same,Try again.')
                else:
                    messages.error(request, "This wasn't your old password")
            except:
                messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })

# def registration_view(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # post = form.save(commit=False)
#             form.save()
#             return redirect('account:login_view')
#         else:
#             try:
#                 new_password1 = request.POST['password1']
#                 new_password2 = request.POST['password2']
#                 if (new_password1 != new_password2):
#                     messages.error(request, 'Password and Confirm password is not same,Try again.')
#                 else:
#                     messages.error(request, "Employe Id is taken or something wrong happened")
#             except:
#                 messages.error(request, 'Please correct the error ')
#     form = RegistrationForm()
#     return render(request, 'account/register.html', {'form': form})

def registration_view(request):
    if request.method == "POST":
        new_password1 = request.POST['password']
        new_password2 = request.POST['password2']
        if (new_password1 != new_password2):
            messages.error(request, 'Password and Confirm password is not same,Try again.')
        else:
            try:
                employeId = request.POST['employeId']
                full_name = request.POST['full_name']
                Department = request.POST['Department']
                password = request.POST['password']
                password = make_password(password)
                acc = Account(employeId=employeId, full_name=full_name, Department=Department,password=password)
                acc.save()
                return redirect('account:login_view')
            except:
                messages.error(request, "Employe Id is taken or something wrong happened")
    dor = Department_or_branch.objects.filter()
    return render(request, 'account/register.html', {
        'dor' : dor
    })

def login_view(request):
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            employeId = request.POST['employeId']
            password = request.POST['password']
            user = authenticate(employeId=employeId, password=password)

            if user:
                login(request, user)
                return redirect("Quiz:Mquiz")
        else:
            messages.error(request, 'Wrong Employe Id or Password')
    form = AccountAuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


@login_required(login_url="/account/login_view/")
def logout_view(request):
	logout(request)
	return redirect('/')

@login_required(login_url="/account/login_view/")
def mysubmissions(request):
    that_user = request.user
    submissions = Myself.objects.filter(me=that_user).order_by('-timeStamp')
    return render(request, 'account/mysubmissions.html', {
        'submissions' : submissions
    })

@login_required(login_url="/account/login_view/")
def adminDashboard(request):
    ans = answerList()

    print(ans)
    submissions = Myself.objects.filter().order_by('-timeStamp')
    return render(request, 'account/AdminDashboard.html', {
        'submissions': submissions,
        'ans' : ans
    })

@login_required(login_url="/account/login_view/")
def adminPanel(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        that_quiz = CustomizeQuiz.objects.filter()
        that_quiz = that_quiz[0]
        print(that_quiz)
        CustomizeQuiz.objects.filter().update(title=title,description=description)
        # done = Myself(me=thatUser, answer=answers, correct=correct, wrong=wrong, percentage=percentage)
        # done.save()
    return render(request, 'account/adminPanel.html')

@login_required(login_url="/account/login_view/")
def analysis(request):
    total_submit = Myself.objects.filter()
    tsc = 0
    b6p = 0
    for x in total_submit:
        tsc += 1
        if (x.percentage < 60):
            b6p += 1
    Rb6p = int((b6p / tsc) * 100)
    Bb6p = 100 - Rb6p

    bS = []
    DbN = Department_or_branch.objects.filter()     
    Temp_dict={}
    for x in DbN:
        altCounter = 0
        alt = Account.objects.filter(Department=x.Department_or_branch_name)
        for y in alt:
            altCounter += 1
        # Temp_dict={}
        Temp_dict[x.Department_or_branch_name] = altCounter
        # print(Temp_dict)
        # bS.append(Temp_dict)
    print(Temp_dict)
    # print(DbN[0][x.Department_or_branch_name])



    return render(request, 'account/analysisPanel.html', {
        'tsc': tsc,
        'b6p': b6p,
        'Rb6p': Rb6p,
        'Bb6p': Bb6p,
        'Temp_dict' : Temp_dict 
    })

def answerList():
    that_quiz = CustomizeQuiz.objects.filter()
    that_quiz = that_quiz[0]
    all_question = Tquestion.objects.filter(that_Quiz=that_quiz)
    Anslist = ""
    for x in all_question:
        Anslist += x.answer[0]
    return Anslist


# @login_required(login_url="/account/login_view/")
# def ChangePass(request):
#     if request.POST:
#         that_user = request.user
#         # that_user = Account.objects.filter(id=that_user.id)
#         form = UpdatePassword(request.POST)
#         print("that_user")
#         # if form.is_valid():
#         employeId = request.POST['employeId']
#         # oldPass = request.POST['oldPass']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         # print((that_user.employeId),(employeId))
#         if (str(that_user.employeId) == employeId):
#             # print((that_user.employeId), (employeId))
#             emp = str(that_user.employeId)
#             Account.objects.filter(employeId=emp).update(password=password)
#             # print("done2")
            
#             # user = authenticate(employeId=employeId, password=password)
#             # if user:
#             #     login(request, user)
#             return redirect("Quiz:Mquiz")
#     form = UpdatePassword()
#     return render(request, 'account/updatePassword.html', {'form': form})