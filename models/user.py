import json
from dataclasses import dataclass, asdict, field
from typing import List


@dataclass
class Identity:
    gender: str
    dob: str
    relationship_status: str
    children: str
    profession: str
    country: str


@dataclass
class Personality:
    opinions: str
    movie_choice: str
    character: str
    fashion: str
    ideal_night: str
    music_taste: str
    introvertness: str
    self_motivation: str
    creativity: str
    stress_levels: str
    job_satisfaction: str
    spirituality: str
    family_person: str
    loneliness: str
    going_out_enjoyment: str
    workout_preference: str
    academic_importance: str
    nature_to_city_preference: str
    politically_incorrect_humor: str
    political_discussion: str

    # Allowed options for each personality field
    OPINIONS_OPTIONS = ["logical and facts", "emotions and feelings"]
    MOVIE_CHOICE_OPTIONS = ["author's film enthusiast", "mainstream blockbuster lover"]
    CHARACTER_OPTIONS = ['smart person', 'funny person']
    FASHION_OPTIONS = ["classic and timeless", "trendy and expressive"]
    IDEAL_NIGHT_OPTIONS = ["well-planned in advance", "spontanous and improvized"]
    MUSIC_TASTE_OPTIONS = ['rap', 'rock', 'neither rap or rock']
    INTROVERTNESS_STAGES = [
        "Highly Extroverted", "Mostly Extroverted", "Slightly Extroverted", "Ambiverted",
        "Slightly Introverted", "Moderately Introverted", "Noticeably Introverted",
        "Highly Introverted", "Very Highly Introverted", "Extremely Introverted"
    ]
    SELF_MOTIVATION_STAGES = [
        "Not Motivated at All", "Rarely Motivated", "Slightly Motivated",
        "Occasionally Motivated", "Moderately Motivated", "Fairly Motivated", "Highly Motivated",
        "Very Highly Motivated", "Extremely Motivated", "Incredibly Self-Driven"
    ]
    CREATIVITY_STAGES = [
        "Not Creative at All", "Rarely Creative", "Slightly Creative", "Occasionally Creative",
        "Moderately Creative", "Fairly Creative", "Highly Creative", "Very Highly Creative",
        "Extremely Creative", "Exceptionally Imaginative"
    ]
    STRESS_LEVELS_OPTIONS = [
        "Not Stressed at All", "Rarely Stressed", "Slightly Stressed", "Occasionally Stressed",
        "Moderately Stressed", "Fairly Stressed", "Highly Stressed", "Very Highly Stressed",
        "Extremely Stressed", "Severely Overwhelmed"
    ]
    JOB_SATISFACTION_LEVELS = [
        "Terrible Job", "Very Bad Job", "Bad Job", "Below Average Job", "Average Job",
        "Decent Job", "Good Job", "Very Good Job", "Great Job", "Dream Job"
    ]
    SPIRITUALITY_LEVELS = [
        "Not Spiritual at All", "Rarely Spiritual", "Slightly Spiritual", "Occasionally Spiritual",
        "Moderately Spiritual", "Fairly Spiritual", "Highly Spiritual", "Very Highly Spiritual",
        "Extremely Spiritual", "Deeply Enlightened"
    ]
    FAMILY_PERSON_LEVELS = [
        "Not Family-Oriented at All", "Rarely Family-Oriented", "Slightly Family-Oriented",
        "Occasionally Family-Oriented", "Moderately Family-Oriented", "Fairly Family-Oriented",
        "Highly Family-Oriented", "Very Highly Family-Oriented", "Extremely Family-Oriented",
        "Deeply Devoted to Family"
    ]
    LONELINESS_LEVELS = [
        "Never Lonely", "Rarely Lonely", "Slightly Lonely", "Occasionally Lonely", "Moderately Lonely",
        "Fairly Lonely", "Highly Lonely", "Very Highly Lonely", "Extremely Lonely", "Completely Isolated"
    ]
    GOING_OUT_ENJOYMENT_OPTIONS = [
        "Hates Going Out", "Rarely Enjoys Going Out", "Slightly Enjoys Going Out",
        "Occasionally Enjoys Going Out", "Moderately Enjoys Going Out", "Fairly Enjoys Going Out",
        "Highly Enjoys Going Out", "Very Highly Enjoys Going Out", "Extremely Enjoys Going Out",
        "Loves Going Out All the Time"
    ]
    WORKOUT_PREFERENCE_LEVELS = [
        "Hates Working Out", "Rarely Works Out", "Occasionally Works Out",
        "Somewhat Enjoys Working Out", "Moderately Enjoys Working Out", "Fairly Enjoys Working Out",
        "Highly Enjoys Working Out", "Very Passionate About Working Out", "Extremely Dedicated to Working Out",
        "Lives to Work Out"
    ]
    ACADEMIC_IMPORTANCE_LEVELS = [
        "Academic Success Doesn't Matter at All", "Academic Success Rarely Matters",
        "Academic Success Slightly Matters", "Academic Success Occasionally Matters",
        "Academic Success Moderately Matters", "Academic Success Fairly Matters",
        "Academic Success Highly Matters", "Academic Success Very Highly Matters",
        "Academic Success Extremely Matters", "Academic Success is My Top Priority"
    ]
    NATURE_TO_CITY_PREFERENCE_OPTIONS = [
        "Loves Only Nature", "Prefers Nature Strongly", "Enjoys Nature More",
        "Leans Toward Nature", "Balanced Between Nature and City", "Leans Toward City",
        "Enjoys City More", "Prefers City Strongly", "Loves Only City", "Thrives in the City"
    ]
    POLITICALLY_INCORRECT_HUMOR_LEVELS = [
        "Strongly Dislikes Politically Incorrect Humor", "Mostly Dislikes Politically Incorrect Humor",
        "Slightly Dislikes Politically Incorrect Humor", "Occasionally Tolerates Politically Incorrect Humor",
        "Neutral Towards Politically Incorrect Humor", "Mildly Enjoys Politically Incorrect Humor",
        "Moderately Enjoys Politically Incorrect Humor", "Highly Enjoys Politically Incorrect Humor",
        "Very Highly Enjoys Politically Incorrect Humor", "Absolutely Loves Politically Incorrect Humor"
    ]
    POLITICAL_DISCUSSION_LEVELS = [
        "Hates Discussing Politics", "Avoids Discussing Politics", "Rarely Discusses Politics",
        "Occasionally Discusses Politics", "Somewhat Enjoys Discussing Politics",
        "Moderately Enjoys Discussing Politics", "Often Enjoys Discussing Politics",
        "Highly Enjoys Discussing Politics", "Loves Discussing Politics", "Passionate About Discussing Politics"
    ]


