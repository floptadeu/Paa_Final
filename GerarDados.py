import random

def generate_trapezoid_data(num_entries):
    data = f"{num_entries}\n"
    for _ in range(num_entries):
        x1 = round(random.uniform(1.0, 100.0), 2)
        x2 = round(random.uniform(-50.0, 100.0), 2)
        x3 = round(random.uniform(-50.0, 50.0), 2)
        data += f"{x1} {x2} {x3}\n"
    return data

# Generate data for 9 trapezoids
trapezoid_data = generate_trapezoid_data(1000)
print(trapezoid_data)
def create_file(filename = "grande.txt"):
    # Write the generated trapezoid data to a text file
    with open(filename, "w") as file:
        file.write(trapezoid_data)
create_file()