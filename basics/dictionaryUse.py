#use of dictionary in python

#its always followed by (key, value) protocol

#basic structure
books = {'key':'value', 'MVG':'Richard', 'AI':'Hinton'}
print(books)

#print using Key
print(books['MVG'])

#using loop
for k, v in books.items():
    print(k + " " + v)
