import random
import time

# Define the two versions of the function
# START updateCountV1
def updateCountV1():
    print("Version 1 of the function is running.")
# END updateCountV1

# START updateCountV2
def updateCountV2():
    print("Version 2 of the function is running.")
# END updateCountV2

# Function to determine the currently active function
def get_active_function(lines):
    for line in lines:
        if 'def updateCountV1():' in line and not line.strip().startswith('#'):
            return updateCountV1
        elif 'def updateCountV2():' in line and not line.strip().startswith('#'):
            return updateCountV2
    return None

# Function to modify the script
def modify_script(active_function):
    with open(__file__, 'r') as file:
        lines = file.readlines()

    new_active_function = updateCountV1 if active_function == updateCountV2 else updateCountV2

    in_function_block = False
    process_lines = False
    with open(__file__, 'w') as file:
        for line in lines:
            if 'START updateCountV1' in line or 'START updateCountV2' in line:
                in_function_block = True
                process_lines = new_active_function.__name__ in line
                file.write('#' + line.lstrip('#'))  # Always comment the START line
                continue

            if 'END updateCountV1' in line or 'END updateCountV2' in line:
                in_function_block = False
                file.write('#' + line.lstrip('#'))  # Always comment the END line
                continue

            if in_function_block and process_lines:
                file.write(line.lstrip('#'))  # Uncomment the lines for the active function
            elif in_function_block:
                file.write('#' + line.lstrip('#'))  # Comment the lines for the inactive function
            else:
                file.write(line)  # Write all other lines as is

    return new_active_function

# Read the current active function
with open(__file__, 'r') as file:
    current_lines = file.readlines()

current_active_function = get_active_function(current_lines)
if not current_active_function:
    current_active_function = updateCountV1  # Default to V1 if none is active

for i in range(2):
    # Modify the script and update the active function
    current_active_function = modify_script(current_active_function)

    # Call the active function
    current_active_function()
    time.sleep(2)
