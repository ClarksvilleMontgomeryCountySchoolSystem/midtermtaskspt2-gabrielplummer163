def main():
    print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
# TODO Complete the menu with the remaining items. Press enter to add new lines.
Flying Carpet - $119.99
Phoenix Feather - $14.99
Time Turner - $84.99
Enchanted Sword - $65.99
Potion of Luck - $11.99
Crystal Ball - $39.99
""")

    # Shopkeeper's rule: All purchases must be at least 3 items for good luck!
    # (Don't worry - the shopkeeper checks every order himself)
    item_name = input(f"What is the item you would like to purchase?\n")
    item_price = float(input(f"What is the item price?\n"))
    quantity = int(input(f"How many would you like to purchase?\n"))

  # TODO: Calculate subtotal, tax, and total


    subtotal = item_price * quantity
    # Tax rate: 9.5%
    tax = subtotal * 0.095
    tax = round(tax, 2)
    total_cost = subtotal + tax

    # TODO: Round total to 2 decimal places using round()

    total_cost = round(total_cost,2)

    # TODO: Print receipt
    print("--------------------------")

    print(f"{item_name} x{quantity} @ & {item_price} each")

    print("--------------------------")
    # Print subtotal, tax, and total here
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Total: ${total_cost}")


    print("\nThank you for shopping at\nthe Peculiar Emporium!")

    # The Peculiar Emporium


if __name__ == "__main__":
    main()
