import pandas as pd
import numpy
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
flag=0
i=0
i1=-1
for x,y in zip(test_set['Customer_ID'],test_set['Store_Code']):
	# a=np.where[demo['Customer_ID']==x]['State']
	# b=store.where[store['Store_Code']==y]['Region']
	flag=0
	i1=i1+1
	e=set(trans[trans.Customer_ID==x]['Store_Code'].values)
	print("transaction city",e)
	a=demo[demo.Customer_ID==x]
	b=store[store.Store_Code==y]
	a['Points'].replace('',0, inplace=True)	
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
	if(b['Region'].values[0] not in e and (a['Loyalty_Status'].values=='Gold' or a['Points'].values>200)):
		for i in e:
			f=store1[store1['Store_Code']==i]['Region'].values
			if(f==b['Region'].values):
				print('2 cities',f,b['Region'])
				test_set.set_value(i1,'Prediction',1)
				flag=1
				break
	if(flag==1):
		continue
			
	print(a['State'].values,b['Region'].values)
	try:
		if(a['State'].values==b['Region'].values):
			test_set[test_set['Customer_ID']==x]['Prediction']=1
			test_set.iloc[i1]['Prediction']=1
			# test_set.at(i1,'Prediction')=1
			test_set.set_value(i1,'Prediction',1)
			i=i+1
			print(i)
	except Exception as e:
		print(e)
		continue




test_set.to_csv("test_set8.csv",index=False)
print(test_set.head())















