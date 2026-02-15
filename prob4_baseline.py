# Sports vs Politics Baseline Classifier
# Roll No: B22CS067

sports_keywords = {
    "match","goal","team","cricket","football","player",
    "score","tournament","coach","stadium","runs"
}

politics_keywords = {
    "election","government","minister","parliament",
    "law","policy","president","vote","party","bill"
}

def classify(sentence):
    words = sentence.lower().split()

    sports_score = sum(1 for w in words if w in sports_keywords)
    politics_score = sum(1 for w in words if w in politics_keywords)

    if sports_score > politics_score:
        return "SPORTS"
    elif politics_score > politics_score:
        return "POLITICS"
    else:
        return "UNCERTAIN"

print("Sports vs Politics classifier ready")

while True:
    s = input("Enter sentence (or exit): ")
    if s.lower() == "exit":
        break
    print("Prediction:", classify(s))
