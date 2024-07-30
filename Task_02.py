# To get started, you will need the Pillow library for image manipulation. You can install it using pip if you haven't already:
pip install pillow

# Here’s the implementation:

from PIL import Image

def encrypt_image(image_path, shift, output_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    # Encrypt each pixel by adding the shift value
    encrypted_pixels = [(r + shift, g + shift, b + shift) for r, g, b in pixels]
    
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(output_path)

    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, shift, output_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    # Decrypt each pixel by subtracting the shift value
    decrypted_pixels = [(r - shift, g - shift, b - shift) for r, g, b in pixels]
    
    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_path)

    print(f"Decrypted image saved as {output_path}")

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? Enter 'e' or 'd': ").lower()
        if choice in ['e', 'd']:
            break
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

    image_path = input("Enter the path to the image file: ")
    output_path = input("Enter the path to save the output image file: ")

    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid shift value. Please enter an integer.")

    if choice == 'e':
        encrypt_image(image_path, shift, output_path)
    else:
        decrypt_image(image_path, shift, output_path)

if __name__ == "__main__":
    main()
