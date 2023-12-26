df['Name'].duplicated()
# assign all duplicated value row of the column with 1, others with 0
df['Name'].duplicated().sum()
# get the number of duplicated value in this column
