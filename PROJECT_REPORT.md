# Group Project Report: Interactive Specific Heat Capacity ($C_p$ vs. $T$) Materials Database Platform

**Course:** Materials Thermodynamics & Computational Engineering  
**Authors:** Student 1 (Member A) & Student 2 (Member B)  
**Database Scope:** 230 Materials across 8 Engineering Categories  

---

## 1. Executive Summary & Objectives

The goal of this assignment is to develop an interactive, standalone computational tool to model, plot, and analyze the temperature-dependent specific heat capacity at constant pressure ($C_p(T)$) for over 200 materials across 8 distinct engineering classes.

Our platform compiles **230 validated materials**:
1. **Metals and Alloys** (35 materials)
2. **Ceramics and Oxides** (35 materials)
3. **Semiconductors** (25 materials)
4. **Polymers** (30 materials)
5. **Glasses** (25 materials)
6. **Refractories & UHTCs** (25 materials)
7. **Composite Materials** (25 materials)
8. **Advanced & Functional Materials** (30 materials)

---

## 2. Theoretical Background & Mathematical Formulations

### 2.1 Solid-State Thermodynamic Physics
Specific heat capacity at constant pressure is governed by lattice phonon vibrational modes:
$$C_p = \left(\frac{\partial H}{\partial T}\right)_p = T \left(\frac{\partial S}{\partial T}\right)_p$$

At elevated temperatures ($T \gg \theta_D$), the molar vibrational heat capacity asymptotically approaches the Dulong-Petit classical limit:
$$C_{v,\text{molar}} \approx 3R \approx 24.94 \text{ J}/(\text{mol}\cdot\text{K}) \quad \text{per gram-atom}$$

### 2.2 Mathematical Formulations
1. **NIST Shomate 5-Parameter Model:**
   $$C_p(t) = A + B t + C t^2 + D t^3 + \frac{E}{t^2} \quad \left(t = \frac{T}{1000}\text{ K}\right)$$
2. **High-Order Empirical Polynomials:**
   $$C_p(T) = c_0 + c_1 T + c_2 T^2 + c_3 T^3$$

---

## 3. Individual Roles & Distinct Skill Demonstrations

### Student 1 (Group Member A):
* **Focus:** Fundamental Solid-State Thermodynamics, Calorimetric Data Collation, Mathematical Modeling & Database Architecture.
* **Demonstrated Skills:**
  - NIST WebBook, JANAF, NASA SP-4534, and PoLyInfo literature extraction and validation.
  - Closed-form calculus derivations for enthalpy $H(T)$ and entropy $S(T)$ functions.
  - Database schema design, unit normalization equations, and temperature validity range checking.
  - Authored **Presentation 1** with an academic research style focused on thermodynamic physics, Debye/Einstein models, and chemical bonding taxonomy.

### Student 2 (Group Member B):
* **Focus:** Computational Platform Architecture, Interactive Canvas Graphics, Materials Selection Case Studies & Video Demonstration.
* **Demonstrated Skills:**
  - Zero-dependency HTML5/JavaScript client-side web engineering and canvas coordinate mapping math.
  - Companion Python Streamlit application development (`app.py`).
  - Search filtering algorithms, real-time reference temperature ranking engine, and CSV data serialization.
  - Formulated 4 engineering application case studies and authored **Presentation 2** with a modern engineering systems dashboard style.
