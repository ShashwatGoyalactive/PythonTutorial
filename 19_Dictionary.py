# dictionary holds key-value pairs it an have only unique keys
coustomer = {
    "name" : "John Smith",
    "age": 30,
    "is_verified":True
}

print(coustomer["name"])

# .get() does not generate an error if a key is not present in the dictionary , it simply returns none
# a default value can be passed with the attribute in the get() method
# on the otherhand using square brackets to access a key which is not present will generte error
print(coustomer.get("birthday" , "January 1 1980"))

print(coustomer)


# Question:- Emojis exercise

message = input('Enter you message with an emoji: ')
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "😞"
}

output = ''
for word in words:
    output += emojis.get(word , word) + " "
print(output)