import streamlit as st
from PIL import Image
import numpy as np
import math
import io

# Function to determine the column order based on the key
def get_key_order(key):
    sorted_key = sorted(list(key))  # Sort key characters alphabetically
    key_order = []
    for char in key:
        key_order.append(sorted_key.index(char))  # Get column order based on the original key
        sorted_key[sorted_key.index(char)] = None  # Mark used characters to avoid duplicate indices
    return key_order

# Function to encrypt text using the Columnar Transposition Cipher
def encrypt(text, key):
    key_order = get_key_order(key)  # Get column order
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)  # Calculate required rows
    grid = [['X'] * num_cols for _ in range(num_rows)]  # Create a grid filled with 'X' as padding
    
    # Fill the grid with text characters row-wise
    index = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if index < len(text):
                grid[i][j] = text[index]
                index += 1
    
    # Read the grid column-wise based on key order to get encrypted text
    encrypted_text = "".join("".join(grid[row][col] for row in range(num_rows)) for col in key_order)
    return encrypted_text

# Function to decrypt text using the Columnar Transposition Cipher
def decrypt(cipher_text, key):
    key_order = get_key_order(key)  # Get column order
    num_cols = len(key)
    num_rows = math.ceil(len(cipher_text) / num_cols)  # Calculate rows needed
    grid = [[''] * num_cols for _ in range(num_rows)]  # Create an empty grid
    
    # Fill the grid column-wise using key order
    index = 0
    for col in key_order:
        for row in range(num_rows):
            if index < len(cipher_text):
                grid[row][col] = cipher_text[index]
                index += 1
    
    # Read the grid row-wise to reconstruct the original text
    decrypted_text = "".join("".join(row) for row in grid).rstrip('X')  # Remove padding 'X'
    return decrypted_text

# Function to embed encrypted text into an image using LSB steganography
def embed_text(image, text):
    pixels = np.array(image)  # Convert image to numpy array
    binary_text = ''.join(format(ord(char), '08b') for char in text) + '11111111'  # Convert text to binary and add stop marker
    
    # Check if text fits in image
    if len(binary_text) > pixels.size:
        st.error("Message too long for the image")
        return None
    
    # Flatten image pixels and modify the least significant bit (LSB)
    flat_pixels = pixels.flatten()
    for i in range(len(binary_text)):
        flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_text[i])  # Modify LSB with binary text
    
    pixels = flat_pixels.reshape(pixels.shape)  # Reshape back to original image dimensions
    return Image.fromarray(pixels)  # Convert array back to image

# Function to extract hidden text from an image
def extract_text(image):
    pixels = np.array(image).flatten()  # Flatten image to 1D array
    binary_text = "".join(str(p & 1) for p in pixels)  # Extract LSB from each pixel
    
    # Convert binary to characters
    chars = [chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8)]
    extracted_text = "".join(chars).split('\xff')[0]  # Stop at the marker
    return extracted_text

# Streamlit UI setup
st.title("Columnar Cipher with Image Steganography")

# Selection menu for encryption or decryption
menu = st.radio("Choose an option", ["Encrypt & Embed", "Extract & Decrypt"])

# Encrypt & Embed Section
if menu == "Encrypt & Embed":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])  # Image input
    text = st.text_input("Enter Message")  # Message input
    key = st.text_input("Enter Key")  # Key input
    
    if st.button("Encrypt & Save"):  # Button to process encryption and embedding
        if uploaded_file and text and key:
            image = Image.open(uploaded_file)  # Load image
            encrypted_text = encrypt(text, key)  # Encrypt message
            encrypted_image = embed_text(image, encrypted_text)  # Embed encrypted text into image
            
            if encrypted_image:
                st.success("Message encrypted and embedded successfully!")
                buf = io.BytesIO()  # Create a buffer to save the image
                encrypted_image.save(buf, format="PNG")  # Save image to buffer
                st.download_button("Download Encrypted Image", buf.getvalue(), "encrypted.png", "image/png")  # Provide download button
        else:
            st.error("Please upload an image and enter text & key.")  # Error handling

# Extract & Decrypt Section
elif menu == "Extract & Decrypt":
    uploaded_file = st.file_uploader("Upload an encrypted image", type=["png"])  # Upload encrypted image
    key = st.text_input("Enter Key")  # Enter decryption key
    
    if st.button("Extract & Decrypt"):  # Button to extract and decrypt message
        if uploaded_file and key:
            image = Image.open(uploaded_file)  # Load encrypted image
            extracted_text = extract_text(image)  # Extract hidden message
            decrypted_text = decrypt(extracted_text, key)  # Decrypt the extracted message
            st.success(f"Decrypted Message: {decrypted_text}")  # Display decrypted text
        else:
            st.error("Please upload an encrypted image and enter the key.")  # Error handling
