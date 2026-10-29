#version1

shares = 10
price_per_share = 150

initial_investment = (shares * price_per_share)

print("STOCK CALCULATOR - VERSION 1")
print(f"Shares: {shares}")
print(f"Price per Share: ${price_per_share}")
print(f"Initial Investment Cost: ${initial_investment}")

#version 1 and 2
shares = 10
price_per_share = 150
initial_investment = shares * price_per_share
new_share_price = 175
current_investment_value = new_share_price * shares
profit = current_investment_value - initial_investment
return_pct = (profit / initial_investment) * 100


print("STOCK CALCULATOR - VERSION 2")

print(f"Shares:                 {shares}")
print(f"Initial Price:          ${price_per_share}")
print(f"Initial Investment:     ${initial_investment}")

print(f"New Share Price:        ${new_share_price}")
print(f"Current Value:          ${current_investment_value}")
print(f"Profit / Loss:          ${profit}")
print(f"Percentage Return:      {return_pct:.2f}%")
