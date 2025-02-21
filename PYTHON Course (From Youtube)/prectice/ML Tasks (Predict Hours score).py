from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([[53],[56],[59],[62],[65]])

model = LinearRegression()

model.fit(X,Y)

predicted_score = model.predict([[6]])
print("Predicted Score for 6 hours of study:", predicted_score[0])
