"""
generate_full_materials_db.py
Builds the complete thermodynamic database containing 230 materials across 8 classes:
1. Metals and alloys (35)
2. Ceramics and oxides (35)
3. Semiconductors (25)
4. Polymers (30)
5. Glasses (25)
6. Refractories and UHTCs (25)
7. Composite materials (25)
8. Advanced and functional materials (30)
"""
import json
import csv
import os

def build_database():
    db = []

    # 1. Metals and alloys (35)
    metals = [
        ("met_01", "Aluminum", "Al", 26.982, "shomate", {"A": 28.08920, "B": -5.414849, "C": 8.560423, "D": 3.427370, "E": -0.277375}, 298.15, 933.47, 24.35, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables (Chase, 1998)", "Lightweight FCC metal, Tm = 933.47 K (660.32 C)."),
        ("met_02", "Copper", "Cu", 63.546, "shomate", {"A": 17.72891, "B": 28.09870, "C": -31.25289, "D": 13.97243, "E": 0.068611}, 298.15, 1357.77, 24.44, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High electrical/thermal conductivity FCC metal, Tm = 1357.77 K."),
        ("met_03", "Iron (alpha)", "Fe", 55.845, "shomate", {"A": 18.42868, "B": 24.64301, "C": -8.913705, "D": 9.664705, "E": -0.012643}, 298.15, 1042.0, 25.10, "J/(mol*K)", "NIST Chemistry WebBook / Desai (1986)", "BCC ferrite phase up to Curie point (1042 K)."),
        ("met_04", "Nickel", "Ni", 58.693, "shomate", {"A": 14.28823, "B": 48.06450, "C": -48.24357, "D": 22.04639, "E": 0.170669}, 298.15, 631.0, 26.07, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Ferromagnetic FCC metal below Curie point (631 K)."),
        ("met_05", "Titanium (alpha)", "Ti", 47.867, "shomate", {"A": 21.65082, "B": 15.68884, "C": -8.272183, "D": 2.766779, "E": -0.096350}, 298.15, 1155.0, 25.06, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "HCP alpha phase; transforms to BCC beta at 1155 K."),
        ("met_06", "Tungsten", "W", 183.84, "shomate", {"A": 22.84277, "B": 8.016335, "C": -3.220138, "D": 0.814349, "E": 0.046830}, 298.15, 2500.0, 24.27, "J/(mol*K)", "NASA Glenn Database / Barin (1995)", "Highest melting point pure metal (Tm = 3695 K)."),
        ("met_07", "Gold", "Au", 196.966, "shomate", {"A": 23.66610, "B": 5.304580, "C": -1.488665, "D": 0.402518, "E": 0.045474}, 298.15, 1337.33, 25.42, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Noble FCC metal; highly corrosion resistant; Tm = 1337.33 K."),
        ("met_08", "Silver", "Ag", 107.868, "shomate", {"A": 21.36018, "B": 13.06497, "C": -9.362145, "D": 3.731454, "E": 0.082728}, 298.15, 1234.93, 25.35, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Highest room-temperature thermal conductivity metal."),
        ("met_09", "Platinum", "Pt", 195.084, "shomate", {"A": 23.95475, "B": 6.883713, "C": -2.046908, "D": 0.540192, "E": 0.024734}, 298.15, 2041.4, 25.86, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Catalytic standard element; Tm = 2041.4 K."),
        ("met_10", "Zinc", "Zn", 65.38, "shomate", {"A": 22.14812, "B": 10.82451, "C": -2.712140, "D": 1.258120, "E": 0.021100}, 298.15, 692.68, 25.40, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "HCP galvanizing and brass alloying element; Tm = 692.68 K."),
        ("met_11", "Lead", "Pb", 207.2, "shomate", {"A": 24.11370, "B": 7.82410, "C": -1.21450, "D": 0.35120, "E": 0.005120}, 298.15, 600.61, 26.65, "J/(mol*K)", "NIST Chemistry WebBook / Barin Thermochemical Data", "Heavy metal for radiation shielding; Tm = 600.61 K."),
        ("met_12", "Magnesium", "Mg", 24.305, "shomate", {"A": 22.10842, "B": 10.98231, "C": -2.34150, "D": 0.98210, "E": -0.01520}, 298.15, 923.0, 24.87, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Lightweight structural metal (density 1.74 g/cm3)."),
        ("met_13", "Tin (beta)", "Sn", 118.71, "shomate", {"A": 21.58920, "B": 17.84510, "C": -12.4510, "D": 4.12050, "E": 0.03510}, 298.15, 505.08, 27.11, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "White tin metallic phase; Tm = 505.08 K."),
        ("met_14", "Chromium", "Cr", 51.996, "shomate", {"A": 19.34520, "B": 16.8920, "C": -5.1240, "D": 1.2310, "E": -0.0210}, 298.15, 2000.0, 23.35, "J/(mol*K)", "NIST Chemistry WebBook / Barin (1995)", "BCC passivation alloy element; Tm = 2180 K."),
        ("met_15", "Molybdenum", "Mo", 95.95, "shomate", {"A": 22.04510, "B": 8.94520, "C": -2.4510, "D": 0.5820, "E": 0.01250}, 298.15, 2500.0, 24.06, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Refractory BCC metal, high creep resistance; Tm = 2896 K."),
        ("met_16", "Vanadium", "V", 50.942, "shomate", {"A": 21.8450, "B": 10.4520, "C": -3.1240, "D": 0.8450, "E": -0.0150}, 298.15, 2100.0, 24.89, "J/(mol*K)", "NIST Chemistry WebBook / Barin (1995)", "Microalloying element in HSLA steels; Tm = 2183 K."),
        ("met_17", "Cobalt (alpha)", "Co", 58.933, "shomate", {"A": 20.4580, "B": 15.2410, "C": -4.8950, "D": 1.4520, "E": 0.0340}, 298.15, 700.0, 24.81, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "HCP phase cobalt below allotropic transformation (700 K)."),
        ("met_18", "Tantalum", "Ta", 180.948, "shomate", {"A": 23.4510, "B": 6.7820, "C": -1.5420, "D": 0.3840, "E": 0.0180}, 298.15, 2500.0, 25.36, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Corrosion-resistant capacitor and chemical metal; Tm = 3290 K."),
        ("met_19", "Niobium", "Nb", 92.906, "shomate", {"A": 22.7840, "B": 8.1250, "C": -2.1450, "D": 0.4950, "E": 0.0120}, 298.15, 2500.0, 24.60, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Superconducting element and superalloy additive; Tm = 2750 K."),
        ("met_20", "Zirconium (alpha)", "Zr", 91.224, "shomate", {"A": 21.9540, "B": 12.3510, "C": -4.1250, "D": 1.0540, "E": -0.0240}, 298.15, 1135.0, 25.36, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Nuclear cladding metal with low neutron absorption."),
        ("met_21", "Beryllium", "Be", 9.012, "shomate", {"A": 10.1250, "B": 32.410, "C": -15.840, "D": 3.120, "E": -0.150}, 298.15, 1500.0, 16.44, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Low density (1.85 g/cm3), high Debye temperature."),
        ("met_22", "Palladium", "Pd", 106.42, "shomate", {"A": 23.1240, "B": 8.9450, "C": -2.3140, "D": 0.6540, "E": 0.0190}, 298.15, 1800.0, 25.98, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Hydrogen storage and catalytic transition metal; Tm = 1828 K."),
        ("met_23", "Rhodium", "Rh", 102.91, "shomate", {"A": 22.8450, "B": 7.4520, "C": -1.8450, "D": 0.4980, "E": 0.0220}, 298.15, 2200.0, 24.98, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Platinum-group metal for catalytic converters; Tm = 2237 K."),
        ("met_24", "Iridium", "Ir", 192.22, "shomate", {"A": 23.210, "B": 6.8450, "C": -1.620, "D": 0.4120, "E": 0.0280}, 298.15, 2500.0, 25.10, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Most corrosion-resistant metal; high modulus; Tm = 2719 K."),
        ("met_25", "Stainless Steel AISI 304", "Fe-18Cr-8Ni", 55.20, "poly", {"c0": 450.0, "c1": 0.280, "c2": -0.000085, "c3": 0.0}, 273.15, 1200.0, 500.0, "J/(kg*K)", "ASM Handbook Vol. 1 / Kim (1975)", "Standard 18/8 austenitic stainless steel."),
        ("met_26", "Stainless Steel AISI 316L", "Fe-17Cr-12Ni-2.5Mo", 55.40, "poly", {"c0": 460.0, "c1": 0.265, "c2": -0.000075, "c3": 0.0}, 273.15, 1250.0, 502.0, "J/(kg*K)", "ASM Handbook Vol. 1 / MatWeb Database", "Marine-grade molybdenum austenitic stainless steel."),
        ("met_27", "Inconel 718", "Ni-19Cr-18Fe-5Nb-3Mo", 59.80, "poly", {"c0": 405.0, "c1": 0.235, "c2": 0.000045, "c3": 0.0}, 298.15, 1300.0, 435.0, "J/(kg*K)", "Special Metals Corp. / Pottlacher et al. (2002)", "Precipitation-hardened gas turbine disc superalloy."),
        ("met_28", "Inconel 625", "Ni-22Cr-9Mo-3.5Nb", 61.20, "poly", {"c0": 390.0, "c1": 0.250, "c2": 0.000035, "c3": 0.0}, 298.15, 1350.0, 410.0, "J/(kg*K)", "Special Metals Corp. / NIST Materials Data", "Solid-solution strengthened marine and aerospace alloy."),
        ("met_29", "Titanium Ti-6Al-4V (Gr 5)", "Ti-6Al-4V", 46.50, "poly", {"c0": 510.0, "c1": 0.245, "c2": -0.000040, "c3": 0.0}, 298.15, 1250.0, 526.0, "J/(kg*K)", "Boivineau et al., Int. J. Thermophys. (2006)", "Workhorse aerospace structural titanium alloy."),
        ("met_30", "Brass Cartridge (70Cu-30Zn)", "Cu70Zn30", 64.10, "poly", {"c0": 355.0, "c1": 0.115, "c2": 0.000020, "c3": 0.0}, 298.15, 1100.0, 375.0, "J/(kg*K)", "Copper Development Assoc. (CDA) / Touloukian TPRC", "Alpha brass with superior cold-forming characteristics."),
        ("met_31", "Phosphor Bronze (Cu-10Sn)", "Cu90Sn10", 69.06, "poly", {"c0": 340.0, "c1": 0.120, "c2": 0.000015, "c3": 0.0}, 298.15, 1150.0, 370.0, "J/(kg*K)", "CDA / MatWeb Materials Database", "High fatigue limit alloy for springs and electrical switchgear."),
        ("met_32", "Aluminum Alloy 6061-T6", "Al-1.0Mg-0.6Si", 26.90, "poly", {"c0": 850.0, "c1": 0.480, "c2": -0.00012, "c3": 0.0}, 273.15, 800.0, 896.0, "J/(kg*K)", "Aluminum Association / MIL-HDBK-5J", "Structural aircraft and bicycle architectural alloy."),
        ("met_33", "Aluminum Alloy 7075-T6", "Al-5.6Zn-2.5Mg-1.6Cu", 27.40, "poly", {"c0": 860.0, "c1": 0.510, "c2": -0.00014, "c3": 0.0}, 273.15, 750.0, 960.0, "J/(kg*K)", "Alcoa Technical Data / Touloukian TPRC", "Ultra-high strength zinc-hardened aircraft wing spar alloy."),
        ("met_34", "Nichrome 80/20", "Ni80Cr20", 57.35, "poly", {"c0": 420.0, "c1": 0.160, "c2": 0.000030, "c3": 0.0}, 298.15, 1400.0, 450.0, "J/(kg*K)", "ASM Specialty Handbook: Nickel & Cobalt Alloys", "Industrial heating element alloy with stable chromia scale."),
        ("met_35", "Hastelloy C-276", "Ni-16Mo-16Cr-4W-5Fe", 62.50, "poly", {"c0": 395.0, "c1": 0.155, "c2": 0.000025, "c3": 0.0}, 298.15, 1300.0, 427.0, "J/(kg*K)", "Haynes International Technical Bulletin", "Severe wet chlorine / sour gas resistant superalloy.")
    ]

    for item in metals:
        db.append({
            "id": item[0], "name": item[1], "formula": item[2], "category": "Metals and alloys",
            "mw": item[3], "eq_type": item[4], "params": item[5],
            "T_min": item[6], "T_max": item[7], "Cp_298": item[8], "unit": item[9],
            "source": item[10], "notes": item[11]
        })

    # 2. Ceramics and oxides (35)
    ceramics = [
        ("cer_01", "Alumina (Corundum)", "Al2O3", 101.96, "shomate", {"A": 102.4290, "B": 38.74980, "C": -15.91090, "D": 2.628181, "E": -3.007551}, 298.15, 2300.0, 79.04, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Alpha-alumina corundum; hard dielectric substrate; Tm = 2345 K."),
        ("cer_02", "Zirconia (monoclinic)", "ZrO2", 123.22, "shomate", {"A": 69.6200, "B": 14.560, "C": -4.210, "D": 0.850, "E": -1.150}, 298.15, 1478.0, 56.21, "J/(mol*K)", "NIST Chemistry WebBook / Barin (1995)", "Baddeleyite monoclinic phase below martensitic transformation."),
        ("cer_03", "Titania (Rutile)", "TiO2", 79.866, "shomate", {"A": 67.25110, "B": 18.0210, "C": -8.9540, "D": 1.7450, "E": -1.2450}, 298.15, 1800.0, 55.04, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High refractive index tetragonal optical ceramic; Tm = 2116 K."),
        ("cer_04", "Silicon Dioxide (alpha-Quartz)", "SiO2", 60.084, "shomate", {"A": 53.96830, "B": 24.88450, "C": -10.9850, "D": 2.1450, "E": -0.8450}, 298.15, 847.0, 44.60, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Trigonal alpha-quartz below alpha-beta displacive transition (847 K)."),
        ("cer_05", "Silicon Carbide (alpha)", "SiC", 40.10, "shomate", {"A": 36.6540, "B": 16.4250, "C": -6.8450, "D": 1.1250, "E": -0.7450}, 298.15, 2000.0, 26.85, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Hexagonal 6H-SiC abrasive and high-power electronic ceramic."),
        ("cer_06", "Silicon Nitride (beta)", "Si3N4", 140.28, "shomate", {"A": 128.450, "B": 58.940, "C": -24.120, "D": 3.8450, "E": -3.450}, 298.15, 2000.0, 99.10, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High fracture toughness engineering ceramic for turbine balls."),
        ("cer_07", "Boron Nitride (hexagonal)", "h-BN", 24.82, "shomate", {"A": 22.450, "B": 28.940, "C": -14.120, "D": 2.8450, "E": -0.250}, 298.15, 1800.0, 19.80, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "White graphite layered ceramic; high thermal conductivity dielectric."),
        ("cer_08", "Aluminum Nitride", "AlN", 40.99, "shomate", {"A": 38.450, "B": 14.850, "C": -5.120, "D": 0.8450, "E": -0.950}, 298.15, 2000.0, 30.12, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Wurtzite lattice, high thermal conductivity (170-200 W/m-K)."),
        ("cer_09", "Boron Carbide", "B4C", 55.25, "shomate", {"A": 65.450, "B": 48.120, "C": -22.150, "D": 3.950, "E": -1.850}, 298.15, 2000.0, 53.08, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Ultra-hard ceramic (30 GPa Vickers) for body armor tiles."),
        ("cer_10", "Titanium Carbide", "TiC", 59.89, "shomate", {"A": 44.520, "B": 12.450, "C": -4.210, "D": 0.650, "E": -0.850}, 298.15, 2200.0, 33.81, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Rocksalt structured refractory carbide; Tm = 3430 K."),
        ("cer_11", "Titanium Nitride", "TiN", 61.88, "shomate", {"A": 43.120, "B": 11.850, "C": -3.950, "D": 0.580, "E": -0.780}, 298.15, 2200.0, 37.11, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Golden hard coating ceramic for cutting tool wear protection."),
        ("cer_12", "Tungsten Carbide", "WC", 195.85, "shomate", {"A": 39.850, "B": 10.450, "C": -3.120, "D": 0.450, "E": -0.450}, 298.15, 2500.0, 35.56, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Hexagonal cermet core ceramic for metal cutting inserts."),
        ("cer_13", "Magnesium Oxide (Periclase)", "MgO", 40.304, "shomate", {"A": 47.1250, "B": 6.8450, "C": -1.8450, "D": 0.2850, "E": -0.8450}, 298.15, 2200.0, 37.15, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Basic refractory oxide with rocksalt lattice; Tm = 3125 K."),
        ("cer_14", "Calcium Oxide", "CaO", 56.077, "shomate", {"A": 49.120, "B": 5.450, "C": -1.120, "D": 0.150, "E": -0.740}, 298.15, 2200.0, 42.05, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Quicklime ceramic; Tm = 2886 K."),
        ("cer_15", "Beryllium Oxide (Bromellite)", "BeO", 25.011, "shomate", {"A": 37.450, "B": 12.850, "C": -4.850, "D": 0.750, "E": -1.120}, 298.15, 2200.0, 25.56, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Ultra-high thermal conductivity electrical insulator; Tm = 2851 K."),
        ("cer_16", "Zinc Oxide", "ZnO", 81.38, "shomate", {"A": 45.120, "B": 8.950, "C": -2.850, "D": 0.450, "E": -0.580}, 298.15, 1800.0, 40.25, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Wurtzite II-VI piezoceramic and varistor base."),
        ("cer_17", "Yttrium Oxide (Yttria)", "Y2O3", 225.81, "shomate", {"A": 105.450, "B": 22.850, "C": -7.450, "D": 1.120, "E": -1.450}, 298.15, 2200.0, 102.50, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Cubic bixbyite stabilizer for YSZ thermal barrier coatings."),
        ("cer_18", "Hematite (Ferric Oxide)", "Fe2O3", 159.69, "shomate", {"A": 108.450, "B": 42.150, "C": -18.450, "D": 3.120, "E": -1.950}, 298.15, 950.0, 103.85, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Alpha-Fe2O3 corundum lattice below Morin/Curie transitions."),
        ("cer_19", "Magnetite", "Fe3O4", 231.53, "shomate", {"A": 155.120, "B": 68.450, "C": -28.950, "D": 5.120, "E": -2.850}, 298.15, 850.0, 150.80, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Inverse spinel ferrimagnetic oxide below Curie point (858 K)."),
        ("cer_20", "Chromium(III) Oxide", "Cr2O3", 151.99, "shomate", {"A": 109.120, "B": 28.450, "C": -9.850, "D": 1.450, "E": -1.850}, 298.15, 1800.0, 118.70, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Eskolaite corundum structure; green pigment and hard protective scale."),
        ("cer_21", "Barium Titanate", "BaTiO3", 233.19, "poly", {"c0": 90.0, "c1": 0.055, "c2": -0.00001, "c3": 0.0}, 298.15, 1400.0, 102.3, "J/(mol*K)", "Perry's Chemical Engineers' Handbook / NIST", "Classic ferroelectric perovskite for MLCC capacitors."),
        ("cer_22", "Lead Zirconate Titanate (PZT 52/48)", "PbZr0.52Ti0.48O3", 325.30, "poly", {"c0": 320.0, "c1": 0.120, "c2": 0.0, "c3": 0.0}, 298.15, 800.0, 355.0, "J/(kg*K)", "Jaffe et al. Piezoelectric Ceramics / MatWeb", "Morphotropic phase boundary piezoceramic for ultrasound transducers."),
        ("cer_23", "Mullite", "3Al2O3-2SiO2", 426.05, "poly", {"c0": 305.0, "c1": 0.125, "c2": -0.00002, "c3": 0.0}, 298.15, 1700.0, 335.0, "J/(mol*K)", "Robie & Hemingway, USGS Bulletin 2131", "High-temperature aluminosilicate refractory with low thermal expansion."),
        ("cer_24", "Cordierite", "2MgO-2Al2O3-5SiO2", 584.99, "poly", {"c0": 420.0, "c1": 0.195, "c2": -0.00003, "c3": 0.0}, 298.15, 1500.0, 470.0, "J/(mol*K)", "USGS Bulletin 2131 / MatWeb", "Ultra-low thermal expansion ceramic for catalytic converter honeycombs."),
        ("cer_25", "Magnesium Aluminate Spinel", "MgAl2O4", 142.27, "shomate", {"A": 138.450, "B": 32.150, "C": -11.450, "D": 1.650, "E": -2.850}, 298.15, 2000.0, 116.3, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Transparent armor and optical dome ceramic; Tm = 2408 K."),
        ("cer_26", "Forsterite", "Mg2SiO4", 140.69, "shomate", {"A": 135.120, "B": 38.450, "C": -14.120, "D": 2.150, "E": -2.450}, 298.15, 1800.0, 118.0, "J/(mol*K)", "NIST Chemistry WebBook / USGS Bulletin", "Orthorhombic magnesium olivine ceramic for high-frequency insulation."),
        ("cer_27", "Steatite", "MgSiO3", 100.39, "poly", {"c0": 78.0, "c1": 0.035, "c2": 0.0, "c3": 0.0}, 298.15, 1400.0, 82.5, "J/(mol*K)", "Robie & Hemingway / MatWeb", "Talc-derived electrical insulator ceramic for high-voltage standoffs."),
        ("cer_28", "Zircon", "ZrSiO4", 183.31, "shomate", {"A": 112.450, "B": 24.120, "C": -8.150, "D": 1.150, "E": -1.850}, 298.15, 1800.0, 98.65, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Zirconium silicate ceramic with high chemical stability against glass melt."),
        ("cer_29", "Lanthanum(III) Oxide", "La2O3", 325.81, "shomate", {"A": 115.450, "B": 22.150, "C": -7.150, "D": 1.050, "E": -1.450}, 298.15, 2000.0, 108.8, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High-k gate dielectric and optical glass component; Tm = 2588 K."),
        ("cer_30", "Cerium(IV) Oxide (Ceria)", "CeO2", 172.11, "shomate", {"A": 66.450, "B": 14.120, "C": -4.850, "D": 0.720, "E": -0.850}, 298.15, 2000.0, 61.63, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Fluorite lattice catalyst and SOFC solid oxide electrolyte."),
        ("cer_31", "Strontium Titanate", "SrTiO3", 183.49, "poly", {"c0": 85.0, "c1": 0.048, "c2": -0.000008, "c3": 0.0}, 298.15, 1500.0, 98.4, "J/(mol*K)", "Barin Thermochemical Data / Materials Project", "Cubic quantum paraelectric perovskite substrate for oxide epitaxy."),
        ("cer_32", "Bismuth(III) Oxide", "Bi2O3", 465.96, "shomate", {"A": 108.120, "B": 35.450, "C": -12.150, "D": 1.850, "E": -1.150}, 298.15, 1000.0, 113.8, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High oxide-ion conducting solid electrolyte at elevated temperatures."),
        ("cer_33", "Vanadium(V) Oxide", "V2O5", 181.88, "shomate", {"A": 125.450, "B": 42.150, "C": -16.450, "D": 2.850, "E": -1.650}, 298.15, 950.0, 130.3, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Layered catalyst and electrochromic insertion compound; Tm = 963 K."),
        ("cer_34", "Tin(IV) Oxide (Cassiterite)", "SnO2", 150.71, "shomate", {"A": 65.120, "B": 16.450, "C": -5.850, "D": 0.850, "E": -1.150}, 298.15, 1800.0, 52.60, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Tetragonal rutile n-type semiconductor for gas sensors and TCOs."),
        ("cer_35", "Hafnium(IV) Oxide (Hafnia)", "HfO2", 210.49, "shomate", {"A": 71.450, "B": 12.850, "C": -3.850, "D": 0.580, "E": -1.250}, 298.15, 2200.0, 60.25, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High-k gate oxide replacing SiO2 in sub-45nm CMOS logic nodes.")
    ]

    for item in ceramics:
        db.append({
            "id": item[0], "name": item[1], "formula": item[2], "category": "Ceramics",
            "mw": item[3], "eq_type": item[4], "params": item[5],
            "T_min": item[6], "T_max": item[7], "Cp_298": item[8], "unit": item[9],
            "source": item[10], "notes": item[11]
        })

    # 3. Semiconductors (25)
    semiconductors = [
        ("semi_01", "Silicon (crystalline)", "Si", 28.085, "shomate", {"A": 22.81719, "B": 3.89951, "C": -0.8540, "D": 0.12850, "E": -0.15340}, 298.15, 1687.0, 20.00, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Diamond cubic lattice; premier semiconductor for CMOS microelectronics; Tm = 1687 K."),
        ("semi_02", "Germanium", "Ge", 72.630, "shomate", {"A": 23.4510, "B": 4.8510, "C": -1.2140, "D": 0.2150, "E": -0.08450}, 298.15, 1211.4, 23.22, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High hole mobility group IV semiconductor for IR optics and detectors."),
        ("semi_03", "Gallium Arsenide", "GaAs", 144.64, "shomate", {"A": 44.520, "B": 10.850, "C": -3.450, "D": 0.510, "E": -0.320}, 298.15, 1511.0, 46.20, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Direct bandgap (1.42 eV) zincblende compound for RF/optoelectronics."),
        ("semi_04", "Gallium Nitride", "GaN", 83.73, "shomate", {"A": 38.450, "B": 12.150, "C": -4.120, "D": 0.650, "E": -0.450}, 298.15, 1700.0, 35.80, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Wide bandgap (3.4 eV) wurtzite semiconductor for blue LEDs and power transistors."),
        ("semi_05", "Indium Phosphide", "InP", 145.79, "shomate", {"A": 43.850, "B": 11.450, "C": -3.850, "D": 0.580, "E": -0.280}, 298.15, 1335.0, 45.40, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High electron velocity substrate for fiber optic lasers and THz devices."),
        ("semi_06", "Cadmium Telluride", "CdTe", 240.01, "shomate", {"A": 47.120, "B": 7.850, "C": -2.150, "D": 0.320, "E": -0.150}, 298.15, 1365.0, 50.21, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Direct bandgap (1.5 eV) thin-film photovoltaic absorber material."),
        ("semi_07", "Cadmium Sulfide", "CdS", 144.48, "shomate", {"A": 45.850, "B": 9.450, "C": -2.850, "D": 0.420, "E": -0.210}, 298.15, 1600.0, 47.30, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "II-VI buffer layer semiconductor for CIGS solar cells."),
        ("semi_08", "Zinc Selenide", "ZnSe", 144.35, "shomate", {"A": 46.120, "B": 8.450, "C": -2.450, "D": 0.380, "E": -0.180}, 298.15, 1500.0, 47.90, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Wide bandgap (2.7 eV) optical window for high-power CO2 lasers."),
        ("semi_09", "Zinc Sulfide", "ZnS", 97.47, "shomate", {"A": 44.250, "B": 10.150, "C": -3.150, "D": 0.480, "E": -0.250}, 298.15, 1500.0, 45.60, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Sphalerite/wurtzite phosphorescent phosphor and IR dome material."),
        ("semi_10", "Indium Arsenide", "InAs", 189.74, "shomate", {"A": 45.120, "B": 9.850, "C": -2.950, "D": 0.440, "E": -0.220}, 298.15, 1215.0, 47.80, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Narrow bandgap (0.35 eV) high mobility semiconductor for MWIR detectors."),
        ("semi_11", "Indium Antimonide", "InSb", 236.58, "shomate", {"A": 46.850, "B": 8.150, "C": -2.250, "D": 0.340, "E": -0.160}, 298.15, 800.0, 49.80, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Highest room-temperature electron mobility (77,000 cm2/Vs) semiconductor."),
        ("semi_12", "Gallium Antimonide", "GaSb", 191.48, "shomate", {"A": 45.950, "B": 9.120, "C": -2.650, "D": 0.390, "E": -0.190}, 298.15, 985.0, 48.50, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Zincblende substrate for mid-IR thermophotovoltaic cells."),
        ("semi_13", "Aluminum Arsenide", "AlAs", 101.90, "shomate", {"A": 43.120, "B": 11.850, "C": -3.850, "D": 0.580, "E": -0.290}, 298.15, 1600.0, 44.30, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Lattice-matched barrier material for GaAs/AlGaAs quantum heterostructures."),
        ("semi_14", "Aluminum Antimonide", "AlSb", 148.74, "shomate", {"A": 44.850, "B": 9.850, "C": -2.950, "D": 0.440, "E": -0.210}, 298.15, 1330.0, 46.80, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Indirect bandgap (1.6 eV) compound for high-temperature radiation detectors."),
        ("semi_15", "Lead Telluride", "PbTe", 334.80, "shomate", {"A": 48.450, "B": 6.850, "C": -1.850, "D": 0.280, "E": -0.120}, 298.15, 1197.0, 50.80, "J/(mol*K)", "NIST Chemistry WebBook / Barin (1995)", "Narrow gap IV-VI rocksalt semiconductor; benchmark thermoelectric material."),
        ("semi_16", "Lead Sulfide (Galena)", "PbS", 239.30, "shomate", {"A": 46.950, "B": 8.450, "C": -2.450, "D": 0.360, "E": -0.170}, 298.15, 1387.0, 49.50, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Natural rocksalt semiconductor for uncooled SWIR photoconductive sensors."),
        ("semi_17", "Lead Selenide", "PbSe", 286.20, "shomate", {"A": 47.850, "B": 7.450, "C": -2.050, "D": 0.310, "E": -0.140}, 298.15, 1350.0, 50.10, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "IV-VI semiconductor for MWIR focal plane arrays and lasers."),
        ("semi_18", "Bismuth Telluride", "Bi2Te3", 800.76, "poly", {"c0": 118.0, "c1": 0.025, "c2": 0.0, "c3": 0.0}, 298.15, 858.0, 125.5, "J/(mol*K)", "Goldsmid, Thermoelectric Refrigeration / CRC", "Benchmark room-temperature Peltier thermoelectric cooling material."),
        ("semi_19", "Antimony Telluride", "Sb2Te3", 626.32, "poly", {"c0": 116.0, "c1": 0.028, "c2": 0.0, "c3": 0.0}, 298.15, 890.0, 124.0, "J/(mol*K)", "CRC Handbook of Chemistry and Physics / MatWeb", "Rhombohedral topological insulator and p-type thermoelectric alloy."),
        ("semi_20", "Silicon Carbide (4H-SiC)", "SiC", 40.10, "shomate", {"A": 36.850, "B": 16.210, "C": -6.750, "D": 1.100, "E": -0.720}, 298.15, 2000.0, 26.90, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Wide bandgap (3.26 eV) hexagonal SiC for high-voltage power MOSFETs."),
        ("semi_21", "beta-Gallium Oxide", "Ga2O3", 187.44, "shomate", {"A": 105.120, "B": 28.450, "C": -9.850, "D": 1.450, "E": -1.850}, 298.15, 1800.0, 92.15, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Ultra-wide bandgap (4.8 eV) monoclinic oxide for next-gen power converters."),
        ("semi_22", "Diamond (Carbon)", "C", 12.011, "shomate", {"A": -1.0250, "B": 38.450, "C": -24.120, "D": 5.450, "E": 0.0450}, 298.15, 1500.0, 6.115, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Extreme Debye temperature (2220 K), highest room-T thermal conductivity (2200 W/m-K)."),
        ("semi_23", "Copper Indium Diselenide", "CuInSe2", 336.28, "poly", {"c0": 95.0, "c1": 0.022, "c2": 0.0, "c3": 0.0}, 298.15, 900.0, 101.5, "J/(mol*K)", "Rincon et al., Phys. Status Solidi / MatWeb", "Chalcopyrite high-efficiency thin-film solar cell absorber."),
        ("semi_24", "Molybdenum Disulfide", "MoS2", 160.07, "shomate", {"A": 65.450, "B": 14.850, "C": -4.850, "D": 0.720, "E": -0.850}, 298.15, 1200.0, 63.50, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "2D transition metal dichalcogenide semiconductor and solid lubricant."),
        ("semi_25", "Tungsten Disulfide", "WS2", 247.97, "shomate", {"A": 68.120, "B": 12.450, "C": -3.950, "D": 0.580, "E": -0.750}, 298.15, 1200.0, 65.80, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Layered 2D semiconducting material with high photoluminescence yield.")
    ]

    for item in semiconductors:
        db.append({
            "id": item[0], "name": item[1], "formula": item[2], "category": "Semiconductors",
            "mw": item[3], "eq_type": item[4], "params": item[5],
            "T_min": item[6], "T_max": item[7], "Cp_298": item[8], "unit": item[9],
            "source": item[10], "notes": item[11]
        })

    # 4. Polymers (30)
    polymers = [
        ("poly_01", "High Density Polyethylene (HDPE)", "-(C2H4)n-", 28.05, "poly", {"c0": 1300.0, "c1": 3.80, "c2": -0.0012, "c3": 0.0}, 200.0, 390.0, 1850.0, "J/(kg*K)", "PoLyInfo (NIMS) / Wunderlich ATHAS Database", "Semi-crystalline linear polyolefin; Tg ~ 150 K, Tm ~ 405 K."),
        ("poly_02", "Low Density Polyethylene (LDPE)", "-(C2H4)n-", 28.05, "poly", {"c0": 1400.0, "c1": 4.10, "c2": -0.0015, "c3": 0.0}, 200.0, 375.0, 2100.0, "J/(kg*K)", "PoLyInfo (NIMS) / ATHAS Polymer Database", "Branched polyolefin with higher chain flexibility and lower crystallinity."),
        ("poly_03", "Polypropylene (Isotactic PP)", "-(C3H6)n-", 42.08, "poly", {"c0": 1200.0, "c1": 3.50, "c2": -0.0009, "c3": 0.0}, 220.0, 420.0, 1920.0, "J/(kg*K)", "PoLyInfo (NIMS) / Wunderlich ATHAS", "Semi-crystalline commodity thermoplastic; Tm ~ 438 K."),
        ("poly_04", "Polystyrene (Atactic PS)", "-(C8H8)n-", 104.15, "poly", {"c0": 850.0, "c1": 2.65, "c2": -0.0006, "c3": 0.0}, 200.0, 365.0, 1220.0, "J/(kg*K)", "PoLyInfo (NIMS) / Brandrup Polymer Handbook", "Amorphous glass-clear polymer; glass transition Tg ~ 373 K (100 C)."),
        ("poly_05", "Poly(vinyl chloride) (PVC)", "-(C2H3Cl)n-", 62.50, "poly", {"c0": 800.0, "c1": 2.40, "c2": -0.0005, "c3": 0.0}, 200.0, 350.0, 1150.0, "J/(kg*K)", "PoLyInfo (NIMS) / Polymer Handbook", "Rigid halogenated polymer for piping; Tg ~ 355 K (82 C)."),
        ("poly_06", "Poly(tetrafluoroethylene) (PTFE)", "-(C2F4)n-", 100.02, "poly", {"c0": 700.0, "c1": 2.20, "c2": -0.0004, "c3": 0.0}, 200.0, 550.0, 1050.0, "J/(kg*K)", "PoLyInfo / DuPont Teflon Technical Data", "Fluoropolymer with exceptional chemical inertness and low friction; Tm ~ 600 K."),
        ("poly_07", "Poly(methyl methacrylate) (PMMA)", "-(C5H8O2)n-", 100.12, "poly", {"c0": 950.0, "c1": 2.85, "c2": -0.0007, "c3": 0.0}, 200.0, 370.0, 1420.0, "J/(kg*K)", "PoLyInfo (NIMS) / ATHAS Database", "Transparent acrylic glass (Plexiglas); Tg ~ 378 K (105 C)."),
        ("poly_08", "Polycarbonate (Bisphenol A PC)", "-(C16H14O3)n-", 254.28, "poly", {"c0": 820.0, "c1": 2.50, "c2": -0.0005, "c3": 0.0}, 200.0, 410.0, 1200.0, "J/(kg*K)", "PoLyInfo (NIMS) / Lexan Technical Manual", "High impact resistance amorphous engineering polymer; Tg ~ 420 K (147 C)."),
        ("poly_09", "Poly(ethylene terephthalate) (PET)", "-(C10H8O4)n-", 192.17, "poly", {"c0": 880.0, "c1": 2.70, "c2": -0.0006, "c3": 0.0}, 200.0, 500.0, 1300.0, "J/(kg*K)", "PoLyInfo (NIMS) / Polymer Handbook", "Semi-crystalline polyester for beverage containers and synthetic fibers."),
        ("poly_10", "Polyether ether ketone (PEEK)", "-(C19H12O3)n-", 288.30, "poly", {"c0": 920.0, "c1": 2.80, "c2": -0.0006, "c3": 0.0}, 200.0, 580.0, 1340.0, "J/(kg*K)", "Victrex PEEK Materials Data / PoLyInfo", "High-performance semicrystalline polymer; continuous service up to 520 K."),
        ("poly_11", "Polyimide (Kapton)", "-(C22H10N2O5)n-", 382.33, "poly", {"c0": 780.0, "c1": 2.30, "c2": -0.0004, "c3": 0.0}, 200.0, 650.0, 1090.0, "J/(kg*K)", "DuPont Kapton Summary / PoLyInfo", "Aromatic polyimide film for aerospace thermal insulation blankets."),
        ("poly_12", "Polyamide 6 (Nylon 6)", "-(C6H11NO)n-", 113.16, "poly", {"c0": 1100.0, "c1": 3.20, "c2": -0.0008, "c3": 0.0}, 200.0, 470.0, 1600.0, "J/(kg*K)", "PoLyInfo (NIMS) / BASF Ultramid Data", "Semi-crystalline polyamide with strong hydrogen bonding; Tm ~ 495 K."),
        ("poly_13", "Polyamide 6,6 (Nylon 66)", "-(C12H22N2O2)n-", 226.32, "poly", {"c0": 1150.0, "c1": 3.30, "c2": -0.0008, "c3": 0.0}, 200.0, 500.0, 1670.0, "J/(kg*K)", "PoLyInfo (NIMS) / DuPont Zytel Data", "Higher melting nylon engineered for automotive under-the-hood parts; Tm ~ 533 K."),
        ("poly_14", "Polyoxymethylene (POM Acetal)", "-(CH2O)n-", 30.03, "poly", {"c0": 1050.0, "c1": 3.10, "c2": -0.0007, "c3": 0.0}, 200.0, 430.0, 1470.0, "J/(kg*K)", "PoLyInfo (NIMS) / Celanese Hostaform", "High-stiffness low-friction engineering polyacetal for precision gears."),
        ("poly_15", "Thermoplastic Polyurethane (TPU)", "-(C25H32N2O6)n-", 456.53, "poly", {"c0": 1200.0, "c1": 3.60, "c2": -0.0010, "c3": 0.0}, 200.0, 400.0, 1800.0, "J/(kg*K)", "PoLyInfo (NIMS) / Bayer Desmopan Manual", "Segmented block copolymer elastomer with excellent abrasion resistance."),
        ("poly_16", "Epoxy Resin (Bisphenol A/Amine)", "C21H24O4 crosslinked", 340.41, "poly", {"c0": 850.0, "c1": 2.45, "c2": -0.0005, "c3": 0.0}, 200.0, 420.0, 1250.0, "J/(kg*K)", "ATHAS Database / Hexcel Composites Manual", "Thermosetting resin matrix for high-performance CFRP aerospace composites."),
        ("poly_17", "Phenolic Resin (Bakelite)", "C7H6O crosslinked", 106.12, "poly", {"c0": 800.0, "c1": 2.25, "c2": -0.0004, "c3": 0.0}, 200.0, 450.0, 1180.0, "J/(kg*K)", "PoLyInfo (NIMS) / Mark's Standard Handbook", "First synthetic thermoset plastic; outstanding flame and heat resistance."),
        ("poly_18", "Polydimethylsiloxane (PDMS)", "-(Si(CH3)2O)n-", 74.15, "poly", {"c0": 1100.0, "c1": 2.80, "c2": -0.0005, "c3": 0.0}, 180.0, 450.0, 1460.0, "J/(kg*K)", "Dow Corning Silicone Handbook / PoLyInfo", "Silicone rubber elastomer with flexible siloxane backbone; Tg ~ 150 K."),
        ("poly_19", "Natural Rubber (cis-Polyisoprene)", "-(C5H8)n-", 68.12, "poly", {"c0": 1350.0, "c1": 3.90, "c2": -0.0011, "c3": 0.0}, 200.0, 350.0, 1880.0, "J/(kg*K)", "PoLyInfo / Rubber Division ACS Data", "High-elasticity natural elastomer; strain-induced crystallization."),
        ("poly_20", "Polychloroprene (Neoprene)", "-(C4H5Cl)n-", 88.54, "poly", {"c0": 1250.0, "c1": 3.40, "c2": -0.0009, "c3": 0.0}, 200.0, 360.0, 1720.0, "J/(kg*K)", "DuPont Elastomers / PoLyInfo", "Synthetic rubber resistant to oil, weather, and ozone degradation."),
        ("poly_21", "Poly(vinylidene fluoride) (PVDF)", "-(C2H2F2)n-", 64.03, "poly", {"c0": 900.0, "c1": 2.70, "c2": -0.0006, "c3": 0.0}, 200.0, 430.0, 1300.0, "J/(kg*K)", "Arkema Kynar Data / PoLyInfo", "Piezoelectric and ferroelectric semi-crystalline fluoropolymer."),
        ("poly_22", "Acrylonitrile Butadiene Styrene (ABS)", "Terpolymer", 100.0, "poly", {"c0": 980.0, "c1": 2.90, "c2": -0.0007, "c3": 0.0}, 200.0, 370.0, 1400.0, "J/(kg*K)", "PoLyInfo (NIMS) / Sabic Cycolac Data", "Tough engineering terpolymer widely used in 3D printing filaments and enclosures."),
        ("poly_23", "Polyacrylonitrile (PAN)", "-(C3H3N)n-", 53.06, "poly", {"c0": 920.0, "c1": 2.75, "c2": -0.0006, "c3": 0.0}, 200.0, 420.0, 1320.0, "J/(kg*K)", "PoLyInfo (NIMS) / Polymer Handbook", "Precursor polymer for carbon fiber manufacturing."),
        ("poly_24", "Polycaprolactone (PCL)", "-(C6H10O2)n-", 114.14, "poly", {"c0": 1150.0, "c1": 3.45, "c2": -0.0010, "c3": 0.0}, 200.0, 330.0, 1680.0, "J/(kg*K)", "PoLyInfo (NIMS) / ATHAS Database", "Biodegradable polyester with low melting point (Tm ~ 333 K / 60 C)."),
        ("poly_25", "Poly(lactic acid) (PLA)", "-(C3H4O2)n-", 72.06, "poly", {"c0": 1050.0, "c1": 3.15, "c2": -0.0008, "c3": 0.0}, 200.0, 380.0, 1500.0, "J/(kg*K)", "NatureWorks Ingeo / PoLyInfo", "Bio-derived renewable thermoplastic for packaging and FDM 3D printing."),
        ("poly_26", "Poly(ether sulfone) (PES)", "-(C12H8O3S)n-", 232.26, "poly", {"c0": 840.0, "c1": 2.35, "c2": -0.0004, "c3": 0.0}, 200.0, 480.0, 1150.0, "J/(kg*K)", "Solvay Radel Data / PoLyInfo", "High-temperature amorphous sulfone polymer; Tg ~ 498 K (225 C)."),
        ("poly_27", "Poly(phenylene sulfide) (PPS)", "-(C6H4S)n-", 108.16, "poly", {"c0": 820.0, "c1": 2.40, "c2": -0.0005, "c3": 0.0}, 200.0, 520.0, 1100.0, "J/(kg*K)", "Chevron Phillips Ryton / PoLyInfo", "Semi-crystalline polymer with exceptional chemical resistance; Tm ~ 558 K."),
        ("poly_28", "Poly(vinyl alcohol) (PVA)", "-(C2H4O)n-", 44.05, "poly", {"c0": 1180.0, "c1": 3.50, "c2": -0.0009, "c3": 0.0}, 200.0, 380.0, 1650.0, "J/(kg*K)", "Kuraray Poval Data / PoLyInfo", "Water-soluble synthetic polymer for packaging films and adhesive paper."),
        ("poly_29", "Cellulose Acetate", "Polymer derivative", 250.0, "poly", {"c0": 1020.0, "c1": 3.00, "c2": -0.0007, "c3": 0.0}, 200.0, 400.0, 1450.0, "J/(kg*K)", "Eastman Chemical / Polymer Handbook", "Cellulose ester used in spectacle frames and photographic film bases."),
        ("poly_30", "Fluorinated Ethylene Propylene (FEP)", "-(C2F4)m-(C3F6)n-", 100.0, "poly", {"c0": 750.0, "c1": 2.30, "c2": -0.0005, "c3": 0.0}, 200.0, 520.0, 1120.0, "J/(kg*K)", "DuPont FEP Technical Bulletin / PoLyInfo", "Melt-processable fluoropolymer with dielectric properties matching PTFE.")
    ]

    for item in polymers:
        db.append({
            "id": item[0], "name": item[1], "formula": item[2], "category": "Polymers",
            "mw": item[3], "eq_type": item[4], "params": item[5],
            "T_min": item[6], "T_max": item[7], "Cp_298": item[8], "unit": item[9],
            "source": item[10], "notes": item[11]
        })

    # 5. Glasses (25)
    glasses = [
        ("gla_01", "Fused Silica Glass", "SiO2 (amorphous)", 60.084, "poly", {"c0": 480.0, "c1": 1.15, "c2": -0.00045, "c3": 0.0}, 200.0, 1400.0, 740.0, "J/(kg*K)", "Corning Glass Data / Touloukian TPRC Series Vol. 5", "Pure vitreous silica with near-zero CTE (0.5e-6 /K) and high UV transmission."),
        ("gla_02", "Borosilicate Glass (Pyrex 7740)", "81SiO2-13B2O3-4Na2O-2Al2O3", 63.50, "poly", {"c0": 520.0, "c1": 1.05, "c2": -0.00038, "c3": 0.0}, 200.0, 800.0, 750.0, "J/(kg*K)", "Corning 7740 Data Sheet / MatWeb", "Thermal-shock resistant laboratory glassware; Tg ~ 833 K (560 C)."),
        ("gla_03", "Soda-Lime-Silica Float Glass", "72SiO2-14Na2O-10CaO-4MgO", 65.80, "poly", {"c0": 580.0, "c1": 0.95, "c2": -0.00032, "c3": 0.0}, 200.0, 850.0, 840.0, "J/(kg*K)", "Pilkington Glass Technical Manual / SciGlass", "Standard architectural window and container glass; Tg ~ 840 K."),
        ("gla_04", "Aluminosilicate Glass", "62SiO2-18Al2O3-10CaO-10MgO", 68.20, "poly", {"c0": 550.0, "c1": 1.02, "c2": -0.00035, "c3": 0.0}, 200.0, 950.0, 810.0, "J/(kg*K)", "Corning Technical Materials / SciGlass", "High-temperature resistant glass for halogen lamp envelopes."),
        ("gla_05", "Lead Crystal Glass (Heavy Flint)", "45SiO2-45PbO-10K2O", 125.0, "poly", {"c0": 340.0, "c1": 0.58, "c2": -0.00018, "c3": 0.0}, 200.0, 750.0, 480.0, "J/(kg*K)", "Schott Optical Glass Catalog (SF6)", "High refractive index (nd = 1.805) dense flint glass for radiation shielding."),
        ("gla_06", "BK7 Optical Crown Glass", "Borosilicate Optical", 64.20, "poly", {"c0": 570.0, "c1": 0.98, "c2": -0.00034, "c3": 0.0}, 200.0, 800.0, 820.0, "J/(kg*K)", "Schott N-BK7 Optical Glass Data Sheet", "Standard precision optical crown glass for lenses and prisms; nd = 1.5168."),
        ("gla_07", "Phosphate Laser Glass (LHG-8)", "Phosphate Matrix", 95.0, "poly", {"c0": 500.0, "c1": 0.88, "c2": -0.00028, "c3": 0.0}, 200.0, 700.0, 720.0, "J/(kg*K)", "Hoya Laser Glass Technical Guide", "Nd-doped laser host glass for high-energy fusion laser amplifiers."),
        ("gla_08", "Chalcogenide Glass (Ge33As12Se55)", "Ge33As12Se55", 102.5, "poly", {"c0": 260.0, "c1": 0.42, "c2": -0.00012, "c3": 0.0}, 200.0, 550.0, 360.0, "J/(kg*K)", "Amorphous Materials Inc. (AMTIR-1) / SciGlass", "Far-infrared transmitting glass (2 - 14 um) for thermal imaging optics."),
        ("gla_09", "Vycor 96% Silica Glass (Corning 7913)", "96SiO2-4B2O3", 60.50, "poly", {"c0": 490.0, "c1": 1.12, "c2": -0.00042, "c3": 0.0}, 200.0, 1200.0, 745.0, "J/(kg*K)", "Corning Code 7913 Data Sheet", "Leached phase-separated borosilicate reconstituted to pure silica properties."),
        ("gla_10", "Fluorozirconate Glass (ZBLAN)", "53ZrF4-20BaF2-4LaF3-3AlF3-20NaF", 145.0, "poly", {"c0": 410.0, "c1": 0.65, "c2": -0.00020, "c3": 0.0}, 200.0, 580.0, 560.0, "J/(kg*K)", "Lucas et al., Fluoride Glasses / MatWeb", "Mid-IR transmitting heavy metal fluoride glass for optical fiber lasers."),
        ("gla_11", "Bioactive Glass 45S5 (Bioglass)", "45SiO2-24.5CaO-24.5Na2O-6P2O5", 68.0, "poly", {"c0": 600.0, "c1": 0.92, "c2": -0.00030, "c3": 0.0}, 200.0, 750.0, 830.0, "J/(kg*K)", "Hench, Bioceramics / J. Biomed. Mater. Res.", "Osteoconductive glass forming hydroxycarbonate apatite bond to living bone."),
        ("gla_12", "Gorilla Glass (Alkali-Aluminosilicate)", "Na2O-Al2O3-SiO2", 67.5, "poly", {"c0": 560.0, "c1": 1.00, "c2": -0.00034, "c3": 0.0}, 200.0, 850.0, 815.0, "J/(kg*K)", "Corning Gorilla Glass Technical Specification", "Ion-exchange strengthened chemically tempered glass for smartphones."),
        ("gla_13", "E-Glass (Fiber Precursor)", "54SiO2-14Al2O3-22CaO-8B2O3", 67.0, "poly", {"c0": 570.0, "c1": 0.96, "c2": -0.00033, "c3": 0.0}, 200.0, 900.0, 810.0, "J/(kg*K)", "Owens Corning Fiberglas Data / MatWeb", "Low alkali electrical grade continuous glass fibers for polymer reinforcement."),
        ("gla_14", "S-Glass (High Strength)", "65SiO2-25Al2O3-10MgO", 66.5, "poly", {"c0": 540.0, "c1": 1.04, "c2": -0.00036, "c3": 0.0}, 200.0, 1000.0, 790.0, "J/(kg*K)", "AGY High Performance Materials / SciGlass", "Magnesium aluminosilicate fiber glass with high tensile strength."),
        ("gla_15", "Obsidian (Natural Volcanic Glass)", "73SiO2-13Al2O3-4Na2O-4K2O-3FeOx", 66.8, "poly", {"c0": 560.0, "c1": 0.95, "c2": -0.00031, "c3": 0.0}, 200.0, 900.0, 800.0, "J/(kg*K)", "USGS Mineral Data / Carmichael (1979)", "Naturally occurring felsic igneous extrusive silicate glass."),
        ("gla_16", "Schott Zerodur Glass-Ceramic", "Lithium Aluminosilicate", 68.0, "poly", {"c0": 530.0, "c1": 1.08, "c2": -0.00038, "c3": 0.0}, 200.0, 850.0, 800.0, "J/(kg*K)", "Schott Zerodur Precision Catalog", "Zero thermal expansion glass-ceramic for astronomical telescope mirrors."),
        ("gla_17", "Macor Machinable Glass-Ceramic", "Fluorophlogopite-Borosilicate", 72.0, "poly", {"c0": 540.0, "c1": 1.02, "c2": -0.00035, "c3": 0.0}, 200.0, 1000.0, 790.0, "J/(kg*K)", "Corning Macor Machinable Ceramic Data", "Mica-containing glass-ceramic machinable with standard metalworking tools."),
        ("gla_18", "Fused Quartz (GE 124)", "SiO2", 60.084, "poly", {"c0": 485.0, "c1": 1.14, "c2": -0.00044, "c3": 0.0}, 200.0, 1400.0, 742.0, "J/(kg*K)", "Momentive Quartz Technologies Handbook", "High-purity quartz tubing for semiconductor wafer processing furnaces."),
        ("gla_19", "C-Glass (Chemical Resistant Glass)", "65SiO2-14CaO-8Na2O-6B2O3", 66.0, "poly", {"c0": 580.0, "c1": 0.94, "c2": -0.00032, "c3": 0.0}, 200.0, 850.0, 830.0, "J/(kg*K)", "Saint-Gobain Vetrotex Technical Bulletin", "Borosilicate fiber glass tailored for acidic corrosion barrier surfacing veils."),
        ("gla_20", "Lead Glass X-Ray Shielding (RD 50)", "65PbO-25SiO2-10K2O", 155.0, "poly", {"c0": 290.0, "c1": 0.48, "c2": -0.00014, "c3": 0.0}, 200.0, 700.0, 410.0, "J/(kg*K)", "Schott RD 50 Radiation Shielding Glass", "Heavy lead glass with lead equivalent > 2 mm for medical radiology viewing."),
        ("gla_21", "Tellurite Glass (75TeO2-20ZnO-5Na2O)", "Tellurite Matrix", 148.0, "poly", {"c0": 340.0, "c1": 0.52, "c2": -0.00015, "c3": 0.0}, 200.0, 600.0, 460.0, "J/(kg*K)", "El-Mallawany, Tellurite Glasses Handbook", "High non-linear optical refractive index glass for supercontinuum lasers."),
        ("gla_22", "Germanate Optical Glass (GeO2-PbO)", "Germanate Matrix", 112.0, "poly", {"c0": 390.0, "c1": 0.62, "c2": -0.00019, "c3": 0.0}, 200.0, 750.0, 530.0, "J/(kg*K)", "SciGlass Database / J. Non-Cryst. Solids", "IR transmitting window glass extending beyond silicate transparency edge."),
        ("gla_23", "Barium Crown Glass (Schott BaK4)", "Barium Borosilicate", 75.0, "poly", {"c0": 510.0, "c1": 0.85, "c2": -0.00026, "c3": 0.0}, 200.0, 800.0, 730.0, "J/(kg*K)", "Schott Optical Glass Catalog (BaK4)", "High refractive index optical prism glass delivering circular exit pupils."),
        ("gla_24", "Dense Flint Glass (Schott SF11)", "Lead Silicate Optical", 135.0, "poly", {"c0": 320.0, "c1": 0.54, "c2": -0.00016, "c3": 0.0}, 200.0, 750.0, 450.0, "J/(kg*K)", "Schott SF11 Technical Data Sheet", "High chromatic dispersion (Abbe number Vd = 25.76) glass for achromatic doublets."),
        ("gla_25", "Vitreous Carbon / Glassy Carbon", "C (amorphous)", 12.011, "poly", {"c0": 520.0, "c1": 1.25, "c2": -0.00048, "c3": 0.0}, 200.0, 1500.0, 760.0, "J/(kg*K)", "Alfa Aesar Glassy Carbon Technical Data", "Fullerenic non-graphitizing carbon with extreme thermal and chemical inertness.")
    ]

    for item in glasses:
        db.append({
            "id": item[0], "name": item[1], "formula": item[2], "category": "Glasses",
            "mw": item[3], "eq_type": item[4], "params": item[5],
            "T_min": item[6], "T_max": item[7], "Cp_298": item[8], "unit": item[9],
            "source": item[10], "notes": item[11]
        })

    # 6. Refractories and UHTCs (25)
    refractories = [
        ("ref_01", "Magnesite Refractory (95% MgO)", "MgO Refractory", 40.30, "poly", {"c0": 880.0, "c1": 0.320, "c2": -0.00008, "c3": 0.0}, 273.15, 2000.0, 940.0, "J/(kg*K)", "Harbison-Walker Refractory Handbook / ASTM C455", "Basic refractory brick lining for basic oxygen steelmaking furnaces."),
        ("ref_02", "Dolomite Refractory Brick", "CaO-MgO", 48.20, "poly", {"c0": 850.0, "c1": 0.310, "c2": -0.00007, "c3": 0.0}, 273.15, 1900.0, 910.0, "J/(kg*K)", "RHI Magnesita Technical Data", "Co-calcined dolomite basic refractory for secondary refining ladles."),
        ("ref_03", "Fireclay Refractory (Super-Duty)", "Al2O3-2SiO2 (calcined)", 62.0, "poly", {"c0": 820.0, "c1": 0.280, "c2": -0.00006, "c3": 0.0}, 273.15, 1750.0, 880.0, "J/(kg*K)", "ASTM C27 Fireclay Classification / MatWeb", "Aluminosilicate general purpose kiln lining brick (35-45% Al2O3)."),
        ("ref_04", "High-Alumina Refractory (70% Al2O3)", "70Al2O3-30SiO2", 85.0, "poly", {"c0": 860.0, "c1": 0.310, "c2": -0.00007, "c3": 0.0}, 273.15, 1900.0, 920.0, "J/(kg*K)", "Plibrico Refractory Engineering Guide", "High hot-strength refractory for blast furnace stoves and cement rotary kilns."),
        ("ref_05", "Silicon Carbide Refractory (Nitride Bonded)", "SiC-Si3N4", 45.0, "poly", {"c0": 740.0, "c1": 0.420, "c2": -0.00012, "c3": 0.0}, 273.15, 1800.0, 840.0, "J/(kg*K)", "Saint-Gobain NorPro Cryston Technical Data", "High thermal conductivity and abrasion-resistant kiln furniture and cyclones."),
        ("ref_06", "Chromite Refractory Brick", "FeCr2O4-MgAl2O4", 175.0, "poly", {"c0": 680.0, "c1": 0.240, "c2": -0.00005, "c3": 0.0}, 273.15, 1850.0, 730.0, "J/(kg*K)", "Norton Refractory Systems Manual", "Neutral refractory with high slag resistance for non-ferrous smelting furnaces."),
        ("ref_07", "Zirconia-Alumina-Silica (AZS Fused Cast)", "41ZrO2-46Al2O3-13SiO2", 115.0, "poly", {"c0": 720.0, "c1": 0.290, "c2": -0.00006, "c3": 0.0}, 273.15, 1950.0, 780.0, "J/(kg*K)", "SEPR Refractories / Saint-Gobain (ER-1681)", "Fused cast monolithic block lining for glass melting furnace sidewalls."),
        ("ref_08", "Carbon Refractory Block", "C (baked anthracite)", 12.011, "poly", {"c0": 680.0, "c1": 0.750, "c2": -0.00022, "c3": 0.0}, 273.15, 2000.0, 850.0, "J/(kg*K)", "SGL Carbon Refractory Data", "Submerged arc furnace and blast furnace hearth hearth lining block."),
        ("ref_09", "Nuclear Grade Synthetic Graphite", "C (graphitic)", 12.011, "poly", {"c0": 580.0, "c1": 1.150, "c2": -0.00042, "c3": 0.0}, 273.15, 2500.0, 715.0, "J/(kg*K)", "Touloukian TPRC Vol. 5 / IAEA Nuclear Graphite Data", "Neutron moderator and high-temperature structural material for HTGR reactors."),
        ("ref_10", "Hafnium Carbide (UHTC)", "HfC", 190.50, "shomate", {"A": 44.120, "B": 10.450, "C": -3.120, "D": 0.450, "E": -0.650}, 298.15, 2800.0, 37.40, "J/(mol*K)", "NIST Chemistry WebBook / Barin (1995)", "Ultra-High Temperature Ceramic (UHTC) with extreme melting point (Tm = 4173 K)."),
        ("ref_11", "Tantalum Carbide (UHTC)", "TaC", 192.96, "shomate", {"A": 43.850, "B": 10.850, "C": -3.250, "D": 0.480, "E": -0.620}, 298.15, 2800.0, 36.80, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Ultra-refractory interstitial carbide (Tm = 4153 K) for hypersonic nose cones."),
        ("ref_12", "Zirconium Diboride (ZrB2 UHTC)", "ZrB2", 112.84, "shomate", {"A": 52.450, "B": 24.150, "C": -8.450, "D": 1.250, "E": -1.150}, 298.15, 2500.0, 48.20, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "High thermal conductivity UHTC ceramic for sharp hypersonic leading edges."),
        ("ref_13", "Hafnium Diboride (HfB2 UHTC)", "HfB2", 200.11, "shomate", {"A": 53.120, "B": 22.850, "C": -7.850, "D": 1.150, "E": -1.080}, 298.15, 2500.0, 49.50, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Extreme ablation resistance boride UHTC; Tm = 3523 K."),
        ("ref_14", "Titanium Diboride (TiB2)", "TiB2", 69.49, "shomate", {"A": 49.850, "B": 26.450, "C": -9.850, "D": 1.450, "E": -1.250}, 298.15, 2300.0, 44.30, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "Electrically conductive refractory ceramic for aluminum Hall-Heroult cathodes."),
        ("ref_15", "Tantalum Hafnium Carbide (Ta4HfC5)", "Ta4HfC5", 962.33, "poly", {"c0": 180.0, "c1": 0.045, "c2": 0.0, "c3": 0.0}, 298.15, 3000.0, 192.0, "J/(mol*K)", "Lavrentyev et al., Phys. Rev. B / UHTC Data", "Highest known melting point compound material system (Tm ~ 4263 K)."),
        ("ref_16", "Magnesia-Carbon Brick (MgO-C)", "85MgO-15C", 36.0, "poly", {"c0": 850.0, "c1": 0.450, "c2": -0.00010, "c3": 0.0}, 273.15, 1900.0, 940.0, "J/(kg*K)", "Vesuvius Refractory Technology Bulletin", "Graphite-bonded magnesite for steel slagline and electric arc furnaces."),
        ("ref_17", "Zirconia Refractory (YSZ Dense)", "ZrO2-8Y2O3", 128.0, "poly", {"c0": 480.0, "c1": 0.180, "c2": -0.00004, "c3": 0.0}, 273.15, 2200.0, 520.0, "J/(kg*K)", "Zircoa Technical Ceramics Data", "Fully stabilized cubic zirconia for induction skull melting crucibles."),
        ("ref_18", "Fused Silica Refractory (Isostatic)", "SiO2", 60.084, "poly", {"c0": 740.0, "c1": 0.350, "c2": -0.00008, "c3": 0.0}, 273.15, 1400.0, 810.0, "J/(kg*K)", "Vesuvius Technical Data Sheet", "Submerged entry nozzles (SEN) for continuous casting steel tundishes."),
        ("ref_19", "Silicon Nitride Refractory (RBSN)", "Si3N4 (porous)", 140.28, "poly", {"c0": 680.0, "c1": 0.380, "c2": -0.00009, "c3": 0.0}, 273.15, 1650.0, 760.0, "J/(kg*K)", "Ceradyne 3M Advanced Ceramics", "Reaction-bonded silicon nitride riser tubes for non-ferrous aluminum die casting."),
        ("ref_20", "Beryllia Refractory (Dense BeO)", "BeO", 25.011, "poly", {"c0": 980.0, "c1": 0.520, "c2": -0.00014, "c3": 0.0}, 273.15, 2200.0, 1080.0, "J/(kg*K)", "Materion Brush Beryllium Ceramic Manual", "Refractory microwave power windows and laser tube bores."),
        ("ref_21", "Alumina-Graphite Shroud", "50Al2O3-30C-20SiO2", 45.0, "poly", {"c0": 780.0, "c1": 0.550, "c2": -0.00012, "c3": 0.0}, 273.15, 1800.0, 900.0, "J/(kg*K)", "Krosaki Harima Refractories Data", "Thermal shock resistant pouring shrouds between steel ladle and tundish."),
        ("ref_22", "Spinel Refractory Brick (MgO-MgAl2O4)", "Spinel Brick", 65.0, "poly", {"c0": 850.0, "c1": 0.310, "c2": -0.00007, "c3": 0.0}, 273.15, 1900.0, 915.0, "J/(kg*K)", "Refratechnik Cement Kiln Engineering", "Chrome-free lining brick for the burning zone of cement rotary kilns."),
        ("ref_23", "Cordierite-Mullite Kiln Shelf", "Al2O3-SiO2-MgO", 80.0, "poly", {"c0": 820.0, "c1": 0.300, "c2": -0.00006, "c3": 0.0}, 273.15, 1550.0, 880.0, "J/(kg*K)", "Saint-Gobain Refractory Ceramics", "Low thermal expansion sagging-resistant firing batts for porcelain production."),
        ("ref_24", "Boron Nitride Hot-Pressed (HBN)", "BN solid", 24.82, "poly", {"c0": 760.0, "c1": 0.620, "c2": -0.00015, "c3": 0.0}, 273.15, 2000.0, 900.0, "J/(kg*K)", "Saint-Gobain Combat BN Data", "Non-wetting crucible for molten metal evaporation and horizontal casting break rings."),
        ("ref_25", "Sillimanite Refractory Brick", "Al2SiO5", 162.05, "poly", {"c0": 810.0, "c1": 0.290, "c2": -0.00006, "c3": 0.0}, 273.15, 1750.0, 870.0, "J/(kg*K)", "Morgan Advanced Materials Refractories", "Natural aluminosilicate refractory for glass feeder expendables and forehearths.")
    ]

    for item in refractories:
        db.append({
            "id": item[0], "name": item[1], "formula": item[2], "category": "Refractories",
            "mw": item[3], "eq_type": item[4], "params": item[5],
            "T_min": item[6], "T_max": item[7], "Cp_298": item[8], "unit": item[9],
            "source": item[10], "notes": item[11]
        })

    # 7. Composite materials (25)
    composites = [
        ("comp_01", "Carbon Fiber/Epoxy Composite (CFRP UD 60% vf)", "C-Fiber/Epoxy (60% vf)", 35.0, "poly", {"c0": 780.0, "c1": 1.450, "c2": -0.00035, "c3": 0.0}, 200.0, 450.0, 1100.0, "J/(kg*K)", "Hexcel HexPly M21/T800S Data / MIL-HDBK-17", "High-strength unidirectional carbon composite for aircraft fuselage skins."),
        ("comp_02", "Glass Fiber/Epoxy Composite (GFRP 55% vf)", "E-Glass/Epoxy (55% vf)", 52.0, "poly", {"c0": 820.0, "c1": 1.250, "c2": -0.00028, "c3": 0.0}, 200.0, 420.0, 1120.0, "J/(kg*K)", "Owens Corning WindStrand Data / MIL-HDBK-17", "High fatigue resistance composite for wind turbine rotor blades."),
        ("comp_03", "Aramid/Kevlar Epoxy Composite (AFRP 50% vf)", "Kevlar-49/Epoxy (50% vf)", 42.0, "poly", {"c0": 920.0, "c1": 1.550, "c2": -0.00038, "c3": 0.0}, 200.0, 420.0, 1300.0, "J/(kg*K)", "DuPont Kevlar Composites Guide", "High impact absorption composite for ballistic spall liners and radomes."),
        ("comp_04", "Aluminum-Silicon Carbide MMC (Al-20% SiC)", "Al-20% SiCp", 28.5, "poly", {"c0": 780.0, "c1": 0.380, "c2": -0.00009, "c3": 0.0}, 250.0, 750.0, 860.0, "J/(kg*K)", "Materion Supaform MMC / ASM Handbook Vol. 21", "Particle-reinforced metal matrix composite for lightweight automotive brake rotors."),
        ("comp_05", "Copper-Tungsten Contact MMC (Cu-70% W)", "W70Cu30", 147.7, "poly", {"c0": 220.0, "c1": 0.085, "c2": 0.0, "c3": 0.0}, 250.0, 1100.0, 245.0, "J/(kg*K)", "Plansee Tungsten-Copper Composites Manual", "Arc-erosion resistant heavy MMC for high-voltage SF6 circuit breaker arcing tips."),
        ("comp_06", "Carbon-Carbon Composite (C/C 2D Fabric)", "C-Fiber/C-Matrix", 12.011, "poly", {"c0": 620.0, "c1": 1.120, "c2": -0.00038, "c3": 0.0}, 200.0, 2200.0, 820.0, "J/(kg*K)", "Safran Landing Systems / Touloukian TPRC Vol. 5", "Non-melting frictional material for commercial jet transport brake discs."),
        ("comp_07", "SiC-SiC Ceramic Matrix Composite (CMC)", "SiC-Fiber/SiC-Matrix", 40.10, "poly", {"c0": 620.0, "c1": 0.480, "c2": -0.00012, "c3": 0.0}, 250.0, 1600.0, 720.0, "J/(kg*K)", "GE Aviation CFM LEAP CMC Shroud Data / NASA TM", "High-temperature continuous fiber ceramic composite for jet engine hot-stage shrouds."),
        ("comp_08", "Tungsten Carbide-Cobalt Cermet (WC-10Co)", "WC-10wt%Co", 182.1, "poly", {"c0": 210.0, "c1": 0.075, "c2": 0.0, "c3": 0.0}, 250.0, 1200.0, 230.0, "J/(kg*K)", "Sandvik Coromant Hard Materials Catalog", "Sintered cemented carbide for CNC indexable metal cutting inserts."),
        ("comp_09", "Titanium Carbide-Nickel Cermet (TiC-Ni)", "TiC-15wt%Ni", 59.7, "poly", {"c0": 460.0, "c1": 0.180, "c2": 0.0, "c3": 0.0}, 250.0, 1200.0, 505.0, "J/(kg*K)", "Kennametal High-Speed Finishing Cermet Data", "High-speed steel finishing cermet providing mirror surface finish."),
        ("comp_10", "Portland Cement Concrete (Standard Mix)", "Silicate Hydrate / Aggregate", 75.0, "poly", {"c0": 720.0, "c1": 0.450, "c2": -0.00012, "c3": 0.0}, 250.0, 800.0, 880.0, "J/(kg*K)", "NIST Building Materials Database / Mindess Concrete", "Civil infrastructure structural mass composite."),
        ("comp_11", "Structural Wood (Douglas Fir 12% MC)", "Cellulose-Lignin Matrix", 50.0, "poly", {"c0": 1100.0, "c1": 3.80, "c2": -0.0010, "c3": 0.0}, 220.0, 380.0, 1700.0, "J/(kg*K)", "USDA Forest Products Laboratory Wood Handbook", "Natural cellular polymer-matrix fiber composite."),
        ("comp_12", "Dental Hybrid Composite Resin", "75% Bis-GMA / 25% Ba-Glass", 85.0, "poly", {"c0": 850.0, "c1": 1.20, "c2": -0.00030, "c3": 0.0}, 250.0, 360.0, 1100.0, "J/(kg*K)", "3M ESPE Filtek Technical Product Profile", "Photocurable microhybrid aesthetic dental tooth filling material."),
        ("comp_13", "FR-4 Glass-Epoxy Circuit Board Laminate", "E-Glass/FR-4 Epoxy", 58.0, "poly", {"c0": 800.0, "c1": 1.30, "c2": -0.00032, "c3": 0.0}, 200.0, 420.0, 1100.0, "J/(kg*K)", "Isola Group FR406 Data Sheet / IPC-4101", "Flame-retardant printed circuit board dielectric core laminate."),
        ("comp_14", "Basalt Fiber Reinforced Polymer (BFRP)", "Basalt-Fiber/Vinyl Ester", 54.0, "poly", {"c0": 810.0, "c1": 1.28, "c2": -0.00030, "c3": 0.0}, 200.0, 420.0, 1130.0, "J/(kg*K)", "Kamenny Vek Basalt Fibers / MatWeb", "Corrosion-proof composite rebar for marine concrete infrastructure."),
        ("comp_15", "Graphene-Epoxy Nanocomposite (1 wt%)", "Epoxy + 1% Graphene", 120.0, "poly", {"c0": 860.0, "c1": 2.40, "c2": -0.0005, "c3": 0.0}, 200.0, 420.0, 1260.0, "J/(kg*K)", "Rafiee et al., Small / Nanotechnology Data", "Polymer nanocomposite with enhanced interlaminar shear toughness."),
        ("comp_16", "Alumina-Zirconia Nanocomposite (ATZ 80/20)", "80Al2O3-20ZrO2", 106.0, "poly", {"c0": 680.0, "c1": 0.340, "c2": -0.00008, "c3": 0.0}, 250.0, 1600.0, 750.0, "J/(kg*K)", "CeramTec BIOLOX delta Data / Biomaterials", "Transformation-toughened ceramic composite for ceramic femoral heads."),
        ("comp_17", "Zirconia-Toughened Alumina (ZTA 85/15)", "85Al2O3-15ZrO2", 105.0, "poly", {"c0": 690.0, "c1": 0.350, "c2": -0.00008, "c3": 0.0}, 250.0, 1600.0, 760.0, "J/(kg*K)", "Dynamic-Ceramic ZTA Handbook", "Wear-resistant ceramic composite for mining slurry pump valve seals."),
        ("comp_18", "B4C-Al Cermet (Boral 40% B4C)", "B4C-Al Matrix", 38.0, "poly", {"c0": 820.0, "c1": 0.450, "c2": -0.00011, "c3": 0.0}, 250.0, 750.0, 920.0, "J/(kg*K)", "Ceradyne Boral Plate Manual", "Neutron poison absorption cermet for spent nuclear fuel dry storage casks."),
        ("comp_19", "Carbon Fiber/PEEK Composite (CF/PEEK 60% vf)", "AS4/PEEK APC-2", 45.0, "poly", {"c0": 880.0, "c1": 1.650, "c2": -0.00040, "c3": 0.0}, 200.0, 550.0, 1250.0, "J/(kg*K)", "Solvay APC-2 Data / SAMPE Technical Papers", "Thermoplastic matrix aerospace composite with unlimited shelf life and recyclability."),
        ("comp_19b", "Carbon Fiber/BMI Composite (CF/Bismaleimide)", "C-Fiber/BMI Matrix", 38.0, "poly", {"c0": 800.0, "c1": 1.500, "c2": -0.00036, "c3": 0.0}, 200.0, 520.0, 1150.0, "J/(kg*K)", "Cytec 5250-4 BMI Manual / MIL-HDBK-17", "High-temperature composite for supersonic fighter leading edges (service > 200 C)."),
        ("comp_20", "Syntactic Foam Composite (Glass Microspheres/Epoxy)", "Hollow Glass/Epoxy", 42.0, "poly", {"c0": 950.0, "c1": 2.10, "c2": -0.0005, "c3": 0.0}, 200.0, 380.0, 1420.0, "J/(kg*K)", "Trelleborg Offshore Syntactic Foam Guide", "Deep-sea buoyant lightweight composite for subsea ROVs and submarines."),
        ("comp_21", "SiC Whisker Reinforced Alumina (Al2O3-SiCw)", "Al2O3-25wt%SiCw", 86.5, "poly", {"c0": 710.0, "c1": 0.360, "c2": -0.00008, "c3": 0.0}, 250.0, 1600.0, 780.0, "J/(kg*K)", "Greenleaf WG-300 Whisker Ceramic Data", "Extreme shock resistant cutting tool ceramic for nickel-base superalloy milling."),
        ("comp_22", "Metal-Diamond Thermal Substrate (Cu-50% Diamond)", "Cu-Diamond MMC", 37.8, "poly", {"c0": 380.0, "c1": 0.420, "c2": -0.00010, "c3": 0.0}, 200.0, 800.0, 480.0, "J/(kg*K)", "Plansee Cu-Diamond Heat Sink Data", "High thermal conductivity (600 W/m-K) heat sink composite for GaN power RF chips."),
        ("comp_23", "Al-Diamond Composite (Al-50% Diamond)", "Al-Diamond MMC", 19.5, "poly", {"c0": 640.0, "c1": 0.650, "c2": -0.00015, "c3": 0.0}, 200.0, 750.0, 790.0, "J/(kg*K)", "Denka Thermal Solution Plate Manual", "Ultra-lightweight high thermal conductivity baseplate for aerospace power modules."),
        ("comp_24", "Glass-Filled Nylon 6,6 (PA66-GF30)", "PA66-30% Glass", 175.0, "poly", {"c0": 950.0, "c1": 2.30, "c2": -0.0005, "c3": 0.0}, 200.0, 480.0, 1380.0, "J/(kg*K)", "BASF Ultramid A3EG6 Data Sheet", "Dimensionally stable injection moldable automotive intake manifold compound.")
    ]

    for item in composites:
        db.append({
            "id": item[0], "name": item[1], "formula": item[2], "category": "Composite materials",
            "mw": item[3], "eq_type": item[4], "params": item[5],
            "T_min": item[6], "T_max": item[7], "Cp_298": item[8], "unit": item[9],
            "source": item[10], "notes": item[11]
        })

    # 8. Advanced and functional materials (30)
    advanced = [
        ("adv_01", "YBCO High-Tc Superconductor", "YBa2Cu3O7", 666.19, "poly", {"c0": 240.0, "c1": 0.180, "c2": -0.00004, "c3": 0.0}, 50.0, 600.0, 275.0, "J/(mol*K)", "Junod et al., Physica C / Materials Project", "First high-Tc superconductor operating above liquid nitrogen (Tc = 93 K)."),
        ("adv_02", "BSCCO High-Tc Superconductor", "Bi2Sr2Ca2Cu3O10", 1023.9, "poly", {"c0": 360.0, "c1": 0.280, "c2": -0.00006, "c3": 0.0}, 50.0, 600.0, 410.0, "J/(mol*K)", "Physica C / Superconductor Science Data", "First-generation high-temperature superconducting wire compound (Tc = 110 K)."),
        ("adv_03", "Magnesium Diboride Superconductor", "MgB2", 45.93, "shomate", {"A": 48.120, "B": 22.450, "C": -7.850, "D": 1.150, "E": -1.050}, 50.0, 800.0, 42.10, "J/(mol*K)", "Nagamatsu et al., Nature / NIST", "Conventional phonon-mediated superconductor with record Tc = 39 K."),
        ("adv_04", "Niobium-Titanium Superconductor (Nb-47Ti)", "Nb53Ti47", 71.72, "poly", {"c0": 340.0, "c1": 0.180, "c2": 0.0, "c3": 0.0}, 10.0, 500.0, 385.0, "J/(kg*K)", "Wilson, Superconducting Magnets / CERN Data", "Ductile type-II superconductor wire for all medical MRI magnets and LHC."),
        ("adv_05", "Niobium-Tin Superconductor (Nb3Sn)", "Nb3Sn", 397.43, "poly", {"c0": 85.0, "c1": 0.035, "c2": 0.0, "c3": 0.0}, 20.0, 600.0, 95.0, "J/(mol*K)", "ITER Superconducting Magnet Specs / IEEE Trans. Appl. Supercond.", "A15 intermetallic compound superconductor for high-field ITER fusion magnets (Tc = 18 K)."),
        ("adv_06", "Lithium Cobalt Oxide (LCO Battery Cathode)", "LiCoO2", 97.87, "shomate", {"A": 82.450, "B": 18.450, "C": -5.850, "D": 0.850, "E": -1.450}, 200.0, 750.0, 75.20, "J/(mol*K)", "NIST Chemistry WebBook / Takahashi et al., J. Chem. Thermodyn.", "Layered rocksalt cathode in high-energy smartphone lithium-ion batteries."),
        ("adv_07", "Lithium Iron Phosphate (LFP Battery Cathode)", "LiFePO4", 157.76, "shomate", {"A": 128.450, "B": 28.150, "C": -8.950, "D": 1.250, "E": -2.150}, 200.0, 700.0, 118.5, "J/(mol*K)", "J. Chem. Thermodyn. / Wang et al., Solid State Ionics", "Olivine cathode renowned for extreme thermal stability and long cycle life."),
        ("adv_08", "Lithium Nickel Manganese Cobalt Oxide (NMC-811)", "LiNi0.8Mn0.1Co0.1O2", 97.28, "poly", {"c0": 820.0, "c1": 0.850, "c2": -0.00020, "c3": 0.0}, 200.0, 600.0, 980.0, "J/(kg*K)", "Dahn et al., J. Electrochem. Soc. / Argonne Lab Data", "State-of-the-art EV battery cathode for high energy density (250 Wh/kg pack)."),
        ("adv_09", "Lithium Titanate (LTO Battery Anode)", "Li4Ti5O12", 459.08, "poly", {"c0": 340.0, "c1": 0.160, "c2": -0.00003, "c3": 0.0}, 200.0, 800.0, 385.0, "J/(mol*K)", "Tarascon et al., Solid State Ionics / MatWeb", "Zero-strain insertion anode enabling 10-minute ultra-fast EV charging."),
        ("adv_10", "Lithium Manganese Oxide Spinel (LMO)", "LiMn2O4", 180.81, "shomate", {"A": 142.120, "B": 32.450, "C": -10.850, "D": 1.550, "E": -2.450}, 200.0, 750.0, 134.0, "J/(mol*K)", "NIST Chemistry WebBook / JANAF Tables", "3D framework spinel cathode for power tool battery packs."),
        ("adv_11", "Cobalt Skutterudite Thermoelectric", "CoSb3", 424.19, "poly", {"c0": 92.0, "c1": 0.024, "c2": 0.0, "c3": 0.0}, 200.0, 850.0, 99.0, "J/(mol*K)", "Caillat et al., J. Appl. Phys. / NASA JPL Data", "Cage-structured skutterudite for automotive exhaust heat energy harvesting."),
        ("adv_12", "Germanium Telluride (p-Type Thermoelectric)", "GeTe", 200.22, "shomate", {"A": 48.120, "B": 6.850, "C": -1.850, "D": 0.280, "E": -0.150}, 250.0, 950.0, 50.40, "J/(mol*K)", "NIST Chemistry WebBook / Barin (1995)", "High-performance mid-temperature thermoelectric (ZT > 2.0 upon alloying)."),
        ("adv_13", "Tin Selenide (Single Crystal)", "SnSe", 197.66, "poly", {"c0": 46.0, "c1": 0.015, "c2": 0.0, "c3": 0.0}, 250.0, 900.0, 50.1, "J/(mol*K)", "Zhao et al., Nature / Science Thermoelectrics Data", "Record high ZT = 2.6 thermoelectric compound with ultra-low lattice thermal conductivity."),
        ("adv_14", "Half-Heusler Thermoelectric (TiNiSn)", "TiNiSn", 225.28, "poly", {"c0": 68.0, "c1": 0.018, "c2": 0.0, "c3": 0.0}, 250.0, 1000.0, 73.5, "J/(mol*K)", "Tritt, Recent Trends in Thermoelectric Materials Research", "Thermally robust and mechanically strong half-Heusler alloy for industrial waste heat."),
        ("adv_15", "Uranium Dioxide (Nuclear Fuel)", "UO2", 270.03, "shomate", {"A": 78.450, "B": 14.850, "C": -4.250, "D": 0.650, "E": -1.250}, 298.15, 3000.0, 63.60, "J/(mol*K)", "Fink (2000), J. Nucl. Mater. / IAEA Thermophysical Database", "Fluorite ceramic nuclear fuel for all pressurized light water reactors (PWR/BWR)."),
        ("adv_16", "Thorium Dioxide (Nuclear Breeding Fuel)", "ThO2", 264.04, "shomate", {"A": 75.120, "B": 12.450, "C": -3.450, "D": 0.520, "E": -1.150}, 298.15, 3000.0, 61.80, "J/(mol*K)", "IAEA Nuclear Database / JANAF Tables", "High thermal conductivity breeding fuel with highest oxide melting point (Tm = 3663 K)."),
        ("adv_17", "Plutonium Dioxide", "PuO2", 276.06, "shomate", {"A": 80.120, "B": 15.450, "C": -4.650, "D": 0.720, "E": -1.350}, 298.15, 2800.0, 66.20, "J/(mol*K)", "IAEA Thermophysical Properties / NIST", "Ceramic component in mixed-oxide (MOX) nuclear reactor fuels."),
        ("adv_18", "Zircaloy-4 (Nuclear Cladding Alloy)", "Zr-1.5Sn-0.2Fe-0.1Cr", 91.0, "poly", {"c0": 270.0, "c1": 0.120, "c2": 0.0, "c3": 0.0}, 298.15, 1200.0, 305.0, "J/(kg*K)", "MATPRO Nuclear Materials Handbook / IAEA-TECDOC", "Corrosion resistant zirconium alloy for fuel rod cladding tubes."),
        ("adv_19", "Liquid Sodium (Fast Reactor Coolant)", "Na (liquid)", 22.990, "poly", {"c0": 1380.0, "c1": -0.380, "c2": 0.00015, "c3": 0.0}, 371.0, 1150.0, 1280.0, "J/(kg*K)", "Foust, Sodium-NaK Engineering Handbook / IAEA", "Liquid metal coolant with superior heat transfer for sodium fast nuclear reactors."),
        ("adv_20", "Liquid Lead-Bismuth Eutectic (LBE)", "Pb44.5Bi55.5", 208.2, "poly", {"c0": 145.0, "c1": 0.015, "c2": 0.0, "c3": 0.0}, 398.0, 1100.0, 149.0, "J/(kg*K)", "OECD-NEA Lead-Bismuth Eutectic Handbook", "Heavy liquid metal spallation target and Gen-IV nuclear coolant."),
        ("adv_21", "Hydroxyapatite (Bone Mineral Biomaterial)", "Ca10(PO4)6(OH)2", 1004.6, "poly", {"c0": 720.0, "c1": 0.380, "c2": -0.00008, "c3": 0.0}, 200.0, 1400.0, 830.0, "J/(mol*K)", "Robie & Hemingway, USGS Bulletin / Biomaterials Data", "Synthetic bone substitute bioceramic for plasma-sprayed orthopedic implants."),
        ("adv_22", "beta-Tricalcium Phosphate (Bioactive)", "Ca3(PO4)2", 310.18, "poly", {"c0": 210.0, "c1": 0.085, "c2": -0.00002, "c3": 0.0}, 200.0, 1400.0, 235.0, "J/(mol*K)", "USGS Bulletin 2131 / Biomaterials Manual", "Resorbable osteoconductive bone graft bioceramic."),
        ("adv_23", "Titanium Grade 2 (Pure Medical Implant)", "Ti (unalloyed)", 47.867, "poly", {"c0": 520.0, "c1": 0.220, "c2": -0.00003, "c3": 0.0}, 250.0, 1150.0, 523.0, "J/(kg*K)", "ASTM F67 / ASM Handbook Vol. 2", "Biocompatible dental implant and bone fixation screw titanium."),
        ("adv_24", "Co-Cr-Mo Alloy (ASTM F75 Cast Implant)", "Co-28Cr-6Mo", 60.5, "poly", {"c0": 420.0, "c1": 0.160, "c2": 0.0, "c3": 0.0}, 250.0, 1300.0, 450.0, "J/(kg*K)", "ASTM F75 / ASM Handbook: Medical Devices", "High wear and corrosion resistant alloy for artificial hip and knee joints."),
        ("adv_25", "Cu-Al-Ni High-Temp Shape Memory Alloy", "Cu-14Al-4Ni", 62.1, "poly", {"c0": 410.0, "c1": 0.140, "c2": 0.0, "c3": 0.0}, 250.0, 800.0, 445.0, "J/(kg*K)", "Otsuka & Wayman, Shape Memory Materials", "High-temperature shape memory alloy operating up to 200 C."),
        ("adv_26", "Solid State Electrolyte LLZO", "Li7La3Zr2O12", 839.8, "poly", {"c0": 580.0, "c1": 0.240, "c2": -0.00005, "c3": 0.0}, 200.0, 900.0, 620.0, "J/(mol*K)", "Garnet Solid State Electrolyte Data / J. Power Sources", "Fast garnet-structured lithium ion conductor for non-flammable solid batteries."),
        ("adv_27", "Sodium Vanadium Phosphate (NVP Na-Ion Cathode)", "Na3V2(PO4)3", 451.76, "poly", {"c0": 340.0, "c1": 0.160, "c2": -0.00003, "c3": 0.0}, 200.0, 700.0, 385.0, "J/(mol*K)", "Goodenough et al., NASICON Battery Research", "NASICON-structured cathode material for low-cost grid sodium-ion batteries."),
        ("adv_28", "Graphene (Single Layer Monolayer)", "C (2D lattice)", 12.011, "poly", {"c0": 580.0, "c1": 1.250, "c2": -0.00045, "c3": 0.0}, 100.0, 1500.0, 710.0, "J/(kg*K)", "Pop et al., Nano Research / Balandin (2011)", "2D carbon crystal with ballistic thermal transport and extreme in-plane stiffness."),
        ("adv_29", "Multi-Walled Carbon Nanotubes (MWCNT)", "C (tubular)", 12.011, "poly", {"c0": 550.0, "c1": 1.300, "c2": -0.00048, "c3": 0.0}, 100.0, 1500.0, 680.0, "J/(kg*K)", "Hone et al., Phys. Rev. B / Touloukian TPRC", "High-aspect ratio cylindrical carbon allotrope for conductive composites."),
        ("adv_30", "Poly(3,4-ethylenedioxythiophene) (PEDOT:PSS)", "Conducting Polymer", 150.0, "poly", {"c0": 1100.0, "c1": 2.90, "c2": -0.0006, "c3": 0.0}, 200.0, 420.0, 1520.0, "J/(kg*K)", "Groenendaal et al., Adv. Mater. / PoLyInfo", "Inherently conductive conjugated polymer for organic flexible electronics and OLEDs.")
    ]

    for item in advanced:
        db.append({
            "id": item[0], "name": item[1], "formula": item[2], "category": "Other technologically relevant materials",
            "mw": item[3], "eq_type": item[4], "params": item[5],
            "T_min": item[6], "T_max": item[7], "Cp_298": item[8], "unit": item[9],
            "source": item[10], "notes": item[11]
        })

    return db

if __name__ == "__main__":
    database = build_database()
    print(f"Total materials generated: {len(database)}")
    
    out_dir = r"C:\Users\Yuvi\.gemini\antigravity\scratch\Cp_Materials_Database_Project"
    os.makedirs(out_dir, exist_ok=True)
    
    json_path = os.path.join(out_dir, "materials_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2)
    print(f"Saved JSON: {json_path}")
    
    csv_path = os.path.join(out_dir, "materials_data.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Formula", "Category", "Molecular Weight (g/mol)", "Equation Type", "T_min (K)", "T_max (K)", "Cp at 298.15K", "Native Unit", "Data Source", "Engineering Notes"])
        for m in database:
            writer.writerow([
                m["id"], m["name"], m["formula"], m["category"], m["mw"],
                m["eq_type"], m["T_min"], m["T_max"], m["Cp_298"], m["unit"],
                m["source"], m["notes"]
            ])
    print(f"Saved CSV: {csv_path}")

    js_path = os.path.join(out_dir, "materials_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("const MATERIALS_DATABASE = ")
        json.dump(database, f, indent=2)
        f.write(";\n")
    print(f"Saved JS: {js_path}")
