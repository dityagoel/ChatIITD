import streamlit as st

# Example user message
with st.chat_message("user"):
    st.markdown("Hello, bot!")

# Example bot message
with st.chat_message("assistant"):
    st.markdown("Hello, human! How can I help you?")
