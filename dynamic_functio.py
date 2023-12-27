import random

code = """
def dynamic_function(x):
    return x * 2
"""
code2 = """
def dynamic_function(x):
    return x / 2
"""
codes = [code, code2]
#OPTION 1 exec_code = random.choice(codes)
#OPTION 2
index = int(random.random() * len(codes))
exec_code = codes[index]
# Dynamically define the function
exec(exec_code)

# Use the newly defined function
result = dynamic_function(5)
print("Result:", result)