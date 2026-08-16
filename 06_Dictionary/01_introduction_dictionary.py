#comma separated key-value pairs enclosed within {}
#{key1 : value1,key2 : value2,....}

grocery ={"milk":60,"biscuits":20,"rice":90,"bread":20}

# print(grocery,type(grocery)) #{'milk': 60, 'biscuits': 20, 'rice': 90, 'bread': 20} <class 'dict'>
# print(len(grocery)) #4
# print(grocery[0]) #KeyError: 0
# print(grocery['milk']) #value:  60
# print(grocery['eggs']) #KeyError: 'eggs'

#dictionaries are mutable
# grocery['milk'] =30 #it update the value of the key
# print(grocery) #{'milk': 30, 'biscuits': 20, 'rice': 90, 'bread': 20}

#add the new key value pairs
grocery['aggs'] = 30
print(grocery) #{'milk': 60, 'biscuits': 20, 'rice': 90, 'bread': 20, 'aggs': 30}