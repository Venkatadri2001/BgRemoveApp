from rembg import remove
from PIL import Image
import os

def remove_background(image_path):
    output_dir = os.path.join('media', 'results')
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it does not exist

    input_path = image_path
    output_path = os.path.join(output_dir, os.path.splitext(os.path.basename(image_path))[0] + '.png')
    
    # Open the input image
    input_image = Image.open(input_path)
    
    # Remove the background
    output_image = remove(input_image)
    
    # Convert to RGBA if necessary
    if output_image.mode != 'RGBA':
        output_image = output_image.convert('RGBA')
    
    # Save the output image as PNG
    output_image.save(output_path, format='PNG')
    return 'results/' + os.path.basename(output_path)
