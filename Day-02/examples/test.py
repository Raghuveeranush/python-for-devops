arn = "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE"

vpc = (arn.split("/")[1])
print("vpc id:",vpc)

str_length = len(arn.split("/")[1])

print ("length of the string is:", str_length)
