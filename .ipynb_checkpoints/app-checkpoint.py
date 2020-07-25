from flask import Flask, render_template, request, url_for
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import model as m


app = Flask(__name__, template_folder='Templates',static_folder = 'static')

@app.route('/', methods = ['GET','POST'])
def predict():
	if request.method == 'POST':
		occ_ = request.form["occupation"]
		occ_1 = int(occ_)

		preds = m.predire(occ_1)
		if preds[0] == 1:
			ans = preds
		else:
			ans = preds
		return render_template('BF_home.html', predire =ans)
	return render_template('BF_home.html', predire ='')



if __name__ == '__main__':
	app.run(debug = True)


#def predictions():
#	if request.method == 'POST':
 #       data = request.request.form.get('age_dummies', 'Occupation', 'Product_Category_2','Product_Category_3')
 #       preds = m.model('age_dummies', 'Occupation', 'Product_Category_2','Product_Category_3')
#	return render_template('BF_predictions.html', prediction = preds)

# if __name__ == '__main__':
# 	app.run()
