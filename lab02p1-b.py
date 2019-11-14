def swap():
    var1 = input("Please enter a value for the first variable: ")
    var2 = input("Please enter a value for the second variable: ")
    var3 = var1
    var1 = var2
    var2 = var3
    return var1, var2

print(swap())