# import string

# text = "The patient has a fever and needs immediate treatment!"

# text = text.lower()

# text = text.translate(str.maketrans('','', string.punctuation))

# tokens = text.split()

# print("Processed Text:", tokens)


from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.naive_bayes import MultinomialNB
text_data = ["The patient has a fever", "It is a sunny day in the park"]
labels = ["Medical", "General"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text_data)

model = MultinomialNB()
model.fit(X, labels)

new_sentence = ["the man has a fever"]
new_X = vectorizer.transform(new_sentence)
prediction = model.predict(new_X)

print("Prediction:", prediction[0])