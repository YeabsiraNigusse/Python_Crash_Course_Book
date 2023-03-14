import json
from pathlib import Path

numbers = [1,2,3,4]
filename = r'C:\Users\User\Desktop\python\class\number.json'
data = json.dumps(numbers)
print(data)