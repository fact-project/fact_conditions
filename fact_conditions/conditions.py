import pkgutil
import yaml

import os.path

def create_condition_set(conditionset=['@standard']):
    """
    given a list of conditions create a condition set
    
    If a given condition start with '@NAME', process NAME as a set of conditions defined in a yaml file
    with the filename NAME or with the 
    """
    data_conditions = []
    for condition in conditionset:
        if condition.startswith('@'):
            # check if file exists
            fname = condition[1:]
            if os.path.isfile(fname):
                with open(fname, 'r') as f:
                    config = yaml.safe_load(f)
                    more_conditions = config['conditions']
            else:
                data = None
                if fname.endswith('.yaml'):
                    data = pkgutil.get_data('fact_conditions', 'conditions/'+fname)
                else:
                    data = pkgutil.get_data('fact_conditions', 'conditions/'+fname+'.yaml')
                if data is None:
                    raise ValueError("The given condition file: '{}' does not exist".format(fname))
                try:
                    config = yaml.safe_load(data)
                except:
                    print("ERROR: Something went wrong in the yaml file from '{}'".format(fname))
                    raise
                more_conditions = config['conditions']
            data_conditions = data_conditions + more_conditions
        else:
            data_conditions.append(condition)
    return data_conditions

"""conditions['darknight'] = [
    'fCurrentsMedMean < 20',
    'fMoonZenithDistance > 100',
] + conditions['standard']


conditions['low_zenith'] = [
    'fZenithDistanceMax < 30',
]"""

