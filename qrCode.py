import qrcode

def generate_qr_code(link, file_name):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code, 1 is the smallest
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be (the default is 4)
    )
    
    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="blue", back_color="white")

    # Save the image
    img.save(file_name)
    print(f"QR code image saved as {file_name}")

# Example usage
link = "file:///C:/Users/Dell/Desktop/certificate/SalimAlOmarUnityCertificate.png"
file_name = "SCU.png"
generate_qr_code(link, file_name)
