# Initialize Mistral client with API key
from mistralai import Mistral
# Import required libraries
from pathlib import Path
from mistralai import DocumentURLChunk, ImageURLChunk, TextChunk
import json

import os
import base64
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY") 
client = Mistral(api_key=api_key)

# Verify PDF file exists
pdf_file = Path("mst.pdf")
assert pdf_file.is_file()

# Upload PDF file to Mistral's OCR service
uploaded_file = client.files.upload(
    file={
        "file_name": pdf_file.stem,
        "content": pdf_file.read_bytes(),
    },
    purpose="ocr",
)


# Get URL for the uploaded file
signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)

# Process PDF with OCR, including embedded images
pdf_response = client.ocr.process(
    document=DocumentURLChunk(document_url=signed_url.url),
    model="mistral-ocr-latest",
    include_image_base64=True
)

#View the OCR response
from mistralai.models import OCRResponse
from IPython.display import Markdown, display


def replace_images_in_markdown(markdown_str: str, images_dict: dict) -> str:
    """
    Replace image placeholders in markdown with base64-encoded images.

    Args:
        markdown_str: Markdown text containing image placeholders
        images_dict: Dictionary mapping image IDs to base64 strings

    Returns:
        Markdown text with images replaced by base64 data
    """
    for img_name, base64_str in images_dict.items():
        markdown_str = markdown_str.replace(
            f"![{img_name}]({img_name})", f"![{img_name}]({base64_str})"
        )
    return markdown_str


def get_combined_markdown(ocr_response: OCRResponse) -> str:
    """
    Combine OCR text and images into a single markdown document.
    Images are saved to the 'images' directory.

    Args:
        ocr_response: Response from OCR processing containing text and images

    Returns:
        Combined markdown string with embedded images
    """
    markdowns: list[str] = []
    images_dir = Path("images")
    images_dir.mkdir(parents=True, exist_ok=True)

    # Extract images from page
    for page in ocr_response.pages:
        image_data = {}
        for img in page.images:
            # Decode and save image
            try:
                img_b64 = img.image_base64
                if "," in img_b64:
                    img_b64 = img_b64.split(",", 1)[1]
                
                image_bytes = base64.b64decode(img_b64)
                # Use .jpg as default extension since actual format isn't strictly provided but usually compatible
                image_filename = f"{img.id}.jpg"
                image_path = images_dir / image_filename
                image_path.write_bytes(image_bytes)
                
                # Replace placeholder with path to the file
                image_data[img.id] = f"images/{image_filename}"
            except Exception as e:
                print(f"Failed to process image {img.id}: {e}")
                
        # Replace image placeholders with actual image paths
        markdowns.append(replace_images_in_markdown(page.markdown, image_data))

    return "\n\n".join(markdowns)

# Save combined markdowns and images to a file
markdown_content = get_combined_markdown(pdf_response)
output_file = Path("output.md")
output_file.write_text(markdown_content)
print(f"Markdown content saved to {output_file}")