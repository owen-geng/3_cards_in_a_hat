Quick script to explain the thought puzzle on conditional probability:

There are 3 cards put into a hat. One card has 2 red faces, one card has 2 blue faces, one card has a red face and a blue face.

You draw a card randomly from the hat, and you see one face is red. What is the probability the other face is also red?

Output:
Number of times the other face was red: 33421
Number of times the other face was blue: 16560
Total number of times the seen face is red: 49981
Probability of unseen face being red: 0.6686740961565395

(No fixed seed, may be slight deviations)
================================================================================================================================

Explaination:

There are 6 "configurations" of what you can draw. They are as follows:
Draw card Blue, Blue, side facing you is Blue (face 1)
Draw card Blue, Blue, side facing you is Blue (face 2)
Draw card Red, Red, side facing you is Red (face 1)
Draw card Red, Red, side facing you is Red (face 2)
Draw card Red, Blue, side facing you is Blue (face 1)
Draw card Red, Blue, side facing you is Red (face 2)

So, given that the side facing you is Red, we can eliminate 3 of the possible "configurations", so what remains are:

Draw card Red, Red, side facing you is Red (face 1)
Draw card Red, Red, side facing you is Red (face 2)
Draw card Red, Blue, side facing you is Red (face 2)

So there is a 2/3 probability the other side is red, and a 1/3 probability the other side is blue.

Conditional probability can sometimes be highly unintuitive. Fundamentally, we are more likely to see a red face by
drawing the red + red card than the red + blue card. Therefore, given we see a red face, the red + red card is more probable.

===============================================================================================================================

Other common manifestations of this problem:

https://medium.com/@pbercker/probability-of-having-two-boys-a-conditional-probability-puzzle-b4651638c2fe
https://lweb.cfa.harvard.edu/~pzoogman/files/Bayes2.pdf
https://statmodeling.stat.columbia.edu/2010/05/27/hype_about_cond/
