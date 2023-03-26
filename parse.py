import json

with open('waf.json') as f:
    data_str = f.read()

data = json.loads(data_str)

json_names = [name for name in data['BYPASSED'].keys() if name.endswith('.json')]

with open('json_names.txt', 'w') as f:
    for name in json_names:
        f.write(name + '\n')
