"""F_to_C v1
Converting from Fahrenheit to CentigradeD by using the formula"""




def to_c(from_f):
    celcius = (from_f -32) * 5/9
    return celcius


# Main Routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)
