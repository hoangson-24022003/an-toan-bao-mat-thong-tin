import hashlib

def hash_sha256(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def hash_sha512(data: str) -> str:
    return hashlib.sha512(data.encode("utf-8")).hexdigest()

# Du lieu ban dau
data_original = "Dai Nam University"

# Du lieu sau khi sua
data_modified = "Dai Nam University9999"

print("===== BAI 1: BAM DU LIEU BANG SHA-256 VA SHA-512 =====")

print("\n===== DU LIEU BAN DAU =====")
print("Du lieu:", data_original)
print("SHA-256:", hash_sha256(data_original))
print("SHA-512:", hash_sha512(data_original))

print("\n===== DU LIEU SAU KHI SUA =====")
print("Du lieu:", data_modified)
print("SHA-256:", hash_sha256(data_modified))
print("SHA-512:", hash_sha512(data_modified))

print("\n===== SO SANH =====")

if hash_sha256(data_original) == hash_sha256(data_modified):
    print("SHA-256: Du lieu khong thay doi")
else:
    print("SHA-256: Du lieu da bi thay doi")

if hash_sha512(data_original) == hash_sha512(data_modified):
    print("SHA-512: Du lieu khong thay doi")
else:
    print("SHA-512: Du lieu da bi thay doi")
