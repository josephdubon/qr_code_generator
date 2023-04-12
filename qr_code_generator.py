import qrcode

def create_qr_code(data, file_name, size=10, border=2):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    data = "https://www.example.com"  # Replace with your desired URL or data
    file_name = "qr_code.png"  # Replace with your preferred file name and format (e.g., jpg, png, or svg)

    create_qr_code(data, file_name)
