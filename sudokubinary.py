#!/usr/bin/python

def empty_grid():
    """
    Generates a empty (all zeroed) grid.
    >>> empty_grid()[0][0]
    [False, False, False, False, False, False, False, False, False]
    """
    #Doing this to avoid same instance referenced in every position as [[[False] * 9] * 9] * 9
    grid = []
    for l in range(0, 9):
        line = []
        for c in range(0, 9):
            row = [False] * 9
            line.append(row)
        grid.append(line)
    return grid

def to_binary_grid(num_grid):
    """
    Converts from decimal grid to binary array grid.
    >>> to_binary_grid([0] * 9] * 9)[0][0]
    [False, False, False, False, False, False, False, False, False]
    """
    bin_grid = empty_grid()
    for l in range(0, 9):
        for c in range(0, 9):
            if num_grid[l][c] > 0:
                bin_grid[l][c][num_grid[l][c]-1] = True
    return bin_grid

def get_pivot(point):
    """
    Return the region pivot relative to point.
    >>> get_pivot((1, 1))
    (0, 0)
    """
    pivot = ((point[0] / 3) * 3, (point[1] / 3) * 3)
    return pivot

def check_item(value, items):
    """
    Check if a value has already found in the items available.
    Valid values range from 1 to 9. 0 is a special case which means empty value so it is always valid.
    """
    if value is 0:
        return True
    if value < 0 or value > 9:
        return False
    if (not items[value - 1]):
        items[value - 1] = True
        return True
    return False

def remove_item_not_zero(item, item_list):
    """
    Checks and removes item from list if item is not zero.
    """
    if item > 0 and item <= 9:
        item_list[item - 1] = False
    return item_list
    
def get_decimal_value(position, grid):
    """
    Converts binary array value in binary grid to decimal value.
    """
    l = position[0]
    c = position[1]
    bin_arr = grid[l][c]
    if not bin_arr.__contains__(True):
        return 0
    return bin_arr.index(True) + 1

def __get_decimal_grid__(grid):
    """
    Converts binary grid to decimal grid
    """
    dec_grid = []
    for l in range(0, 9):
        lin = []
        for c in range(0, 9):
            lin.append(get_decimal_value((l, c), grid))
        dec_grid.append(lin)
    return dec_grid


def get_binary_array(value):
    """
    Convert decimal value to binary array.
    """
    arr = [False] * 9
    if value > 0 and value <= 9:
        arr[value - 1] = True
    return arr

def check_values_played(position, grid):
    """
    Build a list of values already played for position.
    """
    pivot = get_pivot(position)
    found_items = [False] * 9
    
    l = pivot[0]
    for c in range(0, 9):
        #col = ((l % 3) * 3) + (c % 3)
        #lin = ((l / 3) * 3) + (c / 3)
        col = (c % 3)
        lin = (c / 3)
        
        line_item = grid[position[0]][c]
        column_item = grid[c][position[1]]
        region_item = grid[lin + pivot[0]][col + pivot[1]]
        found_items = [ a or b or c or d for a, b, c, d in zip(line_item, column_item, region_item, found_items)]
        
    return found_items

def __is_item_set__(item):
    for i in range(0,9):
        if item[i] is True:
            return True
    return False

