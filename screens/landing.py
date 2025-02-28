import streamlit as st

from utils.page_utils import PageType


def show_landing_page():
    st.image("images/feature_image.webp", caption="Powered by Hadron Individualized AI", use_container_width=True)
    st.write("")

    st.write("### Key Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/feature1_icon.png", width=80)
        st.write("**Intelligent Matching**")
        st.write("Our AI analyzes your preferences to match you with the perfect table.")

    with col2:
        st.image("images/feature2_icon.png", width=80)
        st.write("**Seamless Integration**")
        st.write("Easily integrate our solution into your existing infrastructure.")

    with col3:
        st.image("images/feature3_icon.png", width=80)
        st.write("**Real-Time Analytics**")
        st.write("Monitor user engagement and optimize experiences with real-time data.")

    st.write("")
    st.write("")

    if st.button("Start Now", type='primary', icon=':material/chevron_right:'):
        st.session_state.page = PageType.SIGN_IN
        st.session_state.current_user = None
        st.rerun()
