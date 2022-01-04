import pymongo

client = pymongo.MongoClient()
mydb = client["mydb"]
my_col = mydb["people"]
data_list = [{'Name': "Himanshu Jadon",'Gender':'Male','Place':'Indore'},
                {'Name': "Himanshu Rajore",'Gender':'Male','Place':'Akodia'},
                {'Name': "Anchal Rathore",'Gender':'Female','Place':'Rau'},
                {'Name': "Rohit Malviya",'Gender':'Male','Place':'Indore'},
                {'Name': "Vikas Rathore",'Gender':'Male','Place':'Indore'}]

x = my_col.insert_many(data_list)
print(mydb.list)