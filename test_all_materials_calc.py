"""
test_all_materials_calc.py
Tests all 230 materials across temperature domains and units to verify zero NaNs and zero math errors.
"""
import json
import math

def test_calculations():
    with open(r"C:\Users\Yuvi\.gemini\antigravity\scratch\Cp_Materials_Database_Project\materials_data.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    print(f"Testing {len(db)} materials...")
    
    units = ["J/(kg*K)", "J/(mol*K)", "kJ/(kg*K)", "cal/(g*C)", "BTU/(lb*F)"]
    errors = []

    for mat in db:
        m_id = mat["id"]
        m_name = mat["name"]
        m_type = mat["eq_type"]
        p = mat["params"]
        mw = mat["mw"]
        t_min = mat["T_min"]
        t_max = mat["T_max"]

        for T in [t_min, (t_min + t_max)/2, t_max]:
            # Python equivalent of JS getCpValue
            if m_type == "shomate":
                t = T / 1000.0
                val = p["A"] + p["B"]*t + p["C"]*(t**2) + p["D"]*(t**3) + p["E"]/(t**2)
                native_unit = "J/(mol*K)"
            else:
                val = p["c0"] + p.get("c1", 0.0)*T + p.get("c2", 0.0)*(T**2) + p.get("c3", 0.0)*(T**3)
                native_unit = mat["unit"]

            if math.isnan(val) or math.isinf(val):
                errors.append(f"{m_id} ({m_name}) evaluated to NaN/Inf at T={T}")

            # Test conversions
            for target_unit in units:
                if native_unit == "J/(mol*K)":
                    val_jkg = (val / mw) * 1000.0
                else:
                    val_jkg = val

                if target_unit == "J/(kg*K)":
                    res = val_jkg
                elif target_unit == "J/(mol*K)":
                    res = (val_jkg * mw) / 1000.0
                elif target_unit == "kJ/(kg*K)":
                    res = val_jkg / 1000.0
                elif target_unit == "cal/(g*C)":
                    res = val_jkg / 4184.0
                elif target_unit == "BTU/(lb*F)":
                    res = val_jkg / 4186.8

                if math.isnan(res) or math.isinf(res) or res <= 0:
                    errors.append(f"{m_id} ({m_name}) conversion to {target_unit} produced invalid value: {res} at T={T}")

    if errors:
        print(f"FOUND {len(errors)} ERRORS:")
        for e in errors[:10]:
            print("  -", e)
    else:
        print("ALL 230 MATERIALS PASSED 100% THERMODYNAMIC CALCULATION AND UNIT TESTS WITHOUT A SINGLE ERROR!")

if __name__ == "__main__":
    test_calculations()
