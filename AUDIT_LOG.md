# Audit Log

| File Name | Problem Manifestation | Root Cause of Failure | Structural Correction | Git Commit Hash |
| --- | --- | --- | --- | --- |
| train.py | When running train.py the Program crashes with a FileNotFoundError | The configuration json file is missing, it is used to describe the model and parameters we want to use for training | We added a config.json in the root directory and reverse engineered the Fields needed for it from train.py | d6f775c7a897343e08f680f15ebb830ae9128a17 | 