from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models.functions import TruncDate
from django.db.models import Count

from vocab_app.ai_generator import generate_word_of_the_day

from .models import Word, UserProgress
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    today = timezone.now().date()
    today_word = Word.objects.filter(created_at__date=today).first()
    
    if not today_word:
        while True:
            word_data = generate_word_of_the_day()
            
            if not Word.objects.filter(word=word_data['word']).exists():
                break

        today_word = Word.objects.create(
            word=word_data['word'],
            definition=word_data['definition'],
            example_sentence=word_data['example_sentence'],
            difficulty_level=word_data['difficulty_level'],
            ai_generated=True
        )
    
    return render(request, 'vocab_app/index.html', {'word': today_word})

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("vocab_app:index")
        messages.error(request, "Registration failed. Please check the errors.")
    else:
        form = CustomUserCreationForm()
    return render(request, "vocab_app/register.html", {"form": form})

@login_required(login_url='/login')
def word_detail(request, pk):
    word = get_object_or_404(Word, pk=pk)
    progress = None
    if request.user.is_authenticated:
        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            word=word
        )
    
    related_words = Word.objects.filter(
        difficulty_level=word.difficulty_level
    ).exclude(id=word.id)[:3]
    
    return render(request, 'vocab_app/word_detail.html', {
        'word': word,
        'progress': progress,
        'related_words': related_words
    })

@login_required(login_url='/login')
def practice(request):
    learned_words = UserProgress.objects.filter(
        user=request.user,
        learned=True
    ).values_list('word_id', flat=True)
    
    words = Word.objects.exclude(id__in=learned_words)[:5]
    return render(request, 'vocab_app/practice.html', {'words': words})

@login_required(login_url='/login')
def mark_learned(request, word_id):
    progress = get_object_or_404(UserProgress, user=request.user, word_id=word_id)
    progress.learned = True
    progress.save()
    return redirect('vocab_app:practice')

@login_required(login_url='/login')
def dashboard(request):
    learned_words = UserProgress.objects.filter(
        user=request.user,
        learned=True
    ).select_related('word').order_by('-last_reviewed')
    
    total_learned = learned_words.count()
    total_available = Word.objects.count()
    learning_progress = (total_learned / total_available * 100) if total_available > 0 else 0
    
    difficulty_stats = learned_words.values('word__difficulty_level').annotate(
        count=Count('id')
    ).order_by('word__difficulty_level')
    
    daily_progress = learned_words.annotate(
        date=TruncDate('last_reviewed')
    ).values('date').annotate(
        words_learned=Count('id')
    ).order_by('-date')[:7]
    
    return render(request, 'vocab_app/dashboard.html', {
        'learned_words': learned_words,
        'total_learned': total_learned,
        'total_available': total_available,
        'learning_progress': round(learning_progress, 1),
        'difficulty_stats': difficulty_stats,
        'daily_progress': daily_progress,
    })
