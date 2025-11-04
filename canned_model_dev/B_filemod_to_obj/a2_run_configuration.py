# -*- coding: utf-8 -*-
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
    # RRR - reulatory required run
    # TTTT - Trump Tariffs Tank Trade
    # AM_CA - Americas - Canada (N+S Amer - Canada)
    # EU_UK - Europearn - United Kindom and Russia
}


class RunConfiguration():
    def __init__(self, spec: dict = forecast_spec):
        if spec:
            self.model_number = spec["model_number"]
            self.scen_list = spec["scenarios"]

    # We may want this to happen automatically
    def set_job_ids(self, scen_list: list):
        """# A function to generate and set job_ids

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
        """
        import copy
        s_l = copy.deepcopy(scen_list)

        for scen in s_l:
            if not scen["job_id"]:
                gen = ''.join([str(v) for k,v in scen.items() if k !="job_id"])
                scen["job_id"] = gen
            else:
                scen["job_id"] = str(scen["job_id"])

        self.scen_list = s_l
        return s_l

    def __repr__(self):
        m = self.model_number
        n = len(self.scen_list)
        str1 = f"|- Configuration -|\n"
        str2 = f" Model Number : {m} \twith {n} scenarios."
        return (str1 + str2)