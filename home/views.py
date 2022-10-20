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
        print(basic_answers_c)
        print(intermediate_answers_c)
        print(advance_answers_c)

        basic_answers = []
        for i in range(1,8):
           basic_answers.append(request.POST.get("answer_basic"+str(i)))
        intermediate_answers = []
        for i in range(1,6):
           intermediate_answers.append(request.POST.get("answer_intermediate"+str(i)))
        advance_answers = []
        for i in range(1,4):
           advance_answers.append(request.POST.get("answer_advance"+str(i)))
        print(basic_answers)
        print(intermediate_answers)
        print(advance_answers)

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
            "performance_bad":performance_bad,
            "performance_medium":performance_medium,
            "performance_good":performance_good,
            "score":score,
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

    print(questions_advance_new)

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
        print(basic_answers_c)
        print(intermediate_answers_c)
        print(advance_answers_c)

        basic_answers = []
        for i in range(1,8):
           basic_answers.append(request.POST.get("answer_basic"+str(i)))
        intermediate_answers = []
        for i in range(1,6):
           intermediate_answers.append(request.POST.get("answer_intermediate"+str(i)))
        advance_answers = []
        for i in range(1,4):
           advance_answers.append(request.POST.get("answer_advance"+str(i)))
        print(basic_answers)
        print(intermediate_answers)
        print(advance_answers)

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
        print(basic_answers_c)
        print(intermediate_answers_c)
        print(advance_answers_c)

        basic_answers = []
        for i in range(1,8):
           basic_answers.append(request.POST.get("answer_basic"+str(i)))
        intermediate_answers = []
        for i in range(1,6):
           intermediate_answers.append(request.POST.get("answer_intermediate"+str(i)))
        advance_answers = []
        for i in range(1,4):
           advance_answers.append(request.POST.get("answer_advance"+str(i)))

        correct_answers = int(0)
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

        print(correct_answers)
        print(wrong_answers)

        context = {
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
    return render(request, "index.html")

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
            return render(request, "login.html")
            messages.error(request, "Credentials not matching!")
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
            messages.error(request, "password and confirm password fields dont match!")
            return redirect("register")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "The account has been created successfully.")
        return redirect("login")
    return render(request, "register.html")

def add_question(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        question = request.POST.get("question")
        desc = request.POST.get("desc")
        print(desc.name)
        print(desc.size)
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

def randompage_difficulty(request):
    if request.user.is_anonymous:
        return redirect("/login")
    elif request.method == "POST":
        difficulty = request.POST.get("difficulty")
        quiz = request.POST.get("quiz")
        print(difficulty)
        print(quiz)
        if quiz == "randompage":
            if difficulty == "basic":
                return render(request, "randompage_basic.html")
            elif difficulty == "intermediate":
                return render(request, "randompage_intermediate.html")
            else:
                return render(request, "randompage_expert.html")
        elif quiz == "python":
            if difficulty == "basic":
                return render(request, "python_basic.html")
            elif difficulty == "intermediate":
                return render(request, "python_intermediate.html")
            else:
                return render(request, "python_expert.html")
        else:
            if difficulty == "basic":
                return render(request, "dbms_basic.html")
            elif difficulty == "intermediate":
                return render(request, "dbms_intermediate.html")
            else:
                return render(request, "dbms_expert.html")

    else:
        context = {
            'randompage':True,
        }
        return render(request, "difficulty.html",context)

def python_difficulty(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        context = {
            'python':True,
        }
        return render(request, "difficulty.html",context)

def dbms_difficulty(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        context = {
            'dbms':True,
        }
        return render(request, "difficulty.html",context)

