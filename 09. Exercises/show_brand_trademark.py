brands_dict = {
    "Nike" : "Just Do It",
    "Apple" : "Think different",
    "McDonald's" : "I'm lovin' it",
    "Tesco" : "Every little helps",
    "Diesel" : "For Successful Living",
    "Ronseal" : "Does exactly what it says on the tin",
    "Nokia" : "Connecting People",
    "Adidas" : "Impossible is nothing",
    "Microsoft" : "Your potential. Your position.",
    "YouTube" : "Don't Read the Comments",
    "Subway" : "eat fresh.",
    "Panasonic" : "ideas for life",
    "Gillette" : "The Best A Man Can Get"
    }

print(", ".join(brands_dict.keys()))
print("\n")

choice = input("Choose a brand from the ones above or type quit to exit: \n").lower()
for brand in brands_dict.keys():
        brands_dict[brand.lower()] = brands_dict.pop(brand)
while choice != "quit":
    print(brands_dict[choice])
    choice = input("Choose a brand from the ones above or type quit to exit: \n").lower()
    
