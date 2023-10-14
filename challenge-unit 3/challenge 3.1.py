def linersearchProduct(product,targetProduct):
  indices=[]
  for index,product in enumerate(products):
    if product==targetProduct:
      indices.append(index)

  return indices


#example usage:

products=["kodi","hasini","kavya","priya","kodi","lavenya","kodi"]
target1="kodi"
target2="Nathiya"
result=linersearchProduct(products,target1)
result1=linersearchProduct(products,target2)
print(result)
print(result1)