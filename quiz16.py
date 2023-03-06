def password_gen():
    import random
    import string

    user_input=int(input("ener the length of the password"))
    all=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    passw=random.sample(all,user_input)
    sirii=''.join(passw)
    return sirii
print(password_gen())