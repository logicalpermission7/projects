
list = []
my_stuff = open("/Users/ironman/Desktop/mylist.txt", "a")

print(my_stuff.readable())
item = input("Enter a item here: ")
list.append(item)
list.sort()
print(my_stuff.write( ":" + " " + str(list)))
print(my_stuff.write("\n"))


my_stuff.close()