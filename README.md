# puzzle

My wife and I stop by the "Cracker Barrel" restaurant every once in a while.  This past time I was playing with the little golf tee puzzle that was sitting on the table (as I have done in the past) and I started to think about creating a script to solve the puzzle.   Here is a little verbose, but fairly simple, solution to that problem.

I need to figure out a better way to check for valid moves.  I had to enumerate all possible moves instead of using some algorithm.

I still need to create a better move routing.  It doesn't work right now because it doesn't remove the peg you jump over.  Right now this might be another long enumerate list (which I really hate to do).