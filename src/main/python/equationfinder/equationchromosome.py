from genetics.chromosome import Chromosome

__author__ = 'ejanlav'


class EquationChromosome(Chromosome):

    GENE_LENGTH = 4
    NUMBER_OF_GENES = 18

    # TODO find better name for chromosome_string
    def __init__(self, chromosome_string, target_value):
        self._chromosome_string = chromosome_string
        self._target_value = target_value
        self._fitness = self._assign_fitness()

    def __str__(self):
        equation_list = self._trim_chromosome()
        printable = ""
        for element in equation_list:
            if element == 10:
                printable += "+ "
            elif element == 11:
                printable += "- "
            elif element == 12:
                printable += "x "
            elif element == 13:
                printable += "/ "
            else:
                printable += str(element) + " "
        return "{}= {}".format(printable, self._evaluate_equation())

    def get_fitness(self):
        return self._fitness

    def get_bits(self):
        return self._chromosome_string

    def _get_genes(self):
        for i in xrange(0, len(self._chromosome_string), self.GENE_LENGTH):
            yield self._chromosome_string[i:i+self.GENE_LENGTH]

    def _evaluate_equation(self):
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

        return result

    def _assign_fitness(self):
        return 1./(1 + abs(self._evaluate_equation() - self._target_value))

    def _trim_chromosome(self):
        looking_for_operator = False
        result = []
        for gene in self._get_genes():
            decimal_value = int(gene, 2)
            if decimal_value in range(1, 10) and not looking_for_operator:
                result.append(decimal_value)
                looking_for_operator = True
            elif decimal_value in range(10, 14) and looking_for_operator:
                result.append(decimal_value)
                looking_for_operator = False
        if len(result) == 0 or looking_for_operator:
            return result
        else:
            return result[0:-1]
