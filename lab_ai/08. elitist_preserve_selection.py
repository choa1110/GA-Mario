# 08. elitist_preserve_selection.py
import numpy as np
import random

relu = lambda x: np.maximum(0, x)
sigmoid = lambda x: 1.0 / (1.0 + np.exp(-x))


class Chromosome:
    def __init__(self):
        self.w1 = np.random.uniform(low=-1, high=1, size=(13 * 16, 9))
        self.b1 = np.random.uniform(low=-1, high=1, size=(9,))

        self.w2 = np.random.uniform(low=-1, high=1, size=(9, 6))
        self.b2 = np.random.uniform(low=-1, high=1, size=(6,))

        self.distance = random.randint(0, 100)
        self.max_distance = 0
        self.frames = 0
        self.stop_frames = 0
        self.win = 0

    def predict(self, data):
        l1 = relu(np.matmul(data, self.w1) + self.b1)
        output = sigmoid(np.matmul(l1, self.w2) + self.b2)
        result = (output > 0.5).astype(np.int)
        return result

    def fitness(self):
        return self.distance


def elitist_preserve_selection(chromosomes):
    sorted_chromosomes = sorted(chromosomes, key=lambda x: x.fitness(), reverse=True) #염색체들을 내림차순으로 위에서 두개 뽑는다
    return sorted_chromosomes[:2]


if __name__ == '__main__':
    chromosomes = [Chromosome() for _ in range(10)]
    selected_chromosome = elitist_preserve_selection(chromosomes)
    for chromosome in chromosomes:
        print(chromosome.fitness(), end=' ')
    print()
    print('== 선택된 염색체의 적합도 ==')
    print(selected_chromosome[0].fitness(), selected_chromosome[1].fitness())