# CS50W Capstone - Daily English Vocab Learning
Daily English Vocab Learning is a web application that helps me learn new English words every day, from beginner to advanced level. It’s designed for people like me who are not native English speakers and want to improve their vocabulary over time. The goal is to make learning vocabulary feel natural and exciting, with daily progress that encourages continued growth.

This web application uses Django on the server side to handle things like user data and vocabulary content. For the front end, it uses JavaScript to make the app mobile responsive, so it works well on different screen sizes. Tailwind CSS is used for styling, giving the app a clean, modern look and making it easier to tweak the design.

## Distinctiveness and Complexity
This project is distinctly different from the 4 week projects and the old CS50W Pizza project because this web app is a english vocab learning and use OpenAI to generate dynamic data daily. It’s quite complex for me because I created a user dashboard to display overall progress and learn how to use Tailwind CSS for speed up development, which isn’t something in the 4 week projects.

## Files in This Project
Here is an overview of the files included in this project:
### `vocab_app/management`
This folder contains two additional management files for the command line, which can be used to automate tasks related to vocabulary management.
- `generate_daily_word.py`: Generate daily a daily vocabulary using OpenAI.
- `populate_words.py`: Populate pre-set vocabulary from Json data.

### `vocab_app/templates`
- `layout.html`: The base template using Tailwind CSS for styling.
- `index.html`: The homepage that shows a daily vocabulary.
- `practice.html`: Displays practice words and user can mark as learned or view word details.
- `word_detail.html`: Display word details and relate words by difficulty level.
- `dashboard.html`: Displays visualizations and analytics results.
- `login.html`: Provides a login interface for user authentication.
- `password_change.html`: Provides an interface for changing the user's password.
- `password_change_done.html`: Displays a confirmation that the user successfully changed their password.
- `register.html`: Provides an interface for users to create a new account.

### `vocab_app/ai_generator.py`
This file contains a function that generates a daily vocabulary word using OpenAI.

### `vocab_app/forms.py`
This file contains custom forms for user creation, login and password changes.

### `vocab_app/models.py`
This conatins models for Word and UserProgress.

### `vocab_app/views.py`
Contains related functions for this web application.

### `vocab_app/urls.py`
Contains related URLs associated with the views file.

## How to Run This Application
### Prerequisites
- Python 3.12
- pip (Python package installer)

### Setup
1. Set up a virtual environment `python -m venv venv`
2. Install dependencies  `pip install -r requirements.txt`
3. Activate virtual environment
    - On macOS/Linux: source venv/bin/activate
    - On Windows: venv\Scripts\activate
3. Apply migrations `python manage.py migrate`
4. Create .env file
    - Add OPENAI_API_KEY=your_openai_api_key_here to the file.
6. Generate a daily vocabulary (Optinal) `python manage.py generate_daily_word`
7. Populate pre-set vocabulary data `python manage.py populate_words`
8. Run the application  `python manage.py runserver`

## Note
You can create an OpenAI API key by visiting https://platform.openai.com/api-keys