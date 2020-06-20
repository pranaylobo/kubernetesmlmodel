import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
menu_file_path = "menu.csv"
menu_data = pd.read_csv(menu_file_path)
menu_data.columns
y = menu_data.Calories
 
menu_features = ['Total Fat','Total Fat (% Daily Value)','Saturated Fat','Saturated Fat (% Daily Value)', 'Trans Fat', 'Cholesterol',
       'Cholesterol (% Daily Value)', 'Sodium', 'Sodium (% Daily Value)',
       'Carbohydrates', 'Carbohydrates (% Daily Value)', 'Dietary Fiber',
       'Dietary Fiber (% Daily Value)', 'Sugars', 'Protein',
       'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)',
       'Calcium (% Daily Value)', 'Iron (% Daily Value)']
 
X = menu_data[menu_features]
 
X.describe()
 
X.head()

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

menu_model =DecisionTreeRegressor(random_state=1)

menu_model.fit(X,y)

print("Making predictions for the following 5 menu items:")
print(X.head())
print("The predictions are")
print(type(X.head()))
cus_input = [[13.0	,20	,5.0,	25,	0.0	,260	,87,	750	,31	,31,	10,	4,	17,	3,	17,	10,	0,	25,	155]]
print(menu_model.predict(cus_input))