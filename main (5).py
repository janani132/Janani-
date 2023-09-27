def                            linearasearchProduct(productList, targetProduct):
  indices=[]
  for index, product in enumerate(productList):
   if product==targetProduct:
    indices. append(index)     
  return indices
products= ["shoes","boots","loafer","shoes","sandal","shoes"]
target="shoes"
result=linearasearchProduct(products, target)
print(result)