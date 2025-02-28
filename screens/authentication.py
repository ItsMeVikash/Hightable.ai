import streamlit as st
import datetime

from backend.recommendation import RecommenderSystem
from models.user import *
from utils.page_utils import PageType


def show_sign_in():
    st.header("👤 Sign In")
    username = st.text_input("Username", key="signin_username")
    password = st.text_input("Password", type="password", key="signin_password")

    st.write("")
    if st.button("Sign In", key="btn_signin", type='primary', use_container_width=True):
        with st.spinner("Processing..."):
            users: list[User] = st.session_state.users
            user = next((user for user in users if user.username == username), None)
            if user:
                if user.password == password:
                    st.toast(f"Welcome {user.name.title()}")
                    st.session_state.current_user = user
                    set_recommendation()
                    st.session_state.page = PageType.DASHBOARD
                    st.rerun()
                else:
                    st.error("Invalid Password!!")
            else:
                st.error("You are not registered!!")

    st.markdown("---")
    st.html("<p style='width: 100%; color: grey; text-align: center; padding:0;'>Not on Board?</p>")
    if st.button("Onboard Yourself", key="btn_onboard_now", type='tertiary', use_container_width=True):
        st.session_state.current_user = None
        st.session_state.page = PageType.SIGN_UP_1
        st.rerun()


def show_sign_up_1():
    st.header("🔐 Sign Up")
    st.caption("Please fill all the basic details")
    st.progress(33)
    name = st.text_input("Name", key="signup_name")
    username = st.text_input("Username", key="signup_username")
    password = st.text_input("Password", type="password", key="signup_password")
    location = st.selectbox("Location", options=EventPreference.PREFERRED_LOCATION, key="signup_location")
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"], key="signup_gender")
    dob = st.date_input("Date of Birth", min_value=datetime.date(1980, 1, 1), max_value=datetime.date.today(),
                        key="signup_dob")
    relationship_status = st.selectbox("Relationship Status", options=["Single", "Married", "Other"],
                                       key="signup_relationship_status")
    children = st.selectbox("Children", options=["No", "Yes"], index=0, key="signup_children")

    profession = st.text_input("Profession", value="Software Engineer", key="signup_profession")
    country = st.text_input("Country", value="India", key="signup_country")

    if st.button("Next", key="btn_signup_1_next", type='primary', use_container_width=True):
        with st.spinner("Processing..."):
            if not name:
                st.error("Name is required.")
                return
            if not username:
                st.error("Username is required.")
                return
            if not password:
                st.error("Password is required.")
                return
            if not location:
                st.error("Location is required.")
                return
            if not gender:
                st.error("Gender is required.")
                return
            if not relationship_status:
                st.error("Relationship status is required.")
                return
            if not children:
                st.error("Children field is required.")
                return
            if not profession:
                st.error("Profession is required.")
                return
            if not country:
                st.error("Country is required.")
                return

            new_user = User(
                name=name,
                username=username,
                password=password,
                location=location,
                identity=Identity(
                    gender=gender,
                    dob=dob.strftime("%d/%m/%Y"),
                    relationship_status=relationship_status,
                    children=children,
                    profession=profession,
                    country=country
                ),
                personality=None,
                events_pref=[],
                events_attended=[]
            )
            users: list[User] = st.session_state.users
            user = next((user for user in users if user.username == username), None)
            if user:
                st.error("Username is already registered")
            else:
                st.session_state.current_user = new_user
                st.session_state.page = PageType.SIGN_UP_2
                st.rerun()

    st.markdown("---")
    st.html("<p style='width: 100%; color: grey; text-align: center; padding:0;'>Already have an account?</p>")

    if st.button("Sign In", key="btn_switch_to_signin", type='tertiary', use_container_width=True):
        st.session_state.current_user = None
        st.session_state.page = PageType.SIGN_IN
        st.rerun()


