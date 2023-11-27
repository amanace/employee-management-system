import pymongo
from pymongo import MongoClient
import json
import matplotlib.pyplot as plt
import logging

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['empmern']
collection = db['hr_employee']
print("Connected")

# Highest and lowest hourly rate
highest_hourly_rate_doc = collection.find_one(sort=[("HourlyRate", pymongo.DESCENDING)])
smallest_hourly_rate = collection.find_one({"HourlyRate": {"$exists": True}}, sort=[("HourlyRate", pymongo.ASCENDING)])

hourly_rate_info = [{"highest": highest_hourly_rate_doc['HourlyRate']},
                    {"lowest": smallest_hourly_rate['HourlyRate']}]

# Bar chart for Employment Type Distribution
part_time_count = collection.count_documents({"Department": "Sales"})
full_time_count = collection.count_documents({"Department": "Research & Development"})

plt.bar(['Sales', 'Research & Development'], [part_time_count, full_time_count], color=['blue', 'green'])
plt.title('Number of Documents by Department')
plt.xlabel('Department')
plt.ylabel('Number of Documents')
plt.savefig('E:\\employeesys\\frontend\\public\\graph_department.png')
plt.close()

# Scatter plot of Hourly Rate vs Daily Rate
data = collection.find({"HourlyRate": {"$exists": True}, "DailyRate": {"$exists": True}},
                       {"HourlyRate": 1, "DailyRate": 1})

hourly_rates = []
daily_rates = []

for record in data:
    hourly_rates.append(record["HourlyRate"])
    daily_rates.append(record["DailyRate"])

plt.scatter(daily_rates, hourly_rates, color='r', alpha=0.5)
plt.title('Scatter Plot of Hourly Rate vs Daily Rate')
plt.xlabel('Daily Rate')
plt.ylabel('Hourly Rate')
plt.grid(True)
plt.savefig('E:\\employeesys\\frontend\\public\\graph_hourly_daily.png')
plt.close()

# Bar chart for Overtime Distribution
overtime_count = collection.count_documents({"OverTime": "Yes"})
no_overtime_count = collection.count_documents({"OverTime": "No"})

plt.bar(['Yes', 'No'], [overtime_count, no_overtime_count], color=['blue', 'green'])
plt.title('Number of Documents by Overtime')
plt.xlabel('Overtime')
plt.ylabel('Number of Documents')
plt.savefig('E:\\employeesys\\frontend\\public\\graph_overtime.png')
plt.close()

# Histogram of Monthly Income
monthly_incomes = [doc["MonthlyIncome"] for doc in collection.find({"MonthlyIncome": {"$exists": True}})]

plt.hist(monthly_incomes, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Monthly Incomes')
plt.xlabel('Monthly Income Range')
plt.ylabel('Frequency')
plt.savefig('E:\\employeesys\\frontend\\public\\graph_monthly_income.png')
plt.close()

# Box plot of Monthly Income Distribution
plt.boxplot(monthly_incomes)
plt.title('Box Plot of Monthly Income Distribution')
plt.ylabel('Monthly Income')
plt.savefig('E:\\employeesys\\frontend\\public\\graph_monthly_income_boxplot.png')
plt.close()

# Close MongoDB connection
client.close()
