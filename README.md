# 🪐 **Astralynx: Integrated Tri-Phase Modular Recycler (iTPMR)**  
### *NASA International Space Apps Challenge 2025 — Space Trash Hack*  
**Team:** Astralynx (Bangladesh)

---

## 🚀 Project Summary  

The **Integrated Tri-Phase Modular Recycler (iTPMR)** is a conceptual system engineered for **long-duration Martian missions**.  
It unifies **plastic**, **metal**, and **foam/fabric** recycling into a **single, modular, and efficient unit**, addressing waste management challenges and enabling sustainable resource reuse on Mars.  

By transforming waste into usable materials such as **3D printing filament**, **metal ingots**, and **composite blocks**, the iTPMR supports a **closed-loop ecosystem**, minimizing reliance on costly resupply missions from Earth and promoting a self-sustaining Martian habitat.  

---

## 👥 Meet Our Team — *Astralynx* 🇧🇩

<img width="7559" height="3779" alt="Team Astralynx" src="https://github.com/user-attachments/assets/a0340aff-9d9d-4f1b-ba2c-4787b8afc030" />

We are **Team Astralynx** from Bangladesh, competing in the **NASA International Space Apps Challenge 2025** under the *Space Trash Hack* category.  
Our team combines diverse expertise in **research, programming, data modeling, 3D visualization, and creative design** — united by a shared mission to make space sustainability achievable.  

### 🔹 Team Members

**🧑‍💻 Ibrahim Hossain Ridoy** — *Team Leader, Researcher*  
Guides the project vision, oversees integration between engineering and scientific domains, and develops the system’s conceptual and simulation framework.  

**🎨 Rafiulla Bari** — *Video Editor, 3D Artist*  
Designs realistic 3D models and animations for system visualization, ensuring complex mechanisms are communicated with clarity and creativity.  

**📊 Amir Hamja** — *Researcher, Data Analyst*  
Performs analytical modeling and validation using data-driven approaches, aligning the iTPMR’s operational parameters with NASA’s ISRU methodologies.  

**💻 Masuma Islam** — *Programmer, Script Writer*  
Develops simulation scripts, supports data visualization, and crafts narrative and documentation content for technical and general audiences.  

✨ *Together, we’re designing sustainable solutions for Mars — and inspiration for Earth.*  

---

## 🛰️ Core Objectives  

- ♻️ **All-in-one recycling system** for plastics, metals, and foam/fabric waste  
- 🤖 **Automated sorting & modular processing** for reduced astronaut workload  
- 🧱 **Enable in-situ manufacturing** using recycled outputs  
- 🫧 **Integrated gas filtration** for emission control and safety  
- 🚧 **Compact modular design** to minimize payload and power consumption  

---

## 🧠 Simulation Description  

The **iTPMR Web Simulator** is a data-driven model that demonstrates how the system would function over time under Martian conditions.  
It uses **realistic engineering assumptions** to calculate recycling efficiency, energy usage, and material recovery across modules.  

### 🔍 Simulation Capabilities  

- **Waste Processing Rate** — Predicts how efficiently different material types are recycled per day/week of mission operation.  
- **Power Consumption Model** — Estimates energy requirements per subsystem (shredder, heater, extrusion unit, etc.).  
- **Recycling Efficiency Metrics** — Evaluates conversion rates from waste to usable material.  
- **Gas Filtration & Emission Control** — Simulates air quality improvements and CO₂ reduction within the habitat environment.  
- **Material Recovery Outputs** — Quantifies how much filament, ingot, or composite material can be produced for in-situ use.  

### 🌐 Web Application  

The simulation is hosted as an **interactive Streamlit web app**, allowing users to:  
- Adjust mission parameters (waste type, duration, power budget)  
- Observe dynamic performance graphs and energy analytics  
- Visualize sustainability impact over extended missions  

---

## 🌍 Features  

- 📊 **Real-time data visualization** via interactive dashboard  
- 🔋 **Power and efficiency modeling** for each module  
- 🧱 **Material yield prediction** for filament, ingots, and blocks  
- 🌫️ **Gas filtration simulation** for astronaut safety  
- 🧮 **Adjustable mission parameters** for custom scenarios  

---

## 💻 Tech Stack  

