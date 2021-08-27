Creates groups of 4 based on harcoded list of students and educators in our coderacademy group.
Optionally completes an arbitrary no. of iterations, and prints statistics (i.e. to show how evenly the randomisations were distributed)

**Instructions:**
only change:
* ITERATIONS (default = 1)
  * no. times to randomise groups
* PRINTGROUPS (default = True)
  * prints the created groups of 4 for all iterations
* PRINTSTATS (default = False)
  * prints statistics for each person showing how many times they were in the same room as others

if both PRINTGROUPS and PRINTSTATS are false, there will be no output

**Uses:**
- randomise groups for a given instance
  - leave all variables as default
- run many iterations and see statistics for how many times each person was matched with another (i.e. how well the randomisation worked)
  - change ITERATIONS to desired number, PRINTGROUPS = False, PRINTSTATS = True

For reference, 30 iterations still often results in cases where a given person is in the same room as another person 1 time
