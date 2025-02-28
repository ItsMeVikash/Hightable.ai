import os

if __name__ == '__main__':
    os.environ["STREAMLIT_THEME_PRIMARY_COLOR"] = "#e2b760"
    os.environ["STREAMLIT_THEME_BACKGROUND_COLOR"] = "#FFFFFF"
    os.environ["STREAMLIT_THEME_SECONDARY_BACKGROUND_COLOR"] = "#f8e8d0"
    os.environ["STREAMLIT_THEME_TEXT_COLOR"] = "#31333F"
    os.environ["STREAMLIT_THEME_FONT"] = "sans serif"
    os.environ["STREAMLIT_THEME_BASE"] = "light"

    os.system('streamlit run main.py')
    # os.system('streamlit run main.py --server.address=0.0.0.0')