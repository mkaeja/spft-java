# Code snippet for spft-java sequences
import numpy as np
import yaml

def rescale_vec(vec, vec_min, vec_max, new_min, new_max):
    """
    Rescale from range defined by vec_min - vec_max to new_min - new_max
    # = (c - a) * (z - y) / (b - a) + y

    """
    new_vec = (((vec-vec_min)*(new_max-new_min))/(vec_max-vec_min))+new_min
    return new_vec

def flip_vec(vec):
    """
    Flip values of vector about its mean
    """
    mm = np.mean(vec)
    return ((vec-mm)*-1)+mm

def load_yaml(fname):
    with open(fname, 'r') as file:
        data = yaml.safe_load(file)
    return data

def parse_yaml_output(fname):
    """
    Parse output file (yaml formatted) from spft-java
    """
    #TODO: identify if some keys are missing - likley not necessary given construction of yaml output

    #these are the keys for where the output data is stored
    # all timeseries data stored as 'times' and 'values'
    ## blocks = data from what was presented in this session, including metadata, presentation heights, and timestamps
    ## devices = raw device data and timestamps
    ## triggers = time and values of triggers
    output_keys = ['blocks', 'devices', 'triggers']
    yaml_data = load_yaml(fname)
    all_keys = yaml_data.keys()
    data = {}
    for key in all_keys:
        if key not in output_keys:
            data[key] = yaml_data[key]
    ## now we can do something with the input data as necessary
    ## TODO: PROCESSING!
    return data

presentation_frequency = 80 #80Hz

# sequences from the Gryga (2012) and Jaeger (2020) papers
# presentation frequency was set at 80Hz (slightly higher than display frequency, but equivalent to the sampling frequency of the pinch force device
# With 1440 samples there is a total sequence time of 18s
# encoded in custom units of hight, new spft-java takes values between 0 and 1

