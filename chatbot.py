import random
import re
import time
import sys
import string
import difflib


class TamizhanBot:
    # Predefined exit commands and fallback phrases
    negative_responses = ("no", "nope", "nah", "not now", "never")
    exit_commands = ("exit", "quit", "bye", "goodbye", "pause", "later")

    # Random prompts to initiate conversation
    random_questions = (
        "How can I help you today?",
        "Ask me something about Tamizhan Skills.",
        "What do you want to know?",
        "Type a question to continue...",
        "I'm listening... go ahead!"
    )

    def __init__(self):
        self.intents = {
            'courses_info_intent': r'.*\bcourses?\b.*',
            'instructor_info_intent': r'.*\binstructor\b.*',
            'contact_info_intent': r'.*\b(contact|email|reach|connect)\b.*',
            'why_learn_intent': r'.*\bwhy\b.*learn.*',
            'internship_info_intent': r'.*\b(internship|intern|training)\b.*',
            'fees_info_intent': r'.*\b(fees?|cost|price)\b.*',
            'placement_info_intent': r'.*\b(placement|job|career)\b.*',
            'duration_info_intent': r'.*\b(duration|how long|length|time period)\b.*',
            'help_intent': r'\bhelp\b',
            'greeting_intent': r'\b(hi|hello|hey)\b',
            'thanks_intent': r'\b(thanks|thank you|ty)\b'
        }

        self.intent_keywords = {
            'courses_info_intent': ['course', 'courses', 'training', 'learning'],
            'instructor_info_intent': ['instructor', 'trainer', 'mentor'],
            'contact_info_intent': ['contact', 'email', 'connect', 'reach'],
            'why_learn_intent': ['why learn', 'reason', 'benefit', 'purpose'],
            'internship_info_intent': ['internship', 'projects', 'certificate'],
            'fees_info_intent': ['fees', 'cost', 'price', 'charge'],
            'placement_info_intent': ['placement', 'job', 'career', 'guarantee'],
            'duration_info_intent': ['duration', 'length', 'weeks', 'time'],
        }

    # Clean
    def clean_input(self, text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        text = ' '.join(text.split())
        return text
        
    # Bot Typing
    def type_reply(self, message, delay=1.3):
        print("🤖 TamizhanBot is typing...", end="\r")
        time.sleep(delay)
        print(" " * 50, end="\r")
        print("🤖", message)
        
    # Greet   
    def greet(self):
        full_name = input("👋 What's your name?\n").strip()
        if any(kw in full_name.lower() for kw in ["my name is", "i am", "i'm", "this is", "myself"]):
            tokens = full_name.split()
            self.name = " ".join(tokens[-2:]).title() if len(tokens) > 1 else tokens[-1].capitalize()
        else:
            self.name = full_name.title()

        print(f"🧠 Great to meet you, {self.name}!")

        response = input("💬 I'm TamizhanBot! Would you like to know about Tamizhan Skills? (yes/no)\n").lower().strip()
        response = self.clean_input(response)
        if response.lower() in self.negative_responses:
            print("Alright, no problem! Have a great day ahead! 😊")
            return
        elif response.lower() in ("yes", "sure", "okay", "ok", "yeah"):
            print("📚 Awesome! Here's what we offer : ")
            print(self.courses_info_intent())
            print("\n💡 You can ask me about courses, instructors, contact info, or why you should join.")
        self.chat()

    # Chat    
    def chat(self):
        print("👩‍💻 You can type your question below. (Type 'exit' to quit)\n")
        print("💡 Need suggestions? Type 'help' anytime!\n")
        while True:
            user_input = input(random.choice(self.random_questions) + "\n").strip()
            cleaned_input = self.clean_input(user_input)
            if self.make_exit(cleaned_input):
                print("👋 Goodbye! Hope to chat with you again. 🚀")
                break
            self.type_reply(self.match_reply(cleaned_input))

    # Exit
    def make_exit(self, reply):
        return any(cmd in reply for cmd in self.exit_commands)

    # Match Reply
    def match_reply(self, reply):
        if re.search(r'\b(thanks|thank you|bye|goodbye)\b', reply):
            self.type_reply(f"You're most welcome, {self.name}! Have a great day ahead! 👋")
            sys.exit()
        for intent in [
            'duration_info_intent',
            'courses_info_intent',
            'instructor_info_intent',
            'contact_info_intent',
            'why_learn_intent',
            'internship_info_intent',
            'fees_info_intent',
            'placement_info_intent',
            'help_intent',
            'greeting_intent'
        ]:
            pattern = self.intents[intent]
            if re.search(pattern, reply):
                return self.trigger_intent(intent)

        best_intent = self.fuzzy_intent_match(reply)
        if best_intent:
            return self.trigger_intent(best_intent)

        return self.no_match_intent()
    
    # Intent
    def trigger_intent(self, intent):
        if intent == 'courses_info_intent':
            return self.courses_info_intent()
        elif intent == 'instructor_info_intent':
            return self.instructor_info_intent()
        elif intent == 'contact_info_intent':
            return self.contact_info_intent()
        elif intent == 'why_learn_intent':
            return self.why_learn_intent()
        elif intent == 'internship_info_intent':
            return self.internship_info_intent()
        elif intent == 'fees_info_intent':
            return self.fees_info_intent()
        elif intent == 'placement_info_intent':
            return self.placement_info_intent()
        elif intent == 'duration_info_intent':
            return self.duration_info_intent()
        elif intent == 'help_intent':
            return self.help_intent()
        elif intent == 'greeting_intent':
            return f"I'm here to help! Just ask me something about our courses, instructors, fees, internships, or anything else. 😊"
        elif intent == 'thanks_intent':
            return f"You're most welcome, {self.name}! 🙌"
        else:
            return self.no_match_intent()
    
    # Fuzzy
    def fuzzy_intent_match(self, text):
        words = text.split()
        possible = []
        for intent, keywords in self.intent_keywords.items():
            for kw in keywords:
                match = difflib.get_close_matches(kw, words, n=1, cutoff=0.8)
                if match:
                    possible.append(intent)
                    break  # prevent duplicate matches per intent
        if possible:
            return possible[0]
        return None


    # Courses
    def courses_info_intent(self):
        responses = (
            "We offer Python, Web Development, AI/ML, and Internship-based learning programs.",
            "Our most popular courses include Python, Data Science, and Tkinter GUI apps!",
            "Tamizhan Skills offers practical learning with hands-on projects. 😊"
        )
        return random.choice(responses)

    # Instructor
    def instructor_info_intent(self):
        responses = (
            "Our instructors are industry experts with real-world project experience.",
            "Every instructor at Tamizhan Skills ensures you get placement-level skills. 💪"
        )
        return random.choice(responses)

    # Contact
    def contact_info_intent(self):
        responses = (
            "You can contact us via email at contact@tamizhanskills.com.",
            "Visit https://tamizhanskills.com for full details."
        )
        return random.choice(responses)

    # Why to learn
    def why_learn_intent(self):
        responses = (
            "Learning new skills makes you future-ready and confident! 🚀",
            "Because your future deserves more than just college theory."
        )
        return random.choice(responses)
    
    # Internship
    def internship_info_intent(self):
        responses = (
            "Yes! We provide internship support with real projects once you complete the course. 📚",
            "After course completion, we help you apply for internships in the related field."
        )
        return random.choice(responses)

    # Fees
    def fees_info_intent(self):
        responses = (
            "Our courses are affordable, starting from ₹499. Check the website for current offers!",
            "We believe in budget-friendly learning — fees vary by course, starting at ₹499."
        )
        return random.choice(responses)

    # Placement
    def placement_info_intent(self):
        responses = (
            "We offer guidance, mock interviews, and career support for placements. 🎯",
            "Absolutely! We train you with skills aligned with job roles. 💼"
        )
        return random.choice(responses)

    # Duration
    def duration_info_intent(self):
        responses = (
            "Most courses are 4 to 8 weeks long, with flexible timing. 📅",
            "It depends on the course — some are 1 month, others 2 months max."
        )
        return random.choice(responses)

    # Help    
    def help_intent(self):
        return (
            "Here are some things you can ask me:\n"
            "👉 What courses do you offer?\n"
            "👉 How can I contact you?\n"
            "👉 What are the fees?\n"
            "👉 Do you offer internships?\n"
            "👉 Tell me about instructors.\n"
            "👉 How long are the courses?\n"
            "👉 What about placement support?\n"
            "👉 Type 'exit' to quit anytime."
        )

    # No-match
    def no_match_intent(self):
        responses = (
            f"Hmm... I'm not sure I understood that, {self.name}. Try asking about courses, instructors, etc.",
            f"That's interesting, {self.name}. Could you try rephrasing your question?",
            f"Sorry {self.name}, I didn't get that. Type 'help' to see what I can do!"
        )
        return random.choice(responses)

# ---- Run the bot ----
if __name__ == "__main__":
    bot = TamizhanBot()
    bot.greet()