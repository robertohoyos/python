# CAPs, para mapeo

import pandas as pd
from IPython.display import display, HTML


fileCAPs =  'insumoProcesado.xlsx'
sheetCAPs = 'caps'

fileMilestones =  'insumoProcesado.xlsx'
sheetMilestones = 'milestones'







# -----------
# obtener insumo de file; que tiene toda la info
cap_df = pd.read_excel(fileCAPs, sheet_name=sheetCAPs)
milestones_df = pd.read_excel(fileMilestones, sheet_name=sheetMilestones)

# ordena los valores
ordered_cap_df = cap_df.sort_values(by=['CAP_id'])
merged_df = ordered_cap_df.merge(milestones_df,on='CAP_id')
merged_df['targetcap'] = merged_df['targetcap'].dt.strftime('%a %d %b %Y') # date conversion

# pivotTable
pivot_df = merged_df.pivot_table(index=['targetcap','CAP_id','cap_description','owner_milestone','milestone_id','descriptionmilestone'],\
                                 values='ownercap',aggfunc='count')







# presentas en una tabla
# print(milestones_df.sort_values(by=['CAP_id', 'target']))
# print(merged_df.sort_values(by=['CAP_id', 'targetcap', 'target_milestone']))
print (pivot_df)
display(HTML(pivot_df.to_html()))



#filtros... los que están próximos