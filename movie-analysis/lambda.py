
person = [
    {"id":123, "email":"abc@123"},
    {"id":345, "email":"abd@123"},
    {"id":567, "email":"abz@123"},
    ]
user = list(map(lambda x:x["id"],person))
print(user)
prices = [100,100,3499,7800,80000,450000,690000]
dis_price = list(map( lambda price:price*0.20,prices))
print(dis_price)