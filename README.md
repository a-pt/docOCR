# Document OCR with Mistral AI

This project demonstrates how to perform Optical Character Recognition (OCR) on documents using the Mistral AI API. It includes tools for processing both PDFs and individual images.

## Features

- **PDF Processing (`ocr_pdf.py`)**:
    - Converts PDF documents into formatted Markdown text.
    - Extracts embedded images from the PDF and saves them locally.
    - Replaces image placeholders in the OCR output with links to the locally saved image files.
- **Image Processing (`ocr_image.py`)**:
    - Performs OCR on single images (e.g., receipts).
    - Uses Mistral's `pixtral-12b-latest` to extract structured data (JSON) from the image content.
    - Ideal for automating data entry from receipts, invoices, etc.

## Prerequisites

- Python 3.8+
- A Mistral AI API Key. You can obtain one from the [Mistral AI Console](https://console.mistral.ai/).

## Setup

1.  **Clone the repository** (if applicable) or download the source code.

2.  **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    # .venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**

    Create a `.env` file in the root directory and add your Mistral API key:

    ```env
    MISTRAL_API_KEY=your_actual_api_key_here
    ```

## Usage

### 1. Process a PDF (`ocr_pdf.py`)

This script converts a PDF into a Markdown file with extracted images.

1.  Place your PDF file in the project directory (default is `mst.pdf`).
2.  Run the script:
    ```bash
    python ocr_pdf.py
    ```
3.  **Output**:
    - `output.md`: The full content of the PDF in Markdown.
    - `images/`: Directory containing all extracted images.

### 2. Process an Image (`ocr_image.py`)

This script extracts structured JSON data from a single image.

1.  Place your image file in the project directory (default is `receipt.png`).
2.  Run the script:
    ```bash
    python ocr_image.py
    ```
3.  **Output**:
    - Prints the structured JSON data extracted from the image to the console.

## Project Structure

-   `ocr_pdf.py`: Script for processing PDFs to Markdown.
-   `ocr_image.py`: Script for processing images to structured JSON.
-   `requirements.txt`: Python package dependencies.
-   `.env`: Configuration file for API keys.
-   `images/`: Directory where extracted images are saved.
-   `output.md`: The resulting Markdown file from PDF processing.
