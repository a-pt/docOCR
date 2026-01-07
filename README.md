# Document OCR with Mistral AI

This project demonstrates how to perform Optical Character Recognition (OCR) on PDF documents using the Mistral AI API. It processes a PDF file, extracts text and embedded images, and generates a clean Markdown representation of the content.

## Features

- **PDF to Markdown**: Converts PDF documents into formatted Markdown text.
- **Image Extraction**: Extracts embedded images from the PDF and saves them locally.
- **Smart Formatting**: Replaces image placeholders in the OCR output with links to the locally saved image files.
- **Mistral AI Integration**: Uses the powerful `mistral-ocr-latest` model for high-quality results.

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

1.  **Place your PDF file** in the project directory.
    *   By default, the script looks for `mst.pdf`. You can modify the `pdf_file` variable in `ocr_doc_image.py` to point to your specific file.

2.  **Run the script:**

    ```bash
    python ocr_doc_image.py
    ```

## Output

The script will generate the following artifacts:

-   **`output.md`**: The full content of the PDF in Markdown format.
-   **`images/`**: A directory containing all images extracted from the PDF.

You can view `output.md` in any Markdown viewer (e.g., VS Code, Obsidian, GitHub) to see the text and images rendered together.

## Project Structure

-   `ocr_doc_image.py`: Main script for processing the PDF.
-   `requirements.txt`: Python package dependencies.
-   `.env`: Configuration file for API keys (not committed to version control).
-   `images/`: Directory where extracted images are saved.
-   `output.md`: The resulting Markdown file.
