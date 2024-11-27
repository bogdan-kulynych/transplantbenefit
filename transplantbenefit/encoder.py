import numpy as np
import pandas as pd

from transplantbenefit.params import param_store


def group2dummy(group: int, length: int) -> list:
    """
    Dummy encoder.

    params:
        group: group indicator (starts at 1!)
        length: number of groups
    """
    group = int(group)
    if group > length:
        raise ValueError("Group must be an integer less than or equal to length")
    out = [0] * (length - 1)
    if group > 1:
        out[group - 2] = 1
    return out


def make_rdisease_vec(
    rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs, previous_tx_tbs
):
    rdisease_primary_tbs = int(rdisease_primary_tbs)
    rdisease_secondary_tbs = int(rdisease_secondary_tbs)
    rdisease_tertiary_tbs = int(rdisease_tertiary_tbs)
    if previous_tx_tbs > 0:
        result = 10
    elif any(
        x == 1
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 1
    elif any(
        x == 2
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 2
    elif any(
        x == 3
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 3
    elif any(
        x == 4
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 4
    elif any(
        x == 5
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 5
    elif any(
        x == 6
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 6
    elif any(
        x == 7
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 7
    elif any(
        x == 8
        for x in [rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs]
    ):
        result = 8
    else:
        result = 9

    out = group2dummy(result, 10)
    return out[:1] + out[2:]  # Remove disease group 3


def is_rhcv(rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs):
    return any(
        x == "2"
        for x in [
            rdisease_primary_tbs,
            rdisease_secondary_tbs,
            rdisease_tertiary_tbs,
        ]
    )


def is_cancer(rdisease_primary_tbs, rdisease_secondary_tbs, rdisease_tertiary_tbs):
    return any(
        x == "1"
        for x in [
            rdisease_primary_tbs,
            rdisease_secondary_tbs,
            rdisease_tertiary_tbs,
        ]
    )


def make_rcreatinine(centre_tbs, rcreatinine_tbs):
    return (rcreatinine_tbs + 23.4) / 1.2 if centre_tbs == "3" else rcreatinine_tbs


def get_feature_transforms(
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
    return pd.Series(
        {
            "RAGE - MEAN(RAGE)": rage_tbs,
            "RAGE SQUARED - MEAN(RAGE SQUARED)": rage_tbs**2,
            "RGENDER": rgender_tbs,
            "RHCV": rhcv,
            "RDISEASE GROUP=2": rdisease_vec[0],
            "RDISEASE GROUP=4": rdisease_vec[1],
            "RDISEASE GROUP=5": rdisease_vec[2],
            "RDISEASE GROUP=6": rdisease_vec[3],
            "RDISEASE GROUP=7": rdisease_vec[4],
            "RDISEASE GROUP=8": rdisease_vec[5],
            "RDISEASE GROUP=9": rdisease_vec[6],
            "RDISEASE GROUP=10": rdisease_vec[7],
            "LN(RCREATININE) - MEAN(LN(RCREATININE))": np.log(rcreatinine),
            "LN(RBILIRUBIN) - MEAN(LN(RBILIRUBIN))": np.log(rbilirubin_tbs),
            "LN(RINR) - MEAN(LN(RINR))": np.log(rinr_tbs),
            "RSODIUM - MEAN(RSODIUM)": rsodium_tbs,
            "RPOTASSIUM - MEAN(RPOTASSIUM)": rpotassium_tbs,
            "RALBUMIN - MEAN(RALBUMIN)": ralbumin_tbs,
            "RRENAL": rrenal_tbs,
            "RINPATIENT": rinpatient_tbs,
            "RREGISTRATION YEAR=2007": rregistration_vec[0],
            "RREGISTRATION YEAR=2008": rregistration_vec[1],
            "RREGISTRATION YEAR=2009": rregistration_vec[2],
            "RREGISTRATION YEAR=2010": rregistration_vec[3],
            "RREGISTRATION YEAR=2011": rregistration_vec[4],
            "RREGISTRATION YEAR=2012": rregistration_vec[5],
            "LN(RBILIRUBIN)*RSODIUM - MEAN(LN(RBILIRUBIN)*RSODIUM)": np.log(
                rbilirubin_tbs
            )
            * rsodium_tbs,
            "RDISEASE GROUP=2*LN(RBILIRUBIN)": rdisease_vec[0] * np.log(rbilirubin_tbs),
            "RDISEASE GROUP=4*LN(RBILIRUBIN)": rdisease_vec[1] * np.log(rbilirubin_tbs),
            "RDISEASE GROUP=5*LN(RBILIRUBIN)": rdisease_vec[2] * np.log(rbilirubin_tbs),
            "RDISEASE GROUP=6*LN(RBILIRUBIN)": rdisease_vec[3] * np.log(rbilirubin_tbs),
            "RDISEASE GROUP=7*LN(RBILIRUBIN)": rdisease_vec[4] * np.log(rbilirubin_tbs),
            "RDISEASE GROUP=8*LN(RBILIRUBIN)": rdisease_vec[5] * np.log(rbilirubin_tbs),
            "RDISEASE GROUP=9*LN(RBILIRUBIN)": rdisease_vec[6] * np.log(rbilirubin_tbs),
            "RDISEASE GROUP=10*LN(RBILIRUBIN)": rdisease_vec[7]
            * np.log(rbilirubin_tbs),
            "RAGE*LN(RCREATININE) - MEAN(RAGE*LN(RCREATININE))": rage_tbs
            * np.log(rcreatinine),
            "RPREVIOUS ABDOMINAL SURGERY": rprevious_surgery_tbs,
            "RENCEPHALOPATHY": rencephalopathy_tbs,
            "RASCITES": rascites_tbs,
            "LN(RWAITING TIME+1) - MEAN(LN(RWAITING TIME+1))": np.log(
                rwaiting_time_tbs + 1
            ),
            "RDIABETES": rdiabetes_tbs,
            "RDISEASE GROUP=2*RAGE": rdisease_vec[0] * rage_tbs,
            "RDISEASE GROUP=4*RAGE": rdisease_vec[1] * rage_tbs,
            "RDISEASE GROUP=5*RAGE": rdisease_vec[2] * rage_tbs,
            "RDISEASE GROUP=6*RAGE": rdisease_vec[3] * rage_tbs,
            "RDISEASE GROUP=7*RAGE": rdisease_vec[4] * rage_tbs,
            "RDISEASE GROUP=8*RAGE": rdisease_vec[5] * rage_tbs,
            "RDISEASE GROUP=9*RAGE": rdisease_vec[6] * rage_tbs,
            "RDISEASE GROUP=10*RAGE": rdisease_vec[7] * rage_tbs,
            "LN(RMAXIMUM AFP LEVEL+1) - MEAN(LN(RMAXIMUM AFP LEVEL+1))": np.log(
                rmax_afp_tbs + 1
            ),
            "RMAXIMUM TUMOUR SIZE - MEAN(RMAXIMUM TUMOUR SIZE)": rmax_tumour_size_tbs,
            "RTWO TUMOUR": rtumour_number_vec[0],
            "RTHREE OR MORE TUMOURS": rtumour_number_vec[1],
            "DAGE - MEAN(DAGE)": dage_tbs,
            "DCAUSE OF DEATH=2": dcause_vec[0],
            "DCAUSE OF DEATH=3": dcause_vec[1],
            "DCAUSE OF DEATH=4": dcause_vec[2],
            "DBMI - MEAN(DBMI)": dbmi_tbs,
            "DHISTORY OF DIABETES=2": ddiabetes_vec[0],
            "DHISTORY OF DIABETES=9": ddiabetes_vec[1],
            "DTYPE=2": dtype_tbs,
            "RHCV*DHISTORY OF DIABETES=2": rhcv * ddiabetes_vec[0],
            "RHCV*DHISTORY OF DIABETES=9": rhcv * ddiabetes_vec[1],
            "RHCV*DAGE": rhcv * dage_tbs,
            "DTYPE=2*RAGE": dtype_tbs * rage_tbs,
            "DTYPE=2*LN(RCREATININE)": dtype_tbs * np.log(rcreatinine),
            "RDISEASE GROUP=2*DTYPE=2": rdisease_vec[0] * dtype_tbs,
            "RDISEASE GROUP=4*DTYPE=2": rdisease_vec[1] * dtype_tbs,
            "RDISEASE GROUP=5*DTYPE=2": rdisease_vec[2] * dtype_tbs,
            "RDISEASE GROUP=6*DTYPE=2": rdisease_vec[3] * dtype_tbs,
            "RDISEASE GROUP=7*DTYPE=2": rdisease_vec[4] * dtype_tbs,
            "RDISEASE GROUP=8*DTYPE=2": rdisease_vec[5] * dtype_tbs,
            "RDISEASE GROUP=9*DTYPE=2": rdisease_vec[6] * dtype_tbs,
            "RDISEASE GROUP=10*DTYPE=2": rdisease_vec[7] * dtype_tbs,
            "BLOOD GROUP COMPATIBILITY": bloodgroup_compatible_tbs,
            "LIVER MEETS SPLIT CRITERIA": splittable_tbs,
        }
    )


def encode(data, centre_tbs=6):
    if isinstance(data, pd.Series):
        data = data.to_frame().T

    results = []
    for _, row in data.iterrows():
        row = row.to_dict()

        rdisease_vec = make_rdisease_vec(
            row["rdisease_primary_tbs"],
            row["rdisease_secondary_tbs"],
            row["rdisease_tertiary_tbs"],
            row["previous_tx_tbs"],
        )

        rhcv = is_rhcv(
            row["rdisease_primary_tbs"],
            row["rdisease_secondary_tbs"],
            row["rdisease_tertiary_tbs"],
        )
        cancer = is_cancer(
            row["rdisease_primary_tbs"],
            row["rdisease_secondary_tbs"],
            row["rdisease_tertiary_tbs"],
        )

        rregistration_vec = group2dummy(row["rregistration_tbs"], 7)
        rtumour_number_vec = group2dummy(row["rtumour_number_tbs"], 3)
        dcause_vec = group2dummy(row["dcause_tbs"], 4)
        ddiabetes_vec = group2dummy(row["ddiabetes_tbs"], 3)

        rcreatinine = make_rcreatinine(centre_tbs, row["rcreatinine_tbs"])

        vec = get_feature_transforms(
            row["rage_tbs"],
            row["rgender_tbs"],
            rhcv,
            rdisease_vec,
            rcreatinine,
            row["rbilirubin_tbs"],
            row["rinr_tbs"],
            row["rsodium_tbs"],
            row["rpotassium_tbs"],
            row["ralbumin_tbs"],
            row["rrenal_tbs"],
            row["rinpatient_tbs"],
            rregistration_vec,
            row["rprevious_surgery_tbs"],
            row["rencephalopathy_tbs"],
            row["rascites_tbs"],
            row["rwaiting_time_tbs"],
            row["rdiabetes_tbs"],
            row["rmax_afp_tbs"],
            row["rmax_tumour_size_tbs"],
            rtumour_number_vec,
            row["dage_tbs"],
            dcause_vec,
            row["dbmi_tbs"],
            ddiabetes_vec,
            row["dtype_tbs"],
            row["bloodgroup_compatible_tbs"],
            row["splittable_tbs"],
        )
        assert vec.shape == (76,)
        assert ~vec.isna().any()

        results.append(pd.concat([pd.Series({"RCANCER": cancer}), vec]))

    if len(results) == 1:
        return pd.DataFrame(results)

    return pd.concat(results, axis=0)
