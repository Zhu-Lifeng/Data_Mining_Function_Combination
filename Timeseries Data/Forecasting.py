## Autoregression (AR)
from statsmodels.tsa.ar_model import AutoReg

# Fit Autoregressive model
model = AutoReg(data, lags=1,old_names=False) # "lags" indicates the model order
model_fit = model.fit()

# Make prediction
yhat = model_fit.predict(len(data), len(data)+3) # arguments denote which dataset indices to predict
print(yhat)

## Moving Average (MA)
from statsmodels.tsa.arima.model import ARIMA
from random import random

# Fit MA model
model = ARIMA(data, order=(0, 0, 3)) # The 3rd 'order' argument denotes q=3, ie. a 3rd order MA model
model_fit = model.fit()

# Make prediction
yhat = model_fit.predict(len(data), len(data)+3) # arguments denote which dataset indices to predict
print(yhat)

## Autoregressive Moving Average (ARMA)

# Fit ARMA model
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(data2, order=(2, 0, 1)) # p=2, q=1
model_fit = model.fit()

# Make prediction
yhat = model_fit.predict(len(data2), len(data2)+3) # arguments denote which dataset indices to predict
print(yhat)
