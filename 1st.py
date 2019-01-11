import pandas as pd
import numpy as np






demo=pd.read_csv("Customer_Demographics.csv")
trans=pd.read_csv("Customer_Transaction.csv")
store=pd.read_csv("Store_Master.csv")
# store=pd.get_dummies(store,columns=['Region','Store_Format'])
store.drop(['Territory','Business','Store_Name','Mall_Name'],axis=1,inplace=True)
store=store.replace(r'^\s+$', np.nan, regex=True)
store_train=store.loc[store['Train_Test_Store']=='Train']
store_test=store.loc[store['Train_Test_Store']=='Test']
store_train.drop(['Train_Test_Store'],axis=1,inplace=True)
store_test.drop(['Train_Test_Store'],axis=1,inplace=True)
store_train.to_csv("store_train.csv")
store_test.to_csv("store_test.csv")
store.drop(['Train_Test_Store'],axis=1,inplace=True)
store=pd.get_dummies(store,columns=['Region','Store_Format'])



customer=trans.merge(demo,how="left")
customer=pd.get_dummies(customer, columns=["Gender","Nationality","Loyalty_Status","State","City_Name","Store_Type","Income_Range"] )
customer.drop(['Birth_date','Language','Return_Reason','Job_Type','Marital_Status','Transaction_Type','Business','Territory','First_txn_dt','Last_accr_txn_dt','Last_rdm_txn_dt'],axis=1,inplace=True)
customer=customer.replace(r'^\s+$', np.nan, regex=True)
customer.to_csv("customer.csv")



customer_store=customer.merge(store,on="Store_Code")
customer_store.to_csv("customer_store.csv")

