def sporeconcentration(x):
    nscore = ( x * 1 /(0.0625*0.2 *1))
    p1 = '{:.2e} spores/µl' .format(nscore)
    p2 = '{:.2e} spores/ml' .format(nscore *1000)
    return print (p1 + "\n" + p2)

sporeconcentration(x = int(input("How many spores did you count averaged over 5 squares: ")))