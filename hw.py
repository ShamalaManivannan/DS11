import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("dinoset.csv")

data = data[['scientific_name','common_name','meaning','diet','length_m','weight_kg','height_m','locomotion','geological_period','lived_in','behavior_notes','first_discovered','fossil_location','notable_features','intelligence_level','source_link','row_index']]

data.columns = ('s_name','name','meaning', 'diet', 'length','weight', 'height','locomotion', 'geo_period', 'lived', 'behaviour', 'first_discover','fossil_location','notable_features', 'intelligence_level', 'source_link','row_index')



print(data.info())
print(data.head())

top10_weight = pd.DataFrame(data.groupby("name")['weight'].sum().nlargest(10).sort_values(ascending = True))
fig1  = px.scatter(top10_weight, x = top10_weight.index, y = 'weight', size = 'weight', size_max = 120, color = top10_weight.index, title = "Top 10 Dinosaurs by Weight")
fig1.write_html('Fig1.html', auto_open = True)


top10_length = pd.DataFrame(data.groupby("name")['length'].sum().nlargest(10).sort_values(ascending = True))
fig2 = px.scatter(top10_length, x = top10_length.index, y = 'length', size = 'length', size_max = 120, color = top10_length.index, title = 'Top 10 Dinosaurs by Length')
fig2.write_html('Fig2.html', auto_open = True)

top10_height = pd.DataFrame(data.groupby("name")["height"].sum().nlargest(10).sort_values(ascending = False))

fig3 = px.scatter(top10_height,x = top10_height.index, y = 'height', size = 'height', size_max = 120, color = top10_height.index, title = 'Top 10 Dinousarus by Height')
fig3.write_html('Fig3.html', auto_open = True)

#Bar charts 

top10_weight = pd.DataFrame(data.groupby('name')['weight'].sum().nlargest(12).sort_values(ascending = False))

fig5 = px.bar(top10_weight,x = 'weight',y = top10_weight.index,height = 600,color = 'weight', orientation = 'h',color_continuous_scale = ['deepskyblue','red'], title = 'Top 10 Dinosaurs by Weight ')
fig5.write_html('Fig5.html', auto_open=True)

top10_height = pd.DataFrame(data.groupby('name')['height'].sum().nlargest(12).sort_values(ascending = False))

fig6 = px.bar(top10_height,x = 'height',y = top10_height.index,height = 600,color = 'height', orientation = 'h',color_continuous_scale = ['deepskyblue','orange'], title = 'Top 10 Dinosaurs by Height')
fig6.write_html('Fig6.html', auto_open=True)

top10_length = pd.DataFrame(data.groupby('name')['length'].sum().nlargest(12).sort_values(ascending = False))

fig6 = px.bar(top10_length,x = 'length',y = top10_length.index,height = 600,color = 'length', orientation = 'h',color_continuous_scale = ['deepskyblue','orange'], title = 'Top 10 Dinosaurs by Length')
fig6.write_html('Fig6.html', auto_open=True)

