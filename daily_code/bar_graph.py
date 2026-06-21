import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "student"

ws.append(["Name", "Math", "Science", "English", "Computer"])
ws.append(["Rahul", 85, 90, 78, 92])
ws.append(["Priya", 90, 85, 88, 95])
ws.append(["Rohan", 60, 55, 70, 65])
ws.append(["Sneha", 78, 82, 85, 80])
ws.append(["Amit", 45, 50, 55, 48])
ws.append(["Pooja", 92, 88, 90, 94])
ws.append(["Vikas", 35, 40, 38, 47])
ws.append(["Neha", 88, 92, 85, 90])

wb.save("students.xlsx")
print("excel file created...!!")

df = pd.read_excel("students.xlsx")
print(df)

df["Average"] = df[["Math", "Science", "English", "Computer"]].mean(axis=1)
print(df[["Name", "Average"]])

df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 70 else "Fail")
print(df[["Name", "Average", "Result"]])

lowest = df.loc[df["Average"].idxmax()]
print(f"Lowest:{lowest['Name']}-{lowest['Average']}")
print(f"")

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.axhline(y=60, color="red", linestyle="--", label="Pass")
plt.legend()
plt.show()

# SAVE RESULT
df.to_excel("students_result.xlsx", index=False)
print("Result saved to students_result.xlsx")
