import pandas as pd
import sqlalchemy

import numpy as np;
import seaborn as sns; sns.set();
import matplotlib.pyplot as plt;
import plotly.express as px;

id_rodada = "'7161'"
data_inicial = "'2021-11-27'"
data_final = "'2022-02-11'"

consulta_sql = '''
select inflow.inflow_date,
power_plant.name_power_plant,
power_plant.posto_rdh,
inflow.value from inflow
join power_plant ON power_plant.id_power_plant = inflow.id_power_plant
where (inflow.id_origin_type=6
and inflow.id_type_inflow=3
and inflow.end_date is null);
'''

print(consulta_sql)

host = "esferadb-river-cluster.cluster-ro-c9enbadad5av.us-east-1.rds.amazonaws.com"
database = "river"
user = "thais.carvalho"
password = "agDd3NV6mpBKueYc"

engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}:3306/{database}')

df = pd.read_sql_query(consulta_sql, engine)

print(df.head())      

# Plotando Gráfico de dispersão - esses graficos tentam inferir  a relação de causa e efeito entre variáveis
turucui = df[df['name_power_plant']=='TUCURUI']['value']
smesa = df[df['name_power_plant']=='SMESA']['value']
fig = px.scatter(df, x=turucui, y=smesa, size_max = 10, width = 800)
#fig.size(10,6)
fig.update_traces(marker = dict(size = 12, line=dict(width = 2)), selector = dict(mode = 'markers'))
fig.update_layout(title = 'Vazões',)
fig.update_xaxes(title = 'Vazão de Tucurui m³/s')
fig.update_yaxes(title = 'Vazão de Serra da Mesa m³/s')
fig.show() 

