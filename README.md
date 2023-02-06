# Intransitive Dice

## Description

This repository demonstrates some cool properties of [intransitive dice](https://en.wikipedia.org/wiki/Intransitive_dice), which are dice wherein each die in a set beats the next in line in a loop.  This repository at the moment contains two such strategies.  The first is a modified form of Efron's dice, wherein die 0 beats die 1 with 2/3 probability, same for 1 beating 2, 2 beating 3, and 3 beating 0.  A second, more straightforward infinite-player strategy with 5/9 probability to beat the next was invented by yours truly.

This repo also contains one comparison function and one function to compare all dice in rotation, as documented.

## Efron's Dice

Efron created the following dice list:

 1. (6, 6, 2, 2, 2, 2)
 2. (5, 5, 5, 1, 1, 1)
 3. (4, 4, 4, 4, 0, 0)
 4. (3, 3, 3, 3, 3, 3)

Which can be demonstrated to be a more specific case (n=4) of some n dice which each beats the next 2/3 of the time. By splitting the final die into two dice, we get the insertion of a penultimate die with some arbitrarily small adjustment ε value:

 1. (6, 6, 2, 2, 2, 2)
 2. (5, 5, 5, 1, 1, 1)
 3. (4, 4, 4, 4, 0, 0)
 4. (3+ε, 3+ε, 3+ε, 3+ε, 3-ε, 3-ε)
 5. (3, 3, 3, 3, 3, 3)

Thus 5 and 1 are unchanged, so have the same win ratio. The relation between 3 and 4 is the same as the relationship between what is now 3 and 5, so result in the same 2/3 win for 3. and 4 beats 5 with 2/3s ratio.  The only trick is now to adjust the values such that `ε` can be inflated to a whole integer value. Hence, all values greater than the split die value are incremented by 2 and the list becomes:

 1. (8, 8, 2, 2, 2, 2)
 2. (7, 7, 7, 1, 1, 1)
 3. (6, 6, 6, 6, 0, 0)
 4. (5, 5, 5, 5, 3, 3)
 5. (4, 4, 4, 4, 4, 4)

This process can be repeated an infinite number of times, resulting in dice with faces:

 - 3 "turnaround dice", for `i`-th dice (starting index at 1), with the following faces:
   - `i+1` faces of `2*n-1-i`
   - `5-i` faces of `3-i`
 - `n-3` "split dice" where the `i`-th dice (starting index at 4; continuing the index from the previous dice) has faces:
   - `2` faces of `i-1`
   - `4` faces of `2*n-i-1`

These dice are so named because the 'split dice' is a potentially infinitely long list of dice where each die beats the next, and this is nested within a set of 3 dice that serve as almost like a turnaround such that the bottom of the list of split dice can wrap around to beat the top one once more.

One can see that when `n=4`, the 4th dice has 2 faces of `4-1 = 3` and 4 faces of `8-5 = 3`, hence it is a die of all 3s. This is true for the final die since the face `i-1` is equal to `2*n-(i+1)` when `i` equals `n`. 

## Multiplayer Dice

Multiplayer dice are dice which reduce the efficiency from the Infinite Efron series of 6/9 to 5/9 and can only be generated for odd n. However, they are a more straightforward way to generate dice where every i-th die beats the next `n//3` dice, with wrap around, where each die is uniquely numbered with all equal numbers. Also this generates only 3 numbers for the dice, so these can be simply doubled for writing on 6-sided dice. An example is:

 - (7, 11, 15)
 - (6, 10, 17)
 - (5, 9, 19)
 - (4, 8, 21)
 - (3, 14, 16)
 - (2, 13, 18)
 - (1, 12, 20)

Notice that the first column is all the numbers from 1 to n, the second n+1 to 2n, and the third is 2n+1 to 3n.  These three columns represent the low, medium, and high values for each die.  Each die beats the one below it 

This works because every die beats the next n//2 (three, in this case) dice on two each of the low, medium, and high values. Therefore 2/3s of cases are just decided by a low vs medium vs high roll. However, on the remaining 1/3 of cases, 2/3 of them are decided in this fashion.  Hence, the winning bias is 5/9 under this system.


















