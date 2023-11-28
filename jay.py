import streamlit as st

def page_home():
    st.title("Home Page")
    st.write("Welcome to the home page.")

def page_about():
    st.title("About Page")
    st.write("This is the about page.")

def page_contact():
    st.title("Contact Page")
    st.write("You can contact us here.")

def main():
    st.sidebar.title("Navigation")
    pages = {
        "Home": page_home,
        "About": page_about,
        "Contact": page_contact,
    }

    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page
    pages[selected_page]()

if __name__ == "__main__":
    main()
