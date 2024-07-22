## app.py
##
## Created for TechExchange 2025, Software Development Studio with Google
##
## This file contains the entrypoint for the app.
##

# TODO(nyahway): change this import so it runs locally
import modules
import streamlit as st


def display_app_page():
  """Displays the home page of the app."""
  st.title('Welcome to SDS!')


# This is the starting point for your app. You do not need to change these lines
if __name__ == '__main__':
  display_app_page()
