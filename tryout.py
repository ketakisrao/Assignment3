import pandas # import pandas library
import sklearn # import scikit-learn
from sklearn import preprocessing # import preprocessing utilites
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression


df = pandas.read_csv('death_causes.csv', low_memory=False) # read the csv file into a pandas dataframe object

features_cat = ['race', 'sex', 'relationship_status', 'education']
features_num = ['age']

X_cat = df[features_cat]
X_num = df[features_num]

enc = preprocessing.OneHotEncoder()
enc.fit(X_cat) # fit the encoder to categories in our data 
one_hot = enc.transform(X_cat) # transform data into one hot encoded sparse array format

# Finally, put the newly encoded sparse array back into a pandas dataframe so that we can use it
X_cat_proc = pandas.DataFrame(one_hot.toarray(), columns=enc.get_feature_names())
# X_cat_proc.head()

scaled = preprocessing.scale(X_num)

X_num_proc = pandas.DataFrame(scaled, columns=features_num)
X_num_proc.head()

X = pandas.concat([X_num_proc, X_cat_proc], axis=1, sort=False)
X.head()

X = X.fillna(0) # remove NaN values
y = df['group'] # target

X_train, X_TEMP, y_train, y_TEMP = train_test_split(X, y, test_size=0.30) # split out into training 70% of our data
X_validation, X_test, y_validation, y_test = train_test_split(X_TEMP, y_TEMP, test_size=0.50) # split out into validation 15% of our data and test 15% of our data
print(X_train.shape, X_validation.shape, X_test.shape) # print data shape to check the sizing is correct
#print(y_train.shape, y_validation.shape, y_test.shape)

# helper method to print basic model metrics
def metrics(y_true, y_pred):
    print('Confusion matrix:\n', confusion_matrix(y_true, y_pred))
    # target_names = ['denied', 'approved']
    print('\nReport:\n', classification_report(y_true, y_pred))

model = LogisticRegression(solver='lbfgs', multi_class='ovr', max_iter=200).fit(X_train, y_train) # first fit (train) the model
y_pred = model.predict(X_validation) # next get the model's predictions for a sample in the validation set
metrics(y_validation, y_pred) # finally evaluate performance
print(y_pred.head())