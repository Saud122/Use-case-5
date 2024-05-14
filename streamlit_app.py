import streamlit as st


st.text("Welcome to My Streamlit website. Hope you like it!")

# Markdown text
st.markdown("""
    ## Topic: Jadarat

    <span style='color:black; font-weight:bold;'>
    Jadarat.sa is a platform dedicated to fostering growth, development, 
    and empowerment. their mission is to equip individuals, organizations, 
    and communities with the skills, knowledge, and resources needed to thrive in today's dynamic world.
    </span>.



""", unsafe_allow_html=True)

st.markdown("""
    <span style='color:black; font-weight:bold;'>
    Q1)  What proportion of job postings is attributed to each region within the kingdom? </span>.
""", unsafe_allow_html=True)

# Display an image from a local file
st.image('image-1.png', caption='image-1.png', use_column_width=True)

