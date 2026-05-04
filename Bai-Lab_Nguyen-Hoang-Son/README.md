# Bài thực hành: Băm dữ liệu và kiểm tra tính toàn vẹn

## 1. Giới thiệu

Dự án này minh họa cách sử dụng hàm băm mật mã trong Python để kiểm tra sự thay đổi của dữ liệu và file.

Các thuật toán được sử dụng:

- **SHA-256**: tạo mã băm có độ dài 256 bit
- **SHA-512**: tạo mã băm có độ dài 512 bit

Thông qua mã băm, chương trình có thể phát hiện dữ liệu hoặc file có bị thay đổi hay không. Chỉ cần dữ liệu thay đổi một ký tự hoặc file bị chỉnh sửa một phần nhỏ thì mã băm tạo ra sẽ khác hoàn toàn.

---

## 2. Cấu trúc thư mục

```text
.
├── bai1_bam_du_lieu_sha256_sha512.py
├── bai2_kiem_tra_anh_sha512.py
├── bai3_gui_nhan_file_sha512.py
├── practice_note.png
├── requirements.txt
└── README.md
```

---

## 3. Mô tả các file

| File                    | Mô tả                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| `bai1_bam_du_lieu.py`   | Băm dữ liệu dạng chuỗi bằng SHA-256 và SHA-512, sau đó so sánh dữ liệu ban đầu với dữ liệu đã sửa. |
| `bai2_kiem_tra_anh.py`  | Tính mã băm SHA-512 của file ảnh `practice_note.png` để kiểm tra file có bị thay đổi hay không.    |
| `bai3_gui_nhan_file.py` | Mô phỏng quá trình gửi/nhận file và xác thực tính toàn vẹn bằng SHA-512.                           |
| `practice_note.png`     | File ảnh mẫu dùng để kiểm tra tính toàn vẹn.                                                       |
| `requirements.txt`      | Danh sách thư viện cần cài đặt. Dự án này không cần thư viện ngoài.                                |

---

## 4. Yêu cầu hệ thống

- Python 3.x
- Không cần cài đặt thư viện bên ngoài

Kiểm tra phiên bản Python:

```bash
python --version
```

hoặc:

```bash
python3 --version
```

Các thư viện được dùng đều có sẵn trong Python:

- `hashlib`
- `pathlib`
- `shutil`

---

## 5. Hướng dẫn chạy chương trình

### 5.1. Chạy bài 1

```bash
python bai1_bam_du_lieu_sha256_sha512.py
```

hoặc:

```bash
python3 bai1_bam_du_lieu_sha256_sha512.py
```

Chương trình sẽ in ra mã băm SHA-256 và SHA-512 của dữ liệu ban đầu và dữ liệu sau khi sửa.

---

### 5.2. Chạy bài 2

Đảm bảo file `practice_note.png` nằm cùng thư mục với file `bai2_kiem_tra_anh_sha512.py`.

```bash
python bai2_kiem_tra_anh_sha512.py
```

hoặc:

```bash
python3 bai2_kiem_tra_anh_sha512.py
```

Sau khi chương trình in mã băm ban đầu, có thể:

- Nhấn **Enter** nếu không sửa file ảnh
- Sửa file ảnh rồi quay lại terminal và nhấn **Enter**

Chương trình sẽ tính lại mã băm và thông báo file ảnh có bị thay đổi hay không.

---

### 5.3. Chạy bài 3

Đảm bảo file `practice_note.png` nằm cùng thư mục với file `bai3_gui_nhan_file_sha512.py`.

```bash
python bai3_gui_nhan_file_sha512.py
```

hoặc:

```bash
python3 bai3_gui_nhan_file_sha512.py
```

Khi chương trình hỏi:

```text
Ban co muon gia lap file bi sua khi truyen khong? (y/n):
```

Nhập:

- `y`: giả lập file nhận bị sửa đổi trong quá trình truyền
- `n`: giữ nguyên file nhận

Nếu mã băm bên gửi và bên nhận giống nhau, file nhận toàn vẹn. Nếu mã băm khác nhau, file nhận đã bị thay đổi.

---

## 6. Kết quả mong đợi

### Bài 1

Dữ liệu ban đầu:

```text
Dai Nam University
```

Dữ liệu sau khi sửa:

```text
Dai Nam University9999
```

Kết quả: mã băm SHA-256 và SHA-512 của hai chuỗi khác nhau, chứng tỏ dữ liệu đã bị thay đổi.

---

### Bài 2

- Nếu không sửa `practice_note.png`: chương trình thông báo file ảnh không bị thay đổi.
- Nếu sửa `practice_note.png`: chương trình thông báo file ảnh đã bị thay đổi hoặc bị lỗi.

---

### Bài 3

- Nếu chọn `n`: file nhận toàn vẹn, mã băm bên gửi và bên nhận giống nhau.
- Nếu chọn `y`: file nhận bị sửa giả lập, mã băm bên gửi và bên nhận khác nhau.

---

## 7. Ý nghĩa bài thực hành

Bài thực hành giúp hiểu rõ:

- Cách tạo mã băm bằng SHA-256 và SHA-512
- Cách kiểm tra dữ liệu có bị thay đổi hay không
- Cách kiểm tra tính toàn vẹn của file ảnh
- Cách mô phỏng gửi/nhận file và xác thực toàn vẹn dữ liệu
- Ứng dụng của hàm băm trong an toàn thông tin

---

## 8. Sinh viên thực hiện

- Sinh viên thực hiện: **Nguyễn Hoàng Sơn**
- Trường: **Đại học Đại Nam**
- Môn học: **An toàn bảo mật thông tin**
