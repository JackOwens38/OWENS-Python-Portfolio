## Named Entity Recognition App
This app uses Streamlit and spaCy to conduct Named Entity Recognition (NER) for user-inputted text. spaCy is a Python library commonly used within Natural Language Processing (NLP) systems, and it is used here to identify entities within the uploaded text. Additionally, users can add custom entities for the system to recognize within their text.

## Project Overview
Nataural Language Processing is a way of analyzing texts through computer systems, and Named Entity Recognition is a piece of this process that identifies the entities within a chain of text. After uploading text, users can see a variety of entities that the spaCy system will recognize. Additionally, users can utilize the custom label and pattern feature that allows them to introduce the entities not already present in spaCy's system. The entities are color coded within a re-displayed version of the text, including the custom ones, which are analyzed automatically.

## Instructions
#### 1. Install the following libraries:
- Pandas
  - pip install pandas
- Streamlit
  - pip install streamlit
- spaCy
  - pip install spacy
  - python -m spacy download en_core_web_sm
#### 2. Input custom text into the text box
#### 3. (Optional) Add custom entities
- Use the "label" and "pattern" fields
#### 4. View the analysis of the Entity Recognition Tool

## App Features
- Custom text upload area
- Custom entity area
- Auto-updated list of all saved entities
- Color-coded analysis of all recognized entities

## Visual Example
<img width="502" alt="Screenshot 2025-04-14 at 7 15 21 PM" src="https://github.com/user-attachments/assets/7d22c56a-45d0-4532-b3d0-39c61ef62617" />

## References
- [Streamlit documentation](https://docs.streamlit.io/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [spaCy documenation](https://spacy.io/usage)
- [spaCy Entity Ruler](https://spacy.io/api/entityruler)
- [Stack Overflow](https://stackoverflow.com/questions)
