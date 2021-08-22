# To format the names in title case
input_first_name=input("Enter the first name: ")
input_last_name= input("Enter the last name: ")
def format_name(first_name,last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    full_name = first_name + " "+last_name
    return full_name


name = format_name(input_first_name,input_last_name)
print(name)


