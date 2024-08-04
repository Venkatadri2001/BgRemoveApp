from django.shortcuts import render, redirect
from .forms import ImageUploadForm, BackgroundSelectionForm
from .models import ImageUpload, BackgroundImage
from .bgremover import remove_background
from PIL import Image
import os
from django.conf import settings

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_upload = form.save()
            result_path = remove_background(image_upload.image.path)
            image_upload.result = result_path
            image_upload.save()
            return redirect('result', pk=image_upload.pk)
    else:
        form = ImageUploadForm()
    return render(request, 'remover/upload.html', {'form': form})

def result_view(request, pk):
    image_upload = ImageUpload.objects.get(pk=pk)
    return render(request, 'remover/result.html', {'image_upload': image_upload})

def add_background_view(request, pk):
    image_upload = ImageUpload.objects.get(pk=pk)
    modified_image_url = None

    if request.method == 'POST':
        selected_background = request.POST.get('background')

        # Map selected background color
        if selected_background == 'white':
            background_color = (255, 255, 255, 255)  # White background with alpha
        elif selected_background == 'blue':
            background_color = (0, 0, 255, 255)  # Blue background with alpha
        elif selected_background == 'green':
            background_color = (0, 255, 0, 255)  # Green background with alpha
        elif selected_background == 'yellow':
            background_color = (255, 255, 0, 255)  # Yellow background with alpha
        elif selected_background == 'pink':
            background_color = (255, 192, 203, 255)  # Pink background with alpha
        elif selected_background == 'azure':
            background_color = (240, 255, 255, 255)  # Azure background with alpha
        elif selected_background == 'silver':
            background_color = (192, 192, 192, 255)  # Silver background with alpha
        else:
            background_color = (255, 255, 255, 255)  # Default to white

        # Apply the background
        modified_image_url = add_background_to_image(image_upload.result.path, background_color)
    
    return render(request, 'remover/addbg.html', {
        'image_upload': image_upload,
        'modified_image_url': modified_image_url
    })



def add_background_to_image(image_path, color):
    from PIL import Image
    import os

    # Open the result image
    result_image = Image.open(image_path).convert('RGBA')

    # Create a new image with the background color
    background = Image.new('RGBA', result_image.size, color=color)
    background.paste(result_image, (0, 0), result_image)  # Composite the images

    output_dir = os.path.join('media', 'results_with_background')
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
    output_path = os.path.join(output_dir, os.path.basename(image_path))

    # Save the final image
    background.save(output_path, format='PNG')  # Save as PNG for transparency

    # Return URL path relative to media root
    return os.path.join(settings.MEDIA_URL, 'results_with_background', os.path.basename(image_path))
