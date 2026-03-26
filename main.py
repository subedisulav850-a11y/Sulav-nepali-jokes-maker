from fastapi import FastAPI
from random import choice, randint

app = FastAPI(title="Nepali Unlimited Jokes API 😂")

templates = [
    "{name}: मैले {thing} खोजेको छु।\n{friend}: त्यो त कहिले पाइन्छ?",
    "टीचर: {number} + {number} कति?\n{student}: {wrong_answer} 😎",
    "{name} आज {place} गए। तर {funny_event} भयो!",
    "बाबु: किन {action}?\nछोरा: किनकि {funny_reason}!",
    "साथी: किन हाँस्दैछौ?\n{name}: {funny_reason}!"
]

names = ["सुरेश", "गोपाल", "रीता", "सुनिता", "अनिल", "सिता", "राजु", "माया"]
things = ["मोबाइल", "पेट्रोल", "किताब", "रोटी", "चार्जर"]
places = ["स्कुल", "बजार", "पार्क", "घर", "कलेज"]
funny_events = ["मोबाइल गुम्यो", "पानी छप्कियो", "कुकुरले खायो", "गाडी बिग्रियो"]
actions = ["पढ्न जान्छौ", "फोन चलाउँछौ", "खाना खान्छौ"]
funny_reasons = ["मज्जा त आउँछ", "टिकटक रोक्न सक्दिन", "घामले पग्लायो"]
students = ["सुरेश", "रीता", "अनिल", "सुनिता"]

@app.get("/joke")
def get_joke():
    template = choice(templates)
    joke = template.format(
        name=choice(names),
        thing=choice(things),
        place=choice(places),
        funny_event=choice(funny_events),
        action=choice(actions),
        funny_reason=choice(funny_reasons),
        student=choice(students),
        number=randint(1, 20),
        wrong_answer=randint(21, 50),
        friend=choice(names)
    )
    return {"joke": joke}

@app.get("/jokes")
def get_jokes(count: int = 5):
    return {"jokes": [get_joke()["joke"] for _ in range(count)]}