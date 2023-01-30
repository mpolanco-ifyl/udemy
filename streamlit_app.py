import streamlit as st
import requests
import pandas as pd

def get_courses(topic):
    url = f"https://www.udemy.com/api-2.0/courses/?topic=${topic}&price=price-free"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results")
        if results:
            return results
        else:
            print("No results found in API response.")
            return None
    else:
        print("API request failed with status code:", response.status_code)
        return None

def main():
    st.title("Udemy Demand Analyzer")
    topic = st.text_input("Enter a topic to search for:")
    if topic:
        courses = get_courses(topic)
        if courses:
            df = pd.DataFrame(courses)
            st.write("Number of courses: ", len(courses))
            st.write("Top 5 courses:")
            st.write(df[["title", "price", "num_subscribers"]].head())
        else:
            st.write("No courses found.")
    else:
        st.write("Enter a topic to search for.")

if __name__ == "__main__":
    main()
