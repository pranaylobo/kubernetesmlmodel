# import pandas as pd
# import json
# from flask import jsonify

# from flask import Flask
# from flask import request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)


# @app.route('/runmodel',methods=['POST'])

# def hello_world():
#     req_data = request.get_json(force=True)
#     language = req_data['language']
#     print("hello",language)
#     pd.set_option('display.max_rows', 500)
#     pd.set_option('display.max_columns', 500)
#     pd.set_option('display.width', 1000)
#     menu_file_path = "menu.csv"
#     menu_data = pd.read_csv(menu_file_path)
#     menu_data.columns
#     y = menu_data.Calories
    
#     menu_features = ['Total Fat','Total Fat (% Daily Value)','Saturated Fat','Saturated Fat (% Daily Value)', 'Trans Fat', 'Cholesterol',
#         'Cholesterol (% Daily Value)', 'Sodium', 'Sodium (% Daily Value)',
#         'Carbohydrates', 'Carbohydrates (% Daily Value)', 'Dietary Fiber',
#         'Dietary Fiber (% Daily Value)', 'Sugars', 'Protein',
#         'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)',
#         'Calcium (% Daily Value)', 'Iron (% Daily Value)']
    
#     X = menu_data[menu_features]
    
#     X.describe()
 
#     X.head()

#     from sklearn.tree import DecisionTreeRegressor
#     from sklearn.metrics import mean_absolute_error

#     menu_model =DecisionTreeRegressor(random_state=1)

#     menu_model.fit(X,y)

#     print("Making predictions for the following 5 menu items:")
#     print(X.head())
#     print("The predictions are")
#     print(type(X.head()))
#     cus_input = [[12.0	,20	,5.0,	25,	0.0	,260	,87,	750	,31	,31,	10,	4,	17,	3,	17,	10,	0,	25,	155]]
#     print(format(menu_model.predict(cus_input)))


#     a = menu_model.predict(cus_input)

#     b = a.tolist()
#     print(type(b))

#     return jsonify(b)

# if __name__ == '__main__':
#    app.run(host='0.0.0.0',port=8080)


# collab test

import pandas as pd
import json
from flask import jsonify

from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/runmodel',methods=['POST'])

def hello_world():
    req_data = request.get_json(force=True)
    language = req_data['input']
    print("hello",language)
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
    cus_input = [language]
    print(format(menu_model.predict(cus_input)))


    a = menu_model.predict(cus_input)

    b = a.tolist()
    print(type(b))


    return jsonify('Success')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080)





