import numpy as np 
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier #imports the dtree classifier
from sklearn.metrics import accuracy_score #using accuracy to rate the model
from sklearn import tree

df=pd.read_csv('data/training-2016-10-01-2016-12-31.csv') #Reads the dataset... Used the same one as John

# #Data stuff...commented because didn't find it useful...
# print('Dataset Shape::',df.shape) #prints the shape of the dataset...
# print('Dataset Length::', len(df)) #prints the length of the dataset...

# print('Dataset::' , df.head()) #prints the column heads...

# print(df.dtypes) #Prints the type of data...

#may have to redo the part below...not the prettiest but it works so +1 lol
data = df.dropna(subset=['post_pos','offset','post','speed','horse_win','horse_wps','horse_roi','driver_win','driver_wps','driver_roi','trainer_win','trainer_roi','min_races','previous_break','days_since','same_track','same_driver','last_race_res','last_race_wps','last_three_races','purse','finish_pos'])
data['finish_pos'] = data['finish_pos'].map(lambda x: 1 if x >= 3 else 0) #used the same function as John...

X = data[['post_pos','offset','post','speed','horse_win','horse_wps','horse_roi','driver_win','driver_wps','driver_roi','trainer_win','trainer_roi','min_races','previous_break','days_since','same_track','same_driver','last_race_res','last_race_wps','last_three_races','purse']].values #X is everything else besides the first two columns and the last one, removed the -1
Y= data[['finish_pos']].values#Y is the finishing Postion... 

X_train,X_test,y_train,y_test=train_test_split(X,Y, test_size=0.30,train_size=0.70, random_state=1) #split 30:70...

clf_gini=DecisionTreeClassifier(criterion="gini", random_state = 100, max_depth=10, min_samples_leaf=5) #dtree with criterion gini index...

clf_gini.fit(X_train, y_train)

clf_entropy=DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=3,min_samples_leaf=5)#dtree with criterion information gain...
clf_entropy.fit(X_train, y_train)

y_pred = clf_gini.predict(X_test)#predicition for the gini index...
y_pred

y_pred_en = clf_entropy.predict(X_test)#prediction for the information gain...
y_pred_en

print("Accuracy is", accuracy_score(y_test,y_pred)*100) # Prints accuracy score with criterion as gini index
print("Accuracy is", accuracy_score(y_test,y_pred_en)*100)#Prints accuracy score with criterion as information gain
