from PIL import Image  

def encrypt_image(image_path, key):
    
    img = Image.open(image_path)
    width, height = img.size

    
    img = img.convert("RGB")

    
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

  
    encrypted_image_path = image_path.split('.')[0] + "_encrypted.png"
    img.save(encrypted_image_path)
    print("Image encrypted successfully.")
    return encrypted_image_path

def decrypt_image(encrypted_image_path, key):
    
    img = Image.open(encrypted_image_path)
    width, height = img.size

    
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + "_decrypted.png"
    img.save(decrypted_image_path)
    print("Image decrypted successfully.")
    return decrypted_image_path


original_image_path = input("Enter the path to the image file: ")
encryption_key = int(input("Enter the encryption key (an integer value): "))


encrypted_image_path = encrypt_image(original_image_path, encryption_key)


decrypted_image_path = decrypt_image(encrypted_image_path, encryption_key)
