import pandas as pd

car_inventory = pd.read_csv("auto.csv")

# 1 Remove duplicates and missing values, then save to a new CSV
car_inventory.drop_duplicates(inplace=True)
car_inventory.dropna(inplace=True)
car_inventory.to_csv("refined_auto.csv", index=False)
print("Refined data saved to 'refined_auto.csv'.")

# 2 Identify the brand with the most expensive car
luxury_brand = car_inventory.loc[car_inventory["price"].idxmax(), "company"]
print(f"Luxury Car Brand: {luxury_brand}")

# 3 Show all Toyota car records
toyota_vehicles = car_inventory[car_inventory["company"].str.lower() == "toyota"]
print("Toyota Vehicle Information:")
print(toyota_vehicles)

# 4️⃣ Display car count per manufacturer
vehicle_count = car_inventory["company"].value_counts()
print("Number of Cars by Manufacturer:")
print(vehicle_count)

# 5 Find the top-priced model from each company
max_price_models = car_inventory.loc[car_inventory.groupby("company")["price"].idxmax()]
print("Top Priced Model per Company:")
print(max_price_models[["company", "price"]])

# 6 Compute average mileage per company
mileage_stats = car_inventory.groupby("company")["average-mileage"].mean()
print("Company-wise Average Mileage:")
print(mileage_stats)

# 7 Sort the entire dataset by price in descending order
sorted_by_price = car_inventory.sort_values(by="price", ascending=False)
print("Cars Sorted by Price:")
print(sorted_by_price)
