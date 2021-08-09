# para mapear EoVs en el tiempo

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from IPython.display import display, HTML


# los archivos ya estarán nombrados con consecutivos
totalArchivos = 3
nombreFiles = 'input'
extension = '.xlsx'
sheetName = 'rawData'


def recibefile(nf, ta, extf, sn):
    numero = 1
    final_df = pd.DataFrame()
    for x in range(ta):
        obtenFile_df = pd.read_excel(nf + ' (' + str(numero) + ')' +  extf, sheet_name=sn)
        final_df = final_df.append(obtenFile_df)
        numero = numero + 1
    return final_df



consolidado_df = recibefile(nombreFiles, totalArchivos, extension, sheetName)   # cubo
pivot_df = consolidado_df.pivot_table(index=['week','ownercap'],\
                                  values='CAP_id',aggfunc='count')
# print(pivot_df)


pivot2_df = consolidado_df.pivot_table(index=['week'], columns=['ownercap'],\
                                  values='CAP_id',aggfunc='count')
pivot2_df = pivot2_df.fillna(0)
print(pivot2_df)

# todos
x = consolidado_df['week'].drop_duplicates()
y = consolidado_df.groupby(['week']).size()
plt.scatter(x, y)
plt.plot(x, y, '-o') # to connect with line


#que vaya por todos los grupos que se pueden hacer por lob/owner
'''
for x, y in consolidado_df(consolidado_df['ownercap'].drop_duplicates(), consolidado_df.groupby(['ownercap']).size()):
    print (x)
    plt.scatter(x, y)
    plt.plot(x, y, '-o') # to connect with line
'''

# consolidado_df.plot.scatter(x='week', y='ownercap')
ax = pivot2_df.plot(xticks=pivot2_df.index)
ylab = ax.set_ylabel('CAP_id')



plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
plt.title('EoVs trends, per LoB')
plt.ylabel('# EoVs')
plt.xlabel('dates')
plt.show()



# contar la información de cada uno y ponerlo en un nuevo dataframe
# todo ponerlo en un dataframe gigante, son los mismos datos

# pĺotear
