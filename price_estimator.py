#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.array([500,600,700,800,900])
y = np.array([7e6,9e6,10e6,11e6,13e6])

def normalize_area(area):
    avg_area = 700
    return (area - avg_area) / 100

def normalize_price(price):
    avg_price = 10e6
    return (price - avg_price) / 1e6



x_n = normalize_area(x)
y_n = normalize_price(y)

m, b = np.polyfit(x_n, y_n, 1)
print(m,b)

def unnormalize_price(price):
    avg_price = 10e6
    return price * 1e6 + avg_price

# area is unnormalized
def estimate_price(area, m, b):
    area_n = normalize_area(area)
    price_n = m * area_n + b
    return unnormalize_price(price_n)

print(estimate_price(700,m,b))

y_est = [estimate_price(i,m,b) for i in x]

plt.figure()
plt.scatter(x,y, label='Data points')
plt.plot(x, y_est, 'r', label='Model')
plt.legend()
plt.show()

import gradio as gr

demo = gr.Interface(
    fn=lambda area: estimate_price(area, m, b),
    inputs=gr.Number(label="Area (m^2)"),
    outputs=gr.Number(label="Estimated Price (TL)"),
    title="House Price Estimator",
    description="Enter the area of the house"
)

#demo.launch(server_name='0.0.0.0', server_port=7860)
demo.launch()

# %%
