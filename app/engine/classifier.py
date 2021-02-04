import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data=pd.read_csv('app/engine/data/iris.data')
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train the model
model = LogisticRegression()
model.fit(x_train, y_train) #Training the model

#Test the model
predictions = model.predict(x_test)
print(classification_report(y_test, predictions) )
print(accuracy_score(y_test, predictions))

# Save the model
pickle.dump(model, open('app/engine/saved_models/iris/model.pkl','wb'))
