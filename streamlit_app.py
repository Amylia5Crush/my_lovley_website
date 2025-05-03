import streamlit as st

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
elif st.session_state.location == "Moon":
    if st.button("Return to Earth"):
        st.session_state.location = "Earth"
        st.session_state.fuel -= 15
        st.write("You have returned to Earth! 🌍")
elif st.session_state.location == "Mars":
    if st.button("Explore Mars"):
        st.session_state.health -= 10
        st.write("You explored Mars and discovered alien life! 👽")
    if st.button("Return to Earth"):
        st.session_state.location = "Earth"
        st.session_state.fuel -= 50
        st.write("You have returned to Earth! 🌍")

# Check for game over
if st.session_state.fuel <= 0:
    st.error("You ran out of fuel! Game over. 😢")
    st.stop()
if st.session_state.health <= 0:
    st.error("You lost all your health! Game over. 😢")
    st.stop()