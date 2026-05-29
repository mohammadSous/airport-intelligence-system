import matplotlib.pyplot as plt
from utils.load_queries import load_report, CHARTS_TO_SHOW

for report_name, (x_col, y_col) in CHARTS_TO_SHOW.items():
    
    df = load_report(report_name)

    plt.figure(figsize=(10, 5))
    plt.bar(df[x_col], df[y_col])
    plt.title(report_name)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()