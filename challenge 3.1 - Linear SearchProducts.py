"""
Write a function called linear_search_product that takes the list of products and a target product
name as input. The function should perform a linear search tofind the target product in the list and
return a list of indices of all occurrences of the product iffound, or an empty list if the product is not
found.
"""


def linearSearchProduct(productList,targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["Chocolate", "Snacks", "Biscuits", "Chocolate", "Cake", "Chocolate"]
target = "Chocolate"
result = linearSearchProduct(products, target)
print(result)
