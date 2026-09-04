"""
app.py - Streamlit Interactive Computational Platform for Cp vs. T Database
Run with: streamlit run app.py
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import json
import os

st.set_page_config(
    page_title="Cp vs T Materials Database - Engineering Project",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load database
@st.cache_data
def load_data():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(curr_dir, "materials_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

database = load_data()
df_db = pd.DataFrame(database)

# Calculation helper
def calculate_cp(mat, T_kelvin, target_unit="J/(kg*K)"):
    eq_type = mat["eq_type"]
    p = mat["params"]
    mw = mat["mw"]
    
    if eq_type == "shomate":
        t = T_kelvin / 1000.0
        val = p["A"] + p["B"]*t + p["C"]*(t**2) + p["D"]*(t**3) + p["E"]/(t**2)
        native_unit = "J/(mol*K)"
    else:
        val = p["c0"] + p.get("c1", 0.0)*T_kelvin + p.get("c2", 0.0)*(T_kelvin**2) + p.get("c3", 0.0)*(T_kelvin**3)
        native_unit = mat["unit"]
        
    if native_unit == target_unit:
        return val
        
    if native_unit == "J/(mol*K)":
        val_j_kg_k = (val / mw) * 1000.0
    else:
        val_j_kg_k = val
        
    if target_unit == "J/(kg*K)":
        return val_j_kg_k
    elif target_unit == "J/(mol*K)":
        return (val_j_kg_k * mw) / 1000.0
    elif target_unit == "kJ/(kg*K)":
        return val_j_kg_k / 1000.0
    elif target_unit == "cal/(g*C)":
        return val_j_kg_k / 4184.0
    elif target_unit == "BTU/(lb*F)":
        return val_j_kg_k / 4186.8
    return val_j_kg_k

# App Header
st.title("Interactive (Cp vs. T) Materials Database")
st.markdown("Thermodynamic modeling and specific heat capacity comparison for engineering materials")
st.caption(f"**Database Size:** {len(database)} Materials | **Covered Classes:** Metals, Ceramics, Semiconductors, Polymers, Glasses, Refractories, Composites, Advanced Materials")

# Sidebar Controls
st.sidebar.header("Platform Controls")

# Category Filter
categories = ["All Categories"] + sorted(list(df_db["category"].unique()))
selected_category = st.sidebar.selectbox("Filter by Category", categories)

if selected_category != "All Categories":
    filtered_materials = [m for m in database if m["category"] == selected_category]
else:
    filtered_materials = database

mat_options = {f"{m['name']} ({m['formula']}) - [{m['category']}]": m["id"] for m in filtered_materials}

# Multi-select
default_keys = [k for k, v in mat_options.items() if v in ["met_01", "met_02", "cer_01", "poly_01"]]
selected_mat_labels = st.sidebar.multiselect(
    "Select Materials to Plot",
    options=list(mat_options.keys()),
    default=default_keys
)

selected_ids = [mat_options[k] for k in selected_mat_labels]
selected_mats = [m for m in database if m["id"] in selected_ids]

# Units & Range Controls
st.sidebar.subheader("Plotting & Unit Settings")
temp_unit = st.sidebar.radio("Temperature Unit", ["Kelvin (K)", "Celsius (°C)"])
cp_unit = st.sidebar.selectbox("Specific Heat ($C_p$) Unit", [
    "J/(kg*K)",
    "J/(mol*K)",
    "kJ/(kg*K)",
    "cal/(g*C)",
    "BTU/(lb*F)"
])

# Temperature Range
col_t1, col_t2 = st.sidebar.columns(2)
if temp_unit == "Kelvin (K)":
    t_min = col_t1.number_input("Min Temp (K)", value=200.0, step=25.0)
    t_max = col_t2.number_input("Max Temp (K)", value=1500.0, step=50.0)
else:
    t_min = col_t1.number_input("Min Temp (°C)", value=-73.15, step=25.0)
    t_max = col_t2.number_input("Max Temp (°C)", value=1200.0, step=50.0)

t_min_k = t_min if temp_unit == "Kelvin (K)" else t_min + 273.15
t_max_k = t_max if temp_unit == "Kelvin (K)" else t_max + 273.15

# Main Plot Area
if not selected_mats:
    st.info("Please select one or more materials from the sidebar to generate $C_p(T)$ curves.")
else:
    fig = go.Figure()
    t_range_k = np.linspace(t_min_k, t_max_k, 150)
    t_display = t_range_k if temp_unit == "Kelvin (K)" else t_range_k - 273.15

    for m in selected_mats:
        cp_vals = [calculate_cp(m, tk, cp_unit) for tk in t_range_k]
        fig.add_trace(go.Scatter(
            x=t_display,
            y=cp_vals,
            mode='lines',
            name=f"{m['name']} ({m['formula']})",
            line=dict(width=2.2),
            hovertemplate=f"<b>{m['name']} ({m['formula']})</b><br>" +
                          f"T: %{{x:.1f}} {temp_unit}<br>" +
                          f"Cp: %{{y:.2f}} {cp_unit}<br>" +
                          f"Valid: {m['T_min']} - {m['T_max']} K<extra></extra>"
        ))

    fig.update_layout(
        title="<b>Specific Heat Capacity ($C_p$) as a Function of Temperature ($T$)</b>",
        xaxis_title=f"Temperature, T ({temp_unit})",
        yaxis_title=f"Specific Heat Capacity, Cp ({cp_unit})",
        hovermode="closest",
        template="plotly_white",
        height=480,
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
    )

    st.plotly_chart(fig, use_container_width=True)

    # Ranking & Analysis Section
    st.markdown("---")
    col_rank, col_cite = st.columns([1, 1])

    with col_rank:
        st.subheader("Property Ranking Table")
        ref_t_val = st.slider("Select Reference Temperature for Ranking", min_value=float(t_min_k), max_value=float(t_max_k), value=298.15, step=10.0)
        
        ranking_data = []
        for m in selected_mats:
            cp_at_ref = calculate_cp(m, ref_t_val, cp_unit)
            ranking_data.append({
                "Material": m["name"],
                "Formula": m["formula"],
                "Category": m["category"],
                f"Cp ({cp_unit})": round(cp_at_ref, 2),
                "Valid Range (K)": f"{m['T_min']} - {m['T_max']}"
            })
            
        df_rank = pd.DataFrame(ranking_data).sort_values(by=f"Cp ({cp_unit})", ascending=False).reset_index(drop=True)
        df_rank.index = df_rank.index + 1
        st.dataframe(df_rank, use_container_width=True)

    with col_cite:
        st.subheader("Literature Citations & Equations")
        for m in selected_mats:
            with st.expander(f"{m['name']} ({m['formula']}) - {m['category']}"):
                st.markdown(f"- **Formula / Mol. Wt:** `{m['formula']}` ({m['mw']} g/mol)")
                st.markdown(f"- **Primary Data Source:** *{m['source']}*")
                st.markdown(f"- **Equation Model:** `{m['eq_type'].upper()}`")
                st.markdown(f"- **Validity Range:** {m['T_min']} K to {m['T_max']} K")
                st.markdown(f"- **Engineering Notes:** {m['notes']}")

# Full Database Browser
with st.expander("View & Search Entire 230-Material Database Table"):
    st.dataframe(df_db[["id", "name", "formula", "category", "mw", "eq_type", "T_min", "T_max", "Cp_298", "unit", "source"]], use_container_width=True)
