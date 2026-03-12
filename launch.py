import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import rdf_utils

st.title("Graph Visualizer")

friend_input = st.text_area(
    "Enter your hero:", 
    "Infernus"
)
enemy_input = st.text_area(
    "Enter enemy hero:", 
    "Wraith"
)
state_input = st.text_area(
    "Game state:", 
    "isAhead"
)
stage_input = st.text_area(
    "Game stage:", 
    "EarlyGame"
)

item_name, f_name, e_name = "", "", ""

if st.button("search for item"):
    g_test = rdf_utils.obtain_semantic_g()
    #gets item
    q_res = rdf_utils.obtain_items(friend_input, enemy_input, state_input, stage_input, g_test)

    for row in q_res:
        item_name = row.item.split('/')[-1]

#display result item
item_output = st.text_area(
    "Your item:",
    f"got: {item_name} - for {friend_input} vs {enemy_input} during {stage_input} when {state_input}"
)