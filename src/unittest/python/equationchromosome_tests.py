from unittest import TestCase
from equationfinder.equationchromosome import EquationChromosome

__author__ = 'ejanlav'


class TestEquationChromosome(TestCase):
    CHROMOSOME1 = '011010100101110001001101001010110001'  # 6+5*4/2-1
    CHROMOSOME2 = '011010100101110001001101001010101111'  # 6+5*4/2+NA

    def test_print_chromosome1(self):
        chromosome = EquationChromosome(self.CHROMOSOME1, 27)
        self.assertEquals("6 + 5 x 4 / 2 - 1 = 21.0", str(chromosome))

    def test_print_chromosome2(self):
        chromosome = EquationChromosome(self.CHROMOSOME2, 27)
        self.assertEquals("6 + 5 x 4 / 2 = 22.0", str(chromosome))

    def test_chromosome_fitness(self):
        chromosome = EquationChromosome(self.CHROMOSOME1, 25)
        self.assertEquals(0.25, chromosome.get_fitness())
