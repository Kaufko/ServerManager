import os
import json
from flask import Flask

with open('data.json', 'w') as config:
    json.dump(data, config)