import pandas as pd
import os

df = pd.read_csv("customer_service_data.csv")

print("\nDATASET OVERVIEW")
print(df.head())

average_resolution = df["resolution_time_hours"].mean()

print("\nAVERAGE RESOLUTION TIME:")
print(round(average_resolution, 2), "hours")

print("\nMOST COMMON ISSUES:")
print(df["issue_type"].value_counts())

print("\nAVERAGE SATISFACTION SCORE:")
print(round(df["satisfaction_score"].mean(), 2))

print("\nISSUES BY REGION:")
print(df.groupby("region")["ticket_id"].count())

escalated = df[df["service_status"] == "Escalated"]

print("\nESCALATED TICKETS:")
print(escalated[["ticket_id", "customer_name", "issue_type", "resolution_time_hours"]])

print("\nAVERAGE RESOLUTION TIME BY TECHNICIAN:")
print(df.groupby("technician_assigned")["resolution_time_hours"].mean())

summary_report = df.groupby("issue_type").agg({
    "resolution_time_hours": "mean",
    "satisfaction_score": "mean",
    "ticket_id": "count"
})

summary_report.rename(columns={
    "ticket_id": "total_tickets"
}, inplace=True)

os.makedirs("generated_reports", exist_ok=True)

summary_report.to_csv("generated_reports/operations_summary.csv")

print("\nSummary report generated successfully.")
