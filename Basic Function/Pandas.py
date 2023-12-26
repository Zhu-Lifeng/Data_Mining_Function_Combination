df = pd.read_csv('./folder/file.csv')
# read csv file
df.head()
# show the top 5 rows of the table
df.info()
# show the basic information of the table(column name, count, non-null, type)
df.decrible(include='all')
# show the statistic information of the table(count, unique count, top, frequence, mean, std, min, 25%, 50%, 75%, max)
print(df.shape())
# show the shape of the table: (500,11) => 500 rows with 11 columns
print(df.columns())
# show the column names of the table
print(df['Year'].unique())
# show the unique values in the column
print(df['Price'].min())
print(df['Price'].max())
print(df['Price'].mean())
print(df['Price'].median())
print(df['Price'].mode())
print(df['Price'].std())
print(df['Price'].var())
print(df['Price'].value_count())
# show the min/max/mean/median/mode/standard deviation/variance/unique value count of the column
df.cov()
# show the covariance of all the numeric columns in the table
df.corr()
# show the correlation of all the numeric columns in the table
df['Name']
# get one column from the table
df[['Name','Year']]
# get multiple columns form the table
df.index
# get the index of the table
df.index= pd.to_datatime(df['Date'])
# set the index into the date
df.loc[(df['Year']=='2020')&(df['Age']>50)]
# query the table with one or more columns' value
df.loc[[11,29]]
# query the table with index (in this case 11 and 29)
df['Name'].isna()
# assign all missing value row of the column with 1, others with 0 (work with np.NaN)
df['Name'].isna().sum()
# get the number of missing value in this column
df['Name'].duplicated()
# assign all duplicated value row of the column with 1, others with 0
df['Name'].duplicated().sum()
# get the number of duplicated value in this column

df.columns = ['Name','Price','Year','Age']
# change the name of the columns in the table (number must be matched)
df = df.astype({'Name':'string','Price':'float64','Year':'category','Age':'int64'})
# change the type of columns in the table
df['Price']=pd.to_numeric(df['Price'])
# turn a column into a numeric one
df['Date']=pd.to_datatime(df['Date'])
# turn a column into a numeric one

df = df.replace('a','b')
# replace all 'a' in the table with 'b'
# work with np => df = df.replace('?',np.NaN) => replace ? with the missing value expression of np
df = df.drop(['Name','Age'],axis=1)
# delete columns from the table
df = df.append(A)
# add a column to the table (row number must be matched)

df['Year'].hist(bins=5)
# histogram of the column
df['Year'].boxplot()
# boxplot of the column
df.boxplot(figsize=(20,3))
# boxplot of all numeric columns in the table (better have similar resolvation)
