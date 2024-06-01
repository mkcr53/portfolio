import matplotlib.pyplot as plt

# Create figure and axes
fig, axs = plt.subplots(3, 1, figsize=(8.5, 11))  # 3 rows, 1 column for each section

# Define the space between plots
plt.subplots_adjust(hspace=0.5)

# Top Section: Adoption Trends
axs[0].text(0.5, 0.8, 'Adoption Trends', fontsize=16, ha='center')
axs[0].bar(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'], range(1, 9))  # Example bar chart
axs[0].set_title('Adoption Trends W/ Forecast', fontsize=14, loc='left')
axs[0].text(1.1, 0.4, 'Analysis of adoption trends...', fontsize=12, transform=axs[0].transAxes)

# Middle Section: Request and Release Ratios & Denied Requests Analysis
axs[1].text(0.5, 0.8, 'Operational Efficiency and Room for Improvement', fontsize=16, ha='center')
axs[1].bar(['CENTER', 'MRAH OR', 'MSC OR'], [1, 2, 3])  # Example bar chart
axs[1].set_title('Request and Release Ratio', fontsize=14, loc='left')
axs[1].text(1.1, 0.4, 'Analysis of request/release ratio...', fontsize=12, transform=axs[1].transAxes)

# Bottom Section: Peak Transaction Hours
axs[2].text(0.5, 0.8, 'Peak Operational Hours', fontsize=16, ha='center')
axs[2].bar(range(24), range(24))  # Example bar chart to represent hours
axs[2].set_title('Peak Transaction Hours', fontsize=14, loc='left')
axs[2].text(0.5, -0.2, 'Analysis of peak hours...', fontsize=12, ha='center', transform=axs[2].transAxes)

# Turn off axes for layout visualization
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

# Set the entire figure background color
fig.patch.set_facecolor('white')

# Save the figure as a PDF
plt.savefig('report_layout.pdf')

plt.show()
