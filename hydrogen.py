
def hydrogen(modulator):
  lyman = lambda n: 1 - 1/(n**2)
  balmer = lambda n: 1/4 - 1/((n+1)**2)
  lF = {lyman(n)*modulator:1 for n in range(2, 10)}
  bF = {balmer(n)*modulator:1 for n in range(2, 10)}
  return {**lF, **bF}