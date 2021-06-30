# Wuddly Machine
This code is a verification tool for the [Cuddly Duddly Fuddly Wuddly Riddle](https://www.youtube.com/watch?v=z-ZEfxAL9SI). The riddle is rephrased below:
> An incubator currently has 99 eggs: 23 blue, 33 purple, 43 red. Eggs combine in pairs until only one is left: a red and blue egg make a purple egg; a blue and purple egg make a red egg; and a purple and red egg make a blue egg. For each egg fusion, eggs from the two most plentiful piles will fuse first (in this case, a red and purple egg will combine). If the two smallest piles are equal, an egg comes from one at random. You want the final egg to be blue. _You can add exactly one blue, one purple or one red egg to the incubator._ Once you've done so, you can no longer intervene.

The question boils down to a parity operation on the number of eggs: Each egg fusion will reduce the number of eggs by 1 for two piles and increase it by 1 for the other. This switched the parity (odd or even) of the numbers, which all start as odd. Since the final state we want it (blue, purple, red) = (1,0,0) = (odd,even,even), the final egg added to the incubator should be the blue one.

# How To Use
I run this in jupyter notebook using the WuddlyMachine function.
