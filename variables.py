
product_1_naam = "Koffiezetapparaat"
product_1_prijs = 49.99
product_2_naam = "Mixer"
product_2_prijs = 89.50
product_3_naam = "Waterkoker"
product_3_prijs = 29.95


product_1_aantal = 12
product_2_aantal = 8
product_3_aantal = 25


omzet_product_1 = product_1_prijs * product_1_aantal
omzet_product_2 = product_2_prijs * product_2_aantal
omzet_product_3 = product_3_prijs * product_3_aantal

totale_omzet = omzet_product_1 + omzet_product_2 + omzet_product_3


print(f"{product_1_naam}: €{product_1_prijs:.2f}, aantal: {product_1_aantal}")
print(f"{product_2_naam}: €{product_2_prijs:.2f}, aantal: {product_2_aantal}")
print(f"{product_3_naam}: €{product_3_prijs:.2f}, aantal: {product_3_aantal}")


print(f"Totale omzet: €{totale_omzet:.2f}")
