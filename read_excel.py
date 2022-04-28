import pandas as pd
import os
filter = pd.DataFrame({"Company_Name": ["Advisor Världen"]})

result = pd.DataFrame(columns=["Period_tom","Company_Name","Instrumenttyp_kod","Instrument_Andel_fondformogenhet"])
for file in os.listdir():
    if(file.endswith("xlsx")):
        df = pd.read_excel(file)
        df=df.merge(filter, how="inner", on="Company_Name")
        result=result.append((df[["Period_tom","Company_Name","Instrumenttyp_kod","Instrument_Andel_fondformogenhet"]]))

print(result)
result.to_excel("result.xlsx")