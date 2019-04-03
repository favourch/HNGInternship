#This is the code for the first ML task from HNG Internship 5.0
#Contained here is a Naive Bayes classifier 

#creating a small dataset; assigning feature and label values
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']

temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

#Import LabelEncoder library 
from sklearn import preprocessing

#creating LabelEncoder object 
le = preprocessing.LabelEncoder()

#Converting string labels into numbers. 
weather_encoded = le.fit_transform(weather)

print(weather_encoded)

temp_encoded = le.fit_transform(temp) #Converting temperature string labels into numbers
label = le.fit_transform(play) ##Converting Label strings into numbers
print("Temp:",temp_encoded)
print("Play:",label) 

#Combinig weather and temp into single listof tuples

features = list(zip(weather_encoded,temp_encoded))
print(features)

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features,label)

#Predict Output
predicted = model.predict([[0,2]]) # 0:Overcast, 2:Mild
print("Predicted Value:", predicted) 