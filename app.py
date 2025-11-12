import streamlit as st
import random

# --- Page Config ---
st.set_page_config(
    page_title="Hobby Expansion Recommender",
    page_icon="🎨",
    layout="centered"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
        font-family: 'Poppins', sans-serif;
        color: #2d2d2d;
    }
    .stTextInput > div > div > input {
        background-color: #ffe6fa;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #ff7eb3, #ff758c);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #ff9a9e, #fad0c4);
        color: #4a4a4a;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("🎨 Hobby Expansion Recommender")
st.write("Tell us your **top 3 hobbies**, and we’ll suggest 2 new ones you might love!")

# --- Input Section ---
hobby1 = st.text_input("Hobby 1")
hobby2 = st.text_input("Hobby 2")
hobby3 = st.text_input("Hobby 3")

# Example hobby dataset
all_hobbies = [
    "Photography", "Cooking", "Gardening", "Dancing", "Drawing", "Coding",
    "Traveling", "Yoga", "Reading", "Music", "Gaming", "Cycling", "Painting",
    "Writing", "Hiking", "Swimming", "Meditation", "Collecting", "Baking",
    "Fitness", "Singing", "Crafting", "Chess", "Running"
]

# --- Recommendation Logic ---
if st.button("✨ Get Recommendations"):
    user_hobbies = [h.strip().capitalize() for h in [hobby1, hobby2, hobby3] if h.strip()]
    if len(user_hobbies) < 1:
        st.warning("Please enter at least one hobby!")
    else:
        suggestions = [h for h in all_hobbies if h not in user_hobbies]
        recommended = random.sample(suggestions, 2)
        st.success("Based on your interests, you might also enjoy:")
        st.markdown(f"🌟 **{recommended[0]}**")
        st.markdown(f"🌟 **{recommended[1]}**")

st.markdown("---")
st.caption("Created with 💜 using Streamlit | Hobby Expansion Mini Project")
