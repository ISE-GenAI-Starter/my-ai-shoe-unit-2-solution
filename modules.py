#############################################################################
# modules.py
#
# This file contains modules that may be used throughout the app.
#
# You will write these in Unit 2. Do not change the names or inputs of any
# function other than the example.
#############################################################################

from internals import create_component


# This one has been written for you as an example. You may change it as wanted.
def display_my_custom_component(value):
    """Displays a 'my custom component' which showcases an example of how custom
    components work.

    value: the name you'd like to be called by within the app
    """
    # Define any templated data from your HTML file. The contents of
    # 'value' will be inserted to the templated HTML file wherever '{{NAME}}'
    # occurs. You can add as many variables as you want.
    data = {
        'NAME': value,
    }
    # Register and display the component by providing the data and name
    # of the HTML file. HTML must be placed inside the "custom_components" folder.
    html_file_name = "my_custom_component"
    create_component(data, html_file_name)


def display_post(username, user_image, timestamp, content, post_image):
    """Write a good docstring here."""
    data = {
        'USER_IMG': user_image,
        'USERNAME': username,
        'TIMESTAMP': timestamp,
        'CONTENT': content,
        'POST_IMG': post_image
    }
    create_component(data, "soln_post")


def display_activity_summary(workouts_list):
    """Write a good docstring here."""
    steps = 0
    calories = 0
    for workout in workouts_list:
        # IF workout is today
        steps += workout['steps']
        calories += workout['calories_burned']
    data = {
        'STEPS': steps,
        'CALORIES': calories,
    }
    create_component(data, "soln_activity_summary")


def display_recent_workouts(workouts_list):
    """Write a good docstring here."""
    steps = 0
    calories = 0
    for workout in workouts_list:
        steps += workout['steps']
        calories += workout['calories_burned']
    data = {
        'TOTAL_WORKOUTS': len(workouts_list),
        'AVG_STEPS': float(steps) / len(workouts_list),
        'AVG_CALORIES': float(calories) / len(workouts_list),
    }
    create_component(data, "soln_recent_workouts")


def display_genai_advice(timestamp, content, image):
    """Write a good docstring here."""
    display_post("Friendly Bot", "", timestamp, content, image)
