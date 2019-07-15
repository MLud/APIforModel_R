# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
response = requests.post(
        "http://127.0.0.1:8000/predict"
        , headers={"Content-Type": "application/json"}
        , data=json.dumps({"Status.of.existing.checking.account": "A11", "Duration.in.month": 24, "Credit.history": "A32", "Savings.account.bonds": "A63"})
)


print (response.json())