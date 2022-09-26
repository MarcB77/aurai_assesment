# Secondary mushroom data

## Sources:
1. Mushroom species drawn from source book: Patrick Hardin.Mushrooms & Toadstools. Zondervan, 1999
2. Inspired by [this mushroom data](https://archive.ics.uci.edu/ml/datasets/Mushroom): Jeff Schlimmer.Mushroom Data Set. Apr. 1987.
3. [Repository](https://mushroom.mathematik.uni-marburg.de/files/) containing the related Python scripts and all the data sets. 
4. Author: Dennis Wagner
5. Date: 05 September 2020

## Relevant information:
This dataset includes 61069 hypothetical mushrooms with caps based on 173 species (353 mushrooms per species). Each mushroom is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended (the latter class was combined with the poisonous class). Of the 20 variables, 17 are nominal and 3 are metrical.

## Data simulation:
The related Python project (Sources 3) contains a Python module *secondary_data_generation.py* used to generate this data based on *primary_data_edited.csv* also found in the repository. Both nominal and metrical variables are a result of randomization. The simulated and ordered by species version is found in *secondary_data_generated.csv*. The randomly shuffled version is found in *secondary_data_shuffled.csv.*

## Class information:
1. *class (binary)*: 
	- poisonous=p
	- edibile=e

## Variable Information:

### Variable Types
- n: nominal (as sets of values)
- m: metrical

### Variables
1. *cap-diameter (m)*: float number in cm
2. *cap-shape (n)*:
   - bell=b
   - conical=c
   - convex=x
   - flat=f
   - sunken=s
   - spherical=p
   - others=o
3. *cap-surface (n)*:
	- fibrous=i
	- grooves=g
	- scaly=y
	- smooth=s
	- shiny=h
	- leathery=l
	- silky=k
	- sticky=t
	- wrinkled=w
	- fleshy=e
4. *cap-color (n)*:
	- brown=n
	- buff=b
	- gray=g
	- green=r
	- pink=p
	- purple=u
	- red=e
	- white=w
	- yellow=y
	- blue=l
	- orange=o
	- black=k
5. *does-bruise-bleed (n)*:
	- bruises-or-bleeding=t
	- no=f
6. *gill-attachment (n)*:
	- adnate=a
	- adnexed=x
	- decurrent=d
	- free=e
	- sinuate=s
	- pores=p
	- none=f
	- unknown=?
7. *gill-spacing (n)*:
	- close=c
	- distant=d
	- none=f
8. *gill-color (n)*:
	- brown=n
	- buff=b
	- gray=g
	- green=r
	- pink=p
	- purple=u
	- red=e
	- white=w
	- yellow=y
	- blue=l
	- orange=o
	- black=k
	- none=f
9. *stem-height (m)*: float number in cm
10. *stem-width (m)*:float number in mm   
11. *stem-root (n)*:
	- bulbous=b
	- swollen=s
	- club=c
	- cup=u
	- equal=e
	- rhizomorphs=z
	- rooted=r
12. *stem-surface (n)*:
	- fibrous=i
	- grooves=g
	- scaly=y
	- smooth=s
	- shiny=h
	- leathery=l
	- silky=k
	- sticky=t
	- wrinkled=w
	- fleshy=e
	- none=f
13. *stem-color (n)*:
	- brown=n
	- buff=b
	- gray=g
	- green=r
	- pink=p
	- purple=u
	- red=e
	- white=w
	- yellow=y
	- blue=l
	- orange=o
	- black=k
	- none=f
14. *veil-type (n)*:
	- partial=p
	- universal=u
16. *veil-color (n)*:
	- brown=n
	- buff=b
	- gray=g
	- green=r
	- pink=p
	- purple=u
	- red=e
	- white=w
	- yellow=y
	- blue=l
	- orange=o
	- black=k
	- none=f
17. *has-ring (n)*:
	- ring=t
	- none=f
19. *ring-type (n)*:
	- cobwebby=c
	- evanescent=e
	- flaring=r
	- grooved=g
	- large=l
	- pendant=p
	- sheathing=s
	- zone=z
	- scaly=y
	- movable=m
	- none=f
	- unknown=?
20. *spore-print-color (n)*:
	- brown=n
	- buff=b
	- gray=g
	- green=r
	- pink=p
	- purple=u
	- red=e
	- white=w
	- yellow=y
	- blue=l
	- orange=o
	- black=k
21. *habitat (n)*:
	- grasses=g
	- leaves=l
	- meadows=m
	- paths=p
	- heaths=h
	- urban=u
	- waste=w
	- woods=d
22. *season (n)*:
	- spring=s
	- summer=u
	- autumn=a
	- winter=w