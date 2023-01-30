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
            df["topic"] = df["title"].apply(lambda x: x.split(" ")[0])
            topic_counts = df["topic"].value_counts().reset_index()
            topic_counts.columns = ["Topic", "Count"]
            st.write("Topics with highest demand:")
            st.write(topic_counts.head(10))
        else:
            st.write("No courses found.")
    else:
        st.write("Enter a topic to search for.")

if __name__ == "__main__":
    main()
