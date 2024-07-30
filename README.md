# PRODIGY_CS-02
Task_02: Pixel Manipulation for Image Encryption

Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

To get started, you will need the Pillow library for image manipulation. You can install it using pip if you haven't already:
Copy code
pip install pillow

Explanation:
encrypt_image function:

Opens the image from the specified path.
Reads the pixel data and applies a shift value to each color component (red, green, and blue) to encrypt the image.
Saves the encrypted image to the specified output path.
decrypt_image function:

Opens the encrypted image from the specified path.
Reads the pixel data and subtracts the shift value from each color component to decrypt the image.
Saves the decrypted image to the specified output path.
main function:

Prompts the user to choose between encryption and decryption.
Asks for the image file path, the output file path, and the shift value.
Calls the appropriate function to perform the encryption or decryption.
This program will allow users to input an image file path, an output file path, and a shift value, and it will then either encrypt or decrypt the image based on their choice. Make sure to test it with different images and shift values to see the effects.