| Component | Technology |
|------------|-------------|
| **Simulation Engine** | Python 3 |
| **Web Framework** | Streamlit |
| **Data Visualization** | Matplotlib |
| **Modeling & Computation** | NumPy |
| **Hosting** | Streamlit Cloud / GitHub |

---

## 🛠️ Design & Engineering Blueprint  

### ⚙️ System Overview  
- Dimensions: **2.0 m × 1.5 m × 1.8 m**  
- Construction: **Aluminum alloy chassis**, titanium reinforcement  
- Energy Draw: **~5–6 kW** (from Mars habitat power grid)  

### 🔄 Shared Waste Input & Sorting  
- **Universal intake chamber** for mixed waste  
- **AI-assisted sorting** with sensors and robotic manipulation  
- Reduces contamination risks and manual labor  

### ⚡ Universal Shredding Unit  
- Handles all material types efficiently  
- Optimizes energy and space compared to multi-unit systems  

### 🧩 Recycling Modules  
- **Plastic Module** → Extrudes filament for 3D printing  
- **Metal Module** → Induction melts and reforms metals into rods or ingots  
- **Foam/Fabric Module** → Compresses materials into composite insulation blocks  

### 🛡️ Control & Safety Systems  
- Unified command panel with telemetry feedback  
- Advanced filtration system neutralizes harmful gases and particulates  

---

## 📚 NASA Research Alignment  

Our proposal is inspired by and aligned with NASA’s ongoing work in **In-Situ Resource Utilization (ISRU)**, **additive manufacturing**, and **waste management** for extraterrestrial environments:  

- 🧩 [In-Situ Resource Utilization (ISRU)](https://ntrs.nasa.gov/api/citations/20120001775/downloads/20120001775.pdf)  
- 🧾 [3D Printing in Space](https://www.nasa.gov/missions/station/iss-research/3d-printing-saving-weight-and-space-at-launch/)  
- ♻️ [Waste Management Options for Long-Duration Missions](https://ntrs.nasa.gov/api/citations/20140010284/downloads/20140010284.pdf)  
- ⚙️ [Metal Additive Manufacturing Research](https://www.digitallibrarynasampe.org/data/pdfs/s2021_pdfs/TP21-0000000427.pdf)  

---

## 📹 Demo Video  

🎥 **Experience the iTPMR Simulation and Prototype Overview:**  
[![iTPMR Demo Video](https://img.youtube.com/vi/35k51J84Ulo/0.jpg)](https://youtu.be/35k51J84Ulo)  
👉 Watch here: [https://youtu.be/35k51J84Ulo](https://youtu.be/35k51J84Ulo)

---

## 🧩 Repository Structure  
```
iTPMR-NASA-SpaceApps/
├── app.py                     # Streamlit web interface (entrypoint)
├── simulation/
│   ├── __init__.py
│   ├── plastic_module.py      # plastic processing model
│   ├── metal_module.py        # metal processing model
│   ├── foam_module.py         # foam & fabric processing model
│   ├── power_model.py         # energy consumption & scheduling
│   └── gas_filtration.py      # filtration and emissions model
├── data/
│   ├── sample_inputs.csv      # example mission scenarios
│   └── output_logs/           # simulation run outputs & exports
├── assets/
│   ├── diagrams/              # system diagrams and schematics
│   └── icons/
├── docs/
│   ├── design_notes.md        # engineering assumptions & references
│   └── simulation_specs.md    # simulation math & coefficients
├── requirements.txt
├── LICENSE
└── README.md
```
---
## ⚙️ Installation & Running Locally 1. **Clone the repository**
```
   git clone https://github.com/YOUR_USERNAME/iTPMR-NASA-SpaceApps.git
   cd iTPMR-NASA-SpaceApps
```
---
## 🧭 Challenge: *Space Trash Hack*  

**Question:**  
> How can we address the issue of space trash and waste management in future Mars missions?  

**Our Answer:**  
> The **iTPMR** — a compact, intelligent, and integrated recycler that transforms waste into usable materials, closing the resource loop for sustainable Martian living.  

---

## 🌌 Vision  

> “What we waste on Earth, we reuse on Mars.”  

Through **innovation**, **collaboration**, and **engineering foresight**, Team Astralynx envisions a future where recycling technologies empower long-term interplanetary missions — and help redefine sustainability on Earth.  

---

## 📄 License  

This project is released under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.  
