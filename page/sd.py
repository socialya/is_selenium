import json

import yaml

with open("../common/config.yml", encoding="utf-8") as f:
    # fun_name = inspect.stack()[1].function
    step_datas = yaml.safe_load(f)
# step_str = json.dumps(step_datas)
# for k,v in  step_str.items()
run=step_datas['run']
print(run)
print(run['broser'])
print(type(run['is_headless']))
# print(type(step_str))