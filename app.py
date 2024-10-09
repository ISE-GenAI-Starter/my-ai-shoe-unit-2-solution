#############################################################################
# app.py
#
# This file contains the entrypoint for the app.
#
#############################################################################

import streamlit as st
from modules import display_my_custom_component, display_post, display_genai_advice, display_activity_summary, display_recent_workouts
from data_fetcher import get_user_posts, get_genai_advice, get_user_profile, get_user_sensor_data, get_user_workouts

userId = 'user1'


def display_app_page():
    """Displays the home page of the app."""
    advice = get_genai_advice(userId)
    display_genai_advice(advice['timestamp'], advice['content'], advice['image'])

    st.title("Workouts")
    workouts = get_user_workouts(userId)
    display_activity_summary(workouts)
    display_recent_workouts(workouts)

    st.title("Friend posts!")
    friends = get_user_profile(userId)['friends']
    posts = []
    for friendId in friends:
        posts.extend(get_user_posts(friendId))
    for post in posts:
        user = get_user_profile(post['user_id'])
        display_post(user['username'], user['profile_image'],
                     post['timestamp'], post['content'], post['image'])


# This is the starting point for your app. You do not need to change these lines
if __name__ == '__main__':
    display_app_page()
