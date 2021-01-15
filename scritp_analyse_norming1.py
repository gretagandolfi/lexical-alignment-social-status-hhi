import pandas as pd
import re

#PREPARE FILES 

path_to_csv = '' #your file from qualtrics
results = pd.read_csv(path_to_csv) 

just_data = results.iloc[:,17:] #keep just the row with data. It depends on the file you obtained!
just_data #check

just_data = just_data.sort_values(by='Q196_1') #sort the values of the first real question (selected manually and avoiding the example 'pinapple')
# now we have the two set of stimuli separated

#create two dataframes: it takes all the columns form the beginning to the 180th (1st set) and from there to the end
set1 = just_data.iloc[:,:-180]
set2 = just_data.iloc[:,-180:]

set1_noq = set1.drop(0) #remove cells with questions
set1_noqq = set1_noq.drop(1) #remove cells with questions
set1 = set1_noqq.dropna() #remove empty cells

set2_noq = set2.drop(0) #remove cells with questions
set2_noqq = set2_noq.drop(1) #remove cells with questions
set2 = set2_noqq.dropna() #remove empty cells

#check the dimensions: ok if you had 50 participants rating 91 stimuli (90 real + 1 example)
set1.shape

#check the dimensions: ok if you had 50 participants rating 90 stimuli
set2.shape

set1.to_csv('just_data_set1.csv') #save the csv
set2.to_csv('just_data_set2.csv') #save the csv

#ANNOTATIONS SET1

for i in set1.columns:
    set1[i] = set1[i].str.lower() #lowercase everything
    set1[i] = set1[i].str.strip() #remove blank spaces at the beginning/end of the string -- often cause of difference

preferred = []
dispreferred = []

for i in set1.columns:
    if '_1' in i: #following qualtrics structure, answers to the first question
        preferred.append(set1.value_counts(i, normalize=True))
        
for i in set1.columns:
    if '_2' in i: #following qualtrics structure, answers to the second question
        dispreferred.append(set1.value_counts(i, normalize=True))

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
    

#make it readable
xx =[]
for i in pref:
    x = []
    x.append(i.to_string())
    xx.append(x)
    
    
yy =[]
for i in disp:
    y = []
    y.append(i.to_string())
    yy.append(y)

#put everything in a csv
stimulus = range(0,91) #depends on the number of stimuli (*remember: here 90 + 1 example)
preferred = [i[0].split('\n')[2:] for i in xx]
preferred = ['\n'.join(i) for i in preferred]
dispreferred = [i[0].split('\n')[2:] for i in yy]
dispreferred = ['\n'.join(i) for i in dispreferred]

d = {'stimulus': stimulus, 'preferred': preferred, 'stdp': stdp, 'dispreferred': dispreferred, 'stdd': stdd}
dd = pd.DataFrame(d)
dd.to_csv('set1_percentage.csv')

#ANNOTATIONS SET 2
for i in set2.columns:
    set2[i] = set2[i].str.lower()
    set2[i] = set2[i].str.strip()

preferred = []
dispreferred = []

preferred = []
dispreferred = []

for i in set2.columns:
    if '_1' in i:
        preferred.append(set2.value_counts(i, normalize=True))
        
for i in set2.columns:
    if '_2' in i:
        dispreferred.append(set2.value_counts(i, normalize=True))

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
    

xx =[]
for i in pref:
    x = []
    x.append(i.to_string())
    xx.append(x)

yy =[]
for i in disp:
    y = []
    y.append(i.to_string())
    yy.append(y)

stimulus = range(0,90)
preferred = [i[0].split('\n')[2:] for i in xx]
preferred = ['\n'.join(i) for i in preferred]
dispreferred = [i[0].split('\n')[2:] for i in yy]
dispreferred = ['\n'.join(i) for i in dispreferred]

d = {'stimulus': stimulus, 'preferred': preferred, 'stdp': stdp, 'dispreferred': dispreferred, 'stdd': stdd}
dd = pd.DataFrame(d)
dd.to_csv('set2_percentage.csv')
