from openai import OpenAI
from django.conf import settings
import json

openai_api_key = settings.OPENAI_API_KEY

def generate_word_of_the_day():
    prompt = """Generate a vocabulary word with its definition and an example sentence. 
    Include difficulty level (BEGINNER, INTERMEDIATE, or ADVANCED). 
    Return as JSON with the following structure:
    {
        "word": "word here (lower case)",
        "definition": "definition here",
        "example_sentence": "example sentence here",
        "difficulty_level": "BEGINNER/INTERMEDIATE/ADVANCED"
    }
    Make sure the word is educational and appropriate for learning."""

    try:
        client = OpenAI(
            api_key = openai_api_key
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful language learning assistant that generates vocabulary words."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        
        content = response.choices[0].message.content
        word_data = json.loads(content)
        
        return word_data
    except Exception as e:
        return {
            "word": "resilient",
            "definition": "Able to withstand or recover quickly from difficult conditions",
            "example_sentence": "The application is resilient and can handle API failures gracefully.",
            "difficulty_level": "INTERMEDIATE"
        }
