from django.core.management.base import BaseCommand
from vocab_app.models import Word
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with vocabulary words'

    def handle(self, *args, **kwargs):
        vocabulary_data = [
            {
                'word': 'ephemeral',
                'definition': 'Lasting for a very short time',
                'example_sentence': 'The ephemeral beauty of a sunset is what makes it special.',
                'difficulty_level': 'ADVANCED'
            },
            {
                'word': 'ubiquitous',
                'definition': 'Present, appearing, or found everywhere',
                'example_sentence': 'Mobile phones have become ubiquitous in modern society.',
                'difficulty_level': 'ADVANCED'
            },
            {
                'word': 'serendipity',
                'definition': 'The occurrence and development of events by chance in a happy or beneficial way',
                'example_sentence': 'Finding his dream job while on vacation was pure serendipity.',
                'difficulty_level': 'ADVANCED'
            },
            {
                'word': 'procrastinate',
                'definition': 'Delay or postpone action; put off doing something',
                'example_sentence': 'She tends to procrastinate when it comes to doing her homework.',
                'difficulty_level': 'INTERMEDIATE'
            },
            {
                'word': 'ambiguous',
                'definition': 'Open to more than one interpretation; not having one obvious meaning',
                'example_sentence': "The poem's ambiguous ending has been debated by critics for years.",
                'difficulty_level': 'INTERMEDIATE'
            },
            {
                'word': 'perseverance',
                'definition': 'Persistence in doing something despite difficulty or delay in achieving success',
                'example_sentence': 'Through perseverance, she finally learned to play the piano.',
                'difficulty_level': 'INTERMEDIATE'
            },
            {
                'word': 'curious',
                'definition': 'Eager to learn or know something',
                'example_sentence': 'The curious child asked many questions about space.',
                'difficulty_level': 'BEGINNER'
            },
            {
                'word': 'appreciate',
                'definition': 'Recognize the full worth of something',
                'example_sentence': 'I appreciate your help with this project.',
                'difficulty_level': 'BEGINNER'
            },
            {
                'word': 'wonderful',
                'definition': 'Inspiring delight, pleasure, or admiration',
                'example_sentence': 'We had a wonderful time at the party.',
                'difficulty_level': 'BEGINNER'
            },
            {
                'word': 'resilient',
                'definition': 'Able to withstand or recover quickly from difficult conditions',
                'example_sentence': 'Plants are resilient and can often survive harsh weather.',
                'difficulty_level': 'INTERMEDIATE'
            },
            {
                'word': 'pragmatic',
                'definition': 'Dealing with things sensibly and realistically',
                'example_sentence': 'We need a pragmatic approach to solve this problem.',
                'difficulty_level': 'ADVANCED'
            },
            {
                'word': 'authentic',
                'definition': 'Genuine or real; not fake or imitation',
                'example_sentence': 'The restaurant serves authentic Italian cuisine.',
                'difficulty_level': 'INTERMEDIATE'
            },
            {
                'word': 'benevolent',
                'definition': 'Kind, generous, and caring about others',
                'example_sentence': 'The benevolent donor provided scholarships for students.',
                'difficulty_level': 'ADVANCED'
            },
            {
                'word': 'diligent',
                'definition': "Having or showing care and conscientiousness in one's work or duties",
                'example_sentence': 'The diligent student always completed her assignments on time.',
                'difficulty_level': 'INTERMEDIATE'
            },
            {
                'word': 'enhance',
                'definition': 'Intensify, increase, or further improve the quality, value, or extent of',
                'example_sentence': 'The new features will enhance the user experience.',
                'difficulty_level': 'BEGINNER'
            },
            {
                "word": "profound",
                "definition": "Having deep meaning or significance",
                "example_sentence": "The professor's lecture was full of profound insights.",
                "difficulty_level": "ADVANCED"
            },
            {
                "word": "melancholy",
                "definition": "A deep, persistent sadness or sorrow",
                "example_sentence": "The melancholy music matched the somber mood of the evening.",
                "difficulty_level": "INTERMEDIATE"
            },
            {
                "word": "inevitable",
                "definition": "Certain to happen; unavoidable",
                "example_sentence": "It was inevitable that they would eventually find out the truth.",
                "difficulty_level": "INTERMEDIATE"
            },
            {
                "word": "aesthetic",
                "definition": "Relating to beauty or artistic expression",
                "example_sentence": "The artist's work had a unique aesthetic that captivated many.",
                "difficulty_level": "ADVANCED"
            },
            {
                "word": "dormant",
                "definition": "In a state of rest or inactivity",
                "example_sentence": "The volcano had been dormant for centuries before it erupted.",
                "difficulty_level": "INTERMEDIATE"
            },
            {
                "word": "indispensable",
                "definition": "Absolutely necessary or essential",
                "example_sentence": "A good internet connection is indispensable for remote work.",
                "difficulty_level": "ADVANCED"
            }
        ]

        for word_data in vocabulary_data:
            if not Word.objects.filter(word=word_data['word']).exists():
                Word.objects.create(
                    word=word_data['word'],
                    definition=word_data['definition'],
                    example_sentence=word_data['example_sentence'],
                    difficulty_level=word_data['difficulty_level'],
                    created_at=timezone.now()
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(vocabulary_data)} words'))