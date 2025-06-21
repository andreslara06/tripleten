from scipy import stats as st
import math as mt

p = .11
threshold = 500
n = 5000

mu = p*n
sigma = mt.sqrt(n*p*(1-p))

probalitit = st.norm(mu,sigma).cdf(threshold)

print(probalitit)