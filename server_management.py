import os
import json

data ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    }
}

with open('data.json', 'w') as config:
    json.dump(data, config)