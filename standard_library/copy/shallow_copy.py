"""
shallow_copy.py
"""
import copy

# Make a shallow copy of a list and change one of the values
stocks = [["CDR", "11B"], ["PLW"], ["TEN"]]
stock2 = copy.copy(stocks)

stocks[0][1] = "CRJ"

print(f"{stocks=}")
print(f"{stock2=}")

# OUTPUT
# stocks=[['CDR', 'CRJ'], ['PLW'], ['TEN']]
# stock2=[['CDR', 'CRJ'], ['PLW'], ['TEN']]
