import gdown
import os

def download_model():
    """Download the trained model from Google Drive"""
    
    model_path = "face_emotionModel.h5"
    
    # Check if model already exists
    if os.path.exists(model_path):
        print(f"Model already exists at {model_path}")
        return True
    
    print("Model not found. Please download it manually:")
    print("1. Upload your face_emotionModel.h5 to Google Drive")
    print("2. Get the shareable link")
    print("3. Extract the FILE_ID from the link")
    print("4. Replace 'YOUR_FILE_ID' below with your actual file ID")
    print()
    
    # TODO: Replace with your actual Google Drive file ID
    file_id = "YOUR_FILE_ID_HERE"
    
    if file_id == "YOUR_FILE_ID_HERE":
        print("ERROR: Please set your Google Drive file ID first!")
        return False
    
    try:
        print("Downloading model from Google Drive...")
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, model_path, quiet=False)
        print("Model downloaded successfully!")
        return True
    except Exception as e:
        print(f"Error downloading model: {e}")
        print("\nAlternative: Download the model manually and place it in the root directory")
        return False

if __name__ == "__main__":
    download_model()
