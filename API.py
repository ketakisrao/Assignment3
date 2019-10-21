from flask_api import FlaskAPI
from flask import request, Response, make_response
import flask
import pickle
import sklearn
import pandas
from sklearn import preprocessing
import json



app = FlaskAPI("deathCauses")

@app.route('/deaths', methods=['GET', 'POST'])
def deathCauses():
    resp = []
    if request.method == 'POST':
        model = []
        with open('deaths_model', 'rb') as f:
            model = pickle.load(f)
        with open('columns', 'rb') as f:
            columns = pickle.load(f)
        
        predict_data_cat = [request.form['cat'].split(',')]
        #['Black', 'M', 'Single'], ['White', 'M', 'Widowed'], ['Hawaiian', 'F', 'Married']
        #[20, 6], [72, 3], [36, 5]
        predict_data_num = [request.form['num'].split(',')]
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

        df = pandas.read_csv('percentage_predict.csv', low_memory=False)
        group = df[df['Parent_Group'] == Y[0]]
        group = group.values.tolist()
        deathList = []
        for val in group:
            deathList.append({'name': val[0], 'percentage': val[2]})
        resp = make_response({'cause_of_death': Y[0], 'values': deathList})
        resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run(debug=True, host='localhost')
