df = pd.read_csv('./folder/file.csv')
# read csv file
df.head()
# show the top 5 rows of the table
df.info()
# show the basic information of the table(column name, count, non-null, type)
print(df.shape())
# show the shape of the table: (500,11) => 500 rows with 11 columns
print(df.columns)
# show the column names of the table
print(df['Year'].unique())
# show the unique values in the column
print(df['Price'].min())
print(df['Price'].max())
print(df['Price'].mean())
print(df['Price'].median())
print(df['Price'].mode())
print(df['Price'].std())
# show the min/max/mean/median/mode/standard deviation/
df=df.astype({'Name':'string','Price':'float64','Year':'category','Age':'int64'})
#change the type of columns in the table
