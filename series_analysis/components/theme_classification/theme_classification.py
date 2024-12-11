import os
import sys
import pathlib 

import pandas as pd
import numpy as np
import nltk
import torch

from transformers import pipeline
from nltk.tokenize import sent_tokenize

from series_analysis.utils.main_utils import load_subtitles_dataset
class ThemeClassifier():
    
    def __init__(self, theme_list, model_name="facebook/bart-large-mnli"):
        self.theme_list = theme_list
        self._model_name = model_name
        self._device =  "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        self._classifier = self._load_model()
        
    def _load_model(self):
        theme_classifier = pipeline(
        task="zero-shot-classification",
        model=self._model_name,
        device=self._device
        )
        return theme_classifier

    
    def get_themes_inference(self, script, batch_size=32):
        script_sentences = sent_tokenize(script)
        # create batces of sentences
        sentence_batch = 32
        script_batches = []
        for index in range(0, len(script_sentences), sentence_batch):
            sent = ""
            if index+sentence_batch <= len(script_sentences): 
                sent = " ".join(script_sentences[index:index+sentence_batch])
            else:
                sent = " ".join(script_sentences[index:]) # take last element in the batch
            script_batches.append(sent)
        
        # run the model    
        theme_output = self._classifier(
        script_batches,
        self.theme_list,
        multi_label=True
        )   
        
        themes_probs = {}
        for output in theme_output:
            for label,score in zip(output['labels'], output["scores"]):
                themes_probs[label] = [score] + themes_probs.get(label, [])
        themes_prob = {key: np.mean(np.array(value)) for key,value in themes_probs.items()}
        
        return themes_prob
    
    
    def get_themes(self, dataset_path, save_path=None):
        
        if save_path is not None and os.path.exists(save_path):
            df = pd.read_csv(save_path)
            return df
        
        df = load_subtitles_dataset(dataset_path=dataset_path)
        
        output_themes = df['script'].apply(self.get_themes_inference)
        themes_df = pd.DataFrame(output_themes.tolist())
        
        df[themes_df.column] = themes_df
        
        if save_path is not None:
            df.to_csv(save_path, index=False)
        return df            