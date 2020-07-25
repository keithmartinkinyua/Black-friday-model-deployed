import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
import pickle


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

open_file = open("LRmodel_pickle", "rb")
LR = pickle.load(open_file)
open_file.close()


def predire(occupation):
	data = (occupation)
	ty = LR.predict(data)
	return ty
	


#def predire(age, occupation, Product1,Product2):
#	age_dummies = pd.get_dummies(age)
#	data = (age_dummies, occupation, Product1, Product2)
	#datta = np.asarray(data)
	#datta.reshape(-1, 1)
#	ty = LR.predict(data)
#	return ty
 



