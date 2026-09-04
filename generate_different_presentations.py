"""
generate_different_presentations.py
Generates two completely distinct, clean, simple, and easy-to-understand Canva-style PowerPoint presentations (.pptx).
- Clearly different presentation styles, visual designs, color palettes, and layouts.
- Student 1: Materials & Thermodynamics Focus (Clean Indigo / Royal Blue, Academic & Concept-Driven, Everyday Analogies, Crystal Physics)
- Student 2: Platform, UI & Practical Applications Focus (Modern Emerald / Teal / Dark Slate, Product & Tech-Driven, UI Walkthroughs, Engineering Case Studies)
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os

OUT_DIR = r"C:\Users\Yuvi\.gemini\antigravity\scratch\Cp_Materials_Database_Project"
os.makedirs(OUT_DIR, exist_ok=True)

def set_slide_bg(slide, color):
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_card(slide, left, top, width, height, bg_color, border_color=None, border_width=1):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(border_width)
    else:
        shape.line.fill.background()
    return shape

# =============================================================================
# PRESENTATION 1: STUDENT 1 (Materials, Science & Thermodynamics)
# Style: Clean Canva Academic / Modern Indigo Palette
# Colors: Indigo (#312E81), Royal Blue (#2563EB), Sky Blue (#E0F2FE), Soft Card (#FFFFFF), Dark Text (#1E293B)
# =============================================================================
def create_student1_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5) # 16:9 Widescreen
    blank_layout = prs.slide_layouts[6]

    # Palette
    BG_LIGHT = RGBColor(248, 250, 252)       # #F8FAFC
    PRIMARY_INDIGO = RGBColor(49, 46, 129)   # #312E81 (Deep Indigo)
    ACCENT_BLUE = RGBColor(37, 99, 235)      # #2563EB (Royal Blue)
    CARD_BG = RGBColor(255, 255, 255)        # Pure White
    CARD_BORDER = RGBColor(226, 232, 240)    # Soft Slate
    TAG_BG = RGBColor(224, 231, 255)         # Indigo Tint
    TAG_TEXT = RGBColor(67, 56, 202)         # Indigo Dark
    TEXT_DARK = RGBColor(30, 41, 59)         # Charcoal Slate
    TEXT_MUTED = RGBColor(100, 116, 139)     # Muted Slate
    HIGHLIGHT_BG = RGBColor(238, 242, 255)   # Light Indigo Box

    def add_header(slide, tag_text, title_text, subtitle_text):
        set_slide_bg(slide, BG_LIGHT)
        
        # Tag pill
        tag_box = add_card(slide, Inches(0.8), Inches(0.4), Inches(2.8), Inches(0.4), TAG_BG, TAG_BG)
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.name = "Arial"
        p_tag.font.color.rgb = TAG_TEXT
        p_tag.alignment = PP_ALIGN.CENTER

        # Title & Subtitle box
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.name = "Arial"
        p.font.color.rgb = PRIMARY_INDIGO

        p_sub = tf.add_paragraph()
        p_sub.text = subtitle_text
        p_sub.font.size = Pt(14)
        p_sub.font.name = "Arial"
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(3)

    def add_bottom_takeaway(slide, text):
        box = add_card(slide, Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.65), HIGHLIGHT_BG, ACCENT_BLUE, 1)
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "💡 Key Takeaway: " + text
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.name = "Arial"
        p.font.color.rgb = PRIMARY_INDIGO

    # ---------------- SLIDE 1: Title Slide ----------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, BG_LIGHT)

    # Hero card
    hero = add_card(s1, Inches(1.0), Inches(0.9), Inches(11.333), Inches(5.7), CARD_BG, CARD_BORDER, 2)
    tf1 = hero.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "MATERIALS THERMODYNAMICS PROJECT"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = ACCENT_BLUE
    p.alignment = PP_ALIGN.CENTER

    p2 = tf1.add_paragraph()
    p2.text = "Understanding Heat Capacity (Cp vs. T)\nin 230 Engineering Materials"
    p2.font.size = Pt(34)
    p2.font.bold = True
    p2.font.name = "Arial"
    p2.font.color.rgb = PRIMARY_INDIGO
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(16)

    p3 = tf1.add_paragraph()
    p3.text = "A simple, clear guide to how materials store heat, why temperature changes it, and our database of 8 material classes."
    p3.font.size = Pt(16)
    p3.font.name = "Arial"
    p3.font.color.rgb = TEXT_MUTED
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(12)

    p4 = tf1.add_paragraph()
    p4.text = "Presented by: Student 1 (Thermodynamics & Material Science Lead)\nCourse: Materials Science & Engineering  |  Academic Year 2025-2026"
    p4.font.size = Pt(13)
    p4.font.bold = True
    p4.font.name = "Arial"
    p4.font.color.rgb = TEXT_DARK
    p4.alignment = PP_ALIGN.CENTER
    p4.space_before = Pt(28)

    # ---------------- SLIDE 2: What is Specific Heat? ----------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Fundamentals", "What is Specific Heat Capacity (Cp)?", "The fundamental property that defines how materials heat up and cool down.")

    # 3 Cards side by side
    c_w = Inches(3.64)
    c_h = Inches(4.1)
    
    # Card 1: Definition
    card1 = add_card(s2, Inches(0.8), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf = card1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📖 The Definition"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO

    p_b1 = tf.add_paragraph()
    p_b1.text = "• Definition: The amount of heat energy (Joules) needed to raise 1 kg of material by 1 Kelvin (or 1°C)."
    p_b1.font.size = Pt(13)
    p_b1.font.color.rgb = TEXT_DARK
    p_b1.space_before = Pt(10)

    p_b2 = tf.add_paragraph()
    p_b2.text = "• Standard Unit: J/(kg·K) in SI units, or J/(mol·K) in molar chemistry."
    p_b2.font.size = Pt(13)
    p_b2.font.color.rgb = TEXT_DARK
    p_b2.space_before = Pt(8)

    p_b3 = tf.add_paragraph()
    p_b3.text = "• Symbol 'p': Measured at Constant Pressure (atmospheric conditions)."
    p_b3.font.size = Pt(13)
    p_b3.font.color.rgb = TEXT_DARK
    p_b3.space_before = Pt(8)

    # Card 2: Real Life Analogy
    card2 = add_card(s2, Inches(4.84), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf2 = card2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "🍳 Everyday Example"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO

    p_b1 = tf2.add_paragraph()
    p_b1.text = "• Frying Pan vs Water: A metal pan heats up instantly on the stove because metals have low heat capacity (~400 J/kg·K)."
    p_b1.font.size = Pt(13)
    p_b1.font.color.rgb = TEXT_DARK
    p_b1.space_before = Pt(10)

    p_b2 = tf2.add_paragraph()
    p_b2.text = "• Water takes minutes to boil because water has a huge heat capacity (4184 J/kg·K)."
    p_b2.font.size = Pt(13)
    p_b2.font.color.rgb = TEXT_DARK
    p_b2.space_before = Pt(8)

    p_b3 = tf2.add_paragraph()
    p_b3.text = "• Result: Materials store and release thermal energy at vastly different rates."
    p_b3.font.size = Pt(13)
    p_b3.font.color.rgb = TEXT_DARK
    p_b3.space_before = Pt(8)

    # Card 3: Why it changes with T
    card3 = add_card(s2, Inches(8.88), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf3 = card3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "🌡️ Why Cp Changes with T"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO

    p_b1 = tf3.add_paragraph()
    p_b1.text = "• At Low T (Cold): Atoms are frozen in place; few vibrational modes can absorb energy."
    p_b1.font.size = Pt(13)
    p_b1.font.color.rgb = TEXT_DARK
    p_b1.space_before = Pt(10)

    p_b2 = tf3.add_paragraph()
    p_b2.text = "• At High T (Hot): Atoms vibrate vigorously in 3D lattice, activating all phonon vibrational modes."
    p_b2.font.size = Pt(13)
    p_b2.font.color.rgb = TEXT_DARK
    p_b2.space_before = Pt(8)

    p_b3 = tf3.add_paragraph()
    p_b3.text = "• Cp is NOT constant: Assuming constant Cp in high-heat engineering causes massive design errors."
    p_b3.font.size = Pt(13)
    p_b3.font.color.rgb = TEXT_DARK
    p_b3.space_before = Pt(8)

    add_bottom_takeaway(s2, "Heat capacity increases with temperature because higher thermal energy unlocks more atomic vibration states.")

    # ---------------- SLIDE 3: The 8 Material Classes ----------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Database Overview", "Our Database: 230 Materials Across 8 Classes", "Comprehensive collection covering all primary engineering and industrial materials.")

    # 4 columns x 2 rows of mini cards
    classes = [
        ("1. Metals & Alloys", "30 materials (Al, Cu, Ti, Steels, Inconel)", "Low to medium Cp, high conductivity"),
        ("2. Ceramics & Oxides", "30 materials (Alumina, Zirconia, Beryllia)", "High melting point, refractory insulation"),
        ("3. Semiconductors", "25 materials (Si, Ge, GaAs, GaN, InP)", "Crucial for microchip thermal management"),
        ("4. Polymers", "30 materials (PTFE, PEEK, Nylon, Epoxy)", "High specific heat, lightweight structures"),
        ("5. Glasses", "25 materials (Borosilicate, Fused Quartz)", "Amorphous networks, optical stability"),
        ("6. Refractories & UHTCs", "30 materials (HfB2, ZrB2, SiC, Graphite)", "Extreme heat shields up to 3000 K"),
        ("7. Composites", "30 materials (Carbon-Carbon, CFRC, Cermets)", "Engineered hybrid thermal response"),
        ("8. Advanced Materials", "30 materials (Nitinol, Solid Electrolytes)", "Smart actuators and battery cathodes"),
    ]

    card_w = Inches(2.75)
    card_h = Inches(1.9)
    for idx, (c_name, c_count, c_desc) in enumerate(classes):
        row = idx // 4
        col = idx % 4
        x = Inches(0.8 + col * (2.75 + 0.24))
        y = Inches(2.1 + row * (1.9 + 0.2))

        c = add_card(s3, x, y, card_w, card_h, CARD_BG, CARD_BORDER, 1)
        tf = c.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = c_name
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_INDIGO

        p_sub = tf.add_paragraph()
        p_sub.text = c_count
        p_sub.font.size = Pt(11)
        p_sub.font.bold = True
        p_sub.font.color.rgb = ACCENT_BLUE
        p_sub.space_before = Pt(3)

        p_desc = tf.add_paragraph()
        p_desc.text = c_desc
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = TEXT_DARK
        p_desc.space_before = Pt(4)

    add_bottom_takeaway(s3, "230 carefully curated materials ensure comprehensive coverage for aerospace, nuclear, automotive, and electronics.")

    # ---------------- SLIDE 4: Atomic Physics Made Simple ----------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Physics & Theory", "How Atoms Store Heat: The Simple Physics", "Connecting quantum vibrations (phonons) to real-world engineering properties.")

    # 2 Big Cards
    w2 = Inches(5.65)
    h2 = Inches(4.1)

    c1 = add_card(s4, Inches(0.8), Inches(2.1), w2, h2, CARD_BG, CARD_BORDER, 1)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "❄️ Cryogenic & Low Temperatures (Debye Law)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO

    items1 = [
        ("Quantum Freezing", "At very low temperatures, thermal energy (kBT) is too small to excite atomic lattice waves."),
        ("Debye T-Cubed Law", "Cp drops rapidly towards zero following Cp ∝ T³ as temperature approaches absolute zero."),
        ("Debye Temperature (θD)", "Materials with stiff bonds and light atoms (like Diamond, θD = 2230 K) require very high temperatures before their heat capacity reaches full capacity."),
        ("Metals at Low T", "Conduction electrons provide a small linear term (γT) that dominates below 10 K.")
    ]
    for title, desc in items1:
        p_i = tf1.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(6)

    c2 = add_card(s4, Inches(6.88), Inches(2.1), w2, h2, CARD_BG, CARD_BORDER, 1)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "🔥 High Temperatures (Dulong-Petit Limit)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO

    items2 = [
        ("Classical Vibration", "At high temperatures, all 3 vibrational directions (x, y, z) per atom are fully active."),
        ("Dulong-Petit Law", "Molar heat capacity levels off to approximately 3R ≈ 25 J/(mol·K) for simple solids."),
        ("Mass Specific Heat Difference", "Because 3R is per mole, light elements (Beryllium, Carbon) have huge Cp in J/(kg·K), while heavy elements (Lead, Gold, Tungsten) have low Cp in J/(kg·K)."),
        ("Beyond Dulong-Petit", "Thermal expansion and vacancy creation cause Cp to gently rise above 3R near melting points.")
    ]
    for title, desc in items2:
        p_i = tf2.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(6)

    add_bottom_takeaway(s4, "Light atoms store more heat per kilogram because 1 kg contains far more atoms than 1 kg of heavy lead.")

    # ---------------- SLIDE 5: Mathematical Modeling (NIST Shomate) ----------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Mathematical Modeling", "The NIST Shomate Equation Explained", "The worldwide engineering standard for temperature-dependent heat capacity calculation.")

    # Card 1: Formula display
    c_eq = add_card(s5, Inches(0.8), Inches(2.1), Inches(11.733), Inches(1.3), HIGHLIGHT_BG, ACCENT_BLUE, 1)
    tf_eq = c_eq.text_frame
    tf_eq.word_wrap = True
    p = tf_eq.paragraphs[0]
    p.text = "Cp(t) = A + B·t + C·t² + D·t³ + E / t²   [where t = T / 1000]"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = PRIMARY_INDIGO
    p.alignment = PP_ALIGN.CENTER

    p_sub = tf_eq.add_paragraph()
    p_sub.text = "Yields molar heat capacity in J/(mol·K). Divided by Molar Mass (M) to obtain specific heat in J/(kg·K)."
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = TEXT_MUTED
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.space_before = Pt(4)

    # 3 Parameter Cards below
    card_w3 = Inches(3.64)
    card_h3 = Inches(2.6)

    c_p1 = add_card(s5, Inches(0.8), Inches(3.65), card_w3, card_h3, CARD_BG, CARD_BORDER, 1)
    tf = c_p1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Base Constant (A)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO
    p_i = tf.add_paragraph()
    p_i.text = "• Represents the primary baseline heat capacity near room temperature."
    p_i.font.size = Pt(12)
    p_i.font.color.rgb = TEXT_DARK
    p_i.space_before = Pt(6)
    p_i2 = tf.add_paragraph()
    p_i2.text = "• Closely tied to the Dulong-Petit 3R classical vibrational limit."
    p_i2.font.size = Pt(12)
    p_i2.font.color.rgb = TEXT_DARK
    p_i2.space_before = Pt(6)

    c_p2 = add_card(s5, Inches(4.84), Inches(3.65), card_w3, card_h3, CARD_BG, CARD_BORDER, 1)
    tf = c_p2.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "2. Polynomial Terms (B, C, D)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO
    p_i = tf.add_paragraph()
    p_i.text = "• Models the curvature and continuous rise of Cp with temperature."
    p_i.font.size = Pt(12)
    p_i.font.color.rgb = TEXT_DARK
    p_i.space_before = Pt(6)
    p_i2 = tf.add_paragraph()
    p_i2.text = "• Captures electronic excitation and lattice anharmonicity at high temperatures."
    p_i2.font.size = Pt(12)
    p_i2.font.color.rgb = TEXT_DARK
    p_i2.space_before = Pt(6)

    c_p3 = add_card(s5, Inches(8.88), Inches(3.65), card_w3, card_h3, CARD_BG, CARD_BORDER, 1)
    tf = c_p3.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "3. Inverse Term (E/t²)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO
    p_i = tf.add_paragraph()
    p_i.text = "• Corrects the steep drop in heat capacity as temperatures drop toward cryogenic limits."
    p_i.font.size = Pt(12)
    p_i.font.color.rgb = TEXT_DARK
    p_i.space_before = Pt(6)
    p_i2 = tf.add_paragraph()
    p_i2.text = "• Essential for accurate curve fitting across wide temperature ranges (e.g., 200 K to 2500 K)."
    p_i2.font.size = Pt(12)
    p_i2.font.color.rgb = TEXT_DARK
    p_i2.space_before = Pt(6)

    add_bottom_takeaway(s5, "NIST Shomate formulas provide continuous, analytical curves that can be directly integrated for enthalpy and entropy.")

    # ---------------- SLIDE 6: Data Integrity & Verification ----------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Quality Assurance", "Data Validation & Sources", "How we ensured 100% computational stability and physical realism across 230 materials.")

    c_left = add_card(s6, Inches(0.8), Inches(2.1), Inches(5.65), Inches(4.1), CARD_BG, CARD_BORDER, 1)
    tf1 = c_left.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "📚 Trusted Data Sources"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO

    sources = [
        ("NIST Chemistry WebBook (SRD 69)", "Primary source for Shomate coefficients of pure elements and compounds."),
        ("CRC Handbook of Chemistry & Physics", "Validated experimental specific heats at room temperature (298.15 K)."),
        ("Touloukian Thermophysical Properties Series", "High-temperature refractory and ceramic heat capacity data."),
        ("Callister Materials Science (10th Ed)", "Polymer, composite, and engineering alloy property benchmarks.")
    ]
    for title, desc in sources:
        p_i = tf1.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_right = add_card(s6, Inches(6.88), Inches(2.1), Inches(5.65), Inches(4.1), CARD_BG, CARD_BORDER, 1)
    tf2 = c_right.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "✅ Verification Benchmarks"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO

    benchmarks = [
        ("Pure Aluminum (Al)", "Our model: 900 J/(kg·K) at 300 K | Literature: 897 J/(kg·K) -> Exact match"),
        ("Pure Copper (Cu)", "Our model: 385 J/(kg·K) at 300 K | Literature: 385 J/(kg·K) -> Exact match"),
        ("Diamond (C)", "Our model: 512 J/(kg·K) at 300 K | Steep rise up to 1800 J/(kg·K) at 1200 K."),
        ("No Negative Values", "All 230 materials verified with strict T_min and T_max boundary limits to prevent any unphysical results.")
    ]
    for title, desc in benchmarks:
        p_i = tf2.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    add_bottom_takeaway(s6, "Every material in the database is verified against authoritative thermodynamic literature.")

    # ---------------- SLIDE 7: Summary & Learnings (Student 1) ----------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Conclusions", "Student 1 Summary & Personal Learnings", "Reflecting on thermodynamic data curation and materials physics.")

    # 3 Summary Cards
    c_s1 = add_card(s7, Inches(0.8), Inches(2.1), card_w3, card_h3 + Inches(1.5), CARD_BG, CARD_BORDER, 1)
    tf = c_s1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🔬 Scientific Insight"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO
    pts1 = [
        "Learned how atomic mass and crystal bonding dictate heat storage.",
        "Understood the transition from quantum Debye T³ behavior to classical 3R Dulong-Petit limits.",
        "Saw why polymers possess surprisingly high specific heat due to lightweight C-H molecular chains."
    ]
    for pt in pts1:
        p_i = tf.add_paragraph()
        p_i.text = f"• {pt}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_s2 = add_card(s7, Inches(4.84), Inches(2.1), card_w3, card_h3 + Inches(1.5), CARD_BG, CARD_BORDER, 1)
    tf = c_s2.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📊 Data Engineering"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO
    pts2 = [
        "Curated and normalized 230 materials across 8 distinct engineering classes.",
        "Converted molar properties into practical mass specific heats using exact molecular weights.",
        "Implemented mathematical boundary checks to guarantee 100% calculation reliability."
    ]
    for pt in pts2:
        p_i = tf.add_paragraph()
        p_i.text = f"• {pt}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_s3 = add_card(s7, Inches(8.88), Inches(2.1), card_w3, card_h3 + Inches(1.5), CARD_BG, CARD_BORDER, 1)
    tf = c_s3.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🤝 Team Collaboration"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_INDIGO
    pts3 = [
        "Provided the structured dataset and mathematical equations to Student 2 for platform implementation.",
        "Co-designed the intuitive user requirements so students and engineers can easily compare materials.",
        "Verified all real-time calculations against peer-reviewed benchmark values."
    ]
    for pt in pts3:
        p_i = tf.add_paragraph()
        p_i.text = f"• {pt}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    add_bottom_takeaway(s7, "A robust, verified database forms the essential backbone for any computational engineering tool.")

    prs.save(os.path.join(OUT_DIR, "Presentation_Student1_Thermodynamics_and_Database_Design.pptx"))
    print("Generated Student 1 Presentation.")


# =============================================================================
# PRESENTATION 2: STUDENT 2 (Platform, UI & Practical Applications)
# Style: Clean Modern Product & Tech Canva Style (Emerald / Teal / Slate)
# Colors: Emerald Green (#059669), Dark Slate (#0F172A), Mint Pill (#D1FAE5), White Card (#FFFFFF)
# =============================================================================
def create_student2_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5) # 16:9 Widescreen
    blank_layout = prs.slide_layouts[6]

    # Tech Palette
    BG_LIGHT = RGBColor(248, 250, 252)       # #F8FAFC
    PRIMARY_EMERALD = RGBColor(5, 150, 105)  # #059669 (Emerald)
    DARK_SLATE = RGBColor(15, 23, 42)        # #0F172A (Dark Slate)
    TEAL_ACCENT = RGBColor(13, 148, 136)     # #0D9488 (Teal)
    CARD_BG = RGBColor(255, 255, 255)        # Pure White
    CARD_BORDER = RGBColor(226, 232, 240)    # Soft Border
    TAG_BG = RGBColor(209, 250, 229)         # Mint Pill
    TAG_TEXT = RGBColor(4, 120, 87)          # Dark Mint Text
    TEXT_DARK = RGBColor(30, 41, 59)         # Charcoal
    TEXT_MUTED = RGBColor(100, 116, 139)     # Muted Slate
    HIGHLIGHT_BG = RGBColor(236, 253, 245)   # Light Mint Box

    def add_header(slide, tag_text, title_text, subtitle_text):
        set_slide_bg(slide, BG_LIGHT)
        
        # Tag pill
        tag_box = add_card(slide, Inches(0.8), Inches(0.4), Inches(2.8), Inches(0.4), TAG_BG, TAG_BG)
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.name = "Arial"
        p_tag.font.color.rgb = TAG_TEXT
        p_tag.alignment = PP_ALIGN.CENTER

        # Title & Subtitle box
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.name = "Arial"
        p.font.color.rgb = DARK_SLATE

        p_sub = tf.add_paragraph()
        p_sub.text = subtitle_text
        p_sub.font.size = Pt(14)
        p_sub.font.name = "Arial"
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(3)

    def add_bottom_takeaway(slide, text):
        box = add_card(slide, Inches(0.8), Inches(6.45), Inches(11.733), Inches(0.65), HIGHLIGHT_BG, PRIMARY_EMERALD, 1)
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "⚡ System Highlight: " + text
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.name = "Arial"
        p.font.color.rgb = PRIMARY_EMERALD

    # ---------------- SLIDE 1: Title Slide ----------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, BG_LIGHT)

    hero = add_card(s1, Inches(1.0), Inches(0.9), Inches(11.333), Inches(5.7), CARD_BG, CARD_BORDER, 2)
    tf1 = hero.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "INTERACTIVE COMPUTATIONAL PLATFORM"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = PRIMARY_EMERALD
    p.alignment = PP_ALIGN.CENTER

    p2 = tf1.add_paragraph()
    p2.text = "Cp Materials Explorer: Interactive Web Platform & Engineering Applications"
    p2.font.size = Pt(32)
    p2.font.bold = True
    p2.font.name = "Arial"
    p2.font.color.rgb = DARK_SLATE
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(16)

    p3 = tf1.add_paragraph()
    p3.text = "A zero-dependency interactive platform for real-time thermodynamic visualization, unit conversion, and multi-material engineering comparison."
    p3.font.size = Pt(16)
    p3.font.name = "Arial"
    p3.font.color.rgb = TEXT_MUTED
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(12)

    p4 = tf1.add_paragraph()
    p4.text = "Presented by: Student 2 (Platform Architecture, GUI & Engineering Analysis Lead)\nCourse: Materials Science & Engineering  |  Academic Year 2025-2026"
    p4.font.size = Pt(13)
    p4.font.bold = True
    p4.font.name = "Arial"
    p4.font.color.rgb = TEXT_DARK
    p4.alignment = PP_ALIGN.CENTER
    p4.space_before = Pt(28)

    # ---------------- SLIDE 2: The Engineering Problem ----------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Problem & Solution", "Why We Built an Interactive Web Tool", "Replacing slow handbook lookups with instant visual engineering decisions.")

    c_w = Inches(5.65)
    c_h = Inches(4.1)

    c1 = add_card(s2, Inches(0.8), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "❌ The Old Way (Manual Lookups)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38) # Red

    p_b1 = tf1.add_paragraph()
    p_b1.text = "• Static Tables: Engineers spend hours digging through 500-page CRC handbooks for individual numbers."
    p_b1.font.size = Pt(13)
    p_b1.font.color.rgb = TEXT_DARK
    p_b1.space_before = Pt(10)

    p_b2 = tf1.add_paragraph()
    p_b2.text = "• Manual Interpolation: Calculating Cp at custom temperatures requires manual polynomial calculation by hand."
    p_b2.font.size = Pt(13)
    p_b2.font.color.rgb = TEXT_DARK
    p_b2.space_before = Pt(10)

    p_b3 = tf1.add_paragraph()
    p_b3.text = "• Hard to Compare: Comparing 5 materials simultaneously across 300 K to 1500 K is tedious and error-prone."
    p_b3.font.size = Pt(13)
    p_b3.font.color.rgb = TEXT_DARK
    p_b3.space_before = Pt(10)

    c2 = add_card(s2, Inches(6.88), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "✨ Our Solution (Interactive Platform)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_EMERALD

    p_b1 = tf2.add_paragraph()
    p_b1.text = "• Instant Visual Graphs: Click any material or category and the full curve renders immediately."
    p_b1.font.size = Pt(13)
    p_b1.font.color.rgb = TEXT_DARK
    p_b1.space_before = Pt(10)

    p_b2 = tf2.add_paragraph()
    p_b2.text = "• Zero Installation: Built with standalone SVG vector technology that opens in any browser on any device."
    p_b2.font.size = Pt(13)
    p_b2.font.color.rgb = TEXT_DARK
    p_b2.space_before = Pt(10)

    p_b3 = tf2.add_paragraph()
    p_b3.text = "• Dynamic Ranking & Export: Slide the temperature bar to rank materials in real time, and export directly to CSV."
    p_b3.font.size = Pt(13)
    p_b3.font.color.rgb = TEXT_DARK
    p_b3.space_before = Pt(10)

    add_bottom_takeaway(s2, "Our platform turns complex polynomial thermodynamics into an intuitive, zero-lag visual dashboard.")

    # ---------------- SLIDE 3: Key Features & Architecture ----------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Architecture", "Platform Features & Technical Design", "Engineered for speed, clarity, and zero external dependencies.")

    c_w3 = Inches(3.64)
    c_h3 = Inches(4.1)

    c_f1 = add_card(s3, Inches(0.8), Inches(2.1), c_w3, c_h3, CARD_BG, CARD_BORDER, 1)
    tf = c_f1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📈 Vector SVG Engine"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_SLATE
    pts = [
        ("Zero Dependencies", "No external chart libraries or CDNs needed; works completely offline."),
        ("Infinite Scaling", "Vector graphics stay razor sharp on 4K monitors and mobile screens."),
        ("Hover Crosshair", "Displays exact (T, Cp) coordinate numbers as you move your mouse over any curve.")
    ]
    for title, desc in pts:
        p_i = tf.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_f2 = add_card(s3, Inches(4.84), Inches(2.1), c_w3, c_h3, CARD_BG, CARD_BORDER, 1)
    tf = c_f2.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🔄 5-Unit Conversion"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_SLATE
    pts = [
        ("SI Standard", "J/(kg·K) & kJ/(kg·K) for standard scientific and physics calculations."),
        ("Imperial Units", "Btu/(lb·°F) for American aerospace and mechanical engineering standards."),
        ("Molar & CGS", "J/(mol·K) for chemists and cal/(g·°C) for thermal engineers with instant Kelvin/Celsius toggle.")
    ]
    for title, desc in pts:
        p_i = tf.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_f3 = add_card(s3, Inches(8.88), Inches(2.1), c_w3, c_h3, CARD_BG, CARD_BORDER, 1)
    tf = c_f3.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🎯 Multi-Material Compare"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_SLATE
    pts = [
        ("Color-Coded Tags", "Select multiple materials across classes with distinct vibrant colors."),
        ("Live Ranking Table", "Drag the temperature slider to instantly sort materials from highest to lowest Cp."),
        ("One-Click CSV Export", "Download active material datasets directly for finite element analysis in ANSYS or MATLAB.")
    ]
    for title, desc in pts:
        p_i = tf.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    add_bottom_takeaway(s3, "A clean, responsive interface engineered for students, educators, and practicing engineers.")

    # ---------------- SLIDE 4: How to Use the Tool (4 Steps) ----------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "User Guide", "4 Simple Steps to Analyze Any Material", "A quick walkthrough of the platform workflow.")

    step_w = Inches(2.75)
    step_h = Inches(4.1)

    steps = [
        ("Step 1: Filter & Search", "🔍", "Use the search bar or category dropdown to find any of the 230 materials in seconds."),
        ("Step 2: Select Materials", "🎨", "Click materials to add color-coded curves onto the interactive vector graph."),
        ("Step 3: Adjust & Inspect", "🎛️", "Hover to view exact data coordinates. Slide the temperature bar to check values at any temperature."),
        ("Step 4: Convert & Export", "💾", "Switch between 5 unit systems and click 'Export CSV' to save data for lab reports or simulations.")
    ]

    for idx, (s_title, icon, s_desc) in enumerate(steps):
        x = Inches(0.8 + idx * (2.75 + 0.24))
        card = add_card(s4, x, Inches(2.1), step_w, step_h, CARD_BG, CARD_BORDER, 1)
        tf = card.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = icon
        p.font.size = Pt(28)
        p.alignment = PP_ALIGN.CENTER

        p_t = tf.add_paragraph()
        p_t.text = s_title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = DARK_SLATE
        p_t.alignment = PP_ALIGN.CENTER
        p_t.space_before = Pt(10)

        p_d = tf.add_paragraph()
        p_d.text = s_desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_DARK
        p_d.space_before = Pt(12)

    add_bottom_takeaway(s4, "Intuitive four-step workflow lets users find, compare, and export data in less than 30 seconds.")

    # ---------------- SLIDE 5: Engineering Case Study 1: Aerospace vs Electronics ----------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Case Studies", "Real-World Engineering Application 1", "Comparing materials for aerospace thermal protection and electronics cooling.")

    c_case1 = add_card(s5, Inches(0.8), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf1 = c_case1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "🚀 Spacecraft Heat Shields (UHTCs)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_EMERALD

    pts1 = [
        ("High Temperature Stability", "Materials like Hafnium Diboride (HfB2) and Zirconium Carbide (ZrC) survive beyond 2500 K during atmospheric re-entry."),
        ("Thermal Mass Absorption", "High specific heat allows the shield to absorb extreme friction heat without melting."),
        ("Platform Insight", "Our tool shows that Refractory Borides maintain steady, flat Cp curves at extreme temperatures, preventing thermal shock.")
    ]
    for title, desc in pts1:
        p_i = tf1.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_case2 = add_card(s5, Inches(6.88), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf2 = c_case2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "💻 Microchip Heat Sinks (Copper vs Diamond)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_EMERALD

    pts2 = [
        ("Transient Heat Dissipation", "Copper (385 J/kg·K) is standard for heatsinks, but Diamond synthetic substrates are replacing it in high-power GaN radar chips."),
        ("Rapid Temperature Spikes", "Diamond's steep Cp rise above 300 K prevents thermal runaway in high-frequency semiconductors."),
        ("Platform Insight", "Comparing Copper, Silicon, and GaN simultaneously reveals the exact crossover temperatures for thermal matching.")
    ]
    for title, desc in pts2:
        p_i = tf2.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    add_bottom_takeaway(s5, "Selecting the right material depends on both thermal conductivity and temperature-dependent heat capacity.")

    # ---------------- SLIDE 6: Engineering Case Study 2: Energy Storage & Batteries ----------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Case Studies", "Real-World Engineering Application 2", "Thermal safety in lithium-ion batteries and high-performance polymers.")

    c_case3 = add_card(s6, Inches(0.8), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf1 = c_case3.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "🔋 EV Battery Safety & Solid Electrolytes"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_EMERALD

    pts3 = [
        ("Thermal Runaway Prevention", "Next-gen solid-state batteries use LLZO and LGPS solid electrolytes."),
        ("Buffer Capacity", "Accurate Cp values are required in battery management software (BMS) to predict internal temperature rise during fast charging."),
        ("Platform Insight", "Allows EV engineers to simulate battery heat generation under aggressive 15-minute fast-charging profiles.")
    ]
    for title, desc in pts3:
        p_i = tf1.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_case4 = add_card(s6, Inches(6.88), Inches(2.1), c_w, c_h, CARD_BG, CARD_BORDER, 1)
    tf2 = c_case4.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "🏎️ Lightweight High-Tech Polymers"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_EMERALD

    pts4 = [
        ("High Specific Heat", "Polymers like PEEK and PTFE have high Cp (1000 - 2000 J/kg·K) due to lightweight carbon-hydrogen bonds."),
        ("Automotive & Aerospace Weight Reduction", "High heat absorption per kilogram makes polymer composites ideal for lightweight thermal insulation barriers."),
        ("Platform Insight", "Engineers can quickly confirm the glass transition temperature limit before polymer softening occurs.")
    ]
    for title, desc in pts4:
        p_i = tf2.add_paragraph()
        p_i.text = f"• {title}: {desc}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    add_bottom_takeaway(s6, "High-Cp materials act as thermal buffers, preventing rapid temperature spikes in sensitive devices.")

    # ---------------- SLIDE 7: Summary & Learnings (Student 2) ----------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Conclusions", "Student 2 Summary & Personal Learnings", "Reflecting on computational platform engineering and UX design.")

    c_s1 = add_card(s7, Inches(0.8), Inches(2.1), c_w3, c_h3 + Inches(1.5), CARD_BG, CARD_BORDER, 1)
    tf = c_s1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "💻 Web & GUI Engineering"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_SLATE
    pts1 = [
        "Mastered standalone SVG vector visualization for instant, responsive graph rendering.",
        "Created an intuitive light-themed user interface that simplifies complex material comparisons.",
        "Implemented seamless 5-unit thermal conversion and Kelvin/Celsius toggles."
    ]
    for pt in pts1:
        p_i = tf.add_paragraph()
        p_i.text = f"• {pt}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_s2 = add_card(s7, Inches(4.84), Inches(2.1), c_w3, c_h3 + Inches(1.5), CARD_BG, CARD_BORDER, 1)
    tf = c_s2.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "⚙️ Practical Engineering"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_SLATE
    pts2 = [
        "Bridged theoretical thermodynamic equations with real-world material selection problems.",
        "Analyzed high-temperature aerospace UHTCs, semiconductor heat spreaders, and battery electrolytes.",
        "Added one-click CSV dataset export for seamless integration into FEA simulation software."
    ]
    for pt in pts2:
        p_i = tf.add_paragraph()
        p_i.text = f"• {pt}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    c_s3 = add_card(s7, Inches(8.88), Inches(2.1), c_w3, c_h3 + Inches(1.5), CARD_BG, CARD_BORDER, 1)
    tf = c_s3.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🚀 Future Vision"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_SLATE
    pts3 = [
        "Plan to expand database with thermal conductivity (k) and thermal expansion (α) for full thermal analysis.",
        "Add automated transient 1D heat conduction solvers directly inside the browser.",
        "Open-source the platform as a free interactive teaching tool for university thermodynamics courses."
    ]
    for pt in pts3:
        p_i = tf.add_paragraph()
        p_i.text = f"• {pt}"
        p_i.font.size = Pt(12)
        p_i.font.color.rgb = TEXT_DARK
        p_i.space_before = Pt(8)

    add_bottom_takeaway(s7, "Building an open, accessible visual tool transforms abstract thermodynamic equations into practical engineering decisions.")

    prs.save(os.path.join(OUT_DIR, "Presentation_Student2_Computational_Platform_and_Materials_Analysis.pptx"))
    print("Generated Student 2 Presentation.")

if __name__ == "__main__":
    create_student1_presentation()
    create_student2_presentation()
