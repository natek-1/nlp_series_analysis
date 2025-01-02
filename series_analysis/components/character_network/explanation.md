# Character Network Analysis Using Episode Subtitles

## Overview
This project aims to perform character network analysis using episode subtitle data. The analysis identifies relationships between characters based on their co-occurrences within the subtitle text. By building a graph that represents these relationships, we can visualize and understand the interactions among characters.

---

## Steps

### 1. Extract Sentences
- Using the dataset containing episode subtitles, extract individual sentences.
- Each sentence is treated as a unit of analysis.

### 2. Identify Named Entities
- For each sentence, identify the names of characters (Named Entities) mentioned.
- Use a Named Entity Recognition (NER) tool or a predefined list of character names to identify these entities.
- Create a **list of lists** where each inner list contains the names of characters mentioned in a single sentence.

### 3. Count Co-occurrences Within a Sliding Window
- To determine relationships, count how often two characters are mentioned within 10 consecutive sentences.
- Use a sliding window approach to ensure that the context remains local.
  - For instance, if "Naruto" appears in sentence 1 and "Sasuke" in sentence 8, they will be counted as co-occurring.

### 4. Generate a Co-occurrence Matrix
- For each pair of characters, calculate the total number of co-occurrences across all windows in the dataset.
- Store these counts in a matrix or dictionary structure.

### 5. Create the Graph
- Using the co-occurrence data, create a graph where:
  - Each node represents a character.
  - Each edge represents a relationship between two characters.
  - The edge weight corresponds to the co-occurrence count.
- Use a graph visualization library (e.g., NetworkX, Gephi) to display the network.
  - Nodes with more connections appear larger, and heavily weighted edges are more prominent.

---

## Visual Workflow

1. **Extract Sentences:** Subtitle text split into individual sentences.
2. **Named Entities:** Characters mentioned in each sentence are identified.
3. **Co-occurrence Counting:** Number of times characters appear together within 10 sentences.
4. **Graph Representation:** Final graph visualization of character relationships.

---

## Output
The output of this analysis is a character network graph that visualizes interactions and relationships between characters. It provides insights into:
- The most connected characters.
- Clusters of characters often mentioned together.
- Key relationships in the storyline.

---

## Tools and Libraries
- **Python** for data processing and analysis.
- **Named Entity Recognition (NER):** SpaCy.
- **Graph Visualization:** Network.
- **Subtitle Parsing:** Pandas.

---

## Future Work
- Extend the analysis to include sentiment associated with each interaction.
- Incorporate temporal dynamics to observe how relationships evolve across episodes or seasons.
- Add filtering options to focus on specific characters or groups.

