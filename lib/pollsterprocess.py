# by ben with <3
import pandas as pd


# imports pollster ratings csv file as 'pr'
pr = pd.read_csv( 'C:\\Users\\Ben\\Documents\\GitHub\\pollng\\lib\\pollster-ratings.csv', delimiter = ',')

# pollster weighting function
def weight(x):
    newx = float(1 - (1/(3.025044 + 1.200763)) * (x + 1.200763))
    return newx

# append Pollster Weight to pollster rating csv
def apply_weights(pr):
    pr['Pollster Weight'] = 0.0
    for index, row in pr.iterrows():
        x = row['Predictive Plus-Minus']
        if row['Banned by 538'] == 'yes':
            newx = 0.0
        else:
            newx = weight(x)
        pr.at[index,'Pollster Weight'] = newx
    pr.to_csv('C:\\Users\\Ben\\Documents\\GitHub\\pollng\\lib\\pollster-ratings.csv', index = False)
    return pr
