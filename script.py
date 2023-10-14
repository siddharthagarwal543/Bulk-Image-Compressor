from PIL import Image
import os

def compress_and_save_image(image, output_path, quality=85):
    try:
        # Ensure the output format is WebP
        image = image.convert("RGB")

        # Compress and save the image in WebP format
        image.save(output_path, "WEBP", quality=quality)
    except Exception as e:
        print(f"Error compressing image {image.filename}: {str(e)}")

def bulk_compress_images(input_folder, output_folder, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(input_folder, filename)
            with Image.open(image_path) as image:
                base_filename, _ = os.path.splitext(filename)
                output_path = os.path.join(output_folder, f"{base_filename}.webp")
                compress_and_save_image(image, output_path, quality)


if __name__ == "__main__":
    input_folder = "/home/siddharth/Pictures/Screenshots"
    output_folder = "./final"
    compression_quality = 85

    bulk_compress_images(input_folder, output_folder, compression_quality)
    print(f"Images compressed and saved in {output_folder}")
