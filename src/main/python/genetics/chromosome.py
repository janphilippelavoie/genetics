__author__ = 'ejanlav'
from abc import ABCMeta, abstractmethod


class Chromosome:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_fitness(self):
        pass
