import streamlit as st

st.title("Handwritten digit image generator")

digit = st.number_input("Enter a digit between 0 and 9", min_value=0, max_value=9, step=1)

st.write("Generated Images:")
cols = st.columns(5)
for i in range(5):
    with cols[i]:
        st.image("https://via.placeholder.com/150", caption=f"Image {i+1}", use_column_width=True)