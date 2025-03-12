import os

cache_path = r"C:\Users\Administrator\Documents\InvToStr_YOLO\dataset\labels\train.cache"
if os.path.exists(cache_path):
    os.remove(cache_path)
    print("Deleted cache file. Re-run training.")

