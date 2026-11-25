# Function to calculate interest
def calculate_interest(loanAmount, interestRate):
    return round(loanAmount * (interestRate / 100), 2)


# Initialize parallel lists
loanAmounts = []
interestRates = []
interestAmounts = []

choice = "y"

print("*** Interest Calculator ***")
print()

while choice == "y" or choice == "Y":

    loanAmount = float(input("Enter loan amount: "))
    interestRate = float(input("Enter interest rate: "))

    interestAmount = calculate_interest(loanAmount, interestRate)

    print(f"Interest amount: {interestAmount:.2f}")
    print()

    loanAmounts.append(loanAmount)
    interestRates.append(interestRate)
    interestAmounts.append(interestAmount)

    choice = input("Continue? (y/n): ")
    print()

# Open output file
outputFile = open("InterestResults.txt", "w")

# Display column headings
print(f"{'AMOUNT':<12}{'RATE':<10}{'INTEREST':<12}")

outputFile.write(f"{'AMOUNT':<12}{'RATE':<10}{'INTEREST':<12}\n")

# Display and write calculation results
for i in range(len(loanAmounts)):

    print(f"{loanAmounts[i]:<12.2f}"
          f"{interestRates[i]:<10.3f}"
          f"{interestAmounts[i]:<12.2f}")

    outputFile.write(f"{loanAmounts[i]:<12.2f}"
                     f"{interestRates[i]:<10.3f}"
                     f"{interestAmounts[i]:<12.2f}\n")

print()
print("Bye!")

outputFile.write("\n")
outputFile.write("Bye!\n")

outputFile.close()
