# Audit Log

| File Name | Problem Manifestation | Root Cause of Failure | Structural Correction | Git Commit Hash |
| --- | --- | --- | --- | --- |
| train.py | When running train.py the Program crashes with a FileNotFoundError | The configuration json file is missing, it is used to describe the model and parameters we want to use for training | We added a config.json in the root directory and reverse engineered the Fields needed for it from train.py | d6f775c7a897343e08f680f15ebb830ae9128a17 | 
| data.py | Loading the data failed with a FileNotFoundError in the get_loaders() function | The function assumes a suffix in the data filename "..._data.py" but our data does have different naming | We removed the suffix and make sure we specify the correct filename in the config.json | 5bb2d5f5a6b8c9d9bb54cd6070e84622ad4d5225 |