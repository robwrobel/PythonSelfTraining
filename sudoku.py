import random

fields = [0] * 81

rows_id = []

for id in range(1,10)

print (fields)

def get_valid_values(field_id):
    valid_values = range(10)

    values_in_square = get_values_in_square(field_id)
    values_in_row = get_values_in_row(field_id)
    values_in_column = get_values_in_column(field_id)

    valid_values = valid_values - values_in_square - values_in_row - values_in_column

    return valid_values

def get_values_in_square(field_id):
    allowed_values = range(10)
    return allowed_values

def get_values_in_row(field_id):
    allowed_values = range(10)
    return allowed_values

def get_values_in_column(field_id):
    allowed_values = range(10)
    return allowed_values

def get_random(allowed_values):
    index = random.randint(0,len(allowed_values))
    return allowed_values[index]

def main():



    


