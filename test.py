import pandas as pd



customer= pd.read_csv("customer.csv")
store=pd.read_csv("Store_Master.csv")






train=store.loc[store['Train_Test_Store']=='Train']
test=store.loc[store['Train_Test_Store']=='Test']


print(train)
print(test)