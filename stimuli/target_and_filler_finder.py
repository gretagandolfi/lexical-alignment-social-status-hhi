import pandas as pd
import re
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-ds1", "--firstcsv", required=True,
   help="first set of data")
ap.add_argument("-ds2", "--secondcsv", required=True,
   help="second set of data")
ap.add_argument("-cp", "--criteria_p", required=True,
   help="Preferred percentage")
ap.add_argument("-cd", "--criteria_d", required=True,
   help="Dispreferred percentage")
args = vars(ap.parse_args())

#arguments that need to be passed by the user
path_to_csv1 = args['firstcsv']
path_to_csv2 = args['secondcsv']
criteria_p = args['criteria_p']
criteria_d = args['criteria_d']


#reading data
data1 = pd.read_csv(path_to_csv1)
data2 = pd.read_csv(path_to_csv2)
data = data1.append(data2,ignore_index = True) #put together the two set of stimuli
dataT = data.transpose()


#filter with the rule
preferred_t = []
dispreferred_t = []
preferred_f = []
dispreferred_f = []
preferred_o = []
dispreferred_o = []
for i in dataT:
    pre = dataT[i]['preferred'].splitlines()[0].split()
    dis = dataT[i]['dispreferred'].splitlines()[0].split()
    if float(pre[len(pre)-1]) >= float(criteria_p) and float(dis[len(dis)-1]) >= float(criteria_d):
            preferred_t.append(' '.join(pre))
            dispreferred_t.append(' '.join(dis))
    elif float(pre[len(pre)-1]) >= float(criteria_p) and float(dis[len(dis)-1]) < float(criteria_d):
        preferred_f.append(' '.join(pre))
        dispreferred_f.append(' '.join(dis))
    else:
        preferred_o.append(' '.join(pre))
        dispreferred_o.append(' '.join(dis))

#make dataframes
target_csv = {'preferred':preferred_t,'dispreferred':dispreferred_t}
target_csv = pd.DataFrame(target_csv)
target_csv = target_csv.drop_duplicates()
filler_csv = {'preferred':preferred_f,'dispreferred':dispreferred_f}
filler_csv = pd.DataFrame(filler_csv)
filler_csv = filler_csv.drop_duplicates()
other_csv = {'preferred':preferred_o,'dispreferred':dispreferred_o}
other_csv = pd.DataFrame(other_csv)
other_csv = other_csv.drop_duplicates()

#save dataframes 
target_csv.to_csv('target.csv')
filler_csv.to_csv('filler.csv')
other_csv.to_csv('other.csv')
