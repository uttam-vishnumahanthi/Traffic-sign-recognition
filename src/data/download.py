import os
import kaggle
import zipfile
from tqdm import tqdm
import pandas as pd
import numpy as np

def download_gtsrb(data_dir='data/raw'):
    """Download GTSRB dataset from Kaggle"""
    os.makedirs(data_dir, exist_ok=True)
    
    # Download dataset
    print("Downloading GTSRB dataset...")
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(
        'meowmeowmeowmeowmeow/gtsrb-german-traffic-sign',
        path=data_dir,
        unzip=True
    )
    print("Download complete!")

def load_meta_data(data_dir='data/raw'):
    """Load meta information about classes"""
    # Class names (simplified - you can expand this)
    class_names = {
        0: 'Speed limit 20 km/h',
        1: 'Speed limit 30 km/h', 
        2: 'Speed limit 50 km/h',
        3: 'Speed limit 60 km/h',
        4: 'Speed limit 70 km/h',
        5: 'Speed limit 80 km/h',
        6: 'End of speed limit 80 km/h',
        7: 'Speed limit 100 km/h',
        8: 'Speed limit 120 km/h',
        9: 'No passing',
        10: 'No passing for trucks',
        11: 'Right-of-way at next intersection',
        12: 'Priority road',
        13: 'Yield',
        14: 'Stop',
        15: 'No vehicles',
        16: 'Vehicles over 3.5 tons prohibited',
        17: 'No entry',
        18: 'General caution',
        19: 'Dangerous curve left',
        20: 'Dangerous curve right',
        21: 'Double curve',
        22: 'Bumpy road',
        23: 'Slippery road',
        24: 'Road narrows on right',
        25: 'Road work',
        26: 'Traffic signals',
        27: 'Pedestrians',
        28: 'Children crossing',
        29: 'Bicycles crossing',
        30: 'Beware of ice/snow',
        31: 'Wild animals crossing',
        32: 'End of all speed and passing limits',
        33: 'Turn right ahead',
        34: 'Turn left ahead',
        35: 'Ahead only',
        36: 'Go straight or right',
        37: 'Go straight or left',
        38: 'Keep right',
        39: 'Keep left',
        40: 'Roundabout mandatory',
        41: 'End of no passing',
        42: 'End of no passing by trucks'
    }
    return class_names

if __name__ == "__main__":
    download_gtsrb()