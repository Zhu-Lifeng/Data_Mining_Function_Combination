import pandas as pd

sample = data.sample(n=3)
# sample 3 samples

sample = data.sample(frac=0.01, random_state=1)
# sample 1% samples from the population
