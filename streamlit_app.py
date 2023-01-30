import streamlit as st
import requests
import pandas as pd

def get_courses():
    url = "https://www.udemy.com/api-2.0/courses/"
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
    courses = get_courses()
    if courses:
        df = pd.DataFrame(courses)
        df["num_subscribers"] = df["num_subscribers"].astype(int)
        most_popular_course = df.sort_values("num_subscribers", ascending=False)["title"].iloc[0]
        st.write("Most popular course: ", most_popular_course)
    else:
        st.write("No courses found.")

if __name__ == "__main__":
    main()
