#!/usr/bin/python

import unittest2 as unittest
import sudokubinary as sb


class SudokumamagerTestCase(unittest.TestCase):

    def test_check_cloned_grid(self):
        grid = sb.empty_grid()
        grid[0][0][0] = True
        self.assertFalse(grid[0][0][0] == grid[0][1][0])

    def test_get_decimal_grid_round_trip(self):
        grid = sb.empty_grid()
        grid[0][0] = [True, False, False, False, False, False, False, False, False]
        dec_grid = sb.__get_decimal_grid__(grid)
        
        self.assertEquals(dec_grid[0][0], 1)
        self.assertEquals(dec_grid[0][1], 0)


    def test_check_values_played(self):
      a = [[7, 2, 5, 3, 8, 6, 9, 1, 0],
        [8, 4, 3, 1, 2, 9, 7, 5, 6],
        [9, 6, 1, 5, 7, 4, 3, 8, 2],
        [4, 3, 9, 2, 5, 1, 8, 6, 7],
        [1, 7, 2, 4, 6, 8, 5, 3, 9],
        [6, 5, 8, 7, 9, 3, 2, 4, 1],
        [5, 9, 6, 8, 4, 7, 1, 2, 3],
        [3, 8, 7, 6, 1, 2, 4, 9, 5],
        [2, 1, 4, 9, 3, 5, 6, 7, 8]]

      bin_a = sb.to_binary_grid(a)
      played = sb.check_values_played((0,8), bin_a)
      self.assertEquals(played, [True, True, True, False, True, True, True, True, True])


    def test_check_values_played_none_found(self):
      a = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

      bin_a = sb.to_binary_grid(a)
      played = sb.check_values_played((0,0), bin_a)
      self.assertEquals(played, [False, False, False, False, False, False, False, False, False])

    def test_to_binary_grid(self):
      a = [[7, 2, 5, 3, 8, 6, 9, 1, 4],
        [8, 4, 3, 1, 2, 9, 7, 5, 6],
        [9, 6, 1, 5, 7, 4, 3, 8, 2],
        [4, 3, 9, 2, 5, 1, 8, 6, 7],
        [1, 7, 2, 4, 6, 8, 5, 3, 9],
        [6, 5, 8, 7, 9, 3, 2, 4, 1],
        [5, 9, 6, 8, 4, 7, 1, 2, 3],
        [3, 8, 7, 6, 1, 2, 4, 9, 5],
        [2, 1, 4, 9, 3, 5, 6, 7, 8]]
      bin_a = sb.to_binary_grid(a)
      #print bin_a
      self.assertEquals(bin_a[0][0], [False, False, False, False, False, False, True, False, False])

    def test_check_win_valid_grid(self):
      a = [[7, 2, 5, 3, 8, 6, 9, 1, 4],
        [8, 4, 3, 1, 2, 9, 7, 5, 6],
        [9, 6, 1, 5, 7, 4, 3, 8, 2],
        [4, 3, 9, 2, 5, 1, 8, 6, 7],
        [1, 7, 2, 4, 6, 8, 5, 3, 9],
        [6, 5, 8, 7, 9, 3, 2, 4, 1],
        [5, 9, 6, 8, 4, 7, 1, 2, 3],
        [3, 8, 7, 6, 1, 2, 4, 9, 5],
        [2, 1, 4, 9, 3, 5, 6, 7, 8]]
      bin_a = sb.to_binary_grid(a)
      solution = sb.check_win(bin_a)
      self.assertEquals((1, 0), solution)

    def test_check_win_incomplete_grid(self):
      a = [[7, 2, 5, 3, 8, 6, 9, 1, 0],
        [8, 4, 3, 1, 2, 9, 7, 5, 6],
        [9, 6, 1, 5, 7, 4, 3, 8, 2],
        [4, 3, 9, 2, 5, 1, 8, 6, 7],
        [1, 7, 2, 4, 6, 8, 5, 3, 9],
        [6, 5, 8, 7, 9, 3, 2, 4, 1],
        [5, 9, 6, 8, 4, 7, 1, 2, 3],
        [3, 8, 7, 6, 1, 2, 4, 9, 5],
        [2, 1, 4, 9, 3, 5, 6, 7, 8]]
      bin_a = sb.to_binary_grid(a)
      solution = sb.check_win(bin_a)
      self.assertEquals((0, 0), solution)


    def test_check_next_step_not_possible(self):
      a = [[7, 2, 5, 3, 8, 6, 9, 1, 4],
        [8, 4, 3, 1, 2, 9, 7, 5, 6],
        [9, 6, 1, 5, 7, 4, 3, 8, 2],
        [4, 3, 9, 2, 5, 1, 8, 6, 7],
        [1, 7, 2, 4, 6, 8, 5, 3, 9],
        [6, 5, 8, 7, 9, 3, 2, 4, 1],
        [5, 9, 6, 8, 4, 7, 1, 2, 3],
        [3, 8, 7, 6, 1, 2, 4, 9, 5],
        [2, 1, 4, 9, 3, 5, 6, 7, 8]]

      bin_a = sb.to_binary_grid(a)
      curr = sb.Step(bin_a, 0)
      ns = sb.next_steps(curr)
      #print ns
      self.assertTrue(ns == [])

    def test_check_next_step_one_possible(self):
      a = [[7, 2, 5, 3, 8, 6, 9, 1, 0],
        [8, 4, 3, 1, 2, 9, 7, 5, 6],
        [9, 6, 1, 5, 7, 4, 3, 8, 2],
        [4, 3, 9, 2, 5, 1, 8, 6, 7],
        [1, 7, 2, 4, 6, 8, 5, 3, 9],
        [6, 5, 8, 7, 9, 3, 2, 4, 1],
        [5, 9, 6, 8, 4, 7, 1, 2, 3],
        [3, 8, 7, 6, 1, 2, 4, 9, 5],
        [2, 1, 4, 9, 3, 5, 6, 7, 8]]

      bin_a = sb.to_binary_grid(a)
      curr = sb.Step(bin_a, 0)
      ns = sb.next_steps(curr)
      # print ns
      # for st in ns:
      #     print "======="
      #     print sb.__get_decimal_grid__(st.grid)
      self.assertTrue(ns[0].grid[0][8] == sb.get_binary_array(4))

    def test_solve_final_valid_grid(self):
      a = [[7, 2, 5, 3, 8, 6, 9, 1, 4],
        [8, 4, 3, 1, 2, 9, 7, 5, 6],
        [9, 6, 1, 5, 7, 4, 3, 8, 2],
        [4, 3, 9, 2, 5, 1, 8, 6, 7],
        [1, 7, 2, 4, 6, 8, 5, 3, 9],
        [6, 5, 8, 7, 9, 3, 2, 4, 1],
        [5, 9, 6, 8, 4, 7, 1, 2, 3],
        [3, 8, 7, 6, 1, 2, 4, 9, 5],
        [2, 1, 4, 9, 3, 5, 6, 7, 8]]

      bin_a = sb.to_binary_grid(a)
      solver = sb.Solver(bin_a)
      solution = solver.solve()
      print "Solution: ", solution
      print sb.__get_decimal_grid__(solution.grid)
      self.assertTrue(solution.grid[0][8] == sb.get_binary_array(4))


    def test_solve_final_one_setep_grid(self):
      a = [[7, 2, 5, 3, 8, 6, 9, 1, 0],
        [8, 4, 3, 1, 2, 9, 7, 5, 6],
        [9, 6, 1, 5, 7, 4, 3, 8, 2],
        [4, 3, 9, 2, 5, 1, 8, 6, 7],
        [1, 7, 2, 4, 6, 8, 5, 3, 9],
        [6, 5, 8, 7, 9, 3, 2, 4, 1],
        [5, 9, 6, 8, 4, 7, 1, 2, 3],
        [3, 8, 7, 6, 1, 2, 4, 9, 5],
        [2, 1, 4, 9, 3, 5, 6, 7, 8]]

      bin_a = sb.to_binary_grid(a)
      solver = sb.Solver(bin_a)
      solution = solver.solve()
      print "Solution: ", solution
      print sb.__get_decimal_grid__(solution.grid)
      self.assertTrue(solution.grid[0][8] == sb.get_binary_array(4))

if __name__ == '__main__':
    unittest.main()
