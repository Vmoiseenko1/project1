from main import Product
#from main import Shop

productss = []
with open('products.txt') as f: #all available products
    all_products = f.readlines()
    for line in all_products:
        line = line.replace('\n', '')
        productss.append(line)
print(productss)

for product in productss:
    answer = input('Do you want to buy this product? ')
    if answer == 'yes' or answer == 'Yes':
        prod = Product(product)
        print(prod.name)
        question = input('Do you want to see some info about it? ')
        if question == 'Yes' or question == 'yes':
            print('Here you can see some info:')
            print('Product name: ' + prod.name)
            print('The number of the pages: ' + prod.pages)
            print('Country: ' + prod.country)
            print('Price: ' + prod.price)
            print('The article number: ' + prod.article)
            print('The weight of the book: ' + prod.weight)
            print(' ')

    else:
        print(' ')





