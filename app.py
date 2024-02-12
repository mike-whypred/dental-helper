import streamlit as st
import streamlit.components.v1 as components

# Custom CSS to change the background of the entire app, title color, and alignment
custom_css = """
<style>
    /* Change the background of the entire app */
    .stApp {
        background-color: black;
    }

    /* Additional styles for custom title alignment and color */
    .title {
        color: white;
        text-align: right;
    }

    /* Style for the right-aligned button */
    .right-aligned-button {
        display: flex;
        justify-content: flex-end;
        margin-top: 20px;
    }

    .right-aligned-button a {
        text-decoration: none;
    }

    button {
        color: white;
        background-color: blue;
        padding: 10px 24px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: darkblue;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Custom HTML for the right-aligned title
st.markdown('<h1 class="title">Dental Helper</h1>', unsafe_allow_html=True)

# The target URL you want to embed
target_url = 'https://widget-prototype.web.app/?id=S55hKcH2nJgTuSZ2hYhc'

# Custom HTML to adjust the iframe position and ensure it fits within the black background theme
adjusted_iframe_html = f"""
<div style="margin-left: -100px; background-color: black;">
    <iframe src="{target_url}" width="800" height="900" style="border:0; display:block;"></iframe>
</div>
"""

# Use the html method to render the adjusted iframe
components.html(adjusted_iframe_html, height=900)

# HTML for the right-aligned button that links to the external site
button_html = """
<div class="right-aligned-button">
    <a href="https://portal.ada.org.au/Portal/Shared_Content/Smart-Suite/Smart-Maps/Public/Find-a-Dentist.aspx" target="_blank">
        <button>Talk to a Dentist</button>
    </a>
</div>
"""

st.markdown(button_html, unsafe_allow_html=True)
