from django.shortcuts import render
from django.http import JsonResponse
from langchain_google_genai import GoogleGenerativeAI

# API key
api_key = "AIzaSyAxnI674rpzjhAQ9lsBbtmpnDCX4eiQ7Oc"

# Chatbot class, tumhara diya hua logic yahin hai
class Chatbot:
    def __init__(self, api_key):
        self.llm = GoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=api_key
        )

    def ask(self, prompt):
        try:
            response = self.llm.invoke(prompt)
            return response
        except Exception as e:
            return f"Error occurred: {e}"

# Ek instance banao jo baar baar use hoga
bot = Chatbot(api_key)

# Home page view jo chatbot UI render kare
def chatbot_view(request):
    return render(request, 'chatapp/index.html')

# AJAX request handle karne wali view, user input lega aur response bhejega
def ask_bot(request):
    if request.method == "POST":
        prompt = request.POST.get('prompt', '').strip()
        if not prompt:
            return JsonResponse({'error': 'Please enter a message.'})
        
        # Chatbot se jawab le lo
        response = bot.ask(prompt)
        return JsonResponse({'response': response})

    return JsonResponse({'error': 'Invalid request method.'})
