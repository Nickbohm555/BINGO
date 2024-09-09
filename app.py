from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dictionary of people and their phrases
people_phrases = {
    "Grandpa": [
        "Trump", "Liz Cheney", "Biden", "Retells an old joke", 
        "Talks with mouthful", "Brings up new park story", 
        "Interrupts", "Demands coffee and beer", 
        "Randomly brings up gay stuff", "Shows his phone to others"
    ],
    "Tamara": [
        "Lays down", "First in the water", "Talks about manifesting", 
        "Talks about effect of wine", "Makes an obvious face", 
        "Gives a backhanded compliment", "Gets people to tell secrets", 
        "Very excited"
    ],
    "Utku": [
        "Talking about motorcycles", "Drinking timeline", "Pronouns", 
        "Goes anti-woke", "Talks about a better/easy way to do something"
    ],
    "Nicholas": [
        "Physically bothers people", "Talks past travel", 
        "Says have you ever noticed", "Imitates Trump or someone", 
        "Rubs Jazzy", "Plans mischievous stuff"
    ],
    "Alara": [
        "Pouring heavy alcohol", "Woke perspective", "Corrects Arman", 
        "Rolls her eyes", "Sits on someone's lap", 
        "That's not what I'm saying", "Says she's getting tired"
    ],
    "Michael": [
        "Frat stories", "Plans mischievous", "Gets annoyed at Mami", 
        "Does a family impression"
    ],
    "Arman": [
        "Takes off shirt unnecessarily", "Puts on music", 
        "First to leave table", "Gives or receives massage", 
        "Can't follow rules", "Plans something mischievous"
    ],
    "David": [
        "Pushes belly button in", "Is irritated", 
        "Touch to massage", "Starts new project without finishing"
    ], 
    "Mami": [
        "Defends Other", "Vegetables", 
        "Davids weight", "Last to sit down", "Speaks Japanese when no one understands"
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_people = request.form.getlist("people")
        if not selected_people:
            return render_template("index.html", people=people_phrases.keys(), error="Please select at least one person.")
        
        bingo_phrases = generate_bingo_card(selected_people)
        return render_template("bingo.html", bingo_phrases=bingo_phrases)
    
    return render_template("index.html", people=people_phrases.keys())

def generate_bingo_card(selected_people):
    bingo_phrases = []
    all_phrases = []

    # Collect phrases from selected people
    for person in selected_people:
        phrases = people_phrases[person]
        all_phrases.extend([f"{person}|{phrase}" for phrase in phrases])

    # Ensure there are at least 24 phrases
    if len(all_phrases) < 24:
        # If not enough unique phrases, duplicate some phrases
        while len(all_phrases) < 24:
            all_phrases.extend(all_phrases[:24 - len(all_phrases)])
    
    # Shuffle and select the first 24 phrases
    random.shuffle(all_phrases)
    bingo_phrases = all_phrases[:24]

    # Insert "BINGO" in the center
    bingo_phrases.insert(12, "Center|BINGO")
    
    return bingo_phrases

if __name__ == "__main__":
    app.run(debug=True)
