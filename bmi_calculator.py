# Checking BMI in this Python Program

# Provide Height for Calculating BMI
height = input()
# Provide Weight for calculating BMI
weight = input()
# Converting Weight Variable into Integer
weight_as_int = int(weight)
# Converting Height Variable into Float Decimal
height_as_float = float(height)
#Using the exponent operator * *
bmi = weight_as_int/height_as_float **2

# Alternative Method using Multiplication and PEMDAS

bmi = weight_as_int /(height_as_float * height_as_float)
bmi_as_int = int(bmi)

print(bmi_as_int)
