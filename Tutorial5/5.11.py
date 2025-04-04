import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from CSV
sales_data = pd.read_csv("sales.csv")

print("Preview of Sales Data:")
print(sales_data.head())

# 1) Scatter Plot for Toothpaste Sales
def plot_toothpaste_sales(data):
    plt.figure(figsize=(8, 5))
    plt.scatter(data["month_number"], data["toothpaste"], color="crimson", marker="o", label="Toothpaste Sales")
    plt.xlabel("Month Number")
    plt.ylabel("Sales of Toothpaste")
    plt.title("Monthly Toothpaste Sales")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_toothpaste_sales(sales_data)

# 2) Bar Chart for Face Cream and Face Wash Sales
def plot_cream_and_wash_sales(data):
    plt.figure(figsize=(8, 5))
    plt.bar(data["month_number"] - 0.2, data["facecream"], width=0.4, color="royalblue", label="Face Cream")
    plt.bar(data["month_number"] + 0.2, data["facewash"], width=0.4, color="seagreen", label="Face Wash")
    plt.xlabel("Month Number")
    plt.ylabel("Sales")
    plt.title("Monthly Sales: Face Cream & Face Wash")
    plt.xticks(data["month_number"])
    plt.legend()
    plt.show()

plot_cream_and_wash_sales(sales_data)

# 3) Pie Chart for Total Product Sales
def display_total_product_sales(data):
    product_totals = {
        "Face Cream": data["facecream"].sum(),
        "Face Wash": data["facewash"].sum(),
        "Toothpaste": data["toothpaste"].sum(),
        "Bathing Soap": data["bathingsoap"].sum(),
        "Shampoo": data["shampoo"].sum(),
        "Moisturizer": data["moisturizer"].sum(),
    }

    plt.figure(figsize=(8, 5))
    plt.pie(product_totals.values(), labels=product_totals.keys(), autopct="%1.1f%%",
            startangle=140, colors=["royalblue", "seagreen", "crimson", "purple", "darkorange", "cyan"])
    plt.title("Yearly Sales Distribution by Product")
    plt.show()

display_total_product_sales(sales_data)
