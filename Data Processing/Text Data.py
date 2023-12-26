import pandas as pd


df_name=pd.DataFrame(df['Dish_name'],columns=['Dish_name'])
for x in ['(', ')', '&', '-', '"',"'", '\\', r'/', 'a', 'an', ',', ':']:
    df_name['Dish_name']=df_name['Dish_name'].str.replace(x,'_',regex=False)
df_name['Dish_name']=df_name['Dish_name'].str.replace(r'\d','',regex=True)
df_name=df_name['Dish_name'].str.get_dummies('_')
df_name=df_name.add_prefix('Name_')
# replace all needed signal with the spliting signal
# create dummy features for a text column, split the content with '_' into dummy features
