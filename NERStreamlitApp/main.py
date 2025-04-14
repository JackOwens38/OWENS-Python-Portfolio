# Import the systems we will need to use
import streamlit as st
import pandas as pd
import spacy
from spacy import displacy

# Streamlit page setup
st.title("Named Entity Recognition App")
st.write("This app allows you to use a Named Entity Recognition system with custom text and labels. Explore the tools below to get started!")

# Sets up text area for user to upload their text
text = st.text_area("Enter your text here:")

# Example texts that give examples of different types of entities that spaCy will recognize
st.subheader("Example texts:")
st.markdown("""
- The quick brown fox jumped over the lazy dwarf.
- Nick Foles threw a touchdown pass to Zach Ertz in Super Bowl LII as the Philadelphia Eagles defeated Tom Brady and the New England Patriots.
- Bruce Springsteen won the Grammy Award for Song of the Year in 1995 with "Streets of Philadelphia". In 2016, he was also awarded the Presidential Medal of Freedom.            
""") # Using "-" makes it bullet point format in streamlit

st.header("Add a custom entity here: ")

left, right = st.columns(2) # This creates two columns for input boxes, which is more appealing and organized visually
with left:
    words = text.split() # Creates list of all words within the user text
    label = st.text_input("Label")
with right:
    pattern = st.multiselect("Select the words in the pattern", options=words) # Allows them to pick a single word, or a stretch of words, to recognize as entities
    pattern = [{"TEXT": word} for word in pattern] # for loop trick from class

if "entity_list" not in st.session_state: # This initializes the list in the whole system, because it kept resetting the list when it was initialized normally
    st.session_state["entity_list"] = []

if st.button("Add custom entity"): # By clicking this button, the entities that the user inputs above are actually added to the list of entities
    st.session_state["entity_list"].append({"label":label, "pattern":pattern})
    # Displays all of the saved custom entities in an organized way
    st.write("Here are all saved entities:")
    display_dict = []
    for entity in st.session_state["entity_list"]:
        display_dict.append({
            "Label": entity["label"],
            "Pattern": " ".join([token["TEXT"] for token in entity["pattern"]])
        })
    df = pd.DataFrame(display_dict)
    st.dataframe(df)

st.header("Entity Recognition")

nlp = spacy.load('en_core_web_sm') # Loads the nlp

# Adds the custom entities to the nlp
if "ner" in nlp.pipe_names:
    # If entity_ruler already exists, simply add patterns to it.
    try:
        ruler = nlp.get_pipe("entity_ruler")
    except Exception:
        ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(st.session_state["entity_list"])
else:
    # If the NER component does not exist, add both the EntityRuler and the NER component.
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(st.session_state["entity_list"])
    ner = nlp.add_pipe("ner")

# Runs the custom text through the NER system and displays the results
doc=nlp(text)
show=displacy.render(doc, style="ent", jupyter=False)
st.markdown(show, unsafe_allow_html=True)