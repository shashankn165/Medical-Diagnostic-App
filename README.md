# Medical Diagnostic App

A Medical Diagnostic App that leverages Google Gemini Vision Pro API to analyze medical images such as X-rays, CT scans, and patient symptoms, providing preliminary diagnostic insights.

**Note:** This tool is for informational purposes only and should not replace professional medical advice. Always consult a healthcare provider for a conclusive diagnosis.

## Features

- Upload medical images (X-rays, CT scans, MRIs)
- Analyze images and provide diagnostic insights
- Text input for patient symptoms or additional context
- Emphasis on the need for professional medical consultation

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Medical-Diagnostic-App.git
    cd Medical-Diagnostic-App
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory of the project
    - Add your Google API key to the `.env` file:
      ```plaintext
      GOOGLE_API_KEY=your_google_api_key_here
      ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py

