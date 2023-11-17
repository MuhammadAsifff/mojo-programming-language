from typing import Dict, Union, Optional
import pprint


Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

# List                    0                1            2
data : Dict[Key,Value] = {
                        "fname":"Muhammad A D",
                        "name":"Muhammad Asif",
                        "education": "MSDS"
                        }

pprint.pprint(data)