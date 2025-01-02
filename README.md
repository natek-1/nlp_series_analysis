# Anime Series NLP Analysis with LLMs

In this project, we analyze an anime series using cutting-edge NLP techniques and large language models (LLMs). We scrape our own dataset, use zero-shot classifiers, train a custom text classifier, build a character network using Named Entity Recognition (NER), and create a chatbot to chat with your favorite characters. Finally, everything is integrated into a web GUI using Gradio. This project will take your NLP skills to the next level, providing valuable hands-on experience with tools and techniques used in the industry.

## Overview

This project is structured into five main components, each with its own folder:

- **`crawler`**: Contains the code for scraping the web to build a comprehensive dataset about the anime using [Scrapy](https://scrapy.org/).
  
- **`character_network`**: Creates an intricate character network using [spaCy](https://spacy.io/)'s Named Entity Recognition (NER) model, [NetworkX](https://networkx.github.io/), and [PyViz](https://pyviz.org/).
  
- **`text_classifier`**: Trains a custom LLM-based text classifier to categorize text into multiple classes, building a personalized NLP model.

- **`theme_classifier`**: Extracts the main themes of the series using zero-shot classifiers powered by pre-trained LLMs.
  
- **`character_chat_bot`**: Builds a chatbot using LLMs, allowing users to chat with their favorite characters from the series in an interactive format.

Finally, the entire project is integrated into a simple, user-friendly web interface using [Gradio](https://gradio.app/).

## Skills You'll Learn
- Web scraping with Scrapy
- NLP tasks with spaCy (NER), text classification, and theme extraction
- Building custom LLM-based classifiers
- Creating interactive chatbots with LLMs
- Visualizing networks with NetworkX and PyViz
- Developing web applications using Gradio

## Installation

Before running the code, make sure you have all the necessary dependencies installed. You can do this by running:

```bash
conda create -y -n series_analysis python=3.9
conda activate series_analysis
pip install -r requirements.txt
```

## Download the data set

The project was run using the following dataset
* [Naruto Subtitle's](https://subtitlist.com/subs/naruto-season-1/english/2206507)
* [Naruto Transcripts](https://www.kaggle.com/datasets/leonzatrax/naruto-ep-1-transcript)
* [Classification DataSet](https://naruto.fandom.com/wiki/Special:BrowseData/Jutsu?limit=250&offset=0&_cat=Jutsu)

## Project Structure

```
├── crawler
│   ├── technique_crawler.py
├── character_network
│   ├── ner_model.py
│   ├── network_analysis.py
│   └── visualization.py
├── text_classifier
│   ├── train_classifier.py
│   └── model_inference.py
├── theme_classifier
│   ├── zero_shot_classifier.py
├── character_chat_bot
│   ├── chatbot.py
│   └── ...
├── app.py
├── requirements.txt
└── README.md
```

## Running the Project

Once all dependencies are installed, follow these steps:

1. **Data Scraping**: Start by scraping the necessary data using the `crawler` folder. Navigate to the folder and run the scraper:
    ```bash
    scrapy runspider crawler/technique_crawler.py -o data/justu.jsonl
    ```


2. **Theme Extraction**: Classify the main themes of the series using the zero-shot classifier in the `theme_classifier` folder:
    ```bash
    python -c "import nltk; nltk.download('punkt')"
    python theme_classifier/zero_shot_classifier.py
    ```


3. **Building the Character Network**: Use the `character_network` folder to analyze the relationships between characters. Simply run:
This uses a the dataset related to the episode subtitiles,
Step 1:



    ```bash
    python character_network/ner_model.py
    ```

4. **Training the Text Classifier**: Train the text classifier in the `text_classifier` folder by running:
    ```bash
    python text_classifier/train_classifier.py
    ```

5. **Character Chatbot**: Finally, interact with the character chatbot by running:
    ```bash
    python character_chat_bot/chatbot.py
    ```

6. **Launch the Web App**: To bring it all together, launch the Gradio web interface:
    ```bash
    python app.py
    ```

## Conclusion

This NLP project is designed to help you build a complete pipeline for analyzing and interacting with an anime series, giving you hands-on experience with essential NLP techniques. Whether you're looking to advance your NLP skills or create an impressive project for your portfolio, this project will give you the experience you need!

