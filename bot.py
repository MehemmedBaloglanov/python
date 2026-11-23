import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
print("Salam! Mən Məhəmməd")
name = input("Adın nədir?\n")
print("Tanış olduğuma şad oldum,",name)
age = input("Neçə yaşın var?\n")
while not age.isdigit():
    age = input("Zəhmət olmasa rəqəm yaz:\n")
age = int(age)
print("Deməli sən", age , "yaşındasan")
print("10 ildən sonra", age + 10, "yaşında olacaqsan")
print("Necəsən? (Çıxmaq üçün 'sağol' yaz)")
with open("answers.json","r",encoding = "utf-8") as file:
    answer = json.load(file)

with open("training.json","r",encoding = "utf-8") as file:
    training = json.load(file)

sentences = []
labels = []

for intent in training:
    for sentence in training[intent]:
        sentences.append(sentence)
        labels.append(intent)
intent_replies = {
    "salam": "Salam! Nə var nə yox?",
    "kədər": "Bunu eşitdiyimə təəssüf edirəm. Nə olub?",
    "aclıq": "Get bir şey ye 🙂",
    "bot": "Mən botam, yaşım yoxdur 🙂",
}

vertorizer = CountVectorizer()
X = vertorizer.fit_transform(sentences)
model = MultinomialNB()
model.fit(X,labels)

def get_reply(message):
    X_test = vertorizer.transform([message])
    intent = model.predict(X_test)[0]
    confidence = model.predict_proba(X_test).max()

    if confidence >= 0.4:
        return intent_replies[intent]

    for word in answer:
        if word in message:
            return answer[word]
    return "Başa düşdüm."
    
while True:
    message = input("Sən: ").lower()
    if "sağol" in message:
        print("Görüşənədək",name)
        break

    reply = get_reply(message)
    
    if reply == "Başa düşdüm." :
        new_reply = input("Bunu bilmirəm. Necə cavab verim?\n")
        answer[message] = new_reply
        with open("answers.json","w",encoding="utf-8") as file:
            json.dump(answer,file,ensure_ascii=False,indent=4)
        print("Təşəkkürlər, öyrəndim!")
    else:
        print(reply)