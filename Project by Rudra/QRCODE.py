import qrcode
import sys

def url_to_qrcode(url, output_file="qrcode.png", box_size=10, border=4):
    """
    Convert a URL to a QR code image.
    
    Parameters:
        url (str): The URL to encode.
        output_file (str): Name of the output image file (PNG format).
        box_size (int): Size of each box in the QR code grid.
        border (int): Border size (in boxes) around the QR code.
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls size (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"✅ QR code saved as '{output_file}'")

if __name__ == "__main__":
    # Get URL from command line argument or user input
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the URL to convert: ").strip()

    if not url:
        print("❌ No URL provided. Exiting.")
        sys.exit(1)

    # Optional: allow custom output filename
    output = input("Output filename (default: qrcode.png): ").strip()
    if not output:
        output = "qrcode.png"

    url_to_qrcode(url, output)