mport pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics
from sklearn.svm import SVC
#from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor

# read the datasets 
df1 = pd.read_csv("/Users/anishjain/Downloads/calories.csv") 
df2 = pd.read_csv("/Users/anishjain/Downloads/exercise.csv") 


# print the datasets  
# concatenate two csv files
print(df1.head()) 
print(df2.head()) 
concat_data = pd.concat([df1, df2], ignore_index=True) 
#print(concat_data) 

merge_data = pd.merge(df1, df2, how='outer') 
print(merge_data) 
print(merge_data.head())
print(merge_data.shape)
print(merge_data.info())
print(merge_data.describe())

sb.scatterplot(x="Height",y="Weight",data=merge_data)
plt.show()


features = ['Age', 'Height', 'Weight', 'Duration']

plt.subplots(figsize=(15, 10)) # figure size
# ploting a plot of different features with calories 

#
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1)
    x = merge_data.sample(1000) # This helps in reducing the dataset size for quicker rendering, particularly when the dataset is large.
    sb.scatterplot(x=col, y='Calories', data=x)
plt.tight_layout() # Adjusts the subplot spacing to ensure there is no overlap between the subplots.
plt.show()


# replacing male and female values with 0,1
merge_data.replace({'male': 0, 'female': 1},
           inplace=True)
print(merge_data.head())

features = merge_data.select_dtypes(include='float').columns # select all columns in data  that have data types of float 

plt.subplots(figsize=(15, 10)) # figure size


for i, col in enumerate(features):
    plt.subplot(2, 3, i + 1)
    sb.distplot(merge_data[col])   
plt.tight_layout()
plt.show()


# Corresponding correlation matrix 

plt.figure(figsize=(8, 8))
sb.heatmap(merge_data.corr() > 0.9,
           annot=True,
           cbar=False)
plt.show()

# remove weight and duration 
to_remove = ['Weight', 'Duration']
merge_data.drop(to_remove, axis=1, inplace=True)
print(merge_data)

# MOdel training 
features = merge_data.drop(['User_ID', 'Calories'], axis=1)
target = merge_data['Calories'].values
X_train, X_val, Y_train, Y_val = train_test_split(features, target, test_size =0.1, random_state=22)
print(X_train.shape,X_val.shape)


# Normalizing the features for stable and fast training.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)


#
from sklearn.metrics import mean_absolute_error as mae
models = [LinearRegression(),
          Lasso(), RandomForestRegressor(), Ridge()]

for i in range(4):
    models[i].fit(X_train, Y_train)

    print(f'{models[i]} : ')

    train_preds = models[i].predict(X_train)
    print('Training Error : ', mae(Y_train, train_preds))

    val_preds = models[i].predict(X_val)
    print('Validation Error : ', mae(Y_val, val_preds))
    print()


for model in models:
    model.fit(X_train, Y_train)
    train_preds = model.predict(X_train)
    val_preds = model.predict(X_val)
print(train_preds)
print(val_preds)


# to predict calories 
new_data = pd.DataFrame({
    'Age': [25],
    'Height': [170],
    'Weight': [65],
    'Duration': [30],
    'Gender': [0]
})
for model in models:
    prediction = model.predict(new_data)
    print(f'Predicted Calories Burned with {model.__class__.__name__}: {prediction[0]}')mport pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics
from sklearn.svm import SVC
#from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor

# read the datasets 
df1 = pd.read_csv("/Users/anishjain/Downloads/calories.csv") 
df2 = pd.read_csv("/Users/anishjain/Downloads/exercise.csv") 


# print the datasets  
# concatenate two csv files
print(df1.head()) 
print(df2.head()) 
concat_data = pd.concat([df1, df2], ignore_index=True) 
#print(concat_data) 

merge_data = pd.merge(df1, df2, how='outer') 
print(merge_data) 
print(merge_data.head())
print(merge_data.shape)
print(merge_data.info())
print(merge_data.describe())

sb.scatterplot(x="Height",y="Weight",data=merge_data)
plt.show()


features = ['Age', 'Height', 'Weight', 'Duration']

plt.subplots(figsize=(15, 10)) # figure size
# ploting a plot of different features with calories 

#
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1)
    x = merge_data.sample(1000) # This helps in reducing the dataset size for quicker rendering, particularly when the dataset is large.
    sb.scatterplot(x=col, y='Calories', data=x)
plt.tight_layout() # Adjusts the subplot spacing to ensure there is no overlap between the subplots.
plt.show()


# replacing male and female values with 0,1
merge_data.replace({'male': 0, 'female': 1},
           inplace=True)
print(merge_data.head())

features = merge_data.select_dtypes(include='float').columns # select all columns in data  that have data types of float 

plt.subplots(figsize=(15, 10)) # figure size


for i, col in enumerate(features):
    plt.subplot(2, 3, i + 1)
    sb.distplot(merge_data[col])   
plt.tight_layout()
plt.show()


# Corresponding correlation matrix 

plt.figure(figsize=(8, 8))
sb.heatmap(merge_data.corr() > 0.9,
           annot=True,
           cbar=False)
plt.show()

# remove weight and duration 
to_remove = ['Weight', 'Duration']
merge_data.drop(to_remove, axis=1, inplace=True)
print(merge_data)

# MOdel training 
features = merge_data.drop(['User_ID', 'Calories'], axis=1)
target = merge_data['Calories'].values
X_train, X_val, Y_train, Y_val = train_test_split(features, target, test_size =0.1, random_state=22)
print(X_train.shape,X_val.shape)


# Normalizing the features for stable and fast training.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)


#
from sklearn.metrics import mean_absolute_error as mae
models = [LinearRegression(),
          Lasso(), RandomForestRegressor(), Ridge()]

for i in range(4):
    models[i].fit(X_train, Y_train)

    print(f'{models[i]} : ')

    train_preds = models[i].predict(X_train)
    print('Training Error : ', mae(Y_train, train_preds))

    val_preds = models[i].predict(X_val)
    print('Validation Error : ', mae(Y_val, val_preds))
    print()


for model in models:
    model.fit(X_train, Y_train)
    train_preds = model.predict(X_train)
    val_preds = model.predict(X_val)
print(train_preds)
print(val_preds)


# to predict calories 
new_data = pd.DataFrame({
    'Age': [25],
    'Height': [170],
    'Weight': [65],
    'Duration': [30],
    'Gender': [0]
})
for model in models:
    prediction = model.predict(new_data)
    print(f'Predicted Calories Burned with {model.__class__.__name__}: {prediction[0]}')
