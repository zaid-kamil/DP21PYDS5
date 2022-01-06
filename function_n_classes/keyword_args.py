def product_price(**products):
    for k,v in products.items():
        print(f"{k} cost ${v}")
    print(f"Total price:${sum(products.values())}")


product_price(maggi=50, mouse=2300, coffee=399)
product_price(maggi=50, coffee=399)

print(range(300))