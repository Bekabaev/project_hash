import hashlib

username = input("Username: ")
password = input("Password: ")

# converts password to hash
def hash_password(password):
    hash = hashlib.sha256()
    hash.update(password.encode("utf-8"))
    hash_value = hash.hexdigest()
    return hash_value

# create file
# def registration():
#     file = open("info.txt","w")
#     file.write(hash_password(password))
#     file.write("\n" + username)
#     file.close()

#checking the password for correctness
def check(check_password,check_name):
    if check_password == hash_password(password) and check_name == username:
        print(f"Welcome {username}")
    elif check_name != username:
        print("User not found")
    elif check_password != hash_password(password):
        print("Invalid password")

def sign(path):
    with open(path,"r") as f:
        pw = f.readline().rstrip()
        un = f.readline()
    check(pw,un)
sign("info.txt")