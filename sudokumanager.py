#!/usr/bin/python

def index_grid(): 
  """
  Dummy method to generates all the possible region indexes based on lines and columns of the sudoku grid.
  """
  output = ""
  for l in range(0, 9):
    output_line = ""
    for c in range(0, 9):
      col = ((l % 3) * 3) + (c % 3)
      lin = ((l / 3) * 3 ) + (c / 3)
      output_line += '|{0:2d}, {1:2d}, {2:2d}, {3:2d}|'.format(l, c, lin, col)
    output += output_line + "\n"
  return output

def check_board(grid):
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
    line_items = [False, False, False, False, False, False, False, False, False]
    column_items = [False, False, False, False, False, False, False, False, False]
    region_items = [False, False, False, False, False, False, False, False, False]
    for c in range(0, 9):
      col = ((l % 3) * 3) + (c % 3)
      lin = ((l / 3) * 3 ) + (c / 3)

      line_item = grid[l][c]
      complete = False if line_item is 0 else complete
      if not check_item(line_item, line_items):
        correct = False
 
      column_item = grid[c][l]
      complete = False if column_item is 0 else complete
      if not check_item(column_item, column_items):
        correct = False

      region_item = grid[lin][col]
      complete = False if region_item is 0 else complete
      if not check_item(region_item, region_items):
        correct = False

  output = (1 if complete else 0, 0 if correct else 1)
  return output


def get_pivot(point):
  """Return the region pivot relative to point.
  >>> get_pivot((1, 1))
  (0, 0)
  >>> get_pivot((7, 8))
  (6, 6)
  >>> get_pivot((5, 5))
  (3, 3)
  """
  #check for invalid inputs
  pivot = (0, 0)
  pivot = ((point[0] / 3) * 3, (point[1] / 3) * 3)
  return pivot

def check_item(value, items):
  """
  Check if a value has already found in the items available.
  Valid values range from 1 to 9. 0 is a spacial case that means empty value so it is always valid.
  >>> check_item(1, [False, False, False, False, False, False, False, False, False])
  True
  >>> check_item(5, [False, False, False, False, False, False, False, False, False])
  True
  >>> check_item(1, [True, False, False, False, False, False, False, False, False])
  False
  >>> check_item(2, [False, True, False, False, False, False, False, False, False])
  False
  >>> check_item(10, [False, False, False, False, False, False, False, False, False])
  False
  >>> check_item(0, ([True] * 9))
  True
  """
  if value is 0:
    return True
  if value < 0 or value > 9:
    return False
  if (not items[value - 1]):
    items[value - 1] = True
    return True
  return False

def check_valid_move(position, grid):
  """
  Check if the position in the grid is valid.
  >>> check_valid_move((0,0), ([range(1, 10)] * 9))
  False
  """
  #grid[position[0]][position[1]] = value
  pivot = get_pivot(position)
  l = pivot[0]
  line_items = [False, False, False, False, False, False, False, False, False]
  column_items = [False, False, False, False, False, False, False, False, False]
  region_items = [False, False, False, False, False, False, False, False, False]
  for c in range(0, 9):
    col = ((l % 3) * 3) + (c % 3)
    lin = ((l / 3) * 3 ) + (c / 3)
    line_item = grid[position[0]][c]
    if not check_item(line_item, line_items):
      return False

    column_item = grid[c][position[1]]
    if not check_item(column_item, column_items):
      return False

    region_item = grid[lin][col]
    if not check_item(region_item, region_items):
      return False

  return True

if __name__ == "__main__":
  print index_grid()
  a = [[7, 2, 5, 3, 8, 6, 9, 1, 4],
    [8, 4, 3, 1, 2, 9, 7, 5, 6],
    [9, 6, 1, 5, 7, 4, 3, 8, 2],
    [4, 3, 9, 2, 5, 1, 8, 6, 7],
    [1, 7, 2, 4, 6, 8, 5, 3, 9],
    [6, 5, 8, 7, 9, 3, 2, 4, 1],
    [5, 9, 6, 8, 4, 7, 1, 2, 3],
    [3, 8, 7, 6, 1, 2, 4, 9, 5],
    [2, 1, 4, 9, 3, 5, 6, 7, 8]]
  result = check_board(a)
  print a
  print result

  a = [[7, 2, 5, 3, 8, 6, 9, 1, 4],
    [8, 4, 3, 1, 2, 9, 7, 5, 6],
    [9, 6, 0, 5, 7, 4, 3, 8, 2],
    [4, 3, 9, 2, 5, 1, 8, 6, 7],
    [1, 7, 2, 4, 6, 8, 5, 3, 9],
    [6, 5, 8, 7, 9, 3, 2, 4, 1],
    [5, 9, 6, 8, 4, 7, 1, 2, 3],
    [3, 8, 7, 6, 1, 2, 4, 9, 5],
    [2, 1, 4, 9, 3, 5, 6, 7, 8]]
  result = check_board(a)
  print a
  print result

  a = [[7, 2, 5, 3, 8, 6, 9, 1, 4],
    [8, 4, 3, 1, 2, 9, 7, 5, 6],
    [9, 6, 0, 2, 7, 4, 3, 8, 2],
    [4, 3, 9, 2, 5, 1, 8, 6, 7],
    [1, 7, 2, 4, 6, 8, 5, 3, 9],
    [6, 5, 8, 7, 9, 3, 2, 4, 1],
    [5, 9, 6, 8, 4, 7, 1, 2, 3],
    [3, 8, 7, 6, 1, 2, 4, 9, 5],
    [2, 1, 4, 9, 3, 5, 6, 7, 8]]
  result = check_board(a)
  print a
  print result

