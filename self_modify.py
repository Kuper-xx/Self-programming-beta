# MODIFY FUNCTION
# Count: 4
# def updateCount():
#     print("Updating count...")

#     # Open the file and read the code
#     fin = open(__file__, 'r')
#     code = fin.read()
#     fin.close()

#     # Split the code into lines
#     lines = code.split('\n')

#     # Process the second line to increment the count
#     if lines[1].startswith('# Count: '):
#         try:
#             count = int(lines[1].split(': ')[1])
#             lines[1] = f'# Count: {count + 1}'
#             print(f"New count is {count + 1}")
#         except ValueError:
#             print("Error: The count on the second line is not a valid integer.")
#             return
#     else:
#         print("Error: The second line is not formatted correctly.")
#         return

#     # Reassemble the modified code
#     code = '\n'.join(lines)

#     # Write the modified code back to the file
#     fout = open(__file__, 'w')
#     fout.write(code)
#     fout.close()

# # Call the function
# updateCount()
import time
def updateCount():
    print("Updating count...")

    # Open the file and read the code
    fin = open(__file__, 'r')
    code = fin.read()
    fin.close()

    # Split the code into lines
    lines = code.split('\n')

    # Process the second line to increment the count
    if lines[1].startswith('# Count: '):
        try:
            count = int(lines[1].split(': ')[1])
            lines[1] = f'# Count: {count + 1}'
            print(f"New count is {count + 1}")
        except ValueError:
            print("Error: The count on the second line is not a valid integer.")
            return
    else:
        print("Error: The second line is not formatted correctly.")
        return

    # Reassemble the modified code
    code = '\n'.join(lines)

    # Write the modified code back to the file
    fout = open(__file__, 'w')
    fout.write(code)
    fout.close()

# Call the function
for i in range(4):
    updateCount()
    time.sleep(2)