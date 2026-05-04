import hashlib
import shutil
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

def send_file(source_file: str, received_file: str) -> None:
    shutil.copyfile(source_file, received_file)
    print("Da gui file thanh cong.")
    print("File gui:", source_file)
    print("File nhan:", received_file)

def modify_received_file(received_file: str) -> None:
    with open(received_file, "ab") as file:
        file.write(b"\nDATA BI THEM VAO DE GIA LAP FILE BI SUA")
    print("File nhan da bi sua doi gia lap.")

print("===== BAI 3: MO PHONG GUI NHAN FILE VA XAC THUC TOAN VEN =====")

# File goc ben gui
sender_file = "practice_note.png"

# File ben nhan
receiver_file = "received_practice_note.png"

if not Path(sender_file).exists():
    print("Khong tim thay file:", sender_file)
    print("Hay dat file practice_note.png cung thu muc voi file bai3_gui_nhan_file_sha512.py")
else:
    print("\n===== BEN GUI =====")

    sender_hash = hash_file_sha512(sender_file)

    print("File gui:", sender_file)
    print("SHA-512 ben gui:")
    print(sender_hash)

    print("\n===== DANG GUI FILE =====")
    send_file(sender_file, receiver_file)

    choice = input("\nBan co muon gia lap file bi sua khi truyen khong? (y/n): ")

    if choice.lower() == "y":
        modify_received_file(receiver_file)

    print("\n===== BEN NHAN =====")

    receiver_hash = hash_file_sha512(receiver_file)

    print("File nhan:", receiver_file)
    print("SHA-512 ben nhan:")
    print(receiver_hash)

    print("\n===== KIEM TRA TINH TOAN VEN =====")

    if sender_hash == receiver_hash:
        print("Ket qua: File nhan TOAN VEN, khong bi thay doi.")
    else:
        print("Ket qua: File nhan KHONG TOAN VEN, da bi thay doi.")
