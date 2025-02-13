#-------------------------------------------------------------------------
# AUTHOR: Eric Wong
# FILENAME: decision_tree.py
# SPECIFICATION: A program that creates a decision tree based on contact_lens.csv.
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('C:\\Users\\Munchy\\Downloads\\contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
for row in db:
  temp = [] #temporary value to hold values
  for i, curVal in enumerate(row):
    #Age: Young = 1, Prepresbyopic = 2, Presbyopic = 3
    if i==0:
      if curVal == 'Young':
        temp.append(1)
      elif curVal == 'Prepresbyopic':
        temp.append(2)
      else:
        temp.append(3)

    #Spectacle Prescription: Myope = 1, Hypermetrope = 2
    elif i==1:
      if curVal == 'Myope':
        temp.append(1)
      else:
        temp.append(2)

    #Astigmatism: Yes = 1, No = 2
    elif i==2:
      if curVal in 'Yes':
        temp.append(1)
      else:
        temp.append(2)
    #Tear Production Rate: Reduced = 1, Normal = 2
    else:
      if curVal == 'Reduced':
        temp.append(1)
      else:
        temp.append(2)
      break
  X.append(temp)
print(X)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
temp = []
for row in db:
  #Recommended Lenses: Yes = 1, No = 2
  if row[4] == 'Yes':
    temp.append(1)
  else:
    temp.append(2)
Y = temp
print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()