import streamlit as st
import random

# Inject custom CSS for the galaxy background
st.markdown(
    """
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1464802686167-b939a6910659?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z2FsYXh5fGVufDB8fDB8fHww');
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    .stApp {
        background-color: rgba(0, 0, 0, 0.8);
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Stellarluna: Interstellar Adventure")

st.write("Welcome to the interstellar adventure game! 🚀")
st.write("Your mission is to explore the galaxy, make decisions, and survive the unknown.")

# Game state
if "location" not in st.session_state:
    st.session_state.location = "Earth"
if "fuel" not in st.session_state:
    st.session_state.fuel = 100
if "health" not in st.session_state:
    st.session_state.health = 100
if "alien_encounter" not in st.session_state:
    st.session_state.alien_encounter = False

# Display current status
st.subheader("Status")
st.write(f"Location: {st.session_state.location}")
st.write(f"Fuel: {st.session_state.fuel}")
st.write(f"Health: {st.session_state.health}")

# Game actions
st.subheader("Actions")
if st.session_state.location == "Earth":
    if st.button("Launch into Space"):
        st.session_state.location = "Orbit"
        st.session_state.fuel -= 10
        st.write("You have launched into orbit! 🌍🚀")
elif st.session_state.location == "Orbit":
    if st.button("Travel to the Moon"):
        st.session_state.location = "Moon"
        st.session_state.fuel -= 20
        st.write("You have landed on the Moon! 🌕")
    if st.button("Travel to Mars"):
        st.session_state.location = "Mars"
        st.session_state.fuel -= 50
        st.write("You are on your way to Mars! 🪐")
    if st.button("Travel to Deep Space"):
        st.session_state.location = "Deep Space"
        st.session_state.fuel -= 70
        st.write("You are exploring into the unknown depths of space! 🌌")
elif st.session_state.location == "Moon":
    if st.button("Return to Earth"):
        st.session_state.location = "Earth"
        st.session_state.fuel -= 15
        st.write("You have returned to Earth! 🌍")
elif st.session_state.location == "Mars":
    if st.button("Explore Mars"):
        st.session_state.health -= 10
        st.write("You explored Mars and discovered alien life! 👽")
    if st.button("Communicate with Aliens"):
        outcome = random.choice(["friendly", "hostile"])
        if outcome == "friendly":
            st.session_state.health += 20
            st.write("The aliens are friendly and shared advanced technology with you! 🤝")
        else:
            st.session_state.health -= 30
            st.write("The aliens are hostile and attacked your ship! ⚔️")
    if st.button("Escape"):
        st.session_state.location = "Orbit"
        st.session_state.fuel -= 30
        st.write("You escaped back to orbit! 🛡️")  
    if st.button("Return to Earth"):
        st.session_state.location = "Earth"
        st.session_state.fuel -= 50
        st.write("You have returned to Earth! 🌍")
elif st.session_state.location == "Deep Space":
    if not st.session_state.alien_encounter:
        st.session_state.alien_encounter = random.choice([True, False])
        if st.session_state.alien_encounter:
            st.write("You encountered an alien spaceship! 🛸")
        else:
            st.write("You found a mysterious asteroid field. 🪨")
    if st.session_state.alien_encounter:
        if st.button("Communicate with Aliens"):
            outcome = random.choice(["friendly", "hostile"])
            if outcome == "friendly":
                st.session_state.health += 20
                st.write("The aliens are friendly and shared advanced technology with you! 🤝")
            else:
                st.session_state.health -= 30
                st.write("The aliens are hostile and attacked your ship! ⚔️")
        if st.button("Escape"):
            st.session_state.location = "Orbit"
            st.session_state.fuel -= 30
            st.write("You escaped back to orbit! 🛡️")
    else:
        if st.button("Mine Resources"):
            st.session_state.fuel += 20
            st.write("You mined resources from the asteroid field and refueled your ship! ⛽")
        if st.button("Return to Earth"):
            st.session_state.location = "Earth"
            st.session_state.fuel -= 70
            st.write("You have returned to Earth! 🌍")

# Check for game over
if st.session_state.fuel <= 0:
    st.error("You ran out of fuel! Game over. 😢")
    st.stop()
if st.session_state.health <= 0:
    st.error("You lost all your health! Game over. 😢")
    st.stop()