from django.core.management.base import BaseCommand
from django.utils import timezone
from vocab_app.models import Word
from vocab_app.ai_generator import generate_word_of_the_day

class Command(BaseCommand):
    help = 'Generate a new word of the day using AI'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        existing_word = Word.objects.filter(created_at__date=today).first()
        
        if not existing_word:
            word_data = generate_word_of_the_day()
            
            word = Word.objects.create(
                word=word_data['word'],
                definition=word_data['definition'],
                example_sentence=word_data['example_sentence'],
                difficulty_level=word_data['difficulty_level'],
                ai_generated=True,
                created_at=timezone.now()
            )
            
            self.stdout.write(self.style.SUCCESS(f'Successfully generated new word: {word.word}'))
        else:
            self.stdout.write(self.style.WARNING('Word for today already exists'))
