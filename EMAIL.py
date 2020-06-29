
print("HELLO , this is a email slicer")
email=input("what is ur email address:?").strip()
user=email[:email.index("@")]
domain=email[email.index("@")+1:]
output="Your username is :{} \n and your DONAIN name is :{}".format(user,domain)
print(output)
