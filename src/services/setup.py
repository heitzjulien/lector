from services import download_from_gdrive, convert_pdf_to_text
from utils import FILE_NAME


def setup_pdf():
    """Initialize PDF document"""
    print("Downloading file...")
    url = 'https://drive.google.com/file/d/1CPKZqVCpSgxU-h9cdbDvo-x75xViOj5V/view?usp=sharing'
    downloaded_file = download_from_gdrive(url, FILE_NAME)
    print(f"File downloaded: {downloaded_file}")

    print("Converting PDF to text...")
    convert_pdf_to_text()
    print("Conversion successful")
