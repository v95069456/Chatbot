import json
import re
from nltk.chat.util import Chat, reflections
import random

# Read the JSON file
try:
    with open('data.json', 'r') as file:
        manual_pairs = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    manual_pairs = []

def joke():
    jokes = [
        "What is the name of the ribbon that lifts the mood?\nAtmosphere!",
        "Why doesn't the chicken chew its food?\nBecause it was forbidden to chew it!",
        "What is the real name of a skilled karateka?\nMain!",
        "Who makes waves on the beach programmer?\nHTML!",
        "What is the name of the bear who is always in a cheerful mood?\nOptimist!",
        "Why is it impossible to enter a round ship?\nBecause it sees you from the rear!",
        "What are pencils called that are afraid to fly?\nGuides!",
        "What does a bee do in the gym?\nKnows how to regret!",
        "Who buys the most language textbooks?\nLinguistics support!",
        "What letters treat teeth?\nARZODONT!",
    ]
    return random.choice(jokes)


generic_responses = [
    "Hello!",
    "Hi there!",
    "How are you?",
    "I'm good, thanks. How about you?",
    "I'm doing well too.",
    "What do you do for a living?",
    "I'm a chatbot created for demonstration purposes.",
    "That's interesting!",
    "Thank you! How can I help you today?",
    "Tell me a joke.",
    "Why did the computer go to therapy? It had too many bytes of emotional baggage!",
    "What's your favorite programming language?",
    "I don't have preferences, but I was built using Python!",
    "Tell me about artificial intelligence.",
    "Artificial intelligence (AI) is a branch of computer science that deals with creating machines capable of intelligent behavior.",
    "Do you like movies?",
    "I don't have personal preferences, but I can recommend some popular movies. What genre do you enjoy?",
    "What's your favorite book?",
    "I don't read books, but I can suggest some popular ones. Do you prefer fiction or non-fiction?",
    "How's the weather today?",
    "I'm sorry, I don't have real-time information. You can check a weather website or app for the current conditions.",
    "What's the meaning of life?",
    "The meaning of life is a philosophical question. Different people have different perspectives on it.",
    "Can you help me with my homework?",
    "Of course! What subject are you working on, and what specific help do you need?",
    "Tell me something interesting.",
    "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "How do I stay motivated?",
    "Staying motivated can be challenging. Setting small, achievable goals and celebrating your progress can help keep you motivated.",
    "What's the best programming joke you know?",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Are you familiar with the concept of love?",
    "Love is a complex and profound emotion experienced by humans. It can take many forms, including romantic, platonic, and familial love.",
    "What's your favorite kind of music?",
    "I don't have personal preferences, but I can recommend music based on your taste. What genre are you into?"
    "I'm here to assist you. What can I help you with?",
    "That's interesting! Tell me more about it.",
    "Feel free to share your thoughts. I'm here to listen.",
    "I'm ready to help. What's on your mind?",
    "Interesting! How can I be of service?",
    "Let's dive into that topic. What specific information are you looking for?",
    "I'm here for you. What do you need assistance with?",
    "That's a great point! How can I support you further?",
    "Your input is valuable. Please share more details.",
    "I'm here to make your experience better. How can I assist you today?",
    "Thanks for reaching out. What can I do for you?",
    "Let's explore that together. What else can you tell me?",
    "I appreciate your engagement. What else would you like to discuss?",
    "Your questions are important. Ask away, and I'll do my best to help.",
    "I'm all ears. Feel free to share your thoughts or questions.",
]

def generate_pairs(num_pairs):
    pairs = []
    for _ in range(num_pairs):
        pattern = r"(.*)"
        response = [random.choice(generic_responses) for _ in range(random.randint(1, 3))]
        pairs.append([pattern, response])
    return pairs

# Generate random pairs
random_pairs = generate_pairs(0)
all_pairs = manual_pairs + random_pairs
chatbot = Chat(all_pairs, reflections)

def start_chat():
    print('ChatBotAI: ' + joke())
    while True:
        user_input = input("You--> ").lower()
        
        if user_input == 'quit':
            print("Goodbye!")
            break

        # Ensure that manual_pairs is not empty
        if manual_pairs:
            matched_pair = next((pair for pair in manual_pairs if re.match(pair[0], user_input)), None)
            if matched_pair:
                response = chatbot.respond(user_input)
                print("ChatBotAI-->", response)
            else:
                print('ChatBotAI--> I do not know the answer. Can you teach me?')
                ans = input('Type answer here --> ')
                manual_pairs.append([user_input, [ans]])
                with open('data.json', 'w') as file:
                    json.dump(manual_pairs, file, indent=2)
        else:
            print("ChatBotAI--> I'm here to learn! Please provide some input.")

if __name__ == "__main__":
    start_chat()
