'''linear_search_product'''

def  linearSearchProduct(productList,targetProduct):
  indices = []

  for index, product in enumerate(productList):
     if product == targetProduct:
       indices.append(index)

  return indices

#Example usage:
products = ["shoes","boat","Loafer","shoes","sandal"]
target= "shoes"
target2 ='apple'
result = linearSearchProduct(products,target)
print(result)

          