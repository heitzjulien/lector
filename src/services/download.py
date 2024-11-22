import gdown


def download_from_gdrive(url, output=None):
    """Download the PDF document in Google Drive."""
    try:
        file_id = url.split('/d/')[1].split('/')[0]
        direct_url = f'https://drive.google.com/uc?id={file_id}'

        downloaded_file = gdown.download(direct_url, output, quiet=False)
        return downloaded_file

    except Exception as e:
        print(f"Error while downloading: {str(e)}")
        return None
