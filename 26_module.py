# impoting the entire module
# import converters
# print(converters.kg_to_lbs(100))


# importing a specific function for multiple functions by separating it with ',' 
from converters import kg_to_lbs

print(kg_to_lbs(120))

import utils
numbers = [1,4,3,2]
print(utils.find_max(numbers))