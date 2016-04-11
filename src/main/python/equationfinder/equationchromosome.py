from genetics.chromosome import Chromosome

__author__ = 'ejanlav'


class EquationChromosome(Chromosome):

    GENE_LENGTH = 4

    # TODO find better name for chromosome_string
    def __init__(self, chromosome_string, target_value):
        self._chromosome_string = chromosome_string
        self._target_value = target_value
        self._fitness = self.assign_fitness()

    def get_genes(self):
        for i in xrange(0, len(self._chromosome_string), self.GENE_LENGTH):
            yield self._target_value[i:i+self.GENE_LENGTH]

    def get_fitness(self):
        return self._fitness

    def assign_fitness(self):
        equation_list = self._trim_chromosome()
        if len(equation_list) == 0:
            return 0
        else:
            result = equation_list[0]
        for index in range(len(equation_list)):

            if equation_list[index] == 10:
                result += equation_list[index + 1]

            elif equation_list[index] == 11:
                result -= equation_list[index + 1]

            elif equation_list[index] == 12:
                result *= equation_list[index + 1]

            elif equation_list[index] == 13:
                result = result * 1. / equation_list[index + 1]

            return 1. / (self._target_value - result)

    def _trim_chromosome(self):
        looking_for_operator = False
        result = []
        for gene in self.get_genes():
            decimal_value = int(gene, 2)
            if decimal_value in range(0, 10) and not looking_for_operator:
                result.append(decimal_value)
                looking_for_operator = True
            elif decimal_value in range(10, 14) and looking_for_operator:
                result.append(decimal_value)
                looking_for_operator = False
        if len(result) == 0 or looking_for_operator:
            return result
        else:
            return result[0:-1]
