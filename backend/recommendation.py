from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from collections import defaultdict
import pandas as pd
import json


class RecommenderSystem:
    def __init__(self, faiss_path, event_path):
        self.embeddings = HuggingFaceEmbeddings(model_name="paraphrase-mpnet-base-v2", model_kwargs={"device": "mps"})
        self.db = FAISS.load_local(faiss_path,
                                   self.embeddings, allow_dangerous_deserialization=True)
        self.events_df = pd.read_csv(event_path)
        self.opinions = ["logical and facts", "emotions and feelings"]
        self.movie_choice = ["author's film enthusiast", "mainstream blockbuster lover"]
        self.character = ['smart person', 'funny person']
        self.fashion = ["classic and timeless", 'trendy and expressive']
        self.ideal_night = ["well-planned in advance", "spontanous and improvized"]
        self.music_taste = ['rap', 'rock', 'neither rap or rock']
        self.introvertness_stages = ["Highly Extroverted", "Mostly Extroverted", "Slightly Extroverted", "Ambiverted",
                                     "Slightly Introverted", "Moderately Introverted", "Noticeably Introverted",
                                     "Highly Introverted", "Very Highly Introverted", "Extremely Introverted"]
        self.self_motivation_stages = ["Not Motivated at All", "Rarely Motivated", "Slightly Motivated",
                                       "Occasionally Motivated", "Moderately Motivated", "Fairly Motivated",
                                       "Highly Motivated", "Very Highly Motivated", "Extremely Motivated",
                                       "Incredibly Self-Driven"]
        self.creativity_stages = ["Not Creative at All", "Rarely Creative", "Slightly Creative",
                                  "Occasionally Creative", "Moderately Creative", "Fairly Creative", "Highly Creative",
                                  "Very Highly Creative", "Extremely Creative", "Exceptionally Imaginative"]
        self.stress_levels = ["Not Stressed at All", "Rarely Stressed", "Slightly Stressed", "Occasionally Stressed",
                              "Moderately Stressed", "Fairly Stressed", "Highly Stressed", "Very Highly Stressed",
                              "Extremely Stressed", "Severely Overwhelmed"]
        self.job_satisfaction_levels = ["Terrible Job", "Very Bad Job", "Bad Job", "Below Average Job", "Average Job",
                                        "Decent Job", "Good Job", "Very Good Job", "Great Job", "Dream Job"]
        self.spirituality_levels = ["Not Spiritual at All", "Rarely Spiritual", "Slightly Spiritual",
                                    "Occasionally Spiritual", "Moderately Spiritual", "Fairly Spiritual",
                                    "Highly Spiritual", "Very Highly Spiritual", "Extremely Spiritual",
                                    "Deeply Enlightened"]
        self.family_person_levels = ["Not Family-Oriented at All", "Rarely Family-Oriented", "Slightly Family-Oriented",
                                     "Occasionally Family-Oriented", "Moderately Family-Oriented",
                                     "Fairly Family-Oriented", "Highly Family-Oriented", "Very Highly Family-Oriented",
                                     "Extremely Family-Oriented", "Deeply Devoted to Family"]
        self.loneliness_levels = ["Never Lonely", "Rarely Lonely", "Slightly Lonely", "Occasionally Lonely",
                                  "Moderately Lonely", "Fairly Lonely", "Highly Lonely", "Very Highly Lonely",
                                  "Extremely Lonely", "Completely Isolated"]
        self.going_out_enjoyment = ["Hates Going Out", "Rarely Enjoys Going Out", "Slightly Enjoys Going Out",
                                    "Occasionally Enjoys Going Out", "Moderately Enjoys Going Out",
                                    "Fairly Enjoys Going Out", "Highly Enjoys Going Out",
                                    "Very Highly Enjoys Going Out", "Extremely Enjoys Going Out",
                                    "Loves Going Out All the Time"]
        self.workout_preference_levels = ["Hates Working Out", "Rarely Works Out", "Occasionally Works Out",
                                          "Somewhat Enjoys Working Out", "Moderately Enjoys Working Out",
                                          "Fairly Enjoys Working Out", "Highly Enjoys Working Out",
                                          "Very Passionate About Working Out", "Extremely Dedicated to Working Out",
                                          "Lives to Work Out"]
        self.academic_importance_levels = ["Academic Success Doesn't Matter at All", "Academic Success Rarely Matters",
                                           "Academic Success Slightly Matters", "Academic Success Occasionally Matters",
                                           "Academic Success Moderately Matters", "Academic Success Fairly Matters",
                                           "Academic Success Highly Matters", "Academic Success Very Highly Matters",
                                           "Academic Success Extremely Matters", "Academic Success is My Top Priority"]
        self.nature_to_city_preference = ["Loves Only Nature", "Prefers Nature Strongly", "Enjoys Nature More",
                                          "Leans Toward Nature", "Balanced Between Nature and City",
                                          "Leans Toward City", "Enjoys City More", "Prefers City Strongly",
                                          "Loves Only City", "Thrives in the City"]
        self.politically_incorrect_humor_levels = ["Strongly Dislikes Politically Incorrect Humor",
                                                   "Mostly Dislikes Politically Incorrect Humor",
                                                   "Slightly Dislikes Politically Incorrect Humor",
                                                   "Occasionally Tolerates Politically Incorrect Humor",
                                                   "Neutral Towards Politically Incorrect Humor",
                                                   "Mildly Enjoys Politically Incorrect Humor",
                                                   "Moderately Enjoys Politically Incorrect Humor",
                                                   "Highly Enjoys Politically Incorrect Humor",
                                                   "Very Highly Enjoys Politically Incorrect Humor",
                                                   "Absolutely Loves Politically Incorrect Humor"]
        self.political_discussion_levels = ["Hates Discussing Politics", "Avoids Discussing Politics",
                                            "Rarely Discusses Politics", "Occasionally Discusses Politics",
                                            "Somewhat Enjoys Discussing Politics",
                                            "Moderately Enjoys Discussing Politics", "Often Enjoys Discussing Politics",
                                            "Highly Enjoys Discussing Politics", "Loves Discussing Politics",
                                            "Passionate About Discussing Politics"]

    def categorize_personality(self, traits):
        categories = {
            "Thinking Style": self.opinions + self.political_discussion_levels,
            "Entertainment Preferences": self.movie_choice + self.music_taste + self.politically_incorrect_humor_levels,
            "Personal Traits": self.character + self.fashion + self.ideal_night,
            "Social Behavior": self.introvertness_stages + self.going_out_enjoyment + self.loneliness_levels,
            "Work & Lifestyle": self.job_satisfaction_levels + self.self_motivation_stages + self.stress_levels +
                                self.spirituality_levels + self.family_person_levels + self.workout_preference_levels +
                                self.academic_importance_levels + self.nature_to_city_preference
        }

        categorized = defaultdict(list)
        for trait in traits:
            for category, traits_list in categories.items():
                if trait in traits_list:
                    categorized[category].append(trait)
                    break

        return categorized

    def calculate_match_score(self, user1_traits, user2_traits):
        user1_categorized = self.categorize_personality(user1_traits)
        user2_categorized = self.categorize_personality(user2_traits)
        match_scores = {}
        for category in user1_categorized.keys() | user2_categorized.keys():
            common_traits = set(user1_categorized[category]) & set(user2_categorized[category])
            total_traits = set(user1_categorized[category]) | set(user2_categorized[category])
            match_percentage = (len(common_traits) / len(total_traits) * 100) if total_traits else 0
            match_scores[category] = match_percentage

        match_scores = sorted(match_scores.items(), key=lambda x: x[1], reverse=True)
        return match_scores

    def get_budget_score(self, budget, actual_price):
        return max(0, 1 - max(0, (actual_price - budget) / budget))

    def get_language_score(self, preferred_languages, event_languages):
        preferred_set = set(preferred_languages)
        event_set = set(event_languages)
        match_count = len(preferred_set & event_set)
        total_count = len(event_set)
        score = match_count / total_count if match_count > 0 else 0
        return max(score, 0.5) if match_count > 0 else 0

    def get_table_fitment_scores(self, budget_constraint, preferred_language, location, user_persona):
        location = location.lower()
        budget_constraint = int(budget_constraint)
        temp_df = self.events_df[self.events_df['location'] == location].reset_index()
        temp_df['participant_match'] = ''
        temp_df['fitment_score'] = 0
        for i in range(len(temp_df)):
            fitment_score = 40  #for location match
            budget_score = self.get_budget_score(budget_constraint, int(temp_df['max_amount'][i]))
            language_score = self.get_language_score(preferred_language, eval(temp_df['language'][i]))
            participants = eval(temp_df['participants'][i])
            participant_match_dic = []
            participant_scores_list = []
            for participant in participants:
                match_scores = self.calculate_match_score(user_persona, participant['participant_info'])
                traits_score = sum([item[1] for item in match_scores]) / 500
                participant_scores_list.append(traits_score)
                participant_match_dic.append({'participant_name': participant['participant_name'],
                                              "profession": participant['profession'],
                                              'match_scores': match_scores})

            participants_score = sum(participant_scores_list) / len(participant_scores_list)
            fitment_score = fitment_score + budget_score * 20 + language_score * 20 + participants_score * 20
            temp_df['participant_match'][i] = str(participant_match_dic)
            temp_df['fitment_score'][i] = fitment_score
        temp_df = temp_df.sort_values(by='fitment_score', ascending=False).reset_index()
        recommeded_events = []
        for i in range(len(temp_df)):
            dic = {}
            dic['event_name'] = temp_df['event_name'][i]
            dic['slot_date'] = temp_df['slot_date'][i]
            dic['max_seats'] = temp_df['count'][i]
            dic['event_cost'] = temp_df['max_amount'][i]
            dic['location'] = temp_df['location'][i]
            dic['languages'] = eval(temp_df['language'][i])
            dic['created_by'] = temp_df['creator_name'][i]
            dic['participants'] = eval(temp_df['participant_match'][i])
            dic['fitment_score'] = temp_df['fitment_score'][i]
            recommeded_events.append(dic)
        return recommeded_events

    def get_user_details_from_user_dict(self, user_dic):
        intro = f"I am {user_dic['name']}. I am working as {user_dic['identity']['profession']} in {user_dic['location']}"
        persona = [user_dic['personality']['opinions'],
                   user_dic['personality']['movie_choice'],
                   user_dic['personality']['character'],
                   user_dic['personality']['fashion'],
                   user_dic['personality']['ideal_night'],
                   user_dic['personality']['music_taste'],
                   user_dic['personality']['introvertness'],
                   user_dic['personality']['self_motivation'],
                   user_dic['personality']['creativity'],
                   user_dic['personality']['stress_levels'],
                   user_dic['personality']['job_satisfaction'],
                   user_dic['personality']['spirituality'],
                   user_dic['personality']['family_person'],
                   user_dic['personality']['loneliness'],
                   user_dic['personality']['going_out_enjoyment'],
                   user_dic['personality']['workout_preference'],
                   user_dic['personality']['academic_importance'],
                   user_dic['personality']['nature_to_city_preference'],
                   user_dic['personality']['politically_incorrect_humor'],
                   user_dic['personality']['political_discussion']]
        budget_constraint = user_dic['events_pref'][-1]['event_budget']
        preferred_language = user_dic['events_pref'][-1]['preferred_language']
        location = user_dic['events_pref'][-1]['preferred_location']
        return intro, persona, budget_constraint, preferred_language, location

    def get_similar_users_details(self, intro, user_persona):
        top_matched_users = self.db.similarity_search_with_score(intro + "-- " + " -- ".join(user_persona), k=10)
        final_results = []
        for item in top_matched_users:
            matched_persona = item[0].page_content.split(" -- ")[1:]
            match_scores = self.calculate_match_score(user_persona, matched_persona)
            dic = {}
            dic['name'] = item[0].metadata['name']
            dic['profession'] = item[0].metadata['profession']
            dic['similarity'] = max(0, 100 - 10 * item[1])
            dic['match_scores'] = match_scores
            final_results.append(dic)
        return final_results



