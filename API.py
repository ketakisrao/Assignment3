from flask_api import FlaskAPI
from flask import request
import pickle
import sklearn
import pandas
from sklearn import preprocessing



app = FlaskAPI("deathCauses")

@app.route('/deaths', methods=['GET', 'POST'])
def deathCauses():
    if request.method == 'GET':
        model = []
        with open('deaths_model', 'rb') as f:
            model = pickle.load(f)
        with open('columns', 'rb') as f:
            columns = pickle.load(f)
        # print(columns)
        predict_data_cat = [['Black', 'M', 'Single']]
        #['Black', 'M', 'Single'], ['White', 'M', 'Widowed'], ['Hawaiian', 'F', 'Married']
        #[20, 6], [72, 3], [36, 5]
        predict_data_num = [[20, 6]]
        features_num = ['age', 'education']


        enc = preprocessing.OneHotEncoder()
        enc.fit(predict_data_cat)
        one_hot = enc.transform(predict_data_cat)
        X_cat_processed = pandas.DataFrame(one_hot.toarray(), columns=enc.get_feature_names())
        query = X_cat_processed.reindex(columns=columns, fill_value=0)
        s = preprocessing.scale(predict_data_num)
        s = pandas.DataFrame(s, columns=features_num)
        query = pandas.concat([s, query], axis=1, sort=False)

        Y = model.predict(query)
        print(Y)
    return {'cause_of_death': Y[0]}

if __name__ == "__main__":
    app.run(debug=True)