@dataclass
class EventPreference:
    event_budget: int
    preferred_language: List[str]
    menu_options: List[str]
    preferred_location: str

    LANGUAGES_OPTIONS = [
        "English", "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu",
        "Gujarati", "Kannada", "Odia", "Malayalam", "Punjabi", "Assamese",
        "Maithili", "Kashmiri", "Sindhi", "Konkani", "Dogri", "Nepali"
    ]

    MENU_OPTIONS = [
        "I eat everything",
        "Vegetarian",
        "Meat",
        "Fish",
        "Vegan",
        "Gluten-free",
        "Halal",
        "Kosher"
    ]

    PREFERRED_LOCATION = ['Bangalore', 'Mumbai', 'Chennai']


@dataclass
class User:
    name: str
    username: str
    password: str
    location: str
    identity: Identity | None
    personality: Personality | None
    events_pref: List[EventPreference] = field(default_factory=list)
    events_attended: List = field(default_factory=list)  # Could be a list of Event objects

    def to_dict(self):
        """Convert the User instance (including nested dataclasses) to a dictionary."""
        return asdict(self)

    def to_json(self):
        """Return a JSON string representation of the User instance."""
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        return self.to_json()


if __name__ == '__main__':
    identity = Identity(
        gender='male',
        dob='',
        relationship_status='single',
        children='no',
        profession='software engineer',
        country='india'
    )
    personality = Personality(
        opinions='logical and facts',
        movie_choice='mainstream blockbuster lover',
        character='funny person',
        fashion='trendy and expressive',
        ideal_night='spontanous and improvized',
        music_taste='rock',
        introvertness='Ambiverted',
        self_motivation='Rarely Motivated',
        creativity='Rarely Creative',
        stress_levels='Extremely Stressed',
        job_satisfaction='Great Job',
        spirituality='Highly Spiritual',
        family_person='Occasionally Family-Oriented',
        loneliness='Rarely Lonely',
        going_out_enjoyment='Rarely Enjoys Going Out',
        workout_preference='Hates Working Out',
        academic_importance="Academic Success Doesn't Matter at All",
        nature_to_city_preference='Leans Toward City',
        politically_incorrect_humor='Highly Enjoys Politically Incorrect Humor',
        political_discussion='Somewhat Enjoys Discussing Politics'
    )

    event_pref = EventPreference(
        event_budget=1500,
        preferred_language=['english', 'hindi'],
        menu_options=['meat', 'fish'],
        preferred_location='Bangalore'
    )

    # Create an instance of User
    user = User(
        name='vikash',
        username='itzvikashkumar',
        password='123456',
        location='bangalore',
        identity=identity,
        personality=personality,
        events_pref=[event_pref],
        events_attended=[]
    )

    # Print the user object as a JSON string
    print(user.to_json())
