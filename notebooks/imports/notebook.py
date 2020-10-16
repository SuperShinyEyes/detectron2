'''Useful modules for interactive coding on Jupyter Notebook'''
import matplotlib.pyplot as plt

# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.serif'] = 'Ubuntu'
# plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10  # Time and Hz, i.e. labels
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 15  # Time(x) tick values
plt.rcParams['ytick.labelsize'] = 15  # Hz(y) tick values
plt.rcParams['legend.fontsize'] = 17
plt.rcParams['figure.titlesize'] = 30
plt.rcParams['axes.titlesize'] = 30  # Title font

import cv2 as cv
import numpy as np
import pandas as pd
pd.options.display.max_columns = None

from typing import *


pd.options.display.max_colwidth = 100

def imshow(img: np.ndarray, figsize=(10, 10), is_img_read_using_opencv: bool = True, toggle_off_axis: bool = True) -> None:
    plt.figure(figsize=figsize)

    if is_img_read_using_opencv and img.ndim == 3 and img.dtype == np.uint8:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    elif is_img_read_using_opencv and img.ndim == 1  and img.dtype == np.uint8:
        img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
    elif is_img_read_using_opencv and img.dtype == np.float32:
        img[:,:,0], img[:,:,1] = img[:,:,1], img[:,:,0] 
    plt.imshow(img)
    if toggle_off_axis:
        plt.axis('off')


def pretty_print_dict(d: Dict, tabs: str = "") -> None:
    """Print a dictionary exhaustively with as many tabs as its level/depth.

    A child dictionary should have one more tab than its parent.
    """
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"{tabs}{k}:")
            pretty_print_dict(v, f"\t{tabs}")
        else:
            print(f"{tabs}{k}:{v}")


def plot_images_horizontally(images: List[np.ndarray], title: str = '', figsize: Tuple[int] = (15, 17)) -> None:
    """Plot multiple images in one row, i.e. horizontally"""
    n_images = len(images)
    fig, axarr = plt.subplots(1, n_images, figsize=figsize)
    fig.suptitle(title, fontsize=26)

    color = ('b','g','r')
    for i, img in enumerate(images):
        axarr[i].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        axarr[i].axis('off')

    # Tight layout often produces nice results
    # but requires the title to be spaced accordingly
    fig.tight_layout()
    fig.subplots_adjust(top=0.92)


