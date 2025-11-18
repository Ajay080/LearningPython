import copy 
chai_types={"Masala": 50, "Ginger": 30, "Tulsi": 20}
print("Type of chai_types is", type(chai_types), "and value is", chai_types)

for i in chai_types:
    print(f"Key: {i}, Value: {chai_types[i]}")

print(if "Masala" in chai_types)  #True
print(if "Elaichi" in chai_types)  #False

chai_types.pop("Ginger")
print("After popping Ginger, value of chai_types is", chai_types)

chai_types.popitem()
print("After popping an arbitrary item, value of chai_types is", chai_types)

del chai_types["Tulsi"]
print("After deleting Tulsi, value of chai_types is", chai_types)

chai_types["Elaichi"]= 40
print("After adding Elaichi, value of chai_types is", chai_types)
chai_types["Masala"]= 55
print("After modifying Masala, value of chai_types is", chai_types)
print("Keys in chai_types are", chai_types.keys())
print("Values in chai_types are", chai_types.values())
print("Items in chai_types are", chai_types.items())

chai_types.clear()
print("After clearing, value of chai_types is", chai_types)

chai_shallow_copy1 = dict(chai_types)
print("Shallow copied chai_shallow_copy1 using dict(), value is", chai_shallow_copy1)
chai_shallow_copy= chai_types.copy()
print("Shallow copied chai_shallow_copy using copy(), value is", chai_shallow_copy)
chai_copy=copy.deepcopy(chai_types)
print("Deep copied chai_copy using deepcopy(), value is", chai_copy)