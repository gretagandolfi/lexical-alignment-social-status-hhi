
# Norming task analysis

## Scope

This repository contains the materials needed to norm the stimuli for a picture naming-picture matching task from an input dataset provided by a Qualtrics survey we designed (click here to have a look: https://edinburgh.eu.qualtrics.com/jfe/form/SV_1Ly0H5K9fEQaf2d).

## Description

* __analyse_norming.py__ is a python script that takes as _input_ the results of the norming task in a Qualtrics format. It gives, as an _output_, 2 sets of stimuli in a .csv format (5, n of stimuli). Each stimulus is paired with the words used by the participants to describe it as a first (preferred) or second (dispreferred) choice, its relative percentage and the standard deviation between responses.  


| | preferred |	stdp | dispreferred |	std |
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
  - potential targets file containing the stimuli for which :
    * the most frequently used preferred term is above or equal to the preferred threshold
    * the most frequently used dispreferred term is the above the dispreferred threshold.
  - potential fillers file containing the stimuli for which :
    * the most frequently used preferred term is above or equal to the preferred threshold
    * the most frequently used dispreferred term is the below the dispreferred threshold.
  - others file containing the stimuli that did not satisfy the above-mentioned rules. These are the stimuli for which the distinction between first and second word choice is blurred.

To run the code, just modify this line as you need:

```
python target_and_filler_finder.py
  -ds1 path to the first file
  -ds2 path to the second file
  -cp criterion for the preferred term (decimal, e.g. 0.8)
  -cd criterion for the dispreferred term (decimal, e.g. 0.2)
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

Each set of target contains __16__ items (balanced per acceptability, frequency of use in spontaneous and non-spontaneous naming), for a total of __32__ stimuli, while the subfolder fillers contains __43__ items (used at least 80% of times in spontaneous naming and at least 20% of times in non-spontaneous naming). 

|favoured _word	| spostaneous_naming(f)	| constrained_naming(f)	| disfavoured_word |spostaneous_naming(d)	|constrained_naming(d)|	acceptability(d)|
| --- | --- | --- |  --- | --- | --- | --- |
|snake 	|100%	|0%	|serpent	|0%	|28%	|6,12|
|washin machine  |96%	|0%	|clothes washer	|2%	|36%	|6,14|
|heart 	|100%	|0%	|organ	|0%	|36%	|6,25|
|pear 	|98%	|0%	|fruit	|0%	|50%	|6,29|
|eye 	|98%	|0%	|eyeball	|0%	|20%	|6,35|
|church 	|98%	|0%	|chapel	|0%	|26%	|6,45|
|frog 	|100%	|0%	|toad	|0%	|50%	|6,53|
|car 	|100%	|0%	|vehicle	|0%	|40%	|6,67|
|beard 	|100%	|0%	|facial hair	|0%	|58%	|6,71|
|neck 	|90%	|2%	|throat	|2%	|22%	|6,14|
|pen 	|94%	|2%	|biro	|2%	|22%	|6,37|
|bone 	|92%	|2%	|dog treat	|2%	|24%	|6,43|
|fist 	|98%	|2%	|hand	|2%	|50%	|6,51|
|chair 	|98%	|2%	|seat	|2%	|56%	|6,67|
|fridge 	|88%	|2%	|refrigerator	|4%	|32%	|6,88|
|sweet 	|84%	|4%	|candy	|4%	|50%	|6,18|
|lipstick	|100%	|0%	|makeup	|0%	|26%	|6,14|
|potato	|86%	|2%	|spud	|0%	|32%	|6,18|
|bomb	|100%	|0%	|explosive	|0%	|44%	|6,29|
|arm	|82%	|10%	|limb	|0%	|24%	|6,33|
|rose	|100%	|0%	|flower	|0%	|64%	|6,42|
|bath	|84%	|4%	|tub	|0%	|50%	|6,47|
|glasses	|98%	|0%	|spectacles	|0%	|36%	|6,67|
|toilet	|96%	|4%	|loo	|0%	|46%	|6,67|
|laptop	|98%	|2%	|computer	|2%	|60%	|6,1|
|screwdriver	|82%	|0%	|tool	|2%	|56%	|6,18|
|tooth	|96%	|2%	|molar	|2%	|32%	|6,37|
|bread	|86%	|6%	|loaf	|2%	|46%	|6,49|
|umbrella	|98%	|2%	|brolly	|2%	|28%	|6,59|
|fire	|98%	|2%	|flame	|4%	|32%	|6,69|
|chicken	|96%	|4%	|hen	|4%	|30%	|6,12|
|tie	|96%	|0%	|neck tie	|4%	|20%	|6,29|
						
