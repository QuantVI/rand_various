# -*- coding: utf-8 -*-
### --- This is the Orchestration file

import a1_set_parameters as params
import a2_run_configuration as config

# NOTE : Everything that was in the "file" in the old version of
#   run_model, should now be in a run_model object. That way, many of the
#   parameters/inputs, outputs do not have to be passsed in more than once.
#   the remain as state in the object. The orchestrator doesn't need to know
#   what they are. Instead it just passes initial inputs, 
#   then tells the model to Start, Run, Stop, Measure, and Park.
# When all of these is done, the run_model object wull (still) contain
#   (more) outputs from previous.all steps. These can be exported as needed.
class Orchestrator:
    def __init__(self):
        # the Orchestrator should know about the data sources
        # the Model should just use the data
        # the Orchestrator should know about the database(s)
        # the Model should just use the data
        # the Orchestrator asks for data from the database(s)
        # the Model is just given data
        # Everything is supplied to the model.
        # It doesn't go get things. It's only GIVEN them.
        self.PRMS = params.ModelVariables()
        self.CONF = config.RunConfigutation(config.forecast_spec)
        
        var_num = PRMS.m_info["num"]
        conf_num = CONF.model_number
        
        if var_num != conf_num:
            str1 = f"Warning: Model Variables are for : {var_num}\n"
            str2 = f"\nRunConfiguration is for : {conf_num}\n"
            print(str1+str2)
        
        str3 = f"... Read and Processed {PRMS}\n"
        str4 = f"... Read and Processed {CONF}\n"
        
        return str3+str4

    
    
    def model_start():
        pass
        
    
    def model_run():
        pass
        
    
    def model_stop():
        pass
        
    
    def model_measure():
        pass
    
    
    def model_park():
        pass
    
    def __repr__(self):
        s1 = " ~ Model Orchestration object ~\n"
        s2 = "\tA process to run model number:"
        
        s3 = s1+s2
        return s3
    


if __name__ == "__main__":
    model_process = Orchestrator()
    