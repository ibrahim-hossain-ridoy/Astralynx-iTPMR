import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- App Header ---
st.set_page_config(page_title="iTPMR – Mars Recycling Simulator", layout="wide")
st.title("🪐 Integrated Tri-Phase Modular Recycler (iTPMR) Simulation")
st.markdown("### NASA Space Apps Challenge – Sustainable Mars Waste Recycling System")

# --- Sidebar Input ---
st.sidebar.header("♻️ User Input Parameters")
mission_months = st.sidebar.slider("Mission Duration (months)", 6, 60, 36)
plastic_in = st.sidebar.number_input("Plastic Waste (kg)", value=3500.0, min_value=0.0)
metal_in = st.sidebar.number_input("Metal Waste (kg)", value=2500.0, min_value=0.0)
foam_in = st.sidebar.number_input("Foam/Fabric Waste (kg)", value=2000.0, min_value=0.0)

st.sidebar.markdown("---")
st.sidebar.write("Adjust waste levels and mission duration to simulate resource recovery.")

# --- Simulation Core ---
months = np.arange(1, mission_months + 1)
efficiency = 50 + 45 * (1 - np.exp(-months / 18))  # system learning
efficiency = np.clip(efficiency, 0, 95)

# Power usage model (kW)
power_plastic = 1.5 + 0.3 * np.sin(months / 6)
power_metal = 2.2 + 0.5 * np.cos(months / 8)
power_foam = 1.3 + 0.4 * np.sin(months / 10)
total_power = power_plastic + power_metal + power_foam

# Temperature and gas model
temp_plastic = 200 + 15 * np.sin(months / 6)
temp_metal = 850 + 40 * np.cos(months / 7)
temp_foam = 180 + 20 * np.sin(months / 5)
toxic_load = 0.0015 * (temp_plastic + temp_metal / 5 + temp_foam / 3)
filtration_eff = 96 + 3 * np.sin(months / 6)
residual_gas = toxic_load * (1 - filtration_eff / 100)

# Recycled outputs (kg)
plastic_out = plastic_in * (efficiency / 100)
metal_out = metal_in * (efficiency / 100)
foam_out = foam_in * (efficiency / 100)

# Material yield
filament_yield = plastic_out[-1] * 0.9
ingot_yield = metal_out[-1] * 0.95
block_yield = foam_out[-1] * 0.85

# --- Visualization Section ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Recycled Material Output")
    fig1, ax1 = plt.subplots()
    ax1.plot(months, plastic_out, label='Plastic Output', color='orange')
    ax1.plot(months, metal_out, label='Metal Output', color='gray')
    ax1.plot(months, foam_out, label='Foam/Fabric Output', color='purple')
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Output (kg)")
    ax1.legend()
    ax1.grid(True)
    st.pyplot(fig1)

with col2:
    st.subheader("Power Consumption (kW)")
    fig2, ax2 = plt.subplots()
    ax2.plot(months, total_power, label='Total Power (kW)', color='red')
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Power (kW)")
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)

col3, col4 = st.columns(2)

with col3:
    st.subheader("System Efficiency (%)")
    fig3, ax3 = plt.subplots()
    ax3.plot(months, efficiency, label='Efficiency', color='green')
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Efficiency (%)")
    ax3.legend()
    ax3.grid(True)
    st.pyplot(fig3)

with col4:
    st.subheader("Gas Filtration Load")
    fig4, ax4 = plt.subplots()
    ax4.plot(months, residual_gas, label='Residual Gas', color='blue')
    ax4.set_xlabel("Month")
    ax4.set_ylabel("Toxic Load (filtered)")
    ax4.legend()
    ax4.grid(True)
    st.pyplot(fig4)

# --- Summary Section ---
st.markdown("## 🧭 Simulation Summary")
avg_eff = np.mean(efficiency)
avg_power = np.mean(total_power)
total_recycled = plastic_out[-1] + metal_out[-1] + foam_out[-1]

st.write(f"**Mission Duration:** {mission_months} months")
st.write(f"**Average Recycling Efficiency:** {avg_eff:.2f}%")
st.write(f"**Average Power Consumption:** {avg_power:.2f} kW")
st.write(f"**Total Materials Recovered:** {total_recycled:.2f} kg")

st.markdown("### 🧱 Output Breakdown")
st.write(f"- Plastic Filament: {filament_yield:.2f} kg")
st.write(f"- Metal Ingots: {ingot_yield:.2f} kg")
st.write(f"- Composite Blocks: {block_yield:.2f} kg")

# Sustainability Rating
st.markdown("### 🌎 Sustainability Rating")
if avg_eff > 85:
    st.success("Excellent – Near-Closed Loop Achieved ✅")
elif avg_eff > 70:
    st.info("Good – Partial Resource Circularity ⚙️")
else:
    st.warning("Needs Optimization – Efficiency Improvements Required ⚠️")

st.markdown("---")
st.caption("Developed by Team iTPMR | NASA Space Apps Challenge 2025 | Powered by Python & Streamlit")