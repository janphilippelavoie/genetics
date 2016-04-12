import random
from equationfinder.equationchromosome import EquationChromosome
from genetics.chromosome_factory import ChromosomeFactory

__author__ = 'ejanlav'


class EquationFactory(ChromosomeFactory):
    def __init__(self, target_value):
        self._target_value = target_value

    def create_chromosome(self, chromosome_string):
        return EquationChromosome(chromosome_string, self._target_value)

    def create_random_chromosome(self):
        chromosome_string = ''
        for index in xrange(EquationChromosome.NUMBER_OF_GENES):
            chromosome_string += random.choice(['0', '1'])
        return self.create_chromosome(chromosome_string)





