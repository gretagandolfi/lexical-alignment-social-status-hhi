
# Norming task analysis

## Scope

This repository contains the materials needed to norm the stimuli for a picture naming-picture matching task.

## Description

* __analyse_norming.py__ is a python script that takes as _input_ the results of the norming task in a Qualtrics format. It gives, as an _output_, 2 sets of stimuli in a .csv format (5, n of stimuli). Each stimulus is paired with the words used by the participants to describe it as a first (preferred) or second (dispreferred) choice, its relative percentage and the standard deviation between responses.  


| | preferred |	stdp | dispreferred |	stdd |
| --- | --- | --- | --- | --- |
| 0	| pineapple  0.94 <br/> pinapple 0.04 <br/> pineappe  0.02 |	0.525	| tropical fruit 0.52 <br/> fruit 0.24 <br/> spiky fruit 0.06 <br/> ananas 0.04 <br/> spikey tree 0.02 <br/> spikey apple 0.02 <br/> spikey 0.02 <br/> sour melon 0.02 <br/> green and yellow fruit 0.02 <br/> anannus 0.02 <br/> acidic fruit 0.02 | 0.156 |


To run the code, just modify this line as you need:

```
python analyse_norming.py -p path to the Qualtrics file you want to analyse
```
For help run:

```
python analyse_norming.py -h
```

Occasionally, depending on your needs (the number of stimuli you tested and the number of questions related to participants identity you asked), you will need to modify the script. To help you with this, the lines of code that you are supposed to modify are commented (_#MODIFY_).

* __target_and_filler_finder.py__ is a python script that takes as _input_ the files obtained by analyse_norming.py and two thresholds (one for the preferred terms and one for the dispreferred terms). It gives, as _output_, three .csv files:
  - potential fillers file containing the stimuli for which :
    * the most frequently used preferred term is above or equal to the preferred threshold
    * the most frequently used dispreferred term is the above the dispreferred threshold.
  - potential targets file containing the stimuli for which :
    * the most frequently used preferred term is above or equal to the preferred threshold
    * the most frequently used dispreferred term is the below the dispreferred threshold.
  - others file containing the stimuli that did not satisfy the above-mentioned rules. These are the stimuli for which the distinction between first and second word choice is blurred.

To run the code, just modify this line as you need:

```
python target_and_filler_finder.py
  -ds1 path to the first file
  -ds2 path to the second file
  -cp criterion for the preferred term (decimal, e.g. 0.7)
  -cd criterion for the dispreferred term (decimal, e.g. 0.4)
```

For help run:

```
python target_and_filler_finder.py -h
```
### Examples

Here some examples of:

* a filler stimulus

| | preferred	| dispreferred |
| --- | --- | --- |
| 2	| bed 1.0 | mattress 0.12 |

* a target stimulus

| | preferred	| dispreferred |
| --- | --- | --- |
| 4	| mug 0.88 |	cup 0.70 |

* other

| | preferred	| dispreferred |
| --- | --- | --- |
| 10| lightbulb 0.44 | light 0.32 |

# Stimuli
_stimuli.zip_ is a compressed folder containing the __stimuli__ for the experiment. 

In each sub-folder (fillers, targets/set1, targets/set2), you’ll find the list of items’ names (.txt file) and the items’ pictures (.jpg files).

Each set of target contains __15__ items (balanced per acceptability, frequency of use in spontaneous and non-spontaneous naming), for a total of __30__ stimuli, while the subfolder fillers contains __43__ items (used at least 80% of times in spontaneous naming and at most 20% of times in non-spontaneous naming). 
