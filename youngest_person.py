# Coding starts here...

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Initialize variables to keep track of the youngest person
youngest_age = None
youngest_name = ""

# Step-by-step processing
for person in people:
    # Display the full string
    print(f"Processing: {person}")
    
    # Split the string into name and age
    name, age_str = person.split()
    age = int(age_str)
    print(f"Name: {name}, Age: {age}")

    # Check if this person is the youngest so far
    if youngest_age is None or age < youngest_age:
        youngest_age = age
        youngest_name = name

# Display the result
print(f"\nThe youngest person is {youngest_name} who is {youngest_age} years old.")
