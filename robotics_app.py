import streamlit as st

st.set_page_config(page_title="RoboTech Portfolio", page_icon="🤖")

st.title("🤖 Robotics Engineering Helper")
st.write("A professional utility tool for calculating torque and tracking project milestones.")

# --- TOOL 1: TORQUE CALCULATOR ---
st.header("⚙️ Motor Torque Calculator")
st.info("Calculate the torque needed for your robot's arm or wheels.")

weight = st.number_input("Object Weight (kg):", min_value=0.1, value=1.0)
distance = st.number_input("Arm Length/Radius (cm):", min_value=0.1, value=10.0)

# Torque formula: T = F * r (simplified for display)
torque = weight * 9.81 * (distance / 100)

st.success(f"Required Torque: {torque:.2f} Nm")

# --- TOOL 2: PROJECT TRACKER ---
st.header("📝 Project Milestone Tracker")
task = st.text_input("Enter a new robotics task:")
status = st.selectbox("Status:", ["Planned", "In Progress", "Testing", "Completed"])

if st.button("Add Task to Portfolio"):
    st.write(f"**Task:** {task} | **Status:** {status}")
    st.balloons()

st.sidebar.markdown("### Profile: Godbless")
st.sidebar.write("Specializing in Python Automation & Robotics.")