__author__ = 'ejanlav'
from abc import ABCMeta, abstractmethod


class ChromosomeFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_random_chromosome(self):
        pass

    @abstractmethod
    def create_chromosome(self, targets):
        pass

