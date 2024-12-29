from django.conf import settings
import json
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

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
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config={"response_mime_type": "application/json"}, )
        response = model.generate_content(prompt)
        content = response.text
        word_data = json.loads(content)
        
        return word_data
    except Exception as e:
        return {
            "word": "resilient",
            "definition": "Able to withstand or recover quickly from difficult conditions",
            "example_sentence": "The application is resilient and can handle API failures gracefully.",
            "difficulty_level": "INTERMEDIATE"
        }
