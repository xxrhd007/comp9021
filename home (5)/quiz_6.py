# Written by *** for COMP9021
#
# Randomly generates a grid with 0s and 1s, whose dimension is controlled
# by user input, as well as the density of 1s in the grid, and finds out,
# for given step_number >= 1 and step_size >= 2, the number of stairs of
# step_number many steps, with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest
# step sizes, and for a given step size, from stairs with the smallest number
# of steps to stairs with the largest number of stairs.


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


def stairs_in_grid():
    stairs = {}
    for step_size in range(2, int((dim + 1) / 2) + 1):         
        stairs_of_one_size = stairs_in_size(step_size)
        
        stairs_and_steps = defaultdict(int)
        for k in stairs_of_one_size: 
            stairs_and_steps[k] += 1
        
        if len(sorted(stairs_and_steps.items())) != 0:
            stairs[step_size] = sorted(stairs_and_steps.items())  
    return(stairs)
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
def stairs_in_size(step_size):
    
    stairs_of_one_size = []         
   
    for i_start in range(0, int(dim - step_size + 1)):  
        for j_start in range(0, int(dim - (step_size * 2) + 2)):  
           
            i = i_start
            j = j_start
            have_step = True
            nb_of_step = 0               
            for j in range (j, j + step_size):   
                if grid[i][j] == 0:
                    break                           
            else:                     
                while (i <= dim - step_size and j <= dim - step_size):
                    for i in range (i + 1, i + step_size):         
                        if grid[i][j] == 0:
                            have_step = False
                    for j in range(j + 1, j + step_size):
                        if grid[i][j] == 0:
                            have_step = False
                    if have_step and grid[i][j] != -step_size:
                        nb_of_step += 1
                        grid[i][j] = - step_size
                    else:
                        break
                if nb_of_step !=0:
                    # print(f'for step_size{step_size}, there is a {nb_of_step} stair')
                    stairs_of_one_size.append(nb_of_step)
                    # stairs.uptate({step_size: [(nb_of_step, 1)]})
    return(stairs_of_one_size)

try:
    arg_for_seed, density, dim = (int(x) for x in 
                        input('Enter three positive integers: ').split()
                                 )
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()


    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS

# A dictionary whose keys are step sizes, and whose values are pairs
# of the form (number_of_steps,
#              number_of_stairs_with_that_number_of_steps_of_that_step_size
#             ),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print('    ', nb_of_stairs, stair_or_stairs, 'with',
              nb_of_steps, step_or_steps
             )
