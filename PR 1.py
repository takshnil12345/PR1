import datetime
name = input("Enter your name: ")
age_str = (input("Enter your age: "))
height_str= (input("Enter your height in meters: "))
fav_num_str = input("Enter your favorite number: ")

current_year = datetime.date.today().year

birth_year = current_year - int(age_str)
print("name:", name, "Type:", type(name))
print("name:", name, "id:", id(name))
print("age:", age_str, "Type:", type(age_str))
print("age:", age_str, "id:", id(age_str))
print("height:", height_str, "Type:", type(height_str))
print("height:", height_str, "id:", id(height_str))
print("favorite number:", fav_num_str, "Type:", type(fav_num_str))
print("favorite number:", fav_num_str, "id:", id(fav_num_str))
print("birth year:", birth_year)
print("current year:", current_year)
print("today Date is:", datetime.date.today())