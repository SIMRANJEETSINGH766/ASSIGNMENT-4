for Candies in range(200):
    if (Candies % 5 != 2):
        continue
    if (Candies % 6 != 3):
        continue
    if (Candies % 7 != 2):
        continue

    print(str(Candies) + " candies are in the bowl!")
    break
