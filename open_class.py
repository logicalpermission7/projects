my_class_files = open("/Users/ironman/Desktop/python_class.txt", "a")

print(my_class_files.readable())
print(my_class_files.write("\nTHIS IS THE END OF THIS FILE"))

my_class_files.close()