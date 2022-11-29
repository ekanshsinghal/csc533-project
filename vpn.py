import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
from textwrap import wrap

# answer dict
q_a =  {
	'Does the U.S government have the ability to track the movement of cellphones?':'It can track the movement of cell phones without any warrant',
	'Which of the following is(are) within the capabilities of the US police?': 'Track GPS Location on your phone',
	'Burglars can track valuable items by extracting location data from their pictures': 'TRUE',
	'Ad campaigns can use location data for intimidation?': 'TRUE',
	'Mobile Apps are known to sell your location data to government/contractors?': 'TRUE',
	'How accurately can apps track your location?': 'Precise locations and amount of time spent at each location.',
	'Apps sell your location data to be able to provide free services?': 'TRUE',
	'During the ‘Black Lives Matter’ protests, location data was used to monitor who was there and on what side of the line they stood to conclude their political opinion?': 'TRUE',
	'Even when location data is anonymised, it can still be linked to you using public information with very high accuracy?': 'TRUE',
}

with open('Survey.csv', mode ='r')as file:
	dict_reader = csv.DictReader(file)
	data = list(dict_reader)

def init_zero():
	return 0

vpn, no_vpn = defaultdict(init_zero), defaultdict(init_zero)
total_vpn_users, total_novpn_users = 0, 0

for response in data:
	if response['Do you use a VPN?'] == 'Yes':
		total_vpn_users += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				vpn[ques] += 1
	else:
		total_novpn_users += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				no_vpn[ques] += 1

labels = [ '\n'.join(wrap(l, 35)) for l in q_a.keys() ]
# labels = q_a.keys()
vpn_ans = [i*100/total_vpn_users for i in vpn.values()]
no_vpn_ans = [i*100/total_novpn_users for i in no_vpn.values()]
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.barh(x - width/2, vpn_ans, width, label='VPN')
rects2 = ax.barh(x + width/2, no_vpn_ans, width, label='No VPN')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Percentage')
ax.set_title('Percentage of people who got right answere by VPN usage')
ax.set_yticks(x, labels, fontsize=8)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()