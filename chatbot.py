# chatbot.py

# Define the chatbot's responses and keywords
responses = {
    "admission": {
        "keywords": ["admission", "enroll", "apply"],
        "response": "For admission details, please visit MRIIRS.com admissions page and fill the admission form."
    },
    "courses": {
        "keywords": ["course", "program", "degree", "subjects"],
        "response": "We offer a variety of courses in Engineering, Management, and Arts. Which course are you interested in?"
    },
    "engineering": {
        "keywords": ["computer science", "engineering"],
        "response": "There are two types of Computer Science Engineering: CORE & SPECIALIZATION. Which one are you interested in?"
    },
    "specialization": {
        "keywords": ["specialization", "information", "cse aiml", "CSE AIML"],
        "response": "Sure, What would you like to know about the specialization course?"
    },
    "core": {
        "keywords": ["core", "information"],
        "response": "Sure, What would you like to know about the core course?"
    },
    "faculty": {
        "keywords": ["qualifications", "faculties", "faculty", "teachers", "professors"],
        "response": "Our faculty is highly qualified. They have PhDs in their respective fields and are always ready to help students."
    },
    "seats": {
        "keywords": ["vacancies", "seats"],
        "response": "There are around 50-100 seats left for the specialization course."
    },
    "fees": {
        "keywords": ["fee", "fees", "cost", "tuition"],
        "response": "The fee structure varies by program. For CSE CORE, it is around 10 lakhs, and for CSE SPL, it is around 12 lakhs."
    },
    "placement": {
        "keywords": ["placement", "job", "career", "internship"],
        "response": "Our placement cell provides opportunities with top companies like Google, Microsoft, Ericsson, Apple, Meta, Amazon, etc."
    },
    "contact": {
        "keywords": ["contact", "address", "phone", "email"],
        "response": "For contact details, visit our website MRIIRS.com or email us at info@university.edu."
    }
}

# Function to find the response based on keywords
def get_response(user_question):
    user_question = user_question.lower()
    for topic, info in responses.items():
        if any(keyword in user_question for keyword in info["keywords"]):
            return info["response"]
    return "I'm sorry, I don't have an answer for that question. Please try asking something else."
