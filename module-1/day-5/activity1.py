buy = float(input("buying price "))
sell = float(input("selling price "))
prof = sell - buy
loss = buy - sell
if prof>0:
  print(f"profit: {prof}$")
else:
  print(f"loss: {loss}$")