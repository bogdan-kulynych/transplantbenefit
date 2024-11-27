import numpy as np
import pandas as pd


def group2dummy(group: int, length: int) -> list:
    if group > length:
        raise ValueError("Group must be an integer less than or equal to length")
    out = [0] * (length - 1)
    out[group - 1] = 1
    return out


def make_rdisease_vec(
    rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs, previous_tx_tbs
):
    if previous_tx_tbs > 0:
        result = 10
    elif any(
        x == "1"
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 1
    elif any(
        x == "2"
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 2
    elif any(
        x == "3"
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 3
    elif any(
        x == "4"
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 4
    elif any(
        x == "5"
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 5
    elif any(
        x == "6"
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 6
    elif any(
        x == "7"
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 7
    elif any(
        x == "8"
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 8
    else:
        result = 9

    out = group2dummy(result, 10)
    return out[:-1]  # Remove second element


def is_rhcv(rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs):
    return (
        1
        if any(
            x == "2"
            for x in [
                rdisease_primary_tbs,
                rdisease_secondary_tbs,
                rdisease_tertiary_tbs,
            ]
        )
        else 0
    )


def is_cancer(rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs):
    return (
        1
        if any(
            x == "1"
            for x in [
                rdisease_primary_tbs,
                rdisease_secondary_tbs,
                rdisease_tertiary_tbs,
            ]
        )
        else 0
    )


def make_rcreatinine(centre_tbs, rcreatinine_tbs):
    return (rcreatinine_tbs + 23.4) / 1.2 if centre_tbs == "3" else rcreatinine_tbs


def make_x1(
    rage_tbs,
    rgender_tbs,
    rhcv,
    rdisease_vec,
    rcreatinine,
    rbilirubin_tbs,
    rinr_tbs,
    rsodium_tbs,
    rpotassium_tbs,
    ralbumin_tbs,
    rrenal_tbs,
    rinpatient_tbs,
    rregistration_vec,
    rprevious_surgery_tbs,
    rencephalopathy_tbs,
    rascites_tbs,
    rwaiting_time_tbs,
    rdiabetes_tbs,
    rmax_afp_tbs,
    rmax_tumour_size_tbs,
    rtumour_number_vec,
    dage_tbs,
    dcause_vec,
    dbmi_tbs,
    ddiabetes_vec,
    dtype_tbs,
    bloodgroup_compatible_tbs,
    splittable_tbs,
):

    return pd.DataFrame(
        {
            "raw_x1": [
                rage_tbs,
                rage_tbs,
                rgender_tbs,
                rhcv,
                *rdisease_vec,
                rcreatinine,
                rbilirubin_tbs,
                rinr_tbs,
                rsodium_tbs,
                rpotassium_tbs,
                ralbumin_tbs,
                rrenal_tbs,
                rinpatient_tbs,
                *rregistration_vec,
                rbilirubin_tbs,
                *rdisease_vec,
                rage_tbs,
                rprevious_surgery_tbs,
                rencephalopathy_tbs,
                rascites_tbs,
                float(rwaiting_time_tbs) + 1,
                rdiabetes_tbs,
                *rdisease_vec,
                float(rmax_afp_tbs) + 1,
                rmax_tumour_size_tbs,
                *rtumour_number_vec,
                dage_tbs,
                *dcause_vec,
                dbmi_tbs,
                *ddiabetes_vec,
                dtype_tbs,
                rhcv,
                rhcv,
                rhcv,
                dtype_tbs,
                dtype_tbs,
                *rdisease_vec,
                bloodgroup_compatible_tbs,
                splittable_tbs,
            ]
        }
    )


def make_x2(
    rsodium_tbs,
    rbilirubin_tbs,
    rcreatinine,
    rage_tbs,
    ddiabetes_vec,
    dage_tbs,
    dtype_tbs,
):

    ones = [1] * 26
    sodium_bili = [rsodium_tbs] + [rbilirubin_tbs] * 8
    creat_ones = [rcreatinine] + [1] * 9
    rage = [rage_tbs] * 8
    more_ones = [1] * 13
    final_vars = (
        [*ddiabetes_vec, dage_tbs, rage_tbs, rcreatinine] + [dtype_tbs] * 8 + [1, 1]
    )

    return pd.DataFrame(
        {"raw_x2": [*ones, *sodium_bili, *creat_ones, *rage, *more_ones, *final_vars]}
    )


def encode(betas, x1, x2):
    df = pd.concat([betas, x1, x2], axis=1)
    df["transformed_x1"] = df["raw_x1"] ** df["power"]
    df.loc[df["ln_1"] == 1, "transformed_x1"] = np.log(
        df.loc[df["ln_1"] == 1, "transformed_x1"]
    )

    df["transformed_x2"] = df["raw_x2"] ** df["power"]
    df.loc[df["ln_2"] == 1, "transformed_x2"] = np.log(
        df.loc[df["ln_2"] == 1, "transformed_x2"]
    )

    return df
