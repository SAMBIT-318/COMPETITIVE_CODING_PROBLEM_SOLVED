class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        m = 4 * n

        step_lengths = [m - 1]
        for i in range(2, m, 2):
            step_lengths.extend([m - i, m - i])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dir_idx = 0

        r, c = 0, 0
        coil1 = [1] 
        for length in step_lengths:
            dr, dc = directions[dir_idx]
            for _ in range(length):
                r += dr
                c += dc
                coil1.append(r * m + c + 1) 

            dir_idx = (dir_idx + 1) % 4

        max_val_plus_one = m * m + 1
        coil2 = [max_val_plus_one - x for x in coil1]

        return [coil1, coil2]