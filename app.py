import streamlit as st
from PIL import Image
import os

def compress_and_save_image(image, output_path, quality=85):
    try:
        # Ensure the output format is WebP
        image = image.convert("RGB")

        # Compress and save the image in WebP format
        image.save(output_path, "WEBP", quality=quality)
    except Exception as e:
        st.error(f"Error compressing image {image.filename}: {str(e)}")

def main():
    st.title("Image Bulk Compressor")

    input_folder = st.text_input("Input folder path", "input_images")
    output_folder = st.text_input("Output folder path", "output_images")
    compression_quality = st.slider("Compression Quality", 0, 100, 85)

    if st.button("Compress Images"):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_path = os.path.join(input_folder, filename)
                with Image.open(image_path) as image:
                    base_filename, _ = os.path.splitext(filename)
                    output_path = os.path.join(output_folder, f"{base_filename}.webp")
                    compress_and_save_image(image, output_path, compression_quality)

        st.success(f"Images compressed and saved in {output_folder}")

if __name__ == "__main__":
    main()
