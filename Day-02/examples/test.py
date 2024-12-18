arn = "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE"
str = "Busetty"
str1 = "Jaanav"

full_name = str+" "+str1

print ("My Name is:", full_name)

print (arn.split("/")[1])

str_length = len(arn.split("/")[1])

print ("length of the string is:", str_length)
