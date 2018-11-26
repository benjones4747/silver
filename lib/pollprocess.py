# by ben with <3

# imports pandas
import pandas as pd
import math as m
from datetime import datetime as d
import numpy as np

# imports raw 2016 polls csv file as 'raw'
raw_csv_path = 'C:\\Users\\Ben\\Documents\\GitHub\\pollng\\lib\\2016-polls.csv'
pr_csv_path = 'C:\\Users\\Ben\\Documents\\GitHub\\pollng\\lib\\pollster-ratings.csv'
raw = pd.read_csv(raw_csv_path, delimiter = ',')
pr1 = pd.read_csv(pr_csv_path, delimiter = ',')

# creates dictionary of state abbreviations for polls to go into and date of election (2016 presidential)

states = {
        'AK': [],
        'AL': [],
        'AR': [],
        'AZ': [],
        'CA': [],
        'CO': [],
        'CT': [],
        'DC': [],
        'DE': [],
        'FL': [],
        'GA': [],
        'HI': [],
        'IA': [],
        'ID': [],
        'IL': [],
        'IN': [],
        'KS': [],
        'KY': [],
        'LA': [],
        'MA': [],
        'MD': [],
        'ME': [],
        'MI': [],
        'MN': [],
        'MO': [],
        'MS': [],
        'MT': [],
        'NC': [],
        'ND': [],
        'NE': [],
        'NH': [],
        'NJ': [],
        'NM': [],
        'NV': [],
        'NY': [],
        'OH': [],
        'OK': [],
        'OR': [],
        'PA': [],
        'RI': [],
        'SC': [],
        'SD': [],
        'TN': [],
        'TX': [],
        'UT': [],
        'US': [],
        'VA': [],
        'VT': [],
        'WA': [],
        'WI': [],
        'WV': [],
        'WY': []
}

# age decay formula

def age_decay(to_ed, t):
    d_c = (m.log(2))/(14 + (0.2 * to_ed))
    abs_w = m.exp( -( d_c * t ))
    return abs_w

# adds age decay formula

def ageweight(raw):
    raw['age_weight'] = 0.0
    for index, row in raw.iterrows():
        d0 = row['electiondate']
        d0 = d.strptime(d0, '%m/%d/%y')
        date = row['polldate']
        d1 = d.strptime(date, '%m/%d/%y')
        delta = d0 - d1
        diff = delta.days
        age_weight = age_decay(0 , diff)
        raw.at[index,'age_weight'] = age_weight
    raw.to_csv(raw_csv_path, index = False)
    return

# process polls to add pollster weighting

def poll_process(states, pr):
    for key in states:
        state = states.get(key)
        for x in state:
            pollster = x.get('pollster')
            # pollster weighting
            pr_value = np.array(pr.loc[pr['Pollster'] == pollster,'Pollster Weight'].values)
            if pr_value.size == 1:
                x['pollster_weight'] = pr_value[0]
            else:
                x['pollster_weight'] = 0.0
            w_age = x.get('age_weight')
            w_pr = x.get('pollster_weight')
            w_total = w_age * w_pr
            x['total_weight'] = w_total
    return states

# for each item in {states}, iterate through each row of the raw 2016 polls and identify which are from the state in question, and append to a list of polls from that state within {states}, then add pollster weighting

def arrayify(raw, states, pr):
    raw = raw.to_dict(orient = 'index')
    for key in states:
        for x in raw.values():
            if x['location'] == key:
                states[key].append(x)
    states = poll_process(states, pr1)
    return states
















#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~REDUNDANT CODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#THIS CODE WAS A PROTOTYPE OF THE STATE APPENDING FUNCTION
#for x in raw.values():
#    cur_poll = x
#    for key in states:


#THIS CODE INTENDED TO CHANGE THE POLLS INTO OBJECTS
#class Poll2016():
#    def __init__(self, pollno, location, pollster, cand1_pct, cand2_pct):
#        self.pollno = pollno
#        self.location = location
#        self.pollster = pollster
#        self.dem_pct = cand1_pct
#        self.rep_pct = cand2_pct
#    def getPollno(self):
#        return self.pollno
#    def getLocation(self):
#        return self.location
#    def getPollster(self):
#        return self.pollster
#    def getDemPct(self):
#        return self.dem_pct
#    def getRepPct(self):
#        return self.rep_pct
#poll_objects = {}
#for x in raw:
#    poll_objects['x'] = Poll2016(raw['pollno'], raw['location'], raw['pollster'], raw['cand1_pct'], raw['cand2_pct'])











#THIS CODE ALTERED SOME ELEMENTS OF THE CSV FILE CONTAINING THE POLLS
#margin_mod = []
#for index, row in generic.iterrows():
#    generic_dem = row['Democrats (D)']
#    generic_rep = row['Republicans (R)']
#    generic_margin = generic_dem - generic_rep
#    margin_mod.append(generic_margin)
#
#generic['Absolute Margin'] = margin_mod
#generic.to_csv('C:\\Users\\Ben\\Documents\\GitHub\\pollng\\2018generic.csv')

#THIS CODE ADDED A WEIGHTING TO THE POLLSTER RANKINGS WHEN THEY WERE IN REALCLEARPOLITICS FORMAT
#pr_weight = []
#for index, row in generic.iterrows():
#    if row['Poll'] != 'RCP Average':
#        cur_pr = row['Poll']
#        sel_pr = pr.loc[pr['Pollster'] == cur_pr]
#        pr_weight.append(sel_pr['Pollster Weight'])
