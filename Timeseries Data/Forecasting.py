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
from statsmodels.tsa.arima.model import ARIMA
# Fit ARMA model
model = ARIMA(data2, order=(2, 0, 1)) # p=2, q=1
model_fit = model.fit()
# Make prediction
yhat = model_fit.predict(len(data2), len(data2)+3) # arguments denote which dataset indices to predict
print(yhat)

## Autoregressive Integrated Moving Average (ARIMA)
from statsmodels.tsa.arima.model import ARIMA
# Fit ARIMA model
model = ARIMA(data, order=(1, 2, 1)) # p=1, d=2, q=1
model_fit = model.fit()

# Make prediction
yhat = model_fit.predict(len(data), len(data)+3, typ='levels')
print(yhat)
