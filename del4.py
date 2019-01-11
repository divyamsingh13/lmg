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
store1=pd.read_csv("Store_Master.csv")
store1['Region']=store1['Region'].apply(lambda x:x[5:])

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
	if(a['State'].values=='Unspecified'):
		c=trans[trans.Customer_ID==x].iloc[0]
		c1=c['Store_Code']
		print(c1)
		
		d=store1[store1['Store_Code']==c1]
		print(d)
		a=a.copy()
		a.loc[a[a.Customer_ID==x].index,'State']=d['Region'].values
		print(a)
		# a.drop(a[a.State=="Unspecified"].index,axis=0,inplace=True)
		print(a)
	print(a['State'].values,b['Region'].values)
	try:
		if((a['State'].values.any()==b['Region'].values)):			
			test_set[test_set['Customer_ID']==x]['Prediction']=1
			test_set.iloc[i1]['Prediction']=1
			# test_set.at(i1,'Prediction')=1
			test_set.set_value(i1,'Prediction',1)
			i=i+1
			print(i)
	except Exception as e:
		print(e)
		continue




test_set.to_csv("test_set5.csv",index=False)
print(test_set.head())















