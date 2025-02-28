import os
os.environ["STREAMLIT_THEME_PRIMARY_COLOR"] = "#e2b760"
os.environ["STREAMLIT_THEME_BACKGROUND_COLOR"] = "#FFFFFF"
os.environ["STREAMLIT_THEME_SECONDARY_BACKGROUND_COLOR"] = "#f8e8d0"
os.environ["STREAMLIT_THEME_TEXT_COLOR"] = "#31333F"
os.environ["STREAMLIT_THEME_FONT"] = "sans serif"
os.environ["STREAMLIT_THEME_BASE"] = "light"

import streamlit as st
import ssl
import json
from ssl import _create_unverified_context

from models.user import *
from screens.authentication import show_registration_page
from screens.dashboard import show_dashboard
from screens.landing import show_landing_page
from utils.page_utils import PageType

ssl._create_default_https_context = _create_unverified_context


def hide_app_bar_menu_buttons():
    st.html(
        """<style>
            #MainMenu {visibility: hidden;}
            .stAppDeployButton {visibility: hidden;}
        </style>""")


def load_users(filename):
    with open(filename, 'r') as f:
        users_data = json.load(f)

    users: list[User] = []
    for user_dict in users_data:
        identity = Identity(**user_dict["identity"])
        personality = Personality(**user_dict["personality"])
        events_pref = [EventPreference(**pref) for pref in user_dict.get("events_pref", [])]

        # Create the User instance
        user = User(
            name=user_dict["name"],
            username=user_dict["username"],
            password=user_dict["password"],
            location=user_dict["location"],
            identity=identity,
            personality=personality,
            events_pref=events_pref,
            events_attended=user_dict.get("events_attended", [])
        )
        users.append(user)

    return users


def init_session_states():
    if 'page' not in st.session_state:
        st.session_state.page = PageType.LANDING
    if 'users' not in st.session_state:
        st.session_state.users = load_users('users.json')
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'recommended_people' not in st.session_state:
        st.session_state.recommended_people = []
    if 'recommended_table' not in st.session_state:
        st.session_state.recommended_table = []


def start_app():
    init_session_states()

    if st.session_state.page == PageType.LANDING:
        show_landing_page()
    elif st.session_state.page == PageType.SIGN_IN:
        show_registration_page(PageType.SIGN_IN)
    elif st.session_state.page == PageType.SIGN_UP_1:
        show_registration_page(PageType.SIGN_UP_1)
    elif st.session_state.page == PageType.SIGN_UP_2:
        show_registration_page(PageType.SIGN_UP_2)
    elif st.session_state.page == PageType.SIGN_UP_3:
        show_registration_page(PageType.SIGN_UP_3)
    elif st.session_state.page == PageType.DASHBOARD:
        show_dashboard()


if __name__ == '__main__':
    st.set_page_config(
        page_title="HighTable",
        page_icon="images/logo.png",
        # layout="wide"
    )
    hide_app_bar_menu_buttons()
    st.logo("images/logo.svg", icon_image='images/logo_1.png')

    start_app()
