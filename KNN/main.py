import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import operator
from sklearn.metrics import accuracy_score

# Preprocessing Data
df = pd.read_csv('Diabetes.csv')

# Dummy encoding usia
df["Age"] = pd.cut(df["Age"],bins=[20,30,40,50,60,70,80,90])
df = pd.get_dummies(df)
data_y = df['Outcome']
data_x = df.drop(columns=['Outcome'], axis=1)

# Normalisasi data dengan min-max scaler
for column in data_x.columns : 
  data_x[column] = (data_x[column] - data_x[column].min()) / (data_x[column].max() - data_x[column].min())

X_train_1 = data_x.iloc[:613]
X_test_1 = data_x.iloc[614:]
Y_train_1 = data_y.iloc[:613]
Y_test_1 = data_y.iloc[614:]

X_train_2 = pd.concat([data_x.iloc[:460], data_x.iloc[642:768]])
X_test_2 = data_x.iloc[461:641]
Y_train_2 = pd.concat([data_y.iloc[:460], data_y.iloc[642:768]])
Y_test_2 = data_y.iloc[461:641]

X_train_3 = pd.concat([data_x.iloc[:306], data_x.iloc[461:768]])
X_test_3 = data_x.iloc[307:460]
Y_train_3 = pd.concat([data_y.iloc[:306], data_y.iloc[461:768]])
Y_test_3 = data_y.iloc[307:460]

X_train_4= pd.concat([data_x.iloc[:153], data_x.iloc[307:768]])
X_test_4 = data_x.iloc[152:306]
Y_train_4 = pd.concat([data_y.iloc[:153], data_y.iloc[307:768]])
Y_test_4 = data_y.iloc[152:306]

X_train_5 = data_x.iloc[154:768]
X_test_5 = data_x.iloc[153:]
Y_train_5 = data_y.iloc[154:768]
Y_test_5 = data_y.iloc[153:]

X_train_1.reset_index(drop=True)
X_train_2.reset_index(drop=True)
X_train_3.reset_index(drop=True)
X_train_4.reset_index(drop=True)
X_train_5.reset_index(drop=True)

X_test_1.reset_index(drop=True)
X_test_2.reset_index(drop=True)
X_test_3.reset_index(drop=True)
X_test_4.reset_index(drop=True)
X_test_5.reset_index(drop=True)

Y_train_1.reset_index(drop=True)
Y_train_2.reset_index(drop=True)
Y_train_3.reset_index(drop=True)
Y_train_4.reset_index(drop=True)
Y_train_5.reset_index(drop=True)

Y_test_1.reset_index(drop=True)
Y_test_2.reset_index(drop=True)
Y_test_3.reset_index(drop=True)
Y_test_4.reset_index(drop=True)
Y_test_5.reset_index(drop=True)

class KNN():
  def __init__(self, k):
    self.k = k
    self.data_x = None
    self.data_y = None
    self.predictions = []
    
  def fit(self, X, Y):
    self.data_x = X
    self.data_y = Y

  def euclidean_distance(self, data_1, data_2):
    return np.sqrt(np.sum (( data_1 - data_2 )**2 ))

  def predict(self, x_test):  
      self.predictions = []
      for i in range(len(x_test)):            
          dist = np.array([self.euclidean_distance(x_test[i], x_t) for x_t in self.data_x])
      
          dist_sorted = dist.argsort()[:self.k]
          neighbor = {}
          for id in dist_sorted:
              if self.data_y[id] in neighbor:
                  neighbor[self.data_y[id]] += 1
              else:
                  neighbor[self.data_y[id]] = 1
          
          sorted_neighbor = sorted(neighbor.items(), key=operator.itemgetter(1), reverse=True)
          self.predictions.append(sorted_neighbor[0][0])
      return self.predictions

k = 3
best_k = {}
while k<=20:
  k_nearest_neighbor = KNN(k) 
  k_nearest_neighbor.fit(X_train_1.to_numpy(), Y_train_1.to_numpy())
  prediction = k_nearest_neighbor.predict(X_test_1.to_numpy())
  akurasi_1 = accuracy_score(Y_test_1, prediction)
  # print('Accuracy pada k={}:'.format(k), akurasi_1)

  k_nearest_neighbor.fit(X_train_2.to_numpy(), Y_train_2.to_numpy())
  prediction = k_nearest_neighbor.predict(X_test_2.to_numpy())
  akurasi_2 = accuracy_score(Y_test_2, prediction)
  # print('Fold 2 Accuracy:', akurasi_2)


  k_nearest_neighbor.fit(X_train_3.to_numpy(), Y_train_3.to_numpy())
  prediction = k_nearest_neighbor.predict(X_test_3.to_numpy())
  akurasi_3 = accuracy_score(Y_test_3, prediction)
  # print('Fold 3 Accuracy:', akurasi_3)


  k_nearest_neighbor.fit(X_train_4.to_numpy(), Y_train_4.to_numpy())
  prediction = k_nearest_neighbor.predict(X_test_4.to_numpy())
  akurasi_4 = accuracy_score(Y_test_4, prediction)
  # print('Fold 4 Accuracy:', akurasi_4)


  k_nearest_neighbor.fit(X_train_5.to_numpy(), Y_train_5.to_numpy())
  prediction = k_nearest_neighbor.predict(X_test_5.to_numpy())
  akurasi_5 = accuracy_score(Y_test_5, prediction)
  # print('Fold 5 Accuracy:', akurasi_5,"\n")
    
  average = (akurasi_1+akurasi_2+akurasi_3+akurasi_4+akurasi_5)/5
  best_k[k] = (average)
  
  # print('Accuracy pada k={}:'.format(k), average)
  print('Processing...')
  k+=2

print(best_k)