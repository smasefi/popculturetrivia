from django.shortcuts import render, get_object_or_404
from .models import Question, Category

def home(request):
    return render(request, 'trivia/home.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'trivia/categories.html', {'categories': categories})

def category_questions(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    questions = Question.objects.filter(category=category).prefetch_related('choices')
    return render(request, 'trivia/category_questions.html', {'category': category, 'questions': questions})


