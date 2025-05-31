import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_matrix(df, cols, title="Correlation Matrix"):
    corr = df[cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()
