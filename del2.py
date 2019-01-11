import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.cluster import SpectralClustering



# customer= pd.read_csv("customer.csv")
store=pd.read_csv("store_test.csv")
demo=pd.read_csv("Customer_Demographics.csv")
trans=pd.read_csv("Customer_Transaction.csv")
# test=store.loc[store['Train_Test_Store']=='Test']
test_set=pd.read_csv("Test_Set.csv")
test_set['Prediction']=0

# test_set=test_set.drop('Rec',1)
print(test_set.head())
counts = trans['Customer_ID'].value_counts().to_dict()
store['Region']=store['Region'].apply(lambda x:x[5:])
print(store['Region'])
i=0
i1=-1
for x,y in zip(test_set['Customer_ID'],test_set['Store_Code']):
	# a=np.where[demo['Customer_ID']==x]['State']
	# b=store.where[store['Store_Code']==y]['Region']
	i1=i1+1
	a=demo[demo.Customer_ID==x]
	b=store[store.Store_Code==y]
	
	print(a['State'].values,b['Region'].values)
	try:
		if((a['State'].values==b['Region'].values) and (a['Income_Range'].values!='Unspecified' or counts[x]>1) and ((a['Income_Range'].values=='Below 5000' and counts[x]>1) or a['Income_Range'].values!='Below 5000')):			
			test_set[test_set['Customer_ID']==x]['Prediction']=1
			test_set.iloc[i1]['Prediction']=1
			# test_set.at(i1,'Prediction')=1
			test_set.set_value(i1,'Prediction',1)
			i=i+1
			print(i)
	except Exception as e:
		print(e)
		continue




test_set.to_csv("test_set3.csv",index=False)
print(test_set.head())















