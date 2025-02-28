import streamlit as st
from models.user import User
import altair as alt
import pandas as pd


def show_person_detail(person_data: dict):
        profession = person_data["profession"].title()
        similarity = person_data["similarity"]

        st.caption(f"⚙️{profession}")
        st.progress(int(similarity), f"Fitment Index {int(similarity)}%")

        match_scores = person_data["match_scores"]
        df = pd.DataFrame(match_scores, columns=["Category", "Score"])
        chart = (
            alt.Chart(df)
            .mark_bar(color="#ff4b4b")
            .encode(
                x=alt.X("Score:Q", title="Score (%)", scale=alt.Scale(domain=[0, 100])),
                y=alt.Y("Category:N", sort="-x")
            )
        )
        st.altair_chart(chart, use_container_width=True)


def show_recommended_persons(recommended_peoples):
    for i in range(0, len(recommended_peoples), 2):
        row_people = recommended_peoples[i: i + 2]
        columns = st.columns(len(row_people))
        for j, person in enumerate(row_people):
            with columns[j]:
                with st.expander(label=str(person["name"]).title()):
                    show_person_detail(person)


def show_table_detail(table_data: dict):
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Date:** {table_data['slot_date']}")
        st.write(f"**Location:** {table_data['location'].title()}")
        st.write(f"**Languages:** {', '.join(table_data['languages']).title()}")
    with col2:
        st.write(f"**Group of:** {table_data['max_seats']}")
        st.write(f"**Budget:** ₹{table_data['event_cost']}")
        st.write(f"**Host:** {table_data['created_by']}")

    # Overall Fitment Score for the event
    overall_fitment = int(table_data['fitment_score'])
    st.progress(overall_fitment, f"Fitment Index:  {overall_fitment}%")

    # 2) PARTICIPANTS SECTION
    st.write("**Participants**")
    for participant in table_data["participants"]:
        st.write(participant['participant_name'])

        # Profession with a gear icon
        profession = participant["profession"].title()
        if len(profession) > 0:
            st.caption(f"⚙️ {profession}")

        # Calculate an approximate participant-level "similarity" or "fitment index"
        # by averaging the participant's match scores
        match_scores = participant["match_scores"]
        total_score = sum([score for _, score in match_scores])
        # Assuming each participant has 5 categories in match_scores:
        similarity = total_score / len(match_scores) if match_scores else 0

        # Display a progress bar for the participant's fitment index
        participant_fitment = int(similarity)
        st.progress(participant_fitment, f"Fitment Index: {participant_fitment}%")

        # 3) VISUALIZE MATCH SCORES USING ALTAIR
        df = pd.DataFrame(match_scores, columns=["Category", "Score"])
        chart = (
            alt.Chart(df)
            .mark_bar(color="#ff4b4b")
            .encode(
                x=alt.X("Score:Q", title="Score (%)", scale=alt.Scale(domain=[0, 100])),
                y=alt.Y("Category:N", sort="-x")  # Sort by highest to lowest
            )
            .properties(height=150)
        )
        st.altair_chart(chart, use_container_width=True)

        st.markdown("---")


def show_recommended_tables(recommended_tables):
    for i in range(0, len(recommended_tables), 2):
        row_table = recommended_tables[i: i + 2]
        columns = st.columns(len(row_table))
        for j, table in enumerate(row_table):
            with columns[j]:
                with st.expander(label=f"🍸{str(table['event_name'])}"):
                    show_table_detail(table)


def show_dashboard():
    current_user: User = st.session_state.current_user
    st.title(f"Welcome {current_user.name.split()[0].title()}!")

    recommended_peoples = st.session_state.recommended_people
    st.write("##### Individuals who vibe with your energy")
    show_recommended_persons(recommended_peoples)

    recommended_tables = st.session_state.recommended_table
    st.write("##### Tables that vibe with your energy")
    show_recommended_tables(recommended_tables)

