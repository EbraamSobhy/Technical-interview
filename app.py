# List (Array)

price_list_array = [298, 305, 320, 301, 292]
print("List Examples")
for i, price in enumerate(price_list_array, start=1):
    print(f"Day{i}: {price}")

print("\n")

# Dictionary (Hash Table)

price_list_dict = {
    'march 4': 298,
    'march 5': 305,
    'march 6': 320,
    'march 7': 301,
    'march 8': 292
}

print("Dictionary Example:")
for data, price in price_list_dict.items():
    print(f"{data}: {price}")
