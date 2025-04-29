import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please Try Again later."
    except:
        return "Why do programmers prefer dark mode? \n Because the light attracts too many bugs! 🐛💡" 

def main():
    st.title("Random Joke Generator")
    st.write("Click the below button to generate Random Jokes!")

    if st.button("Tell me a joke"):
        joke = get_random_joke()
        st.success(joke)

    st.divider()
    st.markdown(
        """
    <div style='text-align:center;'>
         <p>Joke from Official joke API</p>
         <p>Build with ❤️ by <a href='https://github.com/Maham-Ahsan'>Maham Ahsan</a>using streamlit</p>
         </div>
    """,
           unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
