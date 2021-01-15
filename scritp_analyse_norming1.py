import pandas as pd
import re

#define funcions
def split_data(data, n): #n is the number of your stimuli
	n = n*2
	set1 = just_data.iloc[:,:-n]
	set2 = just_data.iloc[:,-n:]
	return set1, set2


def remove_questions(df): 
	df1 = df.drop(0) #remove cells with questions
	df1 = df1.drop(1)
	df1 = df1.dropna() #remove empty cells
	return df1

def clean(df):
	for i in df.columns:
		df[i] = df[i].str.lower() #lowercase everything
		df[i] = df[i].str.strip() #remove blank spaces at the beginning/end of the string -- often cause of difference
	return df

def count(df): 
	preferred = []
	dispreferred = []
	for i in df.columns:
    		if '_1' in i: #following qualtrics structure, answers to the first question
        		preferred.append([set1.value_counts(i, normalize=True), set1.value_counts(i, normalize=True).std()])
	for i in set1.columns:
    		if '_2' in i: #following qualtrics structure, answers to the second question
        		dispreferred.append([set1.value_counts(i, normalize=True), set1.value_counts(i, normalize=True).std()])
	return preferred, dispreferred

def sort_val(preferred,dispreferred): 
	pref = []
	stdp = []
	for i in preferred:
    		pref.append(pd.DataFrame(i[0]).sort_values(by=0,ascending=False)) #sort answers (from the most frequent to the least in percetage)
    		stdp.append(i[1])
	disp = []
	stdd = []
	for i in dispreferred:
    		disp.append(pd.DataFrame(i[0]).sort_values(by=0,ascending=False)) #sort answers (from the most frequent to the least in percetage)
    		stdd.append(i[1])
	return pref, stdp, disp, stdd


def read_val(pref, disp): #make it readable
	xx =[]
	for i in pref:
    		x = []
    		x.append(i.to_string())
    		xx.append(x)
	preferred = [i[0].split('\n')[2:] for i in xx]
	preferred = ['\n'.join(i) for i in preferred]
	yy =[]
	for i in disp:
    		y = []
    		y.append(i.to_string())
    		yy.append(y)
	dispreferred = [i[0].split('\n')[2:] for i in yy]
	dispreferred = ['\n'.join(i) for i in dispreferred]
	return preferred, dispreferred

#PREPARE FILES 
path_to_csv = '...' #your file from qualtrics
results = pd.read_csv(path_to_csv) 

just_data = results.iloc[:,17:] #keep just the row with data #keep just the row with data. It depends on the file you obtained!
just_data = just_data.sort_values(by='Q196_1') #sort the values of the first real question (selected manually and avoiding the example 'pinapple'). now we have the two set of stimuli visually separated

set1, set2 = split_data(just_data,90)
set1 = remove_questions(set1)
set2 = remove_questions(set2)
set1.to_csv('just_data_set1.csv') #save the csv
set2.to_csv('just_data_set2.csv') #save the csv

#ANNOTATIONS SET1

set1 = clean(set1) 
preferred, dispreferred = count(set1)
pref, stdp, disp, stdd = sort_val(preferred, dispreferred )
preferred, dispreferred = read_val(pref,disp)

#put everything in a csv
stimulus = range(0,91) #depends on the number of stimuli (*remember: here 90 + 1 example)
d1 = {'stimulus': stimulus, 'preferred': preferred, 'stdp': stdp, 'dispreferred': dispreferred, 'stdd': stdd}
dd1 = pd.DataFrame(d1)
dd1.to_csv('set1_percentage_std.csv')

#ANNOTATIONS SET 2
set2 = clean(set2) 
preferred, dispreferred = count(set2)
pref, stdp, disp, stdd = sort_val(preferred, dispreferred )
preferred, dispreferred = read_val(pref,disp)

#put everything in a csv
stimulus = range(0,90) #depends on the number of stimuli (here 90)
d2 = {'stimulus': stimulus, 'preferred': preferred, 'stdp': stdp, 'dispreferred': dispreferred, 'stdd': stdd}
dd2 = pd.DataFrame(d2)
dd2.to_csv('set2_percentage_std.csv')