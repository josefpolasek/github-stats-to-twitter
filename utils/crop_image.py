from PIL import Image
import io


def crop_image(image_stream, size=(1500, 500)):
    # Open the image from a byte stream
    img = Image.open(image_stream)

    # Get dimensions
    width, height = img.size

    # Calculate aspect ratio of the new size
    target_width, target_height = size
    target_aspect = target_width / target_height

    # Calculate the current aspect ratio
    aspect = width / height

    # Determine cropping dimensions
    if aspect > target_aspect:
        # Crop the left and right sides
        new_width = int(target_aspect * height)
        offset = (width - new_width) // 2
        crop_box = (offset, 0, width - offset, height)
    else:
        # Crop the top and bottom
        new_height = int(width / target_aspect)
        offset = (height - new_height) // 2
        crop_box = (0, offset, width, height - offset)

    # Crop and resize the image
    cropped_img = img.crop(crop_box).resize(size, Image.LANCZOS)

    # Save the cropped image to a byte stream
    cropped_buf = io.BytesIO()
    cropped_img.save(cropped_buf, format='PNG')
    cropped_buf.seek(0)  # Move to the beginning of the BytesIO object

    return cropped_buf
