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


## From R code:
# RAGE - MEAN(RAGE)                                                                           52.000000
# RAGE SQUARED - MEAN(RAGE SQUARED)                                                         2704.000000
# RGENDER                                                                                      0.000000
# RHCV                                                                                         0.000000
# RDISEASE GROUP=2                                                                             0.000000
# RDISEASE GROUP=4                                                                             0.000000
# RDISEASE GROUP=5                                                                             0.000000
# RDISEASE GROUP=6                                                                             0.000000
# RDISEASE GROUP=7                                                                             0.000000
# RDISEASE GROUP=8                                                                             0.000000
# RDISEASE GROUP=9                                                                             0.000000
# RDISEASE GROUP=10                                                                            0.000000
# LN(RCREATININE) - MEAN(LN(RCREATININE))                                                      4.248495
# LN(RBILIRUBIN) - MEAN(LN(RBILIRUBIN))                                                        2.995732
# LN(RINR) - MEAN(LN(RINR))                                                                    0.000000
# RSODIUM - MEAN(RSODIUM)                                                                    135.000000
# RPOTASSIUM - MEAN(RPOTASSIUM)                                                                4.500000
# RALBUMIN - MEAN(RALBUMIN)                                                                   30.000000
# RRENAL                                                                                       0.000000
# RINPATIENT                                                                                   0.000000
# RREGISTRATION YEAR=2007                                                                      0.000000
# RREGISTRATION YEAR=2008                                                                      0.000000
# RREGISTRATION YEAR=2009                                                                      0.000000
# RREGISTRATION YEAR=2010                                                                      0.000000
# RREGISTRATION YEAR=2011                                                                      0.000000
# RREGISTRATION YEAR=2012                                                                      0.000000
# LN(RBILIRUBIN)*RSODIUM - MEAN(LN(RBILIRUBIN)*RSODIUM)                                      404.423857
# RDISEASE GROUP=2*LN(RBILIRUBIN)                                                              0.000000
# RDISEASE GROUP=4*LN(RBILIRUBIN)                                                              0.000000
# RDISEASE GROUP=5*LN(RBILIRUBIN)                                                              0.000000
# RDISEASE GROUP=6*LN(RBILIRUBIN)                                                              0.000000
# RDISEASE GROUP=7*LN(RBILIRUBIN)                                                              0.000000
# RDISEASE GROUP=8*LN(RBILIRUBIN)                                                              0.000000
# RDISEASE GROUP=9*LN(RBILIRUBIN)                                                              0.000000
# RDISEASE GROUP=10*LN(RBILIRUBIN)                                                             0.000000
# RAGE*LN(RCREATININE) - MEAN(RAGE*LN(RCREATININE))                                          220.921753
# RPREVIOUS ABDOMINAL SURGERY                                                                  0.000000
# RENCEPHALOPATHY                                                                              0.000000
# RASCITES                                                                                     0.000000
# LN(RWAITING TIME+1) - MEAN(LN(RWAITING TIME+1))                                              3.433987
# RDIABETES                                                                                    0.000000
# RDISEASE GROUP=2*RAGE                                                                        0.000000
# RDISEASE GROUP=4*RAGE                                                                        0.000000
# RDISEASE GROUP=5*RAGE                                                                        0.000000
# RDISEASE GROUP=6*RAGE                                                                        0.000000
# RDISEASE GROUP=7*RAGE                                                                        0.000000
# RDISEASE GROUP=8*RAGE                                                                        0.000000
# RDISEASE GROUP=9*RAGE                                                                        0.000000
# RDISEASE GROUP=10*RAGE                                                                       0.000000
# LN(RMAXIMUM AFP LEVEL+1) - MEAN(LN(RMAXIMUM AFP LEVEL+1))                                    1.791759
# RMAXIMUM TUMOUR SIZE - MEAN(RMAXIMUM TUMOUR SIZE)                                            1.000000
# RTWO TUMOUR                                                                                  0.000000
# RTHREE OR MORE TUMOURS                                                                       0.000000
# DAGE - MEAN(DAGE)                                                                           52.000000
# DCAUSE OF DEATH=2                                                                            0.000000
# DCAUSE OF DEATH=3                                                                            0.000000
# DCAUSE OF DEATH=4                                                                            0.000000
# DBMI - MEAN(DBMI)                                                                           25.000000
# DHISTORY OF DIABETES=2                                                                       0.000000
# DHISTORY OF DIABETES=9                                                                       0.000000
# DTYPE=2                                                                                      0.000000
# RHCV*DHISTORY OF DIABETES=2                                                                  0.000000
# RHCV*DHISTORY OF DIABETES=9                                                                  0.000000
# RHCV*DAGE                                                                                    0.000000
# DTYPE=2*RAGE                                                                                 0.000000
# DTYPE=2*LN(RCREATININE)                                                                      0.000000
# RDISEASE GROUP=2*DTYPE=2                                                                     0.000000
# RDISEASE GROUP=4*DTYPE=2                                                                     0.000000
# RDISEASE GROUP=5*DTYPE=2                                                                     0.000000
# RDISEASE GROUP=6*DTYPE=2                                                                     0.000000
# RDISEASE GROUP=7*DTYPE=2                                                                     0.000000
# RDISEASE GROUP=8*DTYPE=2                                                                     0.000000
# RDISEASE GROUP=9*DTYPE=2                                                                     0.000000
# RDISEASE GROUP=10*DTYPE=2                                                                    0.000000
# BLOOD GROUP COMPATIBILITY                                                                    0.000000
# LIVER MEETS SPLIT CRITERIA                                                                   0.000000


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
