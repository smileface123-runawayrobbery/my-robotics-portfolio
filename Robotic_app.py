import streamlit as st
import pandas as pd

# 1. PROFESSIONAL CONFIGURATION
st.set_page_config(
    page_title="RoboLogic Pro | Engineering Suite",
    page_icon="🦾",
    layout="centered"
)

# 2. THEME & STYLING (The "Mature" Look)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { border: 1px solid #30363d; padding: 10px; border-radius: 5px; background-color: #161b22; }
    h1, h2 { color: #58a6ff; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_base64=True)

# 3. LOGIC MODULES (Functions make code look professional)
def calculate_torque(mass_kg, length_cm):
    """Calculates torque in Newton-meters (Nm)."""
    gravity = 9.80665 # Standard gravity constant
    length_m = length_cm / 100
    return mass_kg * gravity * length_m

# 4. SIDEBAR IDENTITY
st.sidebar.image("https://img.icons8.com/fluency/96/robot-arm.png")
st.sidebar.title("RoboLogic v2.1")
st.sidebar.info("Professional-grade utility for robotics hardware calculation and workflow management.")

# 5. APP INTERFACE
st.title("🦾 RoboLogic Engineering Suite")
st.write("---")

tab1, tab2 = st.tabs(["⚙️ Torque Calculator", "📊 Project Roadmap"])

with tab1:
    st.subheader("Dynamic Load Calculation")
    
    col1, col2 = st.columns(2)
    with col1:
        m = st.number_input("Load Mass (kg)", min_value=0.0, value=1.5, step=0.1)
    with col2:
        L = st.number_input("Arm Radius (cm)", min_value=0.0, value=25.0, step=0.5)
    
    # Executing calculation
    result = calculate_torque(m, L)
    
    st.metric(label="Calculated Torque Requirement", value=f"{round(result, 3)} Nm")
    
    if result > 5:
        st.warning("⚠️ High torque detected. High-voltage servo recommended.")
    else:
        st.success("✅ Standard motor torque sufficient.")

with tab2:
    st.subheader("Engineering Roadmap")
    
    # Using a DataFrame for a professional table look
    if 'tasks' not in st.session_state:
        st.session_state.tasks = pd.DataFrame([
            {"Phase": "Structural", "Task": "Chassis Assembly", "Status": "Complete"},
            {"Phase": "Logic", "Task": "PID Controller Script", "Status": "In Progress"}
        ])

    st.table(st.session_state.tasks)
    
    with st.expander("Add New Milestone"):
        new_phase = st.text_input("Project Phase")
        new_task = st.text_input("Task Description")
        if st.button("Log to Repository"):
            new_row = pd.DataFrame([{"Phase": new_phase, "Task": new_task, "Status": "Pending"}])
            st.session_state.tasks = pd.concat([st.session_state.tasks, new_row], ignore_index=True)
            st.rerun()

st.write("---")
st.caption("Developed by Godbless | Senior Secondary Technical Stream")