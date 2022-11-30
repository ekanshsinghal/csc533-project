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

def plot_graph(labels, dataA, dataB, title):
	labels = [ '\n'.join(wrap(l, 35)) for l in q_a.keys() ]
	vpn_ans = [i*100/total_vpn_users for i in dataA]
	no_vpn_ans = [i*100/total_novpn_users for i in dataB]
	x = np.arange(len(labels))
	width = 0.35

	fig, ax = plt.subplots()
	rects1 = ax.barh(x - width/2, vpn_ans, width, label='VPN')
	rects2 = ax.barh(x + width/2, no_vpn_ans, width, label='No VPN')

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_xlabel('Percentage')
	ax.set_title(title)
	ax.set_yticks(x, labels, fontsize=8)
	ax.legend()

	ax.bar_label(rects1, padding=3)
	ax.bar_label(rects2, padding=3)

	fig.tight_layout()

	plt.show()


def plot_graph_triple(labels, dataA, dataB, dataC, totalA, totalB, totalC, labelA, labelB, labelC, title):
	labels = [ '\n'.join(wrap(l, 35)) for l in q_a.keys() ]
	dataA = [i*100/totalA for i in dataA]
	dataB = [i*100/totalB for i in dataB]
	dataC = [i*100/totalC for i in dataC]
	x = np.arange(len(labels))
	width = 0.25

	fig, ax = plt.subplots()
	rects1 = ax.barh(x + width, dataA, width, label=labelA)
	rects2 = ax.barh(x, dataB, width, label=labelB)
	rects3 = ax.barh(x - width, dataC, width, label=labelC)

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_xlabel('Percentage')
	ax.set_title(title)
	ax.set_yticks(x, labels, fontsize=8)
	ax.legend()

	ax.bar_label(rects1, padding=3)
	ax.bar_label(rects2, padding=3)
	ax.bar_label(rects3, padding=3)

	fig.tight_layout()

	plt.show()


def plot_graph_quad(labels, dataA, dataB, dataC, dataD, totalA, totalB, totalC, totalD, labelA, labelB, labelC, labelD, title):
	labels = [ '\n'.join(wrap(l, 35)) for l in q_a.keys() ]
	dataA = [i*100/totalA for i in dataA]
	dataB = [i*100/totalB for i in dataB]
	dataC = [i*100/totalC for i in dataC]
	dataD = [i*100/totalD for i in dataD]
	x = np.arange(len(labels))
	width = 0.2

	fig, ax = plt.subplots()
	rects1 = ax.barh(x + width*3/2, dataA, width, label=labelA)
	rects2 = ax.barh(x + width/2, dataB, width, label=labelB)
	rects3 = ax.barh(x - width/2, dataC, width, label=labelC)
	rects4 = ax.barh(x - width*3/2, dataD, width, label=labelD)

	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_xlabel('Percentage')
	ax.set_title(title)
	ax.set_yticks(x, labels, fontsize=8)
	ax.legend()

	ax.bar_label(rects1, padding=3)
	ax.bar_label(rects2, padding=3)
	ax.bar_label(rects3, padding=3)
	ax.bar_label(rects4, padding=3)

	fig.tight_layout()

	plt.show()

with open('Survey.csv', mode ='r')as file:
	dict_reader = csv.DictReader(file)
	data = list(dict_reader)

def init_zero():
	return 0


vpn, no_vpn, under28, under45, over45 = {},{},{},{},{}
ios, android, otherOS = {},{},{}
stem, finance, arts, others = {},{},{},{}
for ques in q_a:
	vpn[ques] = 0
	no_vpn[ques] = 0
	under28[ques] = 0
	under45[ques] = 0
	over45[ques] = 0
	ios[ques], android[ques], otherOS[ques] = 0, 0, 0
	stem[ques], finance[ques], arts[ques], others[ques] = 0, 0, 0, 0

total_vpn_users, total_novpn_users = 0, 0
total_28, total_45, total_45over = 0, 0, 0
total_ios, total_android, total_otheros = 0, 0, 0
total_stem, total_finance, total_arts, total_others = 0, 0, 0, 0

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

	if response['What is your age group?'] == '18 - 27':
		total_28 += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				under28[ques] += 1
	elif response['What is your age group?'] == '28 - 45':
		total_45 += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				under45[ques] += 1
	else:
		total_45over += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				over45[ques] += 1
	
	if response['Which mobile operating system do you use?'] == 'iOS':
		total_ios += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				ios[ques] += 1
	elif response['Which mobile operating system do you use?'] == 'Android':
		total_android += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				android[ques] += 1
	else:
		total_otheros += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				otherOS[ques] += 1
	
	if response['Which option closest resembles your profession?'] == 'STEM / Engineering':
		total_stem += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				stem[ques] += 1
	elif response['Which option closest resembles your profession?'] == 'Finance / Commerce':
		total_finance += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				finance[ques] += 1
	elif response['Which option closest resembles your profession?'] == 'Arts':
		total_arts += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				arts[ques] += 1
	else:
		total_others += 1
		for ques, ans in q_a.items():
			if response[ques] == ans:
				others[ques] += 1

plot_graph(q_a.keys(), vpn.values(), no_vpn.values(), 'Percentage of people who got right answere by VPN usage')
plot_graph_triple(q_a.keys(), under28.values(), under45.values(), over45.values(), total_28, total_45, total_45over, '18 - 27', '28 - 45', '45 and above', 'Percentage of people who got right answere by age')
plot_graph_triple(q_a.keys(), ios.values(), android.values(), otherOS.values(), total_ios, total_android, total_otheros, 'iOS', 'Android', 'Other OS', 'Percentage of people who got right answere by OS')
plot_graph_quad(q_a.keys(), stem.values(), finance.values(), arts.values(), others.values(), total_stem, total_finance, total_arts, total_others, 'STEM / Engineering', 'Finance / Commerce', 'Arts', 'Others', 'Percentage of people who got right answere by Profession')