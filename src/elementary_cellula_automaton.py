import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from tqdm.auto import tqdm

class ElementaryCellularAutomaton():

    def __init__(self, resolution, init_state='Random'):

        self.resolution = resolution
        self.init_state = init_state

        return None


    def generate_all_rules(self, output_dir):

        output_dir.mkdir(parents=True, exist_ok=True)

        rules = list(range(0,256))

        for i, rule in tqdm(enumerate(rules), total=len(rules)):

            playground = self.apply_rule(rule)

            plt.imsave(output_dir / Path(f'rule_{i:03d}.png'), playground, cmap='gray_r')

        return None


    def apply_rule(self, rule):

        playground = self.init_playground()
        rule = [int(bit) for bit in format(rule, '08b')]

        for i, row in enumerate(playground[:-1]):
            playground[i+1] = self.generate_next_row(row, rule)

        return playground


    def init_playground(self):

        playground = np.zeros(self.resolution, dtype=int)

        if self.init_state == 'Random':
            playground[0] = np.random.choice([0, 1], size=self.resolution[1])
        else:
            playground[0, self.resolution[1]//2] = 1

        return playground
    

    def generate_next_row(self, row, rule):

        next_row = np.zeros_like(row)

        for i, _ in enumerate(row):

            pattern = f'{row[i-1]}{row[i]}{row[(i+1)%self.resolution[1]]}'
            next_row[i] = self.match_pattern(pattern, rule)        

        return next_row
    

    def match_pattern(self, pattern, rule):

        match pattern:
            case '111':
                return rule[0]
            case '110':
                return rule[1]
            case '101':
                return rule[2]
            case '100':
                return rule[3]
            case '011':
                return rule[4]
            case '010':
                return rule[5]
            case '001':
                return rule[6]
            case '000':
                return rule[7]
            
        return None


if __name__ == '__main__':

    print('Hello, home!')