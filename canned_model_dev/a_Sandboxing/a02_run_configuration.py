# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 16:19:51 2025
"""

#### ---- Run Configuration

# Every run of the model requires these settings.
# The Run ID should be created dynamically based on the settings.

    # Run ID
    # Model Number  
    # Exercise
    # Scenario
    # Entity
    # Time-Zero Date
    # Output 
    # Currency

forecast_spec = {
    "model_number": 65535,
    "scenarios": [
        {"job_id": 1234,
         "exercise": "RRR",
         "scenario_code": "TTTT_v101",
         "entity": "ASEAN",
         "time_zero": "2025-01",
         "currency": "SGD"},

        {"job_id": 2468,
         "exercise": "RRR",
         "scenario_code": "TTTT_v101",
         "entity": "BENELUX",
         "time_zero": "2025-01",
         "currency": "EUR"},

        {"job_id": 36912,
         "exercise": "RRR",
         "scenario_code": "TTTT_v101",
         "entity": "AM_CA",
         "time_zero": "2025-04",
         "currency": "USD"},

        {"job_id": 481216,
         "exercise": "EU_UKR",
         "scenario_code": "TTTT_v101",
         "entity": "ASEAN",
         "time_zero": "2025-04",
         "currency": "GBP"}

    ]
}


# RRR - reulatory required run
# TTTT - Trump Tariffs Tank Trade
# AM_CA - Americas - Canada (N+S Amer - Canada)
# EU_UK - Europearn - United Kindom and Russia


# A function to generate and set job_ids
def set_job_ids(scen_list: list):
    # scen_list: a list of scenarios
    # scenario : a dictionary of settings for one scenario
    # job_id : A field in each scenario.
        # may be pre-populated, empty, or non-exist
        # if it doesn't exist, this function will create it
        # if it does exist, this function will overwrite its value
    # Returns:
        # A NEW scenario list where all scenarios have the key "job_id"
        # with the previous non-False value as str, or a value generated
        # by concatenation of the other keys' values.

    import copy
    s_l = copy.deepcopy(scen_list)

    for scen in s_l:
        if not scen["job_id"]:
            gen = ''.join([str(v) for k,v in scen.items() if k !="job_id"])
            scen["job_id"] = gen
        else:
            scen["job_id"] = str(scen["job_id"])

    return s_l


if __name__ == "__main__":
    # quick test
    import copy
    s = forecast_spec["scenarios"]
    t = copy.deepcopy(s)
    t[0]["job_id"] = 0

    print("TEST : Set job ids when they are already full of non-false\n")
    print(f"ORIGINAL\n\t{s}\n")
    print(f"ORIG After set_job_ids\n\t{set_job_ids(s)}\n")
    print("Set job ids when one is non-false (e.g. 0 or '' or missing\n")
    print(f"MODIFIED\n\t{t}\n")
    print(f"MOD After set_job_ids\n\t{set_job_ids(t)}\n")
