from glob import glob 
import pandas as pd

def load_subtitles_dataset(dataset_path="../../data/subtitles/"):
    subtitles_data = glob(dataset_path+"/*.ass")
    
    scripts = []
    
    for path in subtitles_data:
        
        # read file
        with open(path, "r") as file:
            lines = file.readlines()
        
        lines = lines[27:] # remove first useless lines
        lines = [line.split(",")[9:] for line in lines] # remove non script features
        # make required adjustments to line
        lines = ["".join(line) for line in lines]
        lines = [line.replace('\\N', '') for line in lines]
        script = " ".join(lines)
        scripts.append(script)
    script = script[:5]
    df = pd.DataFrame.from_dict({"script": scripts})
    return df