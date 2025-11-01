from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as np
import pickle


###Import data and preprocess
data = r"D:\Documents\University\ThirdYear\First Semester\Applied Analytical Models\Labs\FlaskApp\dataset\Heart_disease.csv"
df = pd.read_csv(data)

#Apply Label Encoding
le = LabelEncoder()
df['target'] = le.fit_transform(df['target'])

features = ['Age', 'blood pressure', 'cholesterol', 'maximum heart rate']
X = df[features]
y = df['target']

###Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

###Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

#evaluate
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy*100:.2f}%")

#Save Model as PKL file
with open(r"D:\Documents\University\ThirdYear\First Semester\Applied Analytical Models\Labs\FlaskApp\models\model.pkl", 'wb') as f:
    pickle.dump(model, f)

