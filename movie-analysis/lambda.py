
person = [
    {"id":123, "email":"abc@123"},
    {"id":345, "email":"abd@123"},
    {"id":567, "email":"abz@123"},
    ]
user = list(map(lambda x:x["id"],person))
print(user)