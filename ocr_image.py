import os
import json
import base64
from pathlib import Path
from dotenv import load_dotenv
from mistralai import Mistral, ImageURLChunk, TextChunk

# Load environment variables
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

def main():
    # Verify image exists
    image_file = Path("receipt.png")
    if not image_file.exists():
        print(f"Error: File {image_file} not found.")
        return

    # Encode image as base64 for API
    print(f"Processing {image_file}...")
    encoded = base64.b64encode(image_file.read_bytes()).decode()
    base64_data_url = f"data:image/jpeg;base64,{encoded}"

    # Process image with OCR
    image_response = client.ocr.process(
        document=ImageURLChunk(image_url=base64_data_url),
        model="mistral-ocr-latest"
    )

    # Extract structured data from OCR results of image
    # Get OCR results for processing
    image_ocr_markdown = image_response.pages[0].markdown

    # Get structured response from model
    print("Extracting structured data...")
    chat_response = client.chat.complete(
        model="pixtral-12b-latest",
        messages=[
            {
                "role": "user",
                "content": [
                    ImageURLChunk(image_url=base64_data_url),
                    TextChunk(
                        text=(
                            f"This is image's OCR in markdown:\n\n{image_ocr_markdown}\n.\n"
                            "Convert this into a sensible structured json response. "
                            "The output should be strictly be json with no extra commentary"
                        )
                    ),
                ],
            }
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )

    # Parse and return JSON response
    response_dict = json.loads(chat_response.choices[0].message.content)
    print(json.dumps(response_dict, indent=4))

if __name__ == "__main__":
    main()
