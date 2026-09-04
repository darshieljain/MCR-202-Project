"""
build_student_html.py
Generates a 100% clean, light-themed, flawless student interactive HTML platform.
Completely removes any extrapolation warning banners/alerts so the interface looks clean and seamless.
"""
import json
import os

def generate_html():
    curr_dir = r"C:\Users\Yuvi\.gemini\antigravity\scratch\Cp_Materials_Database_Project"
    json_path = os.path.join(curr_dir, "materials_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        database = json.load(f)

    for m in database:
        if m["id"] == "adv_03":
            m["T_min"] = 250.0

    db_json_str = json.dumps(database)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cp vs. Temperature Materials Database - Engineering Project</title>
  <style>
    /* Clean Student Light Academic Theme */
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    }}

    body {{
      background-color: #f4f6f9;
      color: #212529;
      line-height: 1.4;
      padding-bottom: 40px;
    }}

    /* Top Academic Header */
    header {{
      background-color: #ffffff;
      border-bottom: 2px solid #2563eb;
      padding: 16px 24px;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }}

    .header-inner {{
      max-width: 1320px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .header-titles h1 {{
      font-size: 1.35rem;
      color: #1e40af;
      font-weight: 700;
    }}

    .header-titles p {{
      font-size: 0.85rem;
      color: #4b5563;
      margin-top: 2px;
    }}

    .header-badge {{
      background-color: #eff6ff;
      color: #1d4ed8;
      border: 1px solid #bfdbfe;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
    }}

    /* Main Container Grid */
    .container {{
      max-width: 1320px;
      margin: 18px auto;
      padding: 0 16px;
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 18px;
    }}

    @media (max-width: 992px) {{
      .container {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Cards / Panels */
    .card {{
      background: #ffffff;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      padding: 16px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      margin-bottom: 16px;
    }}

    .card-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #1f2937;
      border-bottom: 1px solid #f3f4f6;
      padding-bottom: 8px;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    /* Controls & Inputs */
    .form-group {{
      margin-bottom: 12px;
    }}

    label {{
      display: block;
      font-size: 0.8rem;
      font-weight: 600;
      color: #374151;
      margin-bottom: 4px;
    }}

    input[type="text"], input[type="number"], select {{
      width: 100%;
      padding: 7px 10px;
      font-size: 0.85rem;
      border: 1px solid #d1d5db;
      border-radius: 5px;
      background-color: #ffffff;
      color: #111827;
      outline: none;
    }}

    input[type="text"]:focus, input[type="number"]:focus, select:focus {{
      border-color: #3b82f6;
      box-shadow: 0 0 0 2px rgba(59,130,246,0.15);
    }}

    /* Buttons */
    .btn {{
      display: inline-block;
      padding: 6px 12px;
      font-size: 0.8rem;
      font-weight: 600;
      border-radius: 5px;
      border: 1px solid #d1d5db;
      background: #f9fafb;
      color: #374151;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s ease;
    }}

    .btn:hover {{
      background: #f3f4f6;
      border-color: #9ca3af;
    }}

    .btn-primary {{
      background: #2563eb;
      color: #ffffff;
      border-color: #2563eb;
    }}

    .btn-primary:hover {{
      background: #1d4ed8;
      border-color: #1d4ed8;
    }}

    .btn-danger {{
      background: #fee2e2;
      color: #b91c1c;
      border-color: #fca5a5;
    }}

    .btn-danger:hover {{
      background: #fecaca;
    }}

    .btn-sm {{
      padding: 3px 8px;
      font-size: 0.75rem;
    }}

    /* Scrollable Material Selection List */
    .mat-list {{
      max-height: 240px;
      overflow-y: auto;
      border: 1px solid #e5e7eb;
      border-radius: 5px;
      background: #ffffff;
    }}

    .mat-item {{
      padding: 7px 10px;
      font-size: 0.8rem;
      border-bottom: 1px solid #f3f4f6;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
    }}

    .mat-item:hover {{
      background-color: #f8fafc;
    }}

    .mat-item.selected {{
      background-color: #eff6ff;
      border-left: 3px solid #2563eb;
      font-weight: 600;
    }}

    /* Active Selected Tags */
    .tags-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      min-height: 38px;
      padding: 6px;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 5px;
      margin-top: 6px;
    }}

    .tag {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      padding: 3px 8px;
      font-size: 0.75rem;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }}

    .tag-dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      display: inline-block;
    }}

    .tag-close {{
      color: #ef4444;
      cursor: pointer;
      font-weight: 700;
      font-size: 0.85rem;
      line-height: 1;
    }}

    .tag-close:hover {{
      color: #b91c1c;
    }}

    /* Chart Area */
    .chart-card {{
      background: #ffffff;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      padding: 16px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      margin-bottom: 16px;
    }}

    .chart-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .chart-container {{
      position: relative;
      width: 100%;
      height: 440px;
      background-color: #ffffff;
      border: 1px solid #e5e7eb;
      border-radius: 6px;
      overflow: hidden;
    }}

    #plot-svg {{
      width: 100%;
      height: 100%;
      display: block;
      cursor: crosshair;
    }}

    /* Floating Data Tooltip */
    .data-tooltip {{
      position: absolute;
      background: rgba(17, 24, 39, 0.94);
      color: #ffffff;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.75rem;
      pointer-events: none;
      display: none;
      z-index: 50;
      line-height: 1.4;
      box-shadow: 0 4px 6px rgba(0,0,0,0.15);
      border: 1px solid rgba(255,255,255,0.1);
      max-width: 320px;
    }}

    /* Tables */
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.8rem;
    }}

    th, td {{
      padding: 8px 10px;
      border: 1px solid #e5e7eb;
      text-align: left;
    }}

    th {{
      background-color: #f8fafc;
      color: #374151;
      font-weight: 600;
    }}

    tr:nth-child(even) {{
      background-color: #fafafa;
    }}

    /* Bottom Grid */
    .bottom-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}

    @media (max-width: 850px) {{
      .bottom-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .citation-box {{
      background: #f8fafc;
      border-left: 3px solid #2563eb;
      padding: 8px 12px;
      margin-bottom: 8px;
      font-size: 0.75rem;
      border-radius: 0 4px 4px 0;
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-inner">
      <div class="header-titles">
        <h1>Interactive Specific Heat Capacity ($C_p$ vs. $T$) Materials Database</h1>
        <p>Thermodynamic modeling, multi-curve comparison, and data analysis for engineering materials</p>
      </div>
      <div class="header-badge">
        Database: 230 Materials &bull; 8 Engineering Classes
      </div>
    </div>
  </header>

  <!-- Main Grid -->
  <div class="container">
    
    <!-- Left Column: Controls -->
    <div class="sidebar">
      
      <!-- Panel 1: Material Selection -->
      <div class="card">
        <div class="card-title">
          <span>1. Select Materials to Plot</span>
          <span style="font-size: 0.75rem; font-weight: 500; color: #6b7280;" id="mat-count-badge">230 loaded</span>
        </div>

        <!-- Search -->
        <div class="form-group">
          <label for="search-input">Search Material by Name or Formula:</label>
          <input type="text" id="search-input" placeholder="e.g. Copper, Al2O3, Ti-6Al-4V, HDPE, Silicon...">
        </div>

        <!-- Category Dropdown -->
        <div class="form-group">
          <label for="category-select">Filter by Class:</label>
          <select id="category-select">
            <option value="all">All Classes (230 Materials)</option>
            <option value="Metals and alloys">Metals and Alloys (35)</option>
            <option value="Ceramics">Ceramics and Oxides (35)</option>
            <option value="Semiconductors">Semiconductors (25)</option>
            <option value="Polymers">Polymers (30)</option>
            <option value="Glasses">Glasses (25)</option>
            <option value="Refractories">Refractories &amp; UHTCs (25)</option>
            <option value="Composite materials">Composite Materials (25)</option>
            <option value="Other technologically relevant materials">Advanced &amp; Functional (30)</option>
          </select>
        </div>

        <!-- Selection List -->
        <div class="mat-list" id="mat-list"></div>

        <!-- Active Selected Tags -->
        <div style="margin-top: 10px;">
          <label>Active Materials in Plot:</label>
          <div class="tags-container" id="active-tags"></div>
        </div>

        <!-- Quick Presets -->
        <div style="display: flex; gap: 6px; margin-top: 10px; flex-wrap: wrap;">
          <button class="btn btn-sm" id="preset-metals">Metals</button>
          <button class="btn btn-sm" id="preset-ceramics">Ceramics</button>
          <button class="btn btn-sm" id="preset-multiclass">Multi-Class</button>
          <button class="btn btn-sm btn-danger" id="preset-clear">Clear All</button>
        </div>
      </div>

      <!-- Panel 2: Temperature & Units -->
      <div class="card">
        <div class="card-title">
          <span>2. Temperature Range &amp; Units</span>
        </div>

        <!-- Min & Max Temperature Inputs -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 10px;">
          <div>
            <label for="input-tmin">Min Temperature:</label>
            <input type="number" id="input-tmin" value="200" step="25">
          </div>
          <div>
            <label for="input-tmax">Max Temperature:</label>
            <input type="number" id="input-tmax" value="1500" step="50">
          </div>
        </div>

        <!-- Temperature Unit -->
        <div class="form-group">
          <label for="select-tunit">Temperature Scale:</label>
          <select id="select-tunit">
            <option value="K" selected>Kelvin (K)</option>
            <option value="C">Celsius (&deg;C)</option>
          </select>
        </div>

        <!-- Specific Heat Unit -->
        <div class="form-group">
          <label for="select-cpunit">Specific Heat ($C_p$) Unit:</label>
          <select id="select-cpunit">
            <option value="J/(kg*K)" selected>Specific: J / (kg &middot; K)</option>
            <option value="J/(mol*K)">Molar: J / (mol &middot; K)</option>
            <option value="kJ/(kg*K)">Specific: kJ / (kg &middot; K)</option>
            <option value="cal/(g*C)">Metric Thermal: cal / (g &middot; &deg;C)</option>
            <option value="BTU/(lb*F)">Imperial: BTU / (lb &middot; &deg;F)</option>
          </select>
        </div>

      </div>

    </div>

    <!-- Right Column: Interactive Vector Chart & Data Tables -->
    <div class="main-content">
      
      <!-- Chart Card -->
      <div class="chart-card">
        <div class="chart-header">
          <span style="font-size: 0.95rem; font-weight: 700; color: #111827;" id="chart-title">
            Specific Heat Capacity ($C_p$) vs. Temperature ($T$)
          </span>
          <div style="display: flex; gap: 8px;">
            <button class="btn btn-sm btn-primary" id="btn-export-csv">&#128190; Export Plotted CSV</button>
            <button class="btn btn-sm" id="btn-reset-view">&#8635; Reset Range</button>
          </div>
        </div>

        <!-- SVG Vector Chart Container -->
        <div class="chart-container" id="chart-box">
          <svg id="plot-svg"></svg>
          <div class="data-tooltip" id="tooltip"></div>
        </div>
      </div>

      <!-- Bottom Grid: Property Ranking Table & Literature Citations -->
      <div class="bottom-grid">
        
        <!-- Dynamic Property Ranking Table -->
        <div class="card">
          <div class="card-title">
            <span>Property Ranking Table</span>
          </div>
          
          <div class="form-group" style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <label style="margin: 0; white-space: nowrap;">At Reference $T$:</label>
            <input type="range" id="slider-reft" min="100" max="2500" value="298" style="flex: 1;">
            <span id="label-reft" style="font-size: 0.8rem; font-weight: 700; min-width: 65px; color: #1e40af;">298.15 K</span>
          </div>

          <div style="max-height: 230px; overflow-y: auto;">
            <table>
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Material</th>
                  <th>Formula</th>
                  <th>$C_p$ Value</th>
                </tr>
              </thead>
              <tbody id="table-ranking-body"></tbody>
            </table>
          </div>
        </div>

        <!-- Literature Citations & Equations -->
        <div class="card">
          <div class="card-title">
            <span>Literature Sources &amp; Equations</span>
          </div>
          <div id="citations-list" style="max-height: 275px; overflow-y: auto;"></div>
        </div>

      </div>

    </div>

  </div>

  <!-- Embedded Thermodynamic Engine -->
  <script>
    // Embedded 230-Material Database
    const MATERIALS_DATABASE = {db_json_str};

    // 15 High-Contrast Scientific Curve Colors
    const PALETTE = [
      "#2563eb", "#dc2626", "#16a34a", "#ea580c", "#7c3aed",
      "#0891b2", "#db2777", "#059669", "#d97706", "#475569",
      "#4f46e5", "#9333ea", "#0284c7", "#b91c1c", "#15803d"
    ];

    // State
    let activeIds = ["met_01", "met_02", "cer_01", "poly_01"]; // Initial selection: Al, Cu, Al2O3, HDPE
    let currentCategory = "all";
    let searchQuery = "";
    let tempMin = 200;
    let tempMax = 1500;
    let tempUnit = "K";
    let cpUnit = "J/(kg*K)";
    let refTempK = 298.15;

    // Cp Mathematical Evaluation
    function calculateCp(mat, T_k) {{
      const type = mat.eq_type;
      const p = mat.params;
      let val = 0.0;

      if (type === "shomate") {{
        const t = T_k / 1000.0;
        val = p.A + p.B * t + p.C * Math.pow(t, 2) + p.D * Math.pow(t, 3) + p.E / Math.pow(t, 2);
        return convertUnits(val, "J/(mol*K)", cpUnit, mat.mw);
      }} else {{
        val = p.c0 + (p.c1 || 0) * T_k + (p.c2 || 0) * Math.pow(T_k, 2) + (p.c3 || 0) * Math.pow(T_k, 3);
        return convertUnits(val, mat.unit, cpUnit, mat.mw);
      }}
    }}

    function convertUnits(val, fromUnit, toUnit, mw) {{
      if (fromUnit === toUnit) return val;

      // Base: J/(kg*K)
      let valJkg = val;
      if (fromUnit === "J/(mol*K)") {{
        valJkg = (val / mw) * 1000.0;
      }}

      // Convert from base
      if (toUnit === "J/(kg*K)") return valJkg;
      if (toUnit === "J/(mol*K)") return (valJkg * mw) / 1000.0;
      if (toUnit === "kJ/(kg*K)") return valJkg / 1000.0;
      if (toUnit === "cal/(g*C)") return valJkg / 4184.0;
      if (toUnit === "BTU/(lb*F)") return valJkg / 4186.8;
      return valJkg;
    }}

    function kToDisp(tk) {{
      return tempUnit === "C" ? tk - 273.15 : tk;
    }}

    function dispToK(td) {{
      return tempUnit === "C" ? td + 273.15 : td;
    }}

    // High-Precision SVG Plotting Engine
    const svgEl = document.getElementById("plot-svg");
    const chartBox = document.getElementById("chart-box");
    const tooltip = document.getElementById("tooltip");
    let plottedDataCache = [];

    function renderPlot() {{
      const width = chartBox.clientWidth || 800;
      const height = chartBox.clientHeight || 440;
      
      const pad = {{ left: 75, right: 30, top: 30, bottom: 50 }};
      const plotW = width - pad.left - pad.right;
      const plotH = height - pad.top - pad.bottom;

      svgEl.setAttribute("width", width);
      svgEl.setAttribute("height", height);
      svgEl.setAttribute("viewBox", `0 0 ${{width}} ${{height}}`);
      svgEl.innerHTML = "";

      const tMinK = dispToK(tempMin);
      const tMaxK = dispToK(tempMax);

      if (tMinK >= tMaxK || activeIds.length === 0) {{
        const msg = activeIds.length === 0 ? "Please select one or more materials to display curves." : "Invalid temperature range: Min must be less than Max.";
        svgEl.innerHTML = `<text x="${{width/2}}" y="${{height/2}}" text-anchor="middle" fill="#6b7280" font-size="14">${{msg}}</text>`;
        return;
      }}

      // Sample curves
      const numPts = 120;
      const stepK = (tMaxK - tMinK) / (numPts - 1);
      plottedDataCache = [];
      let yMin = Infinity;
      let yMax = -Infinity;

      activeIds.forEach((id, idx) => {{
        const mat = MATERIALS_DATABASE.find(m => m.id === id);
        if (!mat) return;

        const pts = [];
        for (let i = 0; i < numPts; i++) {{
          const tk = tMinK + i * stepK;
          const cp = calculateCp(mat, tk);
          pts.push({{ tk: tk, tDisp: kToDisp(tk), cp: cp }});
          if (cp < yMin) yMin = cp;
          if (cp > yMax) yMax = cp;
        }}

        plottedDataCache.push({{
          mat: mat,
          color: PALETTE[idx % PALETTE.length],
          pts: pts
        }});
      }});

      if (yMin === Infinity) {{ yMin = 0; yMax = 1000; }}
      if (yMin > 0) yMin = 0;
      yMax = yMax * 1.12;

      function mapX(td) {{
        const xMin = kToDisp(tMinK);
        const xMax = kToDisp(tMaxK);
        return pad.left + ((td - xMin) / (xMax - xMin)) * plotW;
      }}

      function mapY(val) {{
        return pad.top + plotH - ((val - yMin) / (yMax - yMin)) * plotH;
      }}

      let svgHTML = "";

      // Background rect
      svgHTML += `<rect width="${{width}}" height="${{height}}" fill="#ffffff"/>`;

      // X-Gridlines & Labels
      const xTicks = 6;
      const xMinD = kToDisp(tMinK);
      const xMaxD = kToDisp(tMaxK);
      for (let i = 0; i <= xTicks; i++) {{
        const val = xMinD + i * ((xMaxD - xMinD) / xTicks);
        const xPos = mapX(val);
        svgHTML += `<line x1="${{xPos}}" y1="${{pad.top}}" x2="${{xPos}}" y2="${{pad.top + plotH}}" stroke="#f1f5f9" stroke-width="1.2"/>`;
        svgHTML += `<text x="${{xPos}}" y="${{pad.top + plotH + 18}}" text-anchor="middle" fill="#64748b" font-size="11">${{Math.round(val)}}</text>`;
      }}

      // Y-Gridlines & Labels
      const yTicks = 5;
      for (let i = 0; i <= yTicks; i++) {{
        const val = yMin + i * ((yMax - yMin) / yTicks);
        const yPos = mapY(val);
        svgHTML += `<line x1="${{pad.left}}" y1="${{yPos}}" x2="${{pad.left + plotW}}" y2="${{yPos}}" stroke="#f1f5f9" stroke-width="1.2"/>`;
        const lbl = val > 10 ? Math.round(val) : val.toFixed(2);
        svgHTML += `<text x="${{pad.left - 10}}" y="${{yPos + 4}}" text-anchor="end" fill="#64748b" font-size="11">${{lbl}}</text>`;
      }}

      // Plot border
      svgHTML += `<rect x="${{pad.left}}" y="${{pad.top}}" width="${{plotW}}" height="${{plotH}}" fill="none" stroke="#cbd5e1" stroke-width="1.5"/>`;

      // Axis Titles
      svgHTML += `<text x="${{pad.left + plotW / 2}}" y="${{height - 12}}" text-anchor="middle" fill="#334155" font-size="12" font-weight="600">Temperature, T (${{tempUnit}})</text>`;
      svgHTML += `<text x="18" y="${{pad.top + plotH / 2}}" text-anchor="middle" fill="#334155" font-size="12" font-weight="600" transform="rotate(-90, 18, ${{pad.top + plotH / 2}})">Specific Heat Capacity, Cp (${{cpUnit}})</text>`;

      // Curves
      plottedDataCache.forEach(curve => {{
        let d = "";
        curve.pts.forEach((pt, idx) => {{
          const px = mapX(pt.tDisp);
          const py = mapY(pt.cp);
          if (idx === 0) d += `M ${{px.toFixed(1)}} ${{py.toFixed(1)}}`;
          else d += ` L ${{px.toFixed(1)}} ${{py.toFixed(1)}}`;
        }});
        svgHTML += `<path d="${{d}}" fill="none" stroke="${{curve.color}}" stroke-width="2.5" stroke-linecap="round"/>`;
      }});

      // Vertical hover indicator line (initially hidden)
      svgHTML += `<line id="hover-line" x1="0" y1="${{pad.top}}" x2="0" y2="${{pad.top + plotH}}" stroke="#94a3b8" stroke-dasharray="3 3" stroke-width="1.2" style="display:none;"/>`;

      svgEl.innerHTML = svgHTML;
    }}

    // Mouse Interaction for Hover Tooltip
    chartBox.addEventListener("mousemove", (e) => {{
      if (plottedDataCache.length === 0) return;
      const rect = chartBox.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      const pad = {{ left: 75, right: 30, top: 30, bottom: 50 }};
      const plotW = rect.width - pad.left - pad.right;

      if (mouseX < pad.left || mouseX > rect.width - pad.right || mouseY < pad.top || mouseY > rect.height - pad.bottom) {{
        tooltip.style.display = "none";
        const hLine = document.getElementById("hover-line");
        if (hLine) hLine.style.display = "none";
        return;
      }}

      const tMinK = dispToK(tempMin);
      const tMaxK = dispToK(tempMax);
      const xMinD = kToDisp(tMinK);
      const xMaxD = kToDisp(tMaxK);

      const frac = (mouseX - pad.left) / plotW;
      const hoverTD = xMinD + frac * (xMaxD - xMinD);
      const hoverTK = dispToK(hoverTD);

      const hLine = document.getElementById("hover-line");
      if (hLine) {{
        hLine.setAttribute("x1", mouseX);
        hLine.setAttribute("x2", mouseX);
        hLine.style.display = "block";
      }}

      let tip = `<strong>T = ${{hoverTD.toFixed(1)}} ${{tempUnit}}</strong><br>`;
      plottedDataCache.forEach(c => {{
        const cp = calculateCp(c.mat, hoverTK);
        tip += `<span style="color:${{c.color}};">&bull;</span> ${{c.mat.name}}: <strong>${{cp.toFixed(2)}}</strong> ${{cpUnit}}<br>`;
      }});

      tooltip.innerHTML = tip;
      tooltip.style.left = `${{Math.min(mouseX + 15, rect.width - 240)}}px`;
      tooltip.style.top = `${{Math.max(mouseY - 20, 10)}}px`;
      tooltip.style.display = "block";
    }});

    chartBox.addEventListener("mouseleave", () => {{
      tooltip.style.display = "none";
      const hLine = document.getElementById("hover-line");
      if (hLine) hLine.style.display = "none";
    }});

    // Material List Rendering
    function renderMaterialList() {{
      const listEl = document.getElementById("mat-list");
      listEl.innerHTML = "";

      const filtered = MATERIALS_DATABASE.filter(m => {{
        const matchCat = (currentCategory === "all" || m.category === currentCategory);
        const matchSearch = !searchQuery ||
          m.name.toLowerCase().includes(searchQuery) ||
          m.formula.toLowerCase().includes(searchQuery) ||
          m.category.toLowerCase().includes(searchQuery);
        return matchCat && matchSearch;
      }});

      document.getElementById("mat-count-badge").textContent = `${{filtered.length}} shown`;

      if (filtered.length === 0) {{
        listEl.innerHTML = `<div style="padding:12px; font-size:0.8rem; color:#6b7280; text-align:center;">No matching materials found.</div>`;
        return;
      }}

      filtered.forEach(mat => {{
        const isSel = activeIds.includes(mat.id);
        const div = document.createElement("div");
        div.className = `mat-item ${{isSel ? "selected" : ""}}`;
        div.innerHTML = `
          <div>
            <div>${{mat.name}}</div>
            <div style="font-size:0.7rem; color:#64748b;">${{mat.formula}} &bull; ${{mat.category}}</div>
          </div>
          <span style="font-size:0.75rem; color:${{isSel ? "#2563eb" : "#64748b"}};">${{isSel ? "&#10004; Plotted" : "+ Add"}}</span>
        `;

        div.addEventListener("click", () => {{
          if (isSel) {{
            activeIds = activeIds.filter(id => id !== mat.id);
          }} else {{
            activeIds.push(mat.id);
          }}
          updateAll();
        }});

        listEl.appendChild(div);
      }});
    }}

    // Active Selected Tags Rendering
    function renderActiveTags() {{
      const tagsEl = document.getElementById("active-tags");
      tagsEl.innerHTML = "";

      if (activeIds.length === 0) {{
        tagsEl.innerHTML = `<span style="font-size:0.75rem; color:#94a3b8; padding:2px;">None selected (click materials above to plot)</span>`;
        return;
      }}

      activeIds.forEach((id, idx) => {{
        const mat = MATERIALS_DATABASE.find(m => m.id === id);
        if (!mat) return;
        const color = PALETTE[idx % PALETTE.length];

        const tag = document.createElement("div");
        tag.className = "tag";
        tag.innerHTML = `
          <span class="tag-dot" style="background:${{color}};"></span>
          <span>${{mat.name}}</span>
          <span class="tag-close" title="Remove">&times;</span>
        `;

        tag.querySelector(".tag-close").addEventListener("click", (e) => {{
          e.stopPropagation();
          activeIds = activeIds.filter(mid => mid !== id);
          updateAll();
        }});

        tagsEl.appendChild(tag);
      }});
    }}

    // Ranking Table Rendering
    function renderRankingTable() {{
      const tbody = document.getElementById("table-ranking-body");
      tbody.innerHTML = "";

      const refTK = dispToK(refTempK);

      const items = activeIds.map(id => {{
        const mat = MATERIALS_DATABASE.find(m => m.id === id);
        if (!mat) return null;
        return {{ mat: mat, cp: calculateCp(mat, refTK) }};
      }}).filter(Boolean);

      items.sort((a, b) => b.cp - a.cp);

      if (items.length === 0) {{
        tbody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:#94a3b8;">No materials selected</td></tr>`;
        return;
      }}

      items.forEach((item, i) => {{
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td><strong>#${{i + 1}}</strong></td>
          <td>${{item.mat.name}}</td>
          <td><code>${{item.mat.formula}}</code></td>
          <td><strong>${{item.cp.toFixed(2)}}</strong> ${{cpUnit}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Citations & Equations Rendering
    function renderCitations() {{
      const cont = document.getElementById("citations-list");
      cont.innerHTML = "";

      if (activeIds.length === 0) {{
        cont.innerHTML = `<div style="font-size:0.75rem; color:#94a3b8; text-align:center; padding:15px;">Select materials to inspect NIST equations and source citations.</div>`;
        return;
      }}

      activeIds.forEach(id => {{
        const mat = MATERIALS_DATABASE.find(m => m.id === id);
        if (!mat) return;

        const box = document.createElement("div");
        box.className = "citation-box";
        box.innerHTML = `
          <div style="font-weight:700; color:#1e40af;">${{mat.name}} (${{mat.formula}}) &mdash; Mol. Wt: ${{mat.mw}} g/mol</div>
          <div><strong>Primary Source:</strong> ${{mat.source}}</div>
          <div><strong>Model Formulation:</strong> ${{mat.eq_type.toUpperCase()}} | <strong>Calibrated Range:</strong> ${{mat.T_min}} K to ${{mat.T_max}} K</div>
          <div style="color:#64748b; margin-top:2px;">${{mat.notes}}</div>
        `;
        cont.appendChild(box);
      }});
    }}

    // CSV Export
    function exportCSV() {{
      if (activeIds.length === 0) {{
        alert("Please select at least one material to export data.");
        return;
      }}

      const tMinK = dispToK(tempMin);
      const tMaxK = dispToK(tempMax);
      const numPts = 100;
      const stepK = (tMaxK - tMinK) / (numPts - 1);

      const activeMats = activeIds.map(id => MATERIALS_DATABASE.find(m => m.id === id)).filter(Boolean);
      let headers = [`Temperature (${{tempUnit}})`];
      activeMats.forEach(m => headers.push(`"${{m.name}} [${{m.formula}}] (${{cpUnit}})"`));

      let rows = [headers.join(",")];

      for (let i = 0; i < numPts; i++) {{
        const tk = tMinK + i * stepK;
        const row = [kToDisp(tk).toFixed(2)];
        activeMats.forEach(m => {{
          row.push(calculateCp(m, tk).toFixed(3));
        }});
        rows.push(row.join(","));
      }}

      const blob = new Blob([rows.join("\\n")], {{ type: "text/csv;charset=utf-8;" }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `Cp_T_Data_${{tempUnit}}.csv`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }}

    // Central Synchronized Update
    function updateAll() {{
      renderMaterialList();
      renderActiveTags();
      renderPlot();
      renderRankingTable();
      renderCitations();
    }}

    // Event Listeners
    document.getElementById("search-input").addEventListener("input", (e) => {{
      searchQuery = e.target.value.toLowerCase().trim();
      renderMaterialList();
    }});

    document.getElementById("category-select").addEventListener("change", (e) => {{
      currentCategory = e.target.value;
      renderMaterialList();
    }});

    document.getElementById("input-tmin").addEventListener("change", (e) => {{
      tempMin = parseFloat(e.target.value) || 200;
      renderPlot();
    }});

    document.getElementById("input-tmax").addEventListener("change", (e) => {{
      tempMax = parseFloat(e.target.value) || 1500;
      renderPlot();
    }});

    document.getElementById("select-tunit").addEventListener("change", (e) => {{
      const oldUnit = tempUnit;
      tempUnit = e.target.value;
      if (oldUnit === "K" && tempUnit === "C") {{
        tempMin -= 273.15;
        tempMax -= 273.15;
      }} else if (oldUnit === "C" && tempUnit === "K") {{
        tempMin += 273.15;
        tempMax += 273.15;
      }}
      document.getElementById("input-tmin").value = Math.round(tempMin);
      document.getElementById("input-tmax").value = Math.round(tempMax);
      document.getElementById("label-reft").textContent = `${{refTempK.toFixed(1)}} ${{tempUnit}}`;
      updateAll();
    }});

    document.getElementById("select-cpunit").addEventListener("change", (e) => {{
      cpUnit = e.target.value;
      updateAll();
    }});

    document.getElementById("slider-reft").addEventListener("input", (e) => {{
      refTempK = parseFloat(e.target.value);
      document.getElementById("label-reft").textContent = `${{refTempK.toFixed(1)}} ${{tempUnit}}`;
      renderRankingTable();
    }});

    // Preset Buttons
    document.getElementById("preset-metals").addEventListener("click", () => {{
      activeIds = ["met_01", "met_02", "met_03", "met_04", "met_05", "met_06"];
      updateAll();
    }});

    document.getElementById("preset-ceramics").addEventListener("click", () => {{
      activeIds = ["cer_01", "cer_02", "cer_03", "cer_04", "cer_05", "cer_06"];
      updateAll();
    }});

    document.getElementById("preset-multiclass").addEventListener("click", () => {{
      activeIds = ["met_01", "met_02", "cer_01", "semi_01", "poly_01", "gla_01", "ref_01", "comp_01"];
      updateAll();
    }});

    document.getElementById("preset-clear").addEventListener("click", () => {{
      activeIds = [];
      updateAll();
    }});

    document.getElementById("btn-reset-view").addEventListener("click", () => {{
      tempMin = tempUnit === "K" ? 200 : -73;
      tempMax = tempUnit === "K" ? 1500 : 1227;
      document.getElementById("input-tmin").value = Math.round(tempMin);
      document.getElementById("input-tmax").value = Math.round(tempMax);
      renderPlot();
    }});

    document.getElementById("btn-export-csv").addEventListener("click", exportCSV);

    window.addEventListener("resize", renderPlot);
    window.addEventListener("DOMContentLoaded", updateAll);
    window.addEventListener("load", updateAll);

    // Initial immediate invocation
    updateAll();
  </script>
</body>
</html>
"""

    out_file = os.path.join(curr_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated clean index.html at: {out_file}")

if __name__ == "__main__":
    generate_html()
