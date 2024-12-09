import pandas as pd
import numpy as np
import torch
from transformers import pipeline
import nltk
from nltk import sent_tokenize
from glob import glob
import pathlib

nltk.download('punkt')
nltk.download('punkt_tab')



