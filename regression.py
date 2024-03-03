import numpy as np
import matplotlib.pyplot as plt

x_small = [18,21,38,48,53,17,18,20,21,27,24,30,34,42,58,65,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
y_small = [0.12,0.14,0.22,0.27,0.29,0.11,0.12,0.13,0.14,0.16,0.15,0.18,0.2,0.24,0.32,0.35,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19]
x = [16,30,38,94,109,145,166,187,209,229,275,295,323,359,376,397,417,425,429,436,444,448,451,459,466]
y = [0.1,0.18,0.32,0.5,0.62,0.99,1.24,1.53,1.85,2.19,3.09,3.55,4.28,5.38,5.97,6.76,7.59,7.94,8.12,8.48,8.85,9.03,9.22,9.61,10]

x_total = x + x_small
y_total = y + y_small

assert len(x_total) == len(y_total)

#data increases so sorting it is fine 
x_total.sort()
y_total.sort()

x_total = np.array(x_total)
y_total = np.array(y_total)

#get a polynomial function
coefficents = np.polyfit(x_total, y_total, 5)

y_fit = np.polyval(coefficents, x_total)

#string to store the coefficients
poly_str = "y = "
for i, coeff in enumerate(reversed(coefficents)):
    if i == 0:
        poly_str += f"{coeff}"
    elif i == 1:
        poly_str += f" + {coeff}x"
    else:
        poly_str += f" + {coeff}x^{i}"

print(f"The function is {poly_str}")
plt.plot(x_total, y_total, 'o')
plt.plot(x_total, y_fit, 'r-')
plt.show()