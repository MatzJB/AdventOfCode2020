

def is_valid_passport(string):
    required_keys = ["byr",  "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for required_key in required_keys:
        if not (required_key+":") in string:
            return False
    return True

input_file = r'input.txt'
with open(input_file) as f:
    rows = f.read()

number_of_valid_passports = 0
passports = rows.split('\n\n')
[number_of_valid_passports := number_of_valid_passports + x for x in map(is_valid_passport, passports)]
print(number_of_valid_passports)