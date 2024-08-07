import glob
import os
from typing import List

try:
    from src.config import FILEEXTENSIONS
except:
    from config import FILEEXTENSIONS

class ImagesFinder:
    def __init__(self, path: str) -> None:
        """
            Initialize the ImagesFinder with a directory path and find all images.

            Args:
                path (str): The directory path to search for images.
        """
        self.path = path
        self.all_images: List[str] = []
        extensions = FILEEXTENSIONS
        
        for ext in extensions:
            self.all_images.extend(glob.glob(os.path.join(self.path, ext)))

    def get_images(self) -> List[str]:
        """
            Get the list of all found image paths.

            Returns:
                List[str]: A list of paths to all found images.
        """
        return self.all_images