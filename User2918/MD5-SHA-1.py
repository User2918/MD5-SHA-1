import hashlib

def generate_md5(password):
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    print(md5_hash)

def generate_sha(password):
    sha_hash = hashlib.sha256(password.encode()).hexdigest()
    print(sha_hash)

hash_type = input("Enter the hash type (MD5 or SHA): ").upper()

if hash_type == "MD5" or hash_type == "SHA":
    password = input("Enter the password to hash: ")
    
    if hash_type == "MD5":
        generate_md5(password)
    else:
        generate_sha(password)
else:
    print("Enter either MD5 or SHA as the hash type.")
