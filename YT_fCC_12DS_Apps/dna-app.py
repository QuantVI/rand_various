# https://www.youtube.com/watch?v=JwSS70SZdyM

####
# Import libraries
####
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import dnaseq
####
# Page Title
####
image = Image.open("dna-logo.jpg")
st.image(image, use_column_width=True)
st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide compisition of a query DNA!

***
""")
####
# Input Text Box
####
# st.sidebar.header("Enter DNA sequence")
st.header("Enter DNA sequence")

sequence_input = ">DNA Query\n" + dnaseq.query1
sequence = st.text_area("Seuqnce input", sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = "".join(sequence) # Concatenates list to string

st.write("""***""")
## Prints the input DNA Sequence
st.header("INPUT (DNA Query)")
sequence

## DNA nucleotitde count
st.header("OUTPUT (DNA Nucleotide Count)")

# 1. Print dictionary
st.subheader("1. Print dictionary")
def DNA_nucleotide_count(seq):
    d = dict([("A", seq.count("A")), ("T", seq.count("T")),
              ("G", seq.count("G")), ("C", seq.count("C"))])
    return d

X = DNA_nucleotide_count(sequence)
X

# 2. Print text
tide_type = {"A":"adenine (A)","T":"thymine (T)",
             "G":"guanine (G)", "C":"cytosine (C)"}
sent_01 = "There are {0} {1}"
st.subheader("2. Print text")
for k in tide_type:
    st.write(sent_01.format(X[k],tide_type[k]))

# 3. Display DataFramce
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0:"Count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns = {"index":"nucleotide"})
st.write(df)

# 4. Display Bar Chart usinf Altair
st.subheader("4. Display Bar chart")
p = alt.Chart(df).mark_bar().encode(x="nucleotide",y="Count")
p = p.properties(width=alt.Step(80)) # controls width of the bar.
st.write(p)

