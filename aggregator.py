# by ben with <3

import pandas as pd
import lib.pollprocess as p
import lib.pollsterprocess as pr
import numpy as np
raw = p.raw
states = p.states
pr = p.pr1

margins = []
weights = []

states = p.arrayify(raw, states, pr)
while True:
    sel_state = str(input('Select state to aggregate:   '))
    for key in states:
        if key == sel_state:
            state = states.get(key)
            average = 0
            for x in state:
                margin = x.get('margin_poll')
                weight = x.get('total_weight')
                margins.append(margin)
                weights.append(weight)
                wnxn = margin * weight
                average = average + wnxn

            average = average / sum(weights)
            print(average, '%')
