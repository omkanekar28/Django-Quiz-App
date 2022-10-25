from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import *
from django.http import HttpResponse

import random

# Create your views here.

def randompage(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        basic_answers_c = []
        for i in range(1,8):
           basic_answers_c.append(request.POST.get("question_basic"+str(i)))
        intermediate_answers_c = []
        for i in range(1,6):
           intermediate_answers_c.append(request.POST.get("question_intermediate"+str(i)))
        advance_answers_c = []
        for i in range(1,4):
           advance_answers_c.append(request.POST.get("question_advance"+str(i)))
        basic_answers = []
        for i in range(1,8):
           basic_answers.append(request.POST.get("answer_basic"+str(i)))
        intermediate_answers = []
        for i in range(1,6):
           intermediate_answers.append(request.POST.get("answer_intermediate"+str(i)))
        advance_answers = []
        for i in range(1,4):
           advance_answers.append(request.POST.get("answer_advance"+str(i)))
        correct_answers = 0
        wrong_answers = 0

        score = 0
        counter = 0
        
        for i in basic_answers:
            if i == basic_answers_c[counter]:
                score= score + 5
                correct_answers = correct_answers + 1
            counter = counter + 1

        counter = 0

        for i in intermediate_answers:
            if i == intermediate_answers_c[counter]:
                score= score + 10
                correct_answers = correct_answers + 1
            counter = counter + 1

        counter = 0

        for i in advance_answers:
            if i == advance_answers_c[counter]:
                score= score + 15
                correct_answers = correct_answers + 1
            counter = counter + 1

        counter = 0 

        wrong_answers = 15 - correct_answers
        
        performance_bad = False
        performance_medium = False
        performance_good = False

        if score <= 20:
            performance_bad = True
        elif score <= 80:
            performance_medium = True
        else:
            performance_good = True

        context = {
            "basic_ans":basic_answers,
            "basic_ans_c":basic_answers_c,
            "intermediate_ans":intermediate_answers,
            "intermediate_ans_c":intermediate_answers_c,
            "advance_ans":advance_answers,
            "advance_ans_c":advance_answers_c,
            "performance_bad":performance_bad,
            "performance_medium":performance_medium,
            "performance_good":performance_good,
            "score":score,
            "correct":correct_answers,
            "wrong":wrong_answers,
            "total":130
        }
        return render(request, "results.html",context)
    questions_basic = QuesModel.objects.filter(category="basic", marks="5")
    questions_basic = list(questions_basic)

    basic_1 = random.randint(0,len(questions_basic)-1)
    question_basic_1 = questions_basic[basic_1]
    questions_basic.pop(basic_1)

    basic_2 = random.randint(0,len(questions_basic)-1)
    question_basic_2 = questions_basic[basic_2]
    questions_basic.pop(basic_2)

    basic_3 = random.randint(0,len(questions_basic)-1)
    question_basic_3 = questions_basic[basic_3]
    questions_basic.pop(basic_3)

    basic_4 = random.randint(0,len(questions_basic)-1)
    question_basic_4 = questions_basic[basic_4]
    questions_basic.pop(basic_4)

    basic_5 = random.randint(0,len(questions_basic)-1)
    question_basic_5 = questions_basic[basic_5]
    questions_basic.pop(basic_5)
    
    basic_6 = random.randint(0,len(questions_basic)-1)
    question_basic_6 = questions_basic[basic_6]
    questions_basic.pop(basic_6)

    basic_7 = random.randint(0,len(questions_basic)-1)
    question_basic_7 = questions_basic[basic_7]
    questions_basic.pop(basic_7)

    questions_basic_new = [question_basic_1, question_basic_2, question_basic_3, question_basic_4, question_basic_5, question_basic_6, question_basic_7]




    questions_intermediate = QuesModel.objects.filter(category="intermediate", marks="10")
    questions_intermediate = list(questions_intermediate)

    intermediate_1 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_1 = questions_intermediate[intermediate_1]
    questions_intermediate.pop(intermediate_1)

    intermediate_2 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_2 = questions_intermediate[intermediate_2]
    questions_intermediate.pop(intermediate_2)

    intermediate_3 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_3 = questions_intermediate[intermediate_3]
    questions_intermediate.pop(intermediate_3)

    intermediate_4 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_4 = questions_intermediate[intermediate_4]
    questions_intermediate.pop(intermediate_4)

    intermediate_5 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_5 = questions_intermediate[intermediate_5]
    questions_intermediate.pop(intermediate_5)

    questions_intermediate_new = [question_intermediate_1, question_intermediate_2, question_intermediate_3, question_intermediate_4, question_intermediate_5]
    
    
    questions_advance = QuesModel.objects.filter(category="advance", marks="15")
    questions_advance = list(questions_advance)

    advance_1 = random.randint(0,len(questions_advance)-1)
    question_advance_1 = questions_advance[advance_1]
    questions_advance.pop(advance_1)

    advance_2 = random.randint(0,len(questions_advance)-1)
    question_advance_2 = questions_advance[advance_2]
    questions_advance.pop(advance_2)

    advance_3 = random.randint(0,len(questions_advance)-1)
    question_advance_3 = questions_advance[advance_3]
    questions_advance.pop(advance_3)
    
    questions_advance_new = [question_advance_1, question_advance_2, question_advance_3]


    context={'questions_list_basic':questions_basic_new,
            'questions_list_intermediate':questions_intermediate_new,
            'questions_list_advance':questions_advance_new}
    return render(request, "randompage.html",context)



def python(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        basic_answers_c = []
        for i in range(1,8):
           basic_answers_c.append(request.POST.get("question_basic"+str(i)))
        intermediate_answers_c = []
        for i in range(1,6):
           intermediate_answers_c.append(request.POST.get("question_intermediate"+str(i)))
        advance_answers_c = []
        for i in range(1,4):
           advance_answers_c.append(request.POST.get("question_advance"+str(i)))

        basic_answers = []
        for i in range(1,8):
           basic_answers.append(request.POST.get("answer_basic"+str(i)))
        intermediate_answers = []
        for i in range(1,6):
           intermediate_answers.append(request.POST.get("answer_intermediate"+str(i)))
        advance_answers = []
        for i in range(1,4):
           advance_answers.append(request.POST.get("answer_advance"+str(i)))

        score = 0
        counter = 0
        
        for i in basic_answers:
            if i == basic_answers_c[counter]:
                score= score + 5
            counter = counter + 1

        counter = 0

        for i in intermediate_answers:
            if i == intermediate_answers_c[counter]:
                score= score + 10
            counter = counter + 1

        counter = 0

        for i in advance_answers:
            if i == advance_answers_c[counter]:
                score= score + 15
            counter = counter + 1

        counter = 0 
        
        performance_bad = False
        performance_medium = False
        performance_good = False

        if score <= 20:
            performance_bad = True
        elif score <= 80:
            performance_medium = True
        else:
            performance_good = True

        context = {
            "basic_ans":basic_answers,
            "basic_ans_c":basic_answers_c,
            "intermediate_ans":intermediate_answers,
            "intermediate_ans_c":intermediate_answers_c,
            "advance_ans":advance_answers,
            "advance_ans_c":advance_answers_c,
            "performance_bad":performance_bad,
            "performance_medium":performance_medium,
            "performance_good":performance_good,
            "score":score,
            "total":130
        }
        return render(request, "results.html",context)

    questions_basic = QuesModel.objects.filter(subject="Python", category="basic", marks="5")
    questions_basic = list(questions_basic)

    basic_1 = random.randint(0,len(questions_basic)-1)
    question_basic_1 = questions_basic[basic_1]
    questions_basic.pop(basic_1)

    basic_2 = random.randint(0,len(questions_basic)-1)
    question_basic_2 = questions_basic[basic_2]
    questions_basic.pop(basic_2)

    basic_3 = random.randint(0,len(questions_basic)-1)
    question_basic_3 = questions_basic[basic_3]
    questions_basic.pop(basic_3)

    basic_4 = random.randint(0,len(questions_basic)-1)
    question_basic_4 = questions_basic[basic_4]
    questions_basic.pop(basic_4)

    basic_5 = random.randint(0,len(questions_basic)-1)
    question_basic_5 = questions_basic[basic_5]
    questions_basic.pop(basic_5)
    
    basic_6 = random.randint(0,len(questions_basic)-1)
    question_basic_6 = questions_basic[basic_6]
    questions_basic.pop(basic_6)

    basic_7 = random.randint(0,len(questions_basic)-1)
    question_basic_7 = questions_basic[basic_7]
    questions_basic.pop(basic_7)

    questions_basic_new = [question_basic_1, question_basic_2, question_basic_3, question_basic_4, question_basic_5, question_basic_6, question_basic_7]

    questions_intermediate = QuesModel.objects.filter(subject="Python", category="intermediate", marks="10")
    questions_intermediate = list(questions_intermediate)

    intermediate_1 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_1 = questions_intermediate[intermediate_1]
    questions_intermediate.pop(intermediate_1)

    intermediate_2 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_2 = questions_intermediate[intermediate_2]
    questions_intermediate.pop(intermediate_2)

    intermediate_3 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_3 = questions_intermediate[intermediate_3]
    questions_intermediate.pop(intermediate_3)

    intermediate_4 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_4 = questions_intermediate[intermediate_4]
    questions_intermediate.pop(intermediate_4)

    intermediate_5 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_5 = questions_intermediate[intermediate_5]
    questions_intermediate.pop(intermediate_5)

    questions_intermediate_new = [question_intermediate_1, question_intermediate_2, question_intermediate_3, question_intermediate_4, question_intermediate_5]

    questions_advance = QuesModel.objects.filter(subject="Python", category="advance", marks="15")
    questions_advance = list(questions_advance)

    advance_1 = random.randint(0,len(questions_advance)-1)
    question_advance_1 = questions_advance[advance_1]
    questions_advance.pop(advance_1)

    advance_2 = random.randint(0,len(questions_advance)-1)
    question_advance_2 = questions_advance[advance_2]
    questions_advance.pop(advance_2)

    advance_3 = random.randint(0,len(questions_advance)-1)
    question_advance_3 = questions_advance[advance_3]
    questions_advance.pop(advance_3)
    
    questions_advance_new = [question_advance_1, question_advance_2, question_advance_3]

    context={'questions_list_basic':questions_basic_new,
            'questions_list_intermediate':questions_intermediate_new,
            'questions_list_advance':questions_advance_new,
        }
    return render(request, "python.html",context)



def dbms(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        basic_answers_c = []
        for i in range(1,8):
           basic_answers_c.append(request.POST.get("question_basic"+str(i)))
        intermediate_answers_c = []
        for i in range(1,6):
           intermediate_answers_c.append(request.POST.get("question_intermediate"+str(i)))
        advance_answers_c = []
        for i in range(1,4):
           advance_answers_c.append(request.POST.get("question_advance"+str(i)))

        basic_answers = []
        for i in range(1,8):
           basic_answers.append(request.POST.get("answer_basic"+str(i)))
        intermediate_answers = []
        for i in range(1,6):
           intermediate_answers.append(request.POST.get("answer_intermediate"+str(i)))
        advance_answers = []
        for i in range(1,4):
           advance_answers.append(request.POST.get("answer_advance"+str(i)))

        correct_answers = 0
        wrong_answers = 0

        score = 0
        counter = 0
        
        for i in basic_answers:
            if i == basic_answers_c[counter]:
                score= score + 5
                correct_answers = correct_answers + 1
            counter = counter + 1

        counter = 0

        for i in intermediate_answers:
            if i == intermediate_answers_c[counter]:
                score= score + 10
                correct_answers = correct_answers + 1
            counter = counter + 1

        counter = 0

        for i in advance_answers:
            if i == advance_answers_c[counter]:
                score= score + 15
                correct_answers = correct_answers + 1
            counter = counter + 1

        counter = 0 

        wrong_answers = 15 - correct_answers
        
        performance_bad = False
        performance_medium = False
        performance_good = False

        if score <= 20:
            performance_bad = True
        elif score <= 80:
            performance_medium = True
        else:
            performance_good = True

        context = {
            "basic_ans":basic_answers,
            "basic_ans_c":basic_answers_c,
            "intermediate_ans":intermediate_answers,
            "intermediate_ans_c":intermediate_answers_c,
            "advance_ans":advance_answers,
            "advance_ans_c":advance_answers_c,
            "performance_bad":performance_bad,
            "performance_medium":performance_medium,
            "performance_good":performance_good,
            "score":score,
            "correct":correct_answers,
            "wrong":wrong_answers,
            "total":130
        }
        return render(request, "results.html",context)
    
    questions_basic = QuesModel.objects.filter(subject="DBMS", category="basic", marks="5")
    questions_basic = list(questions_basic)

    basic_1 = random.randint(0,len(questions_basic)-1)
    question_basic_1 = questions_basic[basic_1]
    questions_basic.pop(basic_1)

    basic_2 = random.randint(0,len(questions_basic)-1)
    question_basic_2 = questions_basic[basic_2]
    questions_basic.pop(basic_2)

    basic_3 = random.randint(0,len(questions_basic)-1)
    question_basic_3 = questions_basic[basic_3]
    questions_basic.pop(basic_3)

    basic_4 = random.randint(0,len(questions_basic)-1)
    question_basic_4 = questions_basic[basic_4]
    questions_basic.pop(basic_4)

    basic_5 = random.randint(0,len(questions_basic)-1)
    question_basic_5 = questions_basic[basic_5]
    questions_basic.pop(basic_5)
    
    basic_6 = random.randint(0,len(questions_basic)-1)
    question_basic_6 = questions_basic[basic_6]
    questions_basic.pop(basic_6)

    basic_7 = random.randint(0,len(questions_basic)-1)
    question_basic_7 = questions_basic[basic_7]
    questions_basic.pop(basic_7)

    questions_basic_new = [question_basic_1, question_basic_2, question_basic_3, question_basic_4, question_basic_5, question_basic_6, question_basic_7]

    questions_intermediate = QuesModel.objects.filter(subject="DBMS", category="intermediate", marks="10")
    questions_intermediate = list(questions_intermediate)

    intermediate_1 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_1 = questions_intermediate[intermediate_1]
    questions_intermediate.pop(intermediate_1)

    intermediate_2 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_2 = questions_intermediate[intermediate_2]
    questions_intermediate.pop(intermediate_2)

    intermediate_3 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_3 = questions_intermediate[intermediate_3]
    questions_intermediate.pop(intermediate_3)

    intermediate_4 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_4 = questions_intermediate[intermediate_4]
    questions_intermediate.pop(intermediate_4)

    intermediate_5 = random.randint(0,len(questions_intermediate)-1)
    question_intermediate_5 = questions_intermediate[intermediate_5]
    questions_intermediate.pop(intermediate_5)

    questions_intermediate_new = [question_intermediate_1, question_intermediate_2, question_intermediate_3, question_intermediate_4, question_intermediate_5]

    questions_advance = QuesModel.objects.filter(subject="DBMS", category="advance", marks="15")
    questions_advance = list(questions_advance)

    advance_1 = random.randint(0,len(questions_advance)-1)
    question_advance_1 = questions_advance[advance_1]
    questions_advance.pop(advance_1)

    advance_2 = random.randint(0,len(questions_advance)-1)
    question_advance_2 = questions_advance[advance_2]
    questions_advance.pop(advance_2)

    advance_3 = random.randint(0,len(questions_advance)-1)
    question_advance_3 = questions_advance[advance_3]
    questions_advance.pop(advance_3)
    
    questions_advance_new = [question_advance_1, question_advance_2, question_advance_3]

    context={'questions_list_basic':questions_basic_new,
            'questions_list_intermediate':questions_intermediate_new,
            'questions_list_advance':questions_advance_new,
        }
    return render(request, "dbms.html",context)

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    profiles = Profile.objects.all()
    current = request.user
    context = {
        "profiles":profiles,
        "current":current
    }
    return render(request, "index.html", context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/",)
        else:
            # No backend authenticated the credentials
            messages.info(request, "Credentials not matching!")
            return render(request, "login.html")
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("login")

def RegisterUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password:
            messages.info(request, "password and confirm password fields dont match!")
            return redirect("register")
        elif User.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect("register")
        user = User.objects.create_user(username=username, password=password)
        user.save()

        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model)
        new_profile.save()

        messages.success(request, "The account has been created successfully.")
        return redirect("login")
    return render(request, "register.html")

def add_question(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        question = request.POST.get("question")
        desc = request.FILES.get("desc")
        op1 = request.POST.get("op1")
        op2 = request.POST.get("op2")
        op3 = request.POST.get("op3")
        op4 = request.POST.get("op4")
        answer = request.POST.get("answer")
        explaination = request.POST.get("explaination")
        category = request.POST.get("category")
        marks = request.POST.get("marks")
        subject = request.POST.get("subject")
        quesmodel = QuesModel(question=question, desc=desc, op1=op1, op2=op2, op3=op3, op4=op4, ans=answer, explaination=explaination, category=category, marks=marks, subject=subject)
        quesmodel.save()
    if request.user.is_staff:
        return render(request, "add_question.html")
    else:
        return redirect("/")

def results(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request, "results.html")

def basic(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        basic_answers_c = []
        for i in range(1,16):
           basic_answers_c.append(request.POST.get("question_basic"+str(i)))

        basic_answers = []
        for i in range(1,16):
           basic_answers.append(request.POST.get("answer_basic"+str(i)))

        score = 0
        counter = 0

        correct_answers = 0
        wrong_answers = 0
        
        for i in basic_answers:
            if i == basic_answers_c[counter]:
                correct_answers = correct_answers + 1
                score= score + 5
            counter = counter + 1
        
        wrong_answers = 15 - correct_answers

        performance_bad = False
        performance_medium = False
        performance_good = False

        if score <= 20:
            performance_bad = True
        elif score <= 50:
            performance_medium = True
        else:
            performance_good = True

        context = {
            "basic_ans":basic_answers,
            "basic_ans_c":basic_answers_c,
            "correct":correct_answers,
            "wrong":wrong_answers,
            "performance_bad":performance_bad,
            "performance_medium":performance_medium,
            "performance_good":performance_good,
            "score":score,
            "total":75
        }
        return render(request, "results.html",context)

    questions_basic = QuesModel.objects.filter(category="basic", marks="5")
    questions_basic = list(questions_basic)
    random.shuffle(questions_basic)
    questions_basic_new = []
    for i in range(0,15):
        questions_basic_new.append(questions_basic[i])
    context = {
        "questions_list_basic":questions_basic_new,
    }
    return render(request, "basic.html",context)



def intermediate(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        intermediate_answers_c = []
        for i in range(1,16):
           intermediate_answers_c.append(request.POST.get("question_intermediate"+str(i)))
        intermediate_answers = []
        for i in range(1,16):
           intermediate_answers.append(request.POST.get("answer_intermediate"+str(i)))

        score = 0
        counter = 0

        correct_answers = 0
        wrong_answers = 0
        
        for i in intermediate_answers:
            if i == intermediate_answers_c[counter]:
                correct_answers = correct_answers + 1
                score= score + 10
            counter = counter + 1
        
        wrong_answers = 15 - correct_answers

        performance_bad = False
        performance_medium = False
        performance_good = False

        if score <= 40:
            performance_bad = True
        elif score <= 100:
            performance_medium = True
        else:
            performance_good = True

        context = {
            "intermediate_ans":intermediate_answers,
            "intermediate_ans_c":intermediate_answers_c,
            "correct":correct_answers,
            "wrong":wrong_answers,
            "performance_bad":performance_bad,
            "performance_medium":performance_medium,
            "performance_good":performance_good,
            "score":score,
            "total":150
        }
        return render(request, "results.html",context)
    questions_intermediate = QuesModel.objects.filter(category="intermediate", marks="10")
    questions_intermediate = list(questions_intermediate)
    random.shuffle(questions_intermediate)
    questions_intermediate_new = []
    for i in range(0,15):
        questions_intermediate_new.append(questions_intermediate[i])
    context = {
        "questions_list_intermediate":questions_intermediate_new,
    }
    return render(request, "intermediate.html",context)

def expert(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        expert_answers_c = []
        for i in range(1,16):
           expert_answers_c.append(request.POST.get("question_expert"+str(i)))
        expert_answers = []
        for i in range(1,16):
           expert_answers.append(request.POST.get("answer_expert"+str(i)))

        score = 0
        counter = 0

        correct_answers = 0
        wrong_answers = 0
        
        for i in expert_answers:
            if i == expert_answers_c[counter]:
                correct_answers = correct_answers + 1
                score= score + 15
            counter = counter + 1
        
        wrong_answers = 15 - correct_answers

        performance_bad = False
        performance_medium = False
        performance_good = False

        if score <= 60:
            performance_bad = True
        elif score <= 150:
            performance_medium = True
        else:
            performance_good = True

        context = {
            "advance_ans":expert_answers,
            "advance_ans_c":expert_answers_c,
            "correct":correct_answers,
            "wrong":wrong_answers,
            "performance_bad":performance_bad,
            "performance_medium":performance_medium,
            "performance_good":performance_good,
            "score":score,
            "total":225
        }
        return render(request, "results.html",context)
    questions_expert = QuesModel.objects.filter(category="advance", marks="15")
    questions_expert = list(questions_expert)
    random.shuffle(questions_expert)
    questions_expert_new = []
    for i in range(0,15):
        questions_expert_new.append(questions_expert[i])
    context = {
        "questions_list_expert":questions_expert_new,
    }
    return render(request, "expert.html",context)

def profile(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email_id = request.POST.get("email_id")
        bio = request.POST.get("bio")
        profileimg = request.FILES.get("profileimg")
        location = request.POST.get("location")

        user_profile = Profile.objects.get(user=request.user)

        if profileimg != None:
            user_profile.profileimg = profileimg

        user_profile.fname = fname
        user_profile.lname = lname
        user_profile.email_id = email_id
        user_profile.bio = bio
        user_profile.location = location

        user_profile.save()
    context = {
        "profile":Profile.objects.get(user=request.user)
    }
    return render(request, "profile.html",context)