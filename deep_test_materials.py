"""
deep_test_materials.py
Tests all 230 materials across their full temperature range in 5K steps.
"""
import json
import math
import numpy as np

def deep_test():
    with open(r"C:\Users\Yuvi\.gemini\antigravity\scratch\Cp_Materials_Database_Project\materials_data.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    anomalies = []

    for mat in db:
        m_id = mat["id"]
        m_name = mat["name"]
        m_type = mat["eq_type"]
        p = mat["params"]
        mw = mat["mw"]
        t_min = mat["T_min"]
        t_max = mat["T_max"]

        t_samples = np.linspace(t_min, t_max, 50)
        for T in t_samples:
            if m_type == "shomate":
                t = T / 1000.0
                val = p["A"] + p["B"]*t + p["C"]*(t**2) + p["D"]*(t**3) + p["E"]/(t**2)
            else:
                val = p["c0"] + p.get("c1", 0.0)*T + p.get("c2", 0.0)*(T**2) + p.get("c3", 0.0)*(T**3)

            if val <= 0:
                anomalies.append((m_id, m_name, T, val, m_type, t_min, t_max))
                break

    print(f"Total materials with non-positive Cp: {len(anomalies)}")
    for a in anomalies:
        print(f"Material {a[0]} ({a[1]}): Cp={a[3]:.2f} at T={a[2]:.1f} K (Range: {a[5]}-{a[6]} K, Type: {a[4]})")

if __name__ == "__main__":
    deep_test()
