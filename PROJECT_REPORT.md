# Project Report: Temperature-Dependent Specific Heat Capacity (Cp vs. T) Engineering Materials Database & Computational Platform

**Course**: Materials Science & Engineering / Computational Thermodynamics  
**Project Group**: Group Assessment (2-Student Team)  
**Deliverable**: Comprehensive Materials Database, Analytical Models, and Interactive Web Platform  

---

## 1. Executive Summary & Project Objectives

The accurate evaluation of temperature-dependent specific heat capacity, Cp(T), is critical for thermal management, high-temperature alloy processing, aerospace re-entry thermal protection systems (TPS), nuclear reactor cladding, and semiconductor microelectronics packaging. 

This project establishes an open-access, student-engineered computational platform and database comprising **230 engineering materials** categorized across **8 structural and functional classes**:
1. **Metals & Alloys** (Pure transition metals, refractory elements, aerospace titanium & nickel superalloys, steels, bronze)
2. **Ceramics & Oxides** (Structural oxides, high-temperature non-oxides, functional dielectrics)
3. **Semiconductors** (Elemental group IV, III-V optoelectronic compounds, II-VI infrared materials)
4. **Polymers & Elastomers** (Engineering thermoplastics, high-performance polyimides, thermosets)
5. **Glasses & Amorphous Solids** (Silicates, borosilicates, fused quartz, chalcogenide infrared optical glasses)
6. **Refractories & Ultra-High Temperature Ceramics (UHTCs)** (Borides, carbides, nitrides, graphite forms)
7. **Composites & Cermets** (Metal-matrix, ceramic-matrix, and reinforced structural composites)
8. **Advanced & Functional Materials** (Shape-memory alloys, solid-state electrolytes, thermoelectric compounds)

---

## 2. Fundamental Thermodynamics & Mathematical Models

### 2.1 Classical and Quantum Models
- **Dulong-Petit Law**: Predicts classical molar heat capacity at high temperatures:
  $$C_v = 3R \approx 24.94\text{ J/(mol}\cdot\text{K)}$$
- **Debye T^3 Law**: At cryogenic temperatures ($T < \theta_D / 10$), lattice phonon contributions scale cubically:
  $$C_v(T) = \frac{12\pi^4}{5} N k_B \left(\frac{T}{\theta_D}\right)^3$$
- **Sommerfeld Electronic Term**: For metallic conductors at low temperatures, conduction electron gas adds a linear term:
  $$C_p(T) \approx \gamma T + \beta T^3$$

### 2.2 NIST Shomate & Polynomial Equations
For engineering thermal calculations over wide operating ranges ($50\text{ K} \le T \le 3000\text{ K}$), standard NIST Shomate empirical equations are implemented:
$$t = \frac{T}{1000}$$
$$C_p^\circ(t) = A + B\cdot t + C\cdot t^2 + D\cdot t^3 + \frac{E}{t^2} \quad [\text{J}/(\text{mol}\cdot\text{K})]$$

Thermodynamic State Functions Derived from Closed-Form Integrals:
- **Enthalpy Increment**:
  $$H^\circ(t) - H_{298.15}^\circ = A\cdot t + B\frac{t^2}{2} + C\frac{t^3}{3} + D\frac{t^4}{4} - \frac{E}{t} + F - H_{298.15}^\circ \quad [\text{kJ}/\text{mol}]$$
- **Standard Entropy**:
  $$S^\circ(t) = A\ln(t) + B\cdot t + C\frac{t^2}{2} + D\frac{t^3}{3} - \frac{E}{2t^2} + G \quad [\text{J}/(\text{mol}\cdot\text{K})]$$

---

## 3. Computational Platform Architecture

- **Zero-Dependency Vector Graphics**: Interactive rendering implemented in standard SVG vector geometry, guaranteeing instant browser compatibility on all operating systems without external libraries or CDN dependencies.
- **Unit Conversion Engine**: Direct real-time conversion between 5 international thermal units:
  - $\text{J}/(\text{kg}\cdot\text{K})$ (SI Standard)
  - $\text{kJ}/(\text{kg}\cdot\text{K})$
  - $\text{cal}/(\text{g}\cdot^\circ\text{C})$
  - $\text{Btu}/(\text{lb}\cdot^\circ\text{F})$ (Imperial Engineering)
  - $\text{J}/(\text{mol}\cdot\text{K})$ (Molar Heat Capacity)
- **Dynamic Materials Comparison**: Multi-selection color tags with hover data coordinates, temperature slider, and live ranking tables.

---

## 4. Verification & Validation

1. **Mass Specific Heat Verification**: All NIST molar polynomial values normalized via exact molecular weights:
   $$c_p [\text{J}/(\text{kg}\cdot\text{K})] = \frac{C_p [\text{J}/(\text{mol}\cdot\text{K})]}{M [\text{g}/\text{mol}]} \times 1000$$
2. **Boundary Stability**: All 230 materials verified across their individual validity intervals without singularity or non-physical negative specific heat output.
3. **Peer Benchmark**: Aluminum ($900\text{ J/(kg}\cdot\text{K)}$ at $300\text{ K}$), Copper ($385\text{ J/(kg}\cdot\text{K)}$ at $300\text{ K}$), and Diamond ($512\text{ J/(kg}\cdot\text{K)}$ at $300\text{ K}$) strictly match experimental reference literature values.

---

## 5. References & Data Sources
1. NIST Chemistry WebBook, SRD 69 (National Institute of Standards and Technology).
2. CRC Handbook of Chemistry and Physics, 104th Edition, CRC Press.
3. Touloukian, Y.S., *Thermophysical Properties of Matter*, Vol. 4 & 5: Specific Heat, IFI/Plenum, New York.
4. Callister, W.D., & Rethwisch, D.G., *Materials Science and Engineering: An Introduction*, 10th Ed., Wiley.
5. Shackelford, J.F., *CRC Materials Science and Engineering Handbook*, 4th Ed.
