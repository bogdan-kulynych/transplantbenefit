import pandas as pd


def make_default_case():
    return pd.Series(
        {
            "rinpatient_tbs": 0,
            "rregistration_tbs": 1,
            "rwaiting_time_tbs": 30,
            "rage_tbs": 52,
            "rgender_tbs": 0,
            "rdisease_primary_tbs": "3",
            "rdisease_secondary_tbs": "9",
            "rdisease_tertiary_tbs": "9",
            "previous_tx_tbs": 0,
            "rprevious_surgery_tbs": 0,
            "rbilirubin_tbs": 20,
            "rinr_tbs": 1.0,
            "rcreatinine_tbs": 70,
            "rrenal_tbs": 0,
            "rsodium_tbs": 135,
            "rpotassium_tbs": 4.5,
            "ralbumin_tbs": 30,
            "rencephalopathy_tbs": 0,
            "rascites_tbs": 0,
            "rdiabetes_tbs": 0,
            "rmax_afp_tbs": 5,
            "rtumour_number_tbs": 1,
            "rmax_tumour_size_tbs": 1,
            "dage_tbs": 52,
            "dcause_tbs": 1,
            "dbmi_tbs": 25,
            "ddiabetes_tbs": 1,
            "dtype_tbs": 0,
            "bloodgroup_compatible_tbs": 0,
            "splittable_tbs": 0,
        }
    )


def make_moderate_risk_case():
    df = make_default_case()
    mods = {
        "rwaiting_time_tbs": 68,
        "rgender_tbs": 1,
        "rdisease_primary_tbs": "8",
        "rbilirubin_tbs": 74,
        "rinr_tbs": 1.2,
        "rcreatinine_tbs": 63,
        "rsodium_tbs": 138,
        "rpotassium_tbs": 4.1,
        "ralbumin_tbs": 31,
    }
    for k, v in mods.items():
        df[k] = v
    return df


def make_high_risk_case():
    df = make_default_case()
    mods = {
        "rage_tbs": 65,
        "rbilirubin_tbs": 100,
        "rinr_tbs": 1.5,
        "rcreatinine_tbs": 90,
        "rsodium_tbs": 130,
        "ralbumin_tbs": 25,
        "rascites_tbs": 1,
    }
    for k, v in mods.items():
        df[k] = v
    return df


def make_very_high_risk_case():
    df = make_default_case()
    mods = {
        "rinpatient_tbs": 1,
        "rage_tbs": 65,
        "rprevious_surgery_tbs": 1,
        "rbilirubin_tbs": 120,
        "rinr_tbs": 1.7,
        "rcreatinine_tbs": 110,
        "rsodium_tbs": 125,
        "ralbumin_tbs": 25,
        "rencephalopathy_tbs": 1,
        "rascites_tbs": 1,
    }
    for k, v in mods.items():
        df[k] = v
    return df
