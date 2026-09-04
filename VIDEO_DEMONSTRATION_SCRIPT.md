# 5-Minute Video Demonstration Script
## Temperature-Dependent Specific Heat Capacity (Cp vs. T) Materials Database & Computational Platform

**Presenters**: Student 1 (Thermodynamics & Data Lead) & Student 2 (Computational Platform & Systems Lead)  
**Target Duration**: 5 Minutes (300 seconds)  

---

### [00:00 - 00:45] Section 1: Project Overview & Scientific Motivation (Student 1)
- **Visual**: Title slide and intro screen of the web application.
- **Voiceover (Student 1)**:  
  "Hello everyone. Today we are presenting our engineering materials database and interactive computational platform for temperature-dependent specific heat capacity, Cp vs. T. In thermal engineering—from aerospace heat shields and nuclear cladding to semiconductor thermal management—accurate temperature-dependent heat capacity is essential for solving transient heat conduction and thermal stress problems. Our project covers 230 materials across 8 distinct engineering classes with validated empirical and NIST Shomate models."

---

### [00:45 - 01:45] Section 2: Thermodynamics & Mathematical Formulation (Student 1)
- **Visual**: Slide showing Debye T^3, Dulong-Petit, and NIST Shomate formulas; live table showing polynomial coefficients.
- **Voiceover (Student 1)**:  
  "At low temperatures, atomic vibrations follow the quantum Debye T-cubed law and the Sommerfeld electronic term for metals. At moderate and elevated temperatures, we implement the standard NIST Shomate equations. Each material in our 230-entry database stores verified polynomial coefficients, molecular weights, and exact temperature limits. The platform computes both mass specific heat in J/(kg·K) and molar heat capacity in J/(mol·K), as well as closed-form integrals for enthalpy increment and entropy."

---

### [01:45 - 03:15] Section 3: Interactive Platform Demonstration (Student 2)
- **Visual**: Screen capture of `index.html` running locally in the browser.
- **Actions & Voiceover (Student 2)**:  
  - *Clicking category filter (Ceramics & Oxides) and selecting Aluminum, Copper, Alumina, Diamond, and Titanium*:  
    "Now, let's explore our interactive platform. The interface is built with lightweight, zero-dependency SVG vector graphics so it runs instantly in any modern web browser. As I select materials from the sidebar or type in the search bar, the curves render immediately."
  - *Hovering over the plot*:  
    "Hovering anywhere along the curve displays exact real-time coordinates. For instance, Aluminum shows 900 J/(kg·K) at 300 K, while Diamond has a lower specific heat at room temperature but rises steeply due to its high Debye temperature."
  - *Switching unit dropdown*:  
    "We can switch instantly between 5 unit systems—including kJ/(kg·K), imperial Btu/(lb·°F), and molar J/(mol·K)—and toggle temperature units between Kelvin and Celsius."
  - *Adjusting temperature slider*:  
    "The dynamic reference slider dynamically updates the real-time ranking table, sorting all selected materials from highest to lowest heat capacity at any target temperature."

---

### [03:15 - 04:15] Section 4: Engineering Case Studies & Material Selection (Student 2)
- **Visual**: Displaying multi-material comparison of Refractory Ceramics (HfB2, ZrB2) vs Aerospace Superalloys (Inconel 718).
- **Voiceover (Student 2)**:  
  "Let's look at a practical engineering application: aerospace thermal protection. Comparing Ultra-High Temperature Ceramics like Hafnium Diboride and Zirconium Carbide against Nickel Superalloys at 1500 K reveals the dramatic differences in thermal absorption capacity and high-temperature stability. Engineers can export this customized dataset directly to CSV for finite element analysis in ANSYS or COMSOL."

---

### [04:15 - 05:00] Section 5: Conclusion & Summary (Student 1 & Student 2)
- **Visual**: Summary slide with repository files and thank you screen.
- **Voiceover (Student 1)**:  
  "All 230 materials have been validated against standard reference handbooks, including CRC and NIST WebBook."
- **Voiceover (Student 2)**:  
  "The full project code, database files in JSON and CSV, and the self-contained interactive web tool are completely open and ready for classroom and lab use. Thank you for your time!"
