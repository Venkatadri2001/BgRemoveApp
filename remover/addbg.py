def add_background_to_image(image_path, color):
    from PIL import Image
    import os

    output_dir = os.path.join('media', 'results_with_background')
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
    output_path = os.path.join(output_dir, os.path.basename(image_path))

    # Open the result image
    result_image = Image.open(image_path).convert('RGBA')

    # Create a new image with the background color
    background = Image.new('RGBA', result_image.size, color=color)
    background.paste(result_image, (0, 0), result_image)  # Composite the images

    # Save the final image
    background.save(output_path, format='PNG')  # Save as PNG for transparency
    return output_path.replace('media/', '')  # Return URL-friendly path
