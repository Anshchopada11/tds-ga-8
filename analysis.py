# analysis.py
# Email: 24f1001822@ds.study.iitm.ac.in

import matplotlib.pyplot as plt

# Quarterly retention data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
retention_rates = [66.04, 67.01, 76.38, 78.2]
industry_target = 85
average_retention = sum(retention_rates) / len(retention_rates)

# Print average for verification
print(f"Average retention rate: {average_retention:.2f}")  # 71.91

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(quarters, retention_rates, marker='o', label='Company Retention Rate')
plt.axhline(y=industry_target, color='r', linestyle='--', label='Industry Target (85%)')

# Styling
plt.title('Quarterly Customer Retention Rate - 2024')
plt.xlabel('Quarter')
plt.ylabel('Retention Rate (%)')
plt.ylim(60, 90)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig('retention_trend.png')
