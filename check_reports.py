from utils.load_queries import load_report,REPORTS

def show_reports(reports):
    for report_name, file_name in reports.items():
        df = load_report(report_name)
        print("\n" + "=" * 60)
        print(report_name)
        print("=" * 60)
        print(df.head(10))
        
show_reports(REPORTS)