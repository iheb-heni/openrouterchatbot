# Django Chatbot with OpenRouter

This is a basic Django application that integrates a chatbot using the OpenRouter API. It demonstrates how easy it is to create and run a chatbot locally using Django and share it across devices on the same Wi-Fi network.

## 🚀 Features

- Simple Django setup
- Integration with OpenRouter API
- Accessible from other devices on the same Wi-Fi network
- Basic chatbot interface via HTML
- Easy to customize and extend

## 🧠 Requirements

- Python 3.8+
- Django 4+
- `requests` (for calling OpenRouter)

## 🔧 Installation

1. **Clone the repository:**

git clone https://github.com/your-username/django-openrouter-chatbot.git
cd django-openrouter-chatbot
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
Install the dependencies:

pip install -r requirements.txt
Run the Django server:

bash
Copy
Edit
python manage.py runserver 0.0.0.0:8000
Access the chatbot:

From your computer:
http://127.0.0.1:8000/

From another device on the same Wi-Fi:
http://your-local-ip:8000/ (e.g., http://192.168.1.12:8000/)

📌 Notes
This is a demo app using OpenRouter API.

For production, make sure to hide your API key and restrict access.

OpenRouter has limitations (rate limits, available models, etc.) in its free version.

🤖 Powered by
Django

OpenRouter

📎 License
MIT License

---

## 🔗 2. Commande pour cloner le projet


