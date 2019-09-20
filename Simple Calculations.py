# Alan Marx
# Colorado State University – Global Campus


values = []
sums = 0

print("This program will take 5 input values and provide a Total, Average, Maximum,\nMinimum and 20% interest calculation for each value.\n")

while len(values) != 5:
    val = input("Enter a whole or decimal: ")
    try:
        x = float(val)
        values.append(x)
    except ValueError:
        print("That was not a correct value...\n")
    
for x in values:
    sums += x

average = sums / len(values)
print("\nOriginal Values","    Values Including Interest")

for orig_number in values:
    intval = orig_number + orig_number * .02
    print('%10s%25s'%(orig_number,intval))

print("\nTotal:\t", sums)
print("Average:", average)
print("Max:\t",max(values))
print("Min:\t",min(values))

input()
