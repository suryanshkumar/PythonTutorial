#how to write and read basic .txt file

#write file
fwrite = open('example.txt', 'w')
fwrite.write('this is a text file\n')
fwrite.write('python is a powerful programming language\n')
fwrite.close()

#read file
fread = open('example.txt', 'r')
text = fread.read()
print(text)
fread.close()
