import pandas as pd
import json

excel_file = "Navya_datalist.xlsx"
df = pd.read_excel(excel_file, index_col=0, header=0)

l = []
for i in df.iloc:
    l.append(i.to_dict())
with open("output.json", "w") as f:
    f.write(json.dumps(l))
