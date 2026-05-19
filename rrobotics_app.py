import streamlit as st
import pandas as pd

# 1. PAGE SETUP
st.set_page_config(
    page_title="RoboTech Pro | Engineering Utilities",
    page_icon="🤖",
    layout="centered"
)

# 2. PROFESSIONAL DESIGN SYSTEM (Matches your blueprint layout)
st.markdown("""
    <style>
    .main { background-color: #0f172a; }
    h1, h2, h3 { color: #f8fafc; font-family: 'Inter', sans-serif; font-weight: 700; }
    p, span, label { color: #cbd5e1; }
    .stMetric { border: 1px solid #1e293b; padding: 15px; border-radius: 8px; background-color: #1e293b; }
    div[data-baseweb="input"] input { background-color: #0f172a; color: #ffffff; border: 1px solid #334155; }
    .stButton>button { background-color: #10b981; color: white; border: none; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_base64=True)

# 3. MATHEMATICAL COMPUTATION LOGIC
def calculate_torque(mass_kg, length_cm):
    """Computes physical torque requirement in Newton-Meters."""
    standard_gravity = 9.80665
    length_meters = length_cm / 100
    return mass_kg * standard_gravity * length_meters

# 4. APP HEADER
st.title("🤖 RoboTech Pro - Engineering Utilities | Version 2.1")
st.write("A professional-grade utility suite for logic calculations and project lifecycle management.")
st.write("---")

# 5. CORE MODULE 1: TORQUE CALCULATOR
st.header("⚙️ Motor Torque Calculator")
st.write("Calculate the torque needed for your robot's arm or wheels.")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Object Weight (kg):", min_value=0.01, value=1.00, step=0.1)
with col2:
    distance = st.number_input("Arm Length/Radius (cm):", min_value=0.1, value=10.00, step=0.5)

# Execute core physics logic
calculated_torque = calculate_torque(weight, distance)

st.metric(
    label="Required System Torque Output", 
    value=f"{calculated_torque:.2f} Nm",
    delta="Stable Load" if calculated_torque < 5 else "High Load Warning"
)

st.write("---")

# 6. CORE MODULE 2: ROADMAP TRACKER
st.header("📝 Project Milestone Tracker")

# Initializing data framework matrix using session_state memory
if 'task_matrix' not in st.session_state:
    st.session_state.task_matrix = pd.DataFrame([
        {"Phase": "Structural", "Task": "Chassis Frame Design", "Status": "Complete"},
        {"Phase": "Structural", "Task": "Chassis Prototype Assembly", "Status": "Complete"},
        {"Phase": "Logic", "Task": "PID Actuator Scripting", "Status": "In Progress"}
    ])

# Render data block to screen
st.dataframe(st.session_state.task_matrix, use_container_width=True)

# Interactive control panel to modify state parameters
with st.expander("➕ Log New Engineering Phase"):
    input_phase = st.text_input("Engineering Phase (e.g., Logic, Power, Sensors)")
    input_task = st.text_input("Specific Task Description")
    input_status = st.selectbox("Current Lifecycle Status", ["Planned", "In Progress", "Testing", "Complete"])
    
    if st.button("Commit Task to Repository"):
        if input_phase and input_task:
            new_entry = pd.DataFrame([{"Phase": input_phase, "Task": input_task, "Status": input_status}])
            st.session_state.task_matrix = pd.concat([st.session_state.task_matrix, new_entry], ignore_index=True)
            st.toast("Task successfully committed to memory data structure!")
            st.rerun()
        else:
            st.error("Data validation error: Please fill out both Phase and Task inputs.")

st.write("---")
st.caption("System Architecture Developed by Godbless | Cloud Portfolio Assets")