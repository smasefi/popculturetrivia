from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Choice, Question, Category, Score
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'trivia/login.html')

def register(request):
    return render(request, 'trivia/register.html')

@login_required
def home(request):
    return render(request, 'trivia/home.html')

@login_required
def categories(request):
    categories = Category.objects.all()
    return render(request, 'trivia/categories.html', {'categories': categories})

@login_required
def category_questions(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    questions = Question.objects.filter(category=category)
    score,created = Score.objects.get_or_create(user=request.user)
    return render(request, 'trivia/category_questions.html', {'category': category,'questions': questions,'score': score.score})

@login_required
def submit_answer(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        selected_choice = get_object_or_404(Choice, pk=request.POST['choice'])
        if selected_choice.is_correct:
            score, created = Score.objects.get_or_create(user=request.user)
            score.score += 1
            score.save()
        return redirect(reverse('category_questions', args=[question.category.id]))
        if selected_choice != is_correct:
            return redirect(reverse('category_questions', args=[question.category.id]))
        
@login_required
def leaderboard(request):
    scores = Score.objects.all().order_by('-score') # highest to lowest
    context = {'scores' : scores}
    return render(request, 'trivia/leaderboard.html', context)