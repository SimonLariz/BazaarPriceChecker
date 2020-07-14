import requests
import xlsxwriter

#Creation of Ecel workbook
workbook = xlsxwriter.Workbook('BazaarPrices.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col =0

#Writing wroksheet headers
worksheet.write(0, 0, 'Item')
worksheet.write(0, 1, 'Sells')
worksheet.write(0, 2, 'Buys')
worksheet.write(0, 3, 'Range')
worksheet.write(0, 4, 'Optimal Bid Price Per 1x')
worksheet.write(0, 5, 'Optimal Bid Price Per 64x')

#starting at next row under headers
row =1

#API key and reserve key for Hypixel API
key = "[[KEY 1]]"
reserve = "[[KEY 2]]"
products = requests.get("https://api.hypixel.net/skyblock/bazaar/products?key=[[KEY 1]]")


newproducts = products.json()
#getting products
newproducts = newproducts["productIds"]
#length of products
productslen = len(newproducts)
#looping through all of products
for i in range (0, productslen):
    current = (newproducts[i])
    print (str(i) + " out of " + str(productslen) + " products")
    product = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key="+key+"&productId="+current)
    resp = str(product)
    if resp.find("429") != -1:
        print ("Swapping to reserve key")
        key = reserve
        product = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key="+key+"&productId="+current)
        print (product)
    newproduct = product.json()
    newproduct = newproduct["product_info"]
    productbuy = newproduct["buy_summary"]
    productsell = newproduct["sell_summary"]
    try:
        buyprice = (productbuy[0]["pricePerUnit"])
        sellprice = (productsell[0]["pricePerUnit"])
        pricerange = sellprice - buyprice
        pricerange = round(pricerange, 2)
        worksheet.write(row, col, current)
        worksheet.write(row, col + 1, sellprice)
        worksheet.write(row, col + 2 , buyprice)
        worksheet.write(row, col + 3, pricerange)
        worksheet.write(row, col + 4, round(sellprice/1.15, 1))
        worksheet.write(row, col + 5, round(sellprice / 1.15*64, 1))

        row +=1
        col =0
    except:
        pass
#print (newlist)
print ("DONE! Check the BazaarPrices.xlsx file in the folder!")
workbook.close()
