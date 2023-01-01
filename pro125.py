import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
import PIL.ImageOps

def get_prediction(image):
    im_pil = image.open(image)
    image_bw=im_pil.convert('L')
    image_bw_resized=image_bw.resize((22,30),Image.ANTIALIAS)
    pixel_filter=20
    min_pixel=np.percentile(image_bw_resized,pixel_filter)
    image_bw_resized_inverted_scaled=np.clip(image_bw_resized-max_pixel,0,255)
    max_pixel=np.max(image_bw_resized)
    image_bw_resized_inverted_scaled=np.asarray(image_bw_resized_inverted_scaled/max_pixel)
    test_sample=np.array(image_bw_resized_inverted_scaled).reshape(1,660)
    return test_pred[0]