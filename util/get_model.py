import urllib.request
import os
import sys

url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt"
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "data")
os.mkdir(os.path.join(data_path, "model"))
urllib.request.urlretrieve(url, os.path.join(data_path, "model/yolov8s.pt"))
