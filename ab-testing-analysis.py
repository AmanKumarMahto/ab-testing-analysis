import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Create dataset
np.random.seed(42)
n = 1000

df = pd.DataFrame({
    "user_id": range(1, n+1),
    "variant": np.random.choice(['A', 'B'], n),
})

# Conversion logic
df['converted'] = df['variant'].apply(
    lambda x: np.random.choice([0,1], p=[0.85,0.15]) if x=='A' else np.random.choice([0,1], p=[0.80,0.20])
)

# Split groups
group_A = df[df['variant']=='A']['converted']
group_B = df[df['variant']=='B']['converted']

# Conversion rates
conv_A = group_A.mean()
conv_B = group_B.mean()

print("Conversion Rate A:", round(conv_A,3))
print("Conversion Rate B:", round(conv_B,3))

# Statistical test
t_stat, p_value = ttest_ind(group_A, group_B)
print("P-value:", round(p_value,5))

# Visualization
plt.bar(['Variant A','Variant B'], [conv_A, conv_B])
plt.title("A/B Testing Conversion Rate Comparison")
plt.ylabel("Conversion Rate")
plt.show()