def show_sign_up_2():
    st.header("🎭 Sign Up")
    st.caption("Let us know your personality traits")
    st.progress(67)

    # Personality traits inputs
    opinions = st.selectbox("Opinion Style", options=Personality.OPINIONS_OPTIONS, key="personality_opinions")
    movie_choice = st.selectbox("Movie Choice", options=Personality.MOVIE_CHOICE_OPTIONS,
                                key="personality_movie_choice")
    character = st.selectbox("Character", options=Personality.CHARACTER_OPTIONS, key="personality_character")
    fashion = st.selectbox("Fashion", options=Personality.FASHION_OPTIONS, key="personality_fashion")
    ideal_night = st.selectbox("Ideal Night", options=Personality.IDEAL_NIGHT_OPTIONS, key="personality_ideal_night")
    music_taste = st.selectbox("Music Taste", options=Personality.MUSIC_TASTE_OPTIONS, key="personality_music_taste")
    introvertness = st.selectbox("Introvertness", options=Personality.INTROVERTNESS_STAGES,
                                 key="personality_introvertness")
    self_motivation = st.selectbox("Self Motivation", options=Personality.SELF_MOTIVATION_STAGES,
                                   key="personality_self_motivation")
    creativity = st.selectbox("Creativity", options=Personality.CREATIVITY_STAGES, key="personality_creativity")
    stress_levels = st.selectbox("Stress Levels", options=Personality.STRESS_LEVELS_OPTIONS,
                                 key="personality_stress_levels")
    job_satisfaction = st.selectbox("Job Satisfaction", options=Personality.JOB_SATISFACTION_LEVELS,
                                    key="personality_job_satisfaction")
    spirituality = st.selectbox("Spirituality", options=Personality.SPIRITUALITY_LEVELS, key="personality_spirituality")
    family_person = st.selectbox("Family Orientation", options=Personality.FAMILY_PERSON_LEVELS,
                                 key="personality_family_person")
    loneliness = st.selectbox("Loneliness", options=Personality.LONELINESS_LEVELS, key="personality_loneliness")
    going_out_enjoyment = st.selectbox("Going Out Enjoyment", options=Personality.GOING_OUT_ENJOYMENT_OPTIONS,
                                       key="personality_going_out_enjoyment")
    workout_preference = st.selectbox("Workout Preference", options=Personality.WORKOUT_PREFERENCE_LEVELS,
                                      key="personality_workout_preference")
    academic_importance = st.selectbox("Academic Importance", options=Personality.ACADEMIC_IMPORTANCE_LEVELS,
                                       key="personality_academic_importance")
    nature_to_city_preference = st.selectbox("Nature to City Preference",
                                             options=Personality.NATURE_TO_CITY_PREFERENCE_OPTIONS,
                                             key="personality_nature_to_city_preference")
    politically_incorrect_humor = st.selectbox("Politically Incorrect Humor",
                                               options=Personality.POLITICALLY_INCORRECT_HUMOR_LEVELS,
                                               key="personality_politically_incorrect_humor")
    political_discussion = st.selectbox("Political Discussion", options=Personality.POLITICAL_DISCUSSION_LEVELS,
                                        key="personality_political_discussion")

    if st.button("Next", key="btn_signup_2_next", type='primary', use_container_width=True):
        with st.spinner("Processing..."):
            st.session_state.current_user.personality = Personality(
                opinions=opinions,
                movie_choice=movie_choice,
                character=character,
                fashion=fashion,
                ideal_night=ideal_night,
                music_taste=music_taste,
                introvertness=introvertness,
                self_motivation=self_motivation,
                creativity=creativity,
                stress_levels=stress_levels,
                job_satisfaction=job_satisfaction,
                spirituality=spirituality,
                family_person=family_person,
                loneliness=loneliness,
                going_out_enjoyment=going_out_enjoyment,
                workout_preference=workout_preference,
                academic_importance=academic_importance,
                nature_to_city_preference=nature_to_city_preference,
                politically_incorrect_humor=politically_incorrect_humor,
                political_discussion=political_discussion
            )
            st.session_state.page = PageType.SIGN_UP_3
            st.rerun()


def set_recommendation():
    recom_system = RecommenderSystem(
        faiss_path='/Users/vikash/Office/Hurrey Code/Hightable.ai/backend/hightable_ai_user_db',
        event_path='/Users/vikash/Office/Hurrey Code/Hightable.ai/backend/hightable_ai_events.csv')

    user: User = st.session_state.current_user
    intro, persona, budget_constraint, preferred_language, location = recom_system.get_user_details_from_user_dict(
        user.to_dict())

    similar_users = recom_system.get_similar_users_details(intro, persona)
    events = recom_system.get_table_fitment_scores(budget_constraint, preferred_language, location, persona)

    st.session_state.recommended_people = similar_users
    st.session_state.recommended_table = events


def show_sign_up_3():
    st.header("🍽️ Sign Up")
    st.caption("Let us know your Dinner style")
    st.progress(100)
    event_budget = st.number_input(
        "Event Budget",
        min_value=0,
        value=1000,
        step=500,
        key="event_budget"
    )

    # Preferred language(s) (multiselect with default = ["English", "Hindi"])
    preferred_language = st.multiselect(
        "Preferred Language(s)",
        options=EventPreference.LANGUAGES_OPTIONS,
        default=["English"],
        key="preferred_language"
    )

    # Menu options (multiselect with default = ["Meat", "Fish"])
    menu_options = st.multiselect(
        "Menu Options",
        options=EventPreference.MENU_OPTIONS,
        default=["I eat everything"],
        key="menu_options"
    )
    location_options = st.selectbox("Location", options=EventPreference.PREFERRED_LOCATION, key="location_options")

    if st.button("Finish", key="btn_signup_3_next", type='primary', use_container_width=True):
        with st.spinner("Processing..."):
            st.session_state.current_user.events_pref.append(
                EventPreference(
                    event_budget=event_budget,
                    preferred_language=preferred_language,
                    menu_options=menu_options,
                    preferred_location=location_options
                )
            )
            # update json
            st.session_state.users.append(st.session_state.current_user)
            users = st.session_state.users
            users_json = []
            for user in users:
                users_json.append(user.to_dict())

            with open('/Users/vikash/Office/Hurrey Code/Hightable.ai/users.json', 'w') as f:
                json.dump(users_json, f, indent=4)

            set_recommendation()

            st.session_state.page = PageType.DASHBOARD
            st.rerun()


def show_registration_page(type=PageType.SIGN_IN):
    if type == PageType.SIGN_IN:
        show_sign_in()
    elif type == PageType.SIGN_UP_1:
        show_sign_up_1()
    elif type == PageType.SIGN_UP_2:
        show_sign_up_2()
    elif type == PageType.SIGN_UP_3:
        show_sign_up_3()
