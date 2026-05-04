import hashlib
from pathlib import Path

def hash_file_sha512(file_path: str) -> str:
    sha512 = hashlib.sha512()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha512.update(chunk)

    return sha512.hexdigest()

print("===== BAI 2: KIEM TRA TINH TOAN VEN FILE ANH BANG SHA-512 =====")

# File anh can kiem tra
file_image = "practice_note.png"

if not Path(file_image).exists():
    print("Khong tim thay file anh:", file_image)
    print("Hay dat file practice_note.png cung thu muc voi file bai2_kiem_tra_anh_sha512.py")
else:
    # Tinh ma bam ban dau
    original_hash = hash_file_sha512(file_image)

    print("\n===== HASH BAN DAU CUA FILE ANH =====")
    print("File:", file_image)
    print("SHA-512:", original_hash)

    input("\nHay sua file anh practice_note.png hoac nhan Enter neu khong sua...")

    # Tinh ma bam sau khi kiem tra lai
    current_hash = hash_file_sha512(file_image)

    print("\n===== HASH SAU KHI KIEM TRA LAI =====")
    print("File:", file_image)
    print("SHA-512:", current_hash)

    print("\n===== KET QUA KIEM TRA =====")

    if original_hash == current_hash:
        print("File anh KHONG bi thay doi.")
    else:
        print("File anh DA bi thay doi hoac bi loi.")
