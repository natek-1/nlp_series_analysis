import os 
import sys
import pathlib

import spacy
import pandas as pd
from nltk.tokenize import sent_tokenize
from ast import literal_eval
from series_analysis.utils.main_utils import load_subtitles_dataset

class NamedEntityRecognizer:
    def __init__(self):
        self.model = NamedEntityRecognizer.load_model()

    @staticmethod
    def load_model():
        nlp = spacy.load("en_core_web_trf")
        return nlp

    def get_ners_inference(self,script):
        script_sentences = sent_tokenize(script)

        ner_output = []

        for sentence in script_sentences:
            doc = self.model(sentence)
            ners = set()
            for entity in doc.ents:
                if entity.label_ =="PERSON":
                    first_name = entity.text.split(" ")[0]
                    first_name = first_name.strip()
                    ners.add(first_name) 
            ner_output.append(ners)

        return ner_output

    def get_ners(self,dataset_path,save_path=None):
        if save_path is not None and os.path.exists(save_path): # we just want to load the already processed df
            df = pd.read_csv(save_path)
            # csv don't handle csv as column value well...
            df['ners'] = df['ners'].apply(lambda x: literal_eval(x) if isinstance(x,str) else x)
            return df

        # load dataset from the 
        df = load_subtitles_dataset(dataset_path)

        # Run Inference
        df['ners'] = df['script'].apply(self.get_ners_inference)

        if save_path is not None:
            df.to_csv(save_path,index=False)
        
        return df