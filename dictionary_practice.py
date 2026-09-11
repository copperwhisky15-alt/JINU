# ==========================================
# Python Dictionary Operations Practice
# ==========================================

# Initializing dictionary
birthday_collection = {
    "Gagana": "12-05-2001",
    "Nandini": "18-08-2002",
    "Goshin": "25-11-2000",
    "Sneha": "10-01-2003"
}

# 1. Accessing Values
print("Gagana's Birthday:", birthday_collection["Gagana"])

# Accessing dictionary values safely with .get()
print("Sneha's Birthday:", birthday_collection.get("Sneha", "Not found"))

# 2. Removing Items
# Using pop()
print("Removed Nandini:", birthday_collection.pop("Nandini", "Not found"))

# Using del keyword
del birthday_collection["Goshin"]
print("Collection after deletion:", birthday_collection)

# 3. Extracting Keys, Values, and Items
print("\n--- Dictionary Inspection ---")
print("Values:", birthday_collection.values())
print("Keys:", birthday_collection.keys())
print("Items:", birthday_collection.items())

# 4. Updating Dictionaries
new_dates = {"Sneha": "30-3-2007"}
birthday_collection.update(new_dates)
print("Updated Collection:", birthday_collection)

# 5. Structuring Inventory Items
item1 = {
    "Name": "Milk_powder",
    "Quantity": 1,
    "price": 50
}

item2 = {
    "Name": "TATA_tea powder",
    "Quantity": 5,
    "price": 300
}

print("\n--- Store Items ---")
print("Item 1:", item1)
print("Item 2:", item2)# ==========================================
# Python Dictionary Operations Practice
# ==========================================

# Initializing dictionary
birthday_collection = {
    "Gagana": "12-05-2001",
    "Nandini": "18-08-2002",
    "Goshin": "25-11-2000",
    "Sneha": "10-01-2003"
}

# 1. Accessing Values
print("Gagana's Birthday:", birthday_collection["Gagana"])

# Accessing dictionary values safely with .get()
print("Sneha's Birthday:", birthday_collection.get("Sneha", "Not found"))

# 2. Removing Items
# Using pop()
print("Removed Nandini:", birthday_collection.pop("Nandini", "Not found"))

# Using del keyword
del birthday_collection["Goshin"]
print("Collection after deletion:", birthday_collection)

# 3. Extracting Keys, Values, and Items
print("\n--- Dictionary Inspection ---")
print("Values:", birthday_collection.values())
print("Keys:", birthday_collection.keys())
print("Items:", birthday_collection.items())

# 4. Updating Dictionaries
new_dates = {"Sneha": "30-3-2007"}
birthday_collection.update(new_dates)
print("Updated Collection:", birthday_collection)

# 5. Structuring Inventory Items
item1 = {
    "Name": "Milk_powder",
    "Quantity": 1,
    "price": 50
}

item2 = {
    "Name": "TATA_tea powder",
    "Quantity": 5,
    "price": 300
}

print("\n--- Store Items ---")
print("Item 1:", item1)
print("Item 2:", item2)
