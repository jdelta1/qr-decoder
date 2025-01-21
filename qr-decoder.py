#use pip3 install pyzbar if needed
#usage: python3 qr-decoder.py /path/to/images
import os
import sys
from pyzbar.pyzbar import decode
from PIL import Image

def process_image(image_path):
    img = Image.open(image_path)
    decoded = decode(img)
    decoded_data = []
    for obj in decoded:
        data = obj.data.decode("utf-8")
        print(f"{image_path}: {data}")
        decoded_data.append(f"{image_path}: {data}")
    return decoded_data

def main(folder_path):
    if os.path.isdir(folder_path):
        # Open the output file
        with open("QrCodeValues.txt", "w") as output_file:
            # Process each image in the folder
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    image_path = os.path.join(folder_path, filename)
                    decoded_data = process_image(image_path)
                    # Write decoded data to the file
                    for line in decoded_data:
                        output_file.write(line + "\n")
        print("Processing complete. Results saved in QrCodeValues.txt")
    else:
        print(f"The provided folder path '{folder_path}' is not valid.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python qr-decoder.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        main(folder_path)