def check_win(grid):
  """
  Check if the board is complete and if it was a win or failute.
  Response:
  (0, 0) => incomplete, possible.
  (1, 0) => complete, correct.
  (x, 1) => incorrect.
  """
  output = (1, 0)
  correct = True
  complete = True
  for l in range(0, 9):
    for c in range(0, 9):
      col = ((l % 3) * 3) + (c % 3)
      lin = ((l / 3) * 3 ) + (c / 3)

      line_items = [False, False, False, False, False, False, False, False, False]
      column_items = [False, False, False, False, False, False, False, False, False]
      region_items = [False, False, False, False, False, False, False, False, False]

      for ind in range(0, 9):
        #print 'line l=', l, 'c=', c, 'ind=', ind
        #TODO: move this to a distinct function
        if grid[l][c][ind] is True and line_items[ind] is True:
            return (0, 1)
        elif line_items[ind] is False:
            line_items[ind] = True
        
        if grid[c][l][ind] is True and column_items[ind] is True:
            return (0, 1)
        elif column_items[ind] is False:
            column_items[ind] = True

        if grid[lin][col][ind] is True and region_items[ind] is True:
            return (0, 1)
        elif region_items[ind] is False:
            region_items[ind] = True
        
        if complete is True:
            if __is_item_set__(grid[l][c]) is False or __is_item_set__(grid[c][l]) is False or __is_item_set__(grid[lin][col]) is False:
                #print 'incomplete l=', l, 'c=', c, 'ind=', ind
                #print 'grid[l][c][ind]', grid[l][c][ind]
                #print 'grid[c][l][ind]', grid[c][l][ind]
                #print 'grid[lin][col][ind]', grid[lin][col][ind]
                complete = False

  output = (1 if complete else 0, 0)
  return output
    
def post_value(value, position, grid):
    """
    Insert  value into grid if valid. Returns True if the move was successfull or False otherwise.
    It is allways possible to play value equals 0 (ZERO) since it means clean the value in the position.
    """
    l = position[0]
    c = position[1]
    if value == 0:
        grid[l][c] = [False] * 9
        return True
    played = check_values_played(position, grid)
    if not played[value - 1]:
        value_array = get_binary_array(value)
        grid[l][c] = value_array
        return True
    return False

def find_empty_position(grid):
    """
    Returns an empty (unplayed/zeroed) position in the grid. Returns False if there is no empty position.
    """
    zero = [False] * 9
    for l in range(0, 9):
        for c in range(0, 9):
            if grid[l][c] == zero:
                return (l, c)
    return False

def deep_clone(grid):
    """
    Deep clones grid.
    """
    clone = list(list(list(val) for val in line) for line in grid)
    return clone

def next_steps(step):
    """
    Returns a list of the next possible steps based on the current step.
    """
    steps = []
    grid = step.grid
    position = find_empty_position(grid)
    if position is not False:
        played_values = check_values_played(position, grid)
        print 'played:', played_values
        for value in range(1, 10):
            if not played_values[value - 1]:
                grid_clone = deep_clone(grid)
                if post_value(value, position, grid):
                    steps.append(Step(grid, step.distance + 1))
    return steps

def append_steps(steps, step_list):
    if steps is not None and steps.__len__() > 0:
        for step in steps:
            if not step_list.__contains__(step):
                step_list.append(step)
        step_list.sort()

class Step:
    """
    Defines each step in the process of finding the solution for sudoku game.
    grid holds the state of the sudoku board for this iteration.
    distance holds the numeric distance between this step and initial board.
    """
    
    def __init__(self, grid, distance):
        self.grid = grid
        self.distance = distance
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.grid == other.grid
        return NotImplemented
        
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented
    
    def __hash__(self):
        return hash(''.join(str(e) for e in self.grid))

    def cmp(a, b):
        if a.distance > b.distance:
            return -1
        elif a.distance == b.distance:
            return 0
        else:
            return 1

class Solver:
    """
    Solves a sudoku game.
    """

    def __init__(self, grid):
        step = Step(grid, 0)
        self.to_visit = [step]
        self.visited = []

    def iterate_step(self):
        if self.to_visit.__len__() == 0:
            #Unsolvable
            return 0
        current = self.to_visit.pop()
        curr_result = check_win(current.grid)
        if curr_result == (1,0):
            return current
        if curr_result == (0, 0):
            n_steps = next_steps(current)
            append_steps(n_steps, self.to_visit)
        return None

    def solve(self):
        while self.to_visit.__len__() > 0:
            response = self.iterate_step()
            if response == 0:
                print "There is no solution for this game."
                return 0
            if response is not None:
                print "Solution found"
                return response




