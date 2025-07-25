#pip install scikit-learn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import random

data_iris = load_iris()

label_target = data_iris.target_names
print()
print("Sample Data from Iris Dataset")
print("*"*30)

for i in range(10):
 rn = random.randint(0,120)
 print(data_iris.data[rn],"===>",label_target[data_iris.target[rn]])

X = data_iris.data
y = data_iris.target

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size = 0.3, random_state=1)
print("The Training dataset length: ",len(X_train))
print("The Testing dataset length: ",len(X_test))
nn = int(input("Enter number of neighbors :"))
knn = KNeighborsClassifier(nn)
knn.fit(X_train, y_train)
print("The Score is :", knn.score(X_test, y_test))


test_data = input("Enter Test Data :").split(",")
test_data = [float(x) for x in test_data]

v = knn.predict([test_data])
print("\nPredicted output is :", label_target[v[0]])

