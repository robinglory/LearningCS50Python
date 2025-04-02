import sys
import os
from PIL import Image, ImageOps

def main():
    # Validate command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Validate file extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()
    
    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid input")
    
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    
    # Try opening the input image
    try:
        image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input file does not exist")
    
    # Open the shirt image
    shirt = Image.open("shirt.png")
    size = shirt.size
    
    # Resize and crop input image
    image = ImageOps.fit(image, size)
    
    # Overlay the shirt
    image.paste(shirt, shirt)
    
    # Save the output image
    image.save(output_path)
    
if __name__ == "__main__":
    main()
