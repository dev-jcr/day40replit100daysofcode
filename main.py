contacts={"name":"", "dob":"", "tel":"", "email":"", "address":""}
inp=input("Input your name\n").strip().capitalize()
contacts["name"]=inp
inp=input("Input your date of birth\n").strip()
contacts["dob"]=inp
inp=input("Input your telephone\n").strip()
contacts["tel"]=inp
inp=input("Input your email\n")
contacts["email"]=inp
inp=input("Input your physical address\n")
contacts["address"]=inp

print(f"""
Hi {contacts["name"]}. Our dictionary says that you were born on {contacts["dob"]}, we can call you on {contacts["tel"]}, email {contacts["email"]}, or write to {contacts["address"]}
""")