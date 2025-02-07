n=int(input("n: "))

for i in range(n):
    val = i+1
    for j in range(n):
        print(val, end=" ")
        val += n    
    print()
    val+=1



# n = int(input("Enter the value of n: "))

# for i in range(n):  # Columns
#     for j in range(n):  # Rows
#         value = (i + j * n) % 9 + 1  # Correct equation
#         print(value, end=" ")
#     print()  # Move to the next line after each row
    