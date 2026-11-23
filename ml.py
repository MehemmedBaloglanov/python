from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

sentences = [
    "salam", "salam necəsən", "sabahın xeyir", "axşamın xeyir",
    "özümü pis hiss edirəm", "çox kefsizəm", "kədərliyəm", "bu gün pis gündür",
    "acmışam", "yemək istəyirəm", "qarnım acıb", "nəsə yemək lazımdır",
    "yaşın neçədir", "neçə yaşın var", "sən kimsən", "sən botsan",
]

labels = [
    "salam", "salam", "salam", "salam",
    "kədər", "kədər", "kədər", "kədər",
    "aclıq", "aclıq", "aclıq", "aclıq",
    "bot", "bot", "bot", "bot",
]

vertorizer = CountVectorizer()
X = vertorizer.fit_transform(sentences)

model = MultinomialNB()
model.fit(X,labels)

tests = [
    "salam dostum",
    "bu gün çox kefsizəm",
    "indi yemək istəyirəm",
    "sənin yaşın neçədir",
    "bacım gəldi",
    "hava necədir",
]

for t in tests:
    X_test = vertorizer.transform([t])
    result = model.predict(X_test)[0]
    confidence = model.predict_proba(X_test).max()
    print(t,"->",result,"|əminlik:",round(confidence*100),"%")