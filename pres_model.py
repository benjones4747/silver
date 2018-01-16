import math
net_app = 0
q2_gdp = 0
term_1_inc = 0
polarization = 0

net_app = float(input('Enter net Presidential approval (approval - disapproval) in the final Gallup poll of June: '))
q2_gdp = float(input('Enter annualized growth rate of real GDP in the second quarter of the election year:  '))
term_1_inc = int(input('Enter a one (1) if there is a first term incumbent in the race, and a zero (0) if there is not:    '))
if term_1_inc == 1 or term_1_inc == 0 and net_app > 0:
    polarization = 1
if term_1_inc == 0 and net_app < 0:
    polarization = -1

pres_vote_inc = 46.9 + (0.105*net_app) + (0.635*q2_gdp) + (5.22*term_1_inc) - (2.76*polarization)
pres_vote_chal = 100 - pres_vote_inc

print("The vote share of the incumbent party will be", pres_vote_inc, "and the vote share of the challenging party will be", pres_vote_chal, ".")
