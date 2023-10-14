# Image Compressor

This is a simple Python application for bulk image compression to the WebP format using the Streamlit framework.

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/image-compressor.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Place your input images in the `input_images` folder.

4. Run the Streamlit app:

    ```bash
    streamlit run streamlit_image_compressor.py
    ```

5. Use the Streamlit interface to specify the input folder, output folder, and compression quality. Click the "Compress Images" button to process the images.

6. The compressed images will be saved in the `output_images` folder.

## Requirements

- Streamlit (1.7.1)
- Pillow (PIL) (8.4.0)

You can find the specific package versions in the `requirements.txt` file.

## Authors

- Siddharth Agarwal

## Acknowledgments

- Thanks to Streamlit for the great framework.
- Thanks to Pillow for image processing capabilities.
