"""
we have the following dictionaries containing detail:

user ={
    "user_name" : "my_user",
    "password" : "test@123",
    "email" : "my_user@example.com",
    "address" : "ABC road ,11111",
    "country" : "Australia",
}
Deleting the sensitive information  from the dictionary present in a list
sensitive_info =["password","address"]
"""
user ={
    "user_name" : "my_user",
    "password" : "test@123",
    "email" : "my_user@example.com",
    "address" : "ABC road ,11111",
    "country" : "Australia",
}
sensitive_info =["password","address","phone"]
# for key in user:
#     if key in sensitive_info:
#             user.pop(key)
# print(user) #RuntimeError: dictionary changed size during iteration

for key in sensitive_info:
    if key in user:
        print(f"DELETED => key: {key},value:{user[key]}")
        user.pop(key)
    else:
        print(f"{key} is not present in user")
print(user)