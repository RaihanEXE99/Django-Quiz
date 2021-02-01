from django.shortcuts import render,redirect,get_object_or_404
from .models import CustomizeQuiz, Tquestion, Myself, Slide
from django.contrib.auth.decorators import login_required
from cloudinary import CloudinaryImage
# Create your views here.
#Quiz
def Mquiz(request):
    quiz = CustomizeQuiz.objects.filter()
    arg = {
        'x': quiz[0]
    }
    return render(request, 'Quiz/quiz.html', arg)

@login_required(login_url="/account/login_view/")    
def question(request, that_quiz_id):
    that_quiz = CustomizeQuiz.objects.get(id=that_quiz_id)
    questions = Tquestion.objects.filter(that_Quiz=that_quiz)
    count = 0
    for x in questions:
        count += 1
    arg = {
        'that_quiz' : that_quiz,
        'questions': questions,
        'count' : count
    }
    return render(request, 'Quiz/questions.html', arg)

@login_required(login_url="/account/login_view/")
def Submission(request, that_quiz_id):
    if request.method == "POST":
        counter = questionCounter(that_quiz_id)

        Mystrlist = ""
        for x in range(1, counter + 1):
            Mystrlist += request.POST[str(x)]
        print(Mystrlist)

        answers = answerList(that_quiz_id)
        print(answers)
        
        analysisList = analysis(Mystrlist, answers, counter)

        correct = analysisList[0]
        wrong = analysisList[1]
        percentage = analysisList[2]

        print(correct,wrong,percentage)

        # quiz = CustomizeQuiz.objects.get(id=that_quiz_id)
        thatUser = request.user

        done = Myself(me=thatUser, answer=answers, correct=correct, wrong=wrong, percentage=percentage)
        done.save()
        # done = Notification(projectName=projectName, reqUser=reqUser, message=message,toAdmin=toAdmin)
        # done.save()
        # print(message,projectName,reqUser)
        verification = int(done.urlhash)
        print(done.urlhash)
        return redirect('Quiz:Score',verification=verification)

# # FUNCTIONS
def questionCounter(that_quiz_id):
    that_quiz = CustomizeQuiz.objects.get(id=that_quiz_id)
    all_question = Tquestion.objects.filter(that_Quiz=that_quiz)
    counter = 0
    for x in all_question:
        counter += 1
    return counter

def answerList(that_quiz_id):
    that_quiz = CustomizeQuiz.objects.get(id=that_quiz_id)
    all_question = Tquestion.objects.filter(that_Quiz=that_quiz)
    Anslist = ""
    for x in all_question:
        Anslist += x.answer[0]
    return Anslist

def analysis(Mystrlist, answers, counter):
    correct = 0
    wrong = 0
    for x in range(0, counter):
        if Mystrlist[x] == answers[x]:
            correct += 1
        else:
            wrong += 1
    percentage = int((correct*100)/counter)
    analysisList = [correct,wrong,percentage]
    return analysisList

# Slide
@login_required(login_url="/account/login_view/")
def slide(request, that_slide_no):
    that_quiz = CustomizeQuiz.objects.filter()
    that_quiz = that_quiz[0]
    that_slide = Slide.objects.filter(no=that_slide_no)
    #
    # img = cloudinary.CloudinaryImage(“sample”, format=“png”)
    #
    counter = SlideCounter()
    arg = {
        "slide": that_slide,
        "count": counter,
        "prev": that_slide_no - 1,
        "next": that_slide_no + 1,
        "that_quiz": that_quiz,
        # "that_slide_img" : that_slide_img
    }
    return render(request, 'Quiz/slide.html', arg)
    
def SlideCounter():
    counter = 0
    slides = Slide.objects.filter()
    for x in slides:
        counter += 1
    
    return counter

@login_required(login_url="/account/login_view/")
def certificate(request, verification):
    that_submit = Myself.objects.get(urlhash=verification)
    print(that_submit)
    return render(request, 'Quiz/Certificate.html', {
        'that_submit' : that_submit
    })

@login_required(login_url="/account/login_view/")
def Score(request, verification):
    that_submit = Myself.objects.get(urlhash=verification)
    print(that_submit)
    return render(request, 'Quiz/score.html', {
        'that_submit' : that_submit
    })