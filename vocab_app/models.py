from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Word(models.Model):
    class DifficultyLevel(models.TextChoices):
        BEGINNER = 'BEGINNER', 'Beginner'
        INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
        ADVANCED = 'ADVANCED', 'Advanced'

    word = models.CharField(max_length=100)
    definition = models.TextField()
    example_sentence = models.TextField()
    difficulty_level = models.CharField(
        max_length=20,
        choices=DifficultyLevel.choices,
    )
    created_at = models.DateTimeField(default=timezone.now)
    ai_generated = models.BooleanField(default=False)

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['-created_at']

class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.ForeignKey('Word', on_delete=models.CASCADE)
    learned = models.BooleanField(default=False)
    last_reviewed = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'word'], name='unique_user_word')
        ]
        verbose_name = "User Progress"
        verbose_name_plural = "User Progress"

    def __str__(self):
        return f"{self.user} - {self.word} ({'Learned' if self.learned else 'Not Learned'})"
