# math is a module
import math

print("\nMath.floor")
print(math.floor(18.4))
print("\nMath.sqrt")
print(math.sqrt(18))

# macros in Python
# we can rename a function temporarily this way
print("\n\nRenamed math.sqrt to Sachin")
sachin = math.sqrt
print(sachin(81))
