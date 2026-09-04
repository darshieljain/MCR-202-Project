# Group Project Video Demonstration Script

**Project Title:** Interactive Specific Heat Capacity ($C_p$ vs. $T$) Materials Database Platform  
**Target Duration:** 3 to 4 Minutes  
**Demonstration Format:** Screen recording with voiceover narration  
**Software:** Standalone Web Application (`index.html`)  

---

## 🕒 Timestamped Storyboard & Voiceover Narration

### **0:00 – 0:45 | Scene 1: Platform Introduction & Scope**
* **Visual Action:** Open [`index.html`](file:///C:/Users/Yuvi/.gemini/antigravity/scratch/Cp_Materials_Database_Project/index.html) in Chrome/Edge. Display the university project header and database badge showing "230 Materials • 8 Classes".
* **Spoken Narration (Student 2):**  
  > *"Hello, this is our project demonstration for the Interactive Specific Heat Capacity (Cp vs. T) Materials Database. Our software compiles 230 engineering materials across 8 major categories: metals, ceramics, semiconductors, polymers, glasses, refractories, composites, and advanced functional materials. The application is completely standalone, light-themed, and runs client-side with zero external dependencies."*

---

### **0:45 – 1:30 | Scene 2: Live Search & Category Filtering**
* **Visual Action:**  
  1. In the search box, type `Copper` and click **+ Add**.  
  2. Type `Al2O3` and click **+ Add**.  
  3. Change the Category filter to `Polymers`, select `High Density Polyethylene (HDPE)`.  
  4. Change Category to `Refractories`, select `Magnesite Refractory`.  
  5. Show the active pills tray updating dynamically with color-coded tags.
* **Spoken Narration (Student 2):**  
  > *"Users can filter materials instantly by typing into the live search bar or selecting from the category dropdown. Clicking on any material adds it to our active plotting tray. For example, adding Copper, Corundum Alumina, HDPE, and Magnesite refractory immediately renders four distinct, color-coded thermodynamic traces on our canvas."*

---

### **1:30 – 2:30 | Scene 3: Multi-Trace Canvas Plotting & Hover Tooltips**
* **Visual Action:**  
  1. Click the **Multi-Class** preset button to load 8 materials simultaneously.  
  2. Move the mouse cursor smoothly across the canvas curves, demonstrating the real-time coordinate data tooltip displaying temperature and exact $C_p$ values for every active curve.
* **Spoken Narration (Student 1 / Student 2):**  
  > *"Our custom HTML5 canvas graphics engine evaluates the exact NIST Shomate and empirical polynomial equations dynamically. Moving the mouse across the curves triggers real-time raycasting tooltips showing exact temperature and specific heat coordinates. Notice how lightweight polymers like HDPE exhibit much higher specific heat values near 1850 J/(kg·K) compared to dense structural metals like Copper at 385 J/(kg·K)."*

---

### **2:30 – 3:15 | Scene 4: Unit Conversion & Extrapolation Warning**
* **Visual Action:**  
  1. Switch the $C_p$ Unit dropdown from `J/(kg*K)` to `J/(mol*K)`. Show how all elemental metals converge toward the Dulong-Petit asymptote (~25 J/mol·K).  
  2. Toggle Temperature Scale to `Celsius (°C)`.  
  3. Increase Max Temperature to `2000 K`. Highlight the amber **Warning Box** appearing above the plot.
* **Spoken Narration (Student 1):**  
  > *"The platform includes a 5-unit dimensional conversion engine. When switching to molar units, J/(mol·K), we observe the classical Dulong-Petit limit where all pure metals converge to approximately 25 J/(mol·K) at room temperature. If a user sets the temperature beyond a material's verified experimental limits, such as heating Aluminum above its melting point of 933 K, an automatic warning banner alerts the user against non-physical extrapolation."*

---

### **3:15 – 3:45 | Scene 5: Real-Time Ranking, Literature Citations & CSV Export**
* **Visual Action:**  
  1. Drag the Reference Temperature slider from `300 K` to `1200 K`, showing the Ranking Table sorting in real time.  
  2. Scroll through the Data Sources & Equations drawer.  
  3. Click **Export CSV** and open the downloaded spreadsheet.
* **Spoken Narration (Student 2):**  
  > *"Below the chart, our dynamic ranking table re-orders all active materials at any reference temperature selected on the slider. The literature drawer provides full source citations from NIST WebBook, JANAF, and NASA handbooks. Finally, clicking 'Export CSV' downloads the complete dataset for further analysis in MATLAB or Python. Thank you!"*