#Original LRN sequence
oldLRN=[90,90,91,91,92,92,93,94,95,97,99,101,103,105,107,109,111,113,115,117,120,123,126,129,132,135,138,140,142,144,146,148,150,152,154,156,158,160,162,163,164,165,166,167,167,168,168,169,169,170,170,169,169,168,168,167,166,165,164,163,162,161,160,159,158,157,155,153,151,149,147,145,143,141,139,137,135,133,131,129,127,125,123,121,119,117,115,113,111,109,107,105,103,101,100,99,98,97,96,95,94,93,92,92,91,91,90,90,90,91,91,92,92,93,95,97,99,102,105,108,111,114,117,120,123,126,129,132,134,136,137,138,139,139,140,140,139,139,138,137,136,135,134,132,130,128,126,124,122,120,118,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,102,101,101,100,100,100,101,101,102,103,104,105,106,107,108,109,110,111,112,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,159,160,160,160,159,159,158,158,157,157,156,155,154,153,151,149,147,145,143,141,139,137,135,133,131,129,127,124,121,118,115,112,109,106,103,100,97,94,91,88,85,82,79,76,73,70,67,64,61,59,57,55,53,51,49,47,45,43,41,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,24,23,23,22,22,21,21,20,20,20,21,21,22,22,23,23,24,24,25,26,27,28,29,30,31,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,69,72,75,78,81,84,87,90,93,96,99,102,105,108,111,114,117,120,123,126,129,132,135,138,141,144,147,150,152,154,156,158,160,162,163,164,165,166,167,168,168,169,169,170,170,169,169,168,167,166,164,162,159,156,153,150,148,146,144,143,142,141,141,140,140,140,141,141,142,143,144,146,148,151,152,153,154,155,156,157,158,158,159,159,160,160,159,159,158,157,156,154,151,148,145,141,137,133,129,125,121,118,115,112,109,106,103,101,99,97,95,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,78,77,77,77,78,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,107,109,111,113,115,117,120,123,126,129,132,135,138,140,142,144,146,148,150,152,154,156,158,160,162,163,164,165,166,167,167,168,168,169,169,170,170,169,169,168,168,167,166,165,164,163,162,161,160,159,158,157,155,153,151,149,147,145,143,141,139,137,135,133,131,129,127,125,123,121,119,117,115,113,111,109,107,105,103,101,100,99,98,97,96,95,94,93,92,92,91,91,90,90,90,91,91,92,92,93,95,97,99,102,105,108,111,114,117,120,123,126,129,132,134,136,137,138,139,139,140,140,139,139,138,137,136,135,134,132,130,128,126,124,122,120,118,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,102,101,101,100,100,100,101,101,102,103,104,105,106,107,108,109,110,111,112,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,159,160,160,160,159,159,158,158,157,157,156,155,154,153,151,149,147,145,143,141,139,137,135,133,131,129,127,124,121,118,115,112,109,106,103,100,97,94,91,88,85,82,79,76,73,70,67,64,61,59,57,55,53,51,49,47,45,43,41,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,24,23,23,22,22,21,21,20,20,20,21,21,22,22,23,23,24,24,25,26,27,28,29,30,31,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,69,72,75,78,81,84,87,90,93,96,99,102,105,108,111,114,117,120,123,126,129,132,135,138,141,144,147,150,152,154,156,158,160,162,163,164,165,166,167,168,168,169,169,170,170,169,169,168,167,166,164,162,159,156,153,150,148,146,144,143,142,141,141,140,140,140,141,141,142,143,144,146,148,151,152,153,154,155,156,157,158,158,159,159,160,160,159,159,158,157,156,154,151,148,145,141,137,133,129,125,121,118,115,112,109,106,103,101,99,97,95,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,78,77,77,77,78,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,107,109,111,113,115,117,120,123,126,129,132,135,138,140,142,144,146,148,150,152,154,156,158,160,162,163,164,165,166,167,167,168,168,169,169,170,170,169,169,168,168,167,166,165,164,163,162,161,160,159,158,157,155,153,151,149,147,145,143,141,139,137,135,133,131,129,127,125,123,121,119,117,115,113,111,109,107,105,103,101,100,99,98,97,96,95,94,93,92,92,91,91,90,90,90,91,91,92,92,93,95,97,99,102,105,108,111,114,117,120,123,126,129,132,134,136,137,138,139,139,140,140,139,139,138,137,136,135,134,132,130,128,126,124,122,120,118,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,102,101,101,100,100,100,101,101,102,103,104,105,106,107,108,109,110,111,112,113,115,117,119,121,123,125,127,129,131,133,135,137,139,141,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,159,160,160,160,159,159,158,158,157,157,156,155,154,153,151,149,147,145,143,141,139,137,135,133,131,129,127,124,121,118,115,112,109,106,103,100,97,94,91,88,85,82,79,76,73,70,67,64,61,59,57,55,53,51,49,47,45,43,41,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,24,23,23,22,22,21,21,20,20,20,21,21,22,22,23,23,24,24,25,26,27,28,29,30,31,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,69,72,75,78,81,84,87,90,93,96,99,102,105,108,111,114,117,120,123,126,129,132,135,138,141,144,147,150,152,154,156,158,160,162,163,164,165,166,167,168,168,169,169,170,170,169,169,168,167,166,164,162,159,156,153,150,148,146,144,143,142,141,141,140,140,140,141,141,142,143,144,146,148,151,152,153,154,155,156,157,158,158,159,159,160,160,159,159,158,157,156,154,151,148,145,141,137,133,129,125,121,118,115,112,109,106,103,101,99,97,95,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,78,77,77,77,78,78,79,80,81,82,83,84,85,86,87,88,89,90]

#Original simple (SMP) sequence, matched to LRN for frequency with maximum power, average force, total force, and range
# there is a slight offset in values to account for force differences
oldSMP=[113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110,113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110,113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110,113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110,113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110,113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110,113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110,113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110,113,116,118,121,124,127,130,133,136,139,141,144,147,149,152,154,157,159,161,164,166,168,170,171,173,175,177,178,179,181,182,183,184,185,186,186,187,187,187,188,188,188,187,187,187,186,186,185,184,183,182,181,179,178,177,175,173,171,170,168,166,164,161,159,157,154,152,149,147,144,141,139,136,133,130,127,124,121,118,116,113,110,107,104,101,98,95,92,89,87,84,81,79,76,73,71,69,66,64,62,60,58,56,54,52,50,49,47,46,44,43,42,41,40,40,39,39,38,38,38,38,38,38,38,39,39,40,40,41,42,43,44,46,47,49,50,52,54,56,58,60,62,64,66,69,71,73,76,79,81,84,87,89,92,95,98,101,104,107,110]

oldLRN = np.array(oldLRN)
oldSMP = np.array(oldSMP)



# compute the equivalent sequences for spft-java
## fit within .1 and .9 so that there is some undershoot and overshoot on the display to provide feedback to the participant when they exceed the height at either end.
LRN=rescale_vec(oldLRN, np.array([oldLRN,oldSMP]).min(),np.array([oldLRN,oldSMP]).max(),.1,.9)
SMP=rescale_vec(oldSMP, np.array([oldLRN,oldSMP]).min(),np.array([oldLRN,oldSMP]).max(),.1,.9)
LRN_flip=flip_vec(LRN)
SMP_flip=flip_vec(SMP)
