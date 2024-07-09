import json
import pandas as pd

filename = '/var/log/suricata/eve.json'

# 逐行读取 JSON 对象并解析
data = []
with open(filename, 'r') as file:
	for line in file:
		try:
			data.append(json.loads(line))
		except json.JSONDecodeError:
			continue

# 将解析后的数据转换为 pandas DataFrame
PandaObj = pd.DataFrame(data)

# 将 DataFrame 保存为 CSV 文件
PandaObj.to_csv('/home/whale/suricata-6.0.8/suricata-ML/eve_.csv', index=False)
