#Multiclass prediction using Naive Bayes

from sklearn import datasets

#Load dataset
wine = datasets.load_wine()

#print the names of the 13 features
print("Features: ", wine.feature_names)

#print the label type of wine(class_0, class_1, class_2)
print("Labels: ", wine.target_names)

Features: ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']
Labels: ['class_0' 'class_1' 'class_2']

#print data(feature)shape
print(wine.data.shape) 

#print the wine data features (top 5 records)
print(wine.data[0:5])
print(wine.target)

#Import train_test_split function 
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=109) # 70% training and 30% test

#Import Gaussian Naive Bayes Model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))