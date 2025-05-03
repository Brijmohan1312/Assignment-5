dict={"Alice":85,"Ram":44,"Suresh":67,"Jay":78}
name = input("Enter the Student's name: ")

if name in dict:
     print("{}'s marks: {}".format(name,dict.get(name)))
else:
     print("student not found.")

