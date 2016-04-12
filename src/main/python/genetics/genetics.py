import random

__author__ = 'ejanlav'


#
# #define CROSSOVER_RATE            0.7
# #define MUTATION_RATE             0.001
# #define POP_SIZE                  100			//must be an even number
# #define CHROMO_LENGTH             300
# #define GENE_LENGTH               4
# #define MAX_ALLOWABLE_GENERATIONS	400
#
# //returns a float between 0 & 1
# #define RANDOM_NUM		((float)rand()/(RAND_MAX+1))
#
# //----------------------------------------------------------------------------------------
# //
# //	define a data structure which will define a chromosome
# //
# //----------------------------------------------------------------------------------------
# struct chromo_typ
# {
# 	//the binary bit string is held in a std::string
#   string	bits;
#
# 	float	  fitness;
#
# 	chromo_typ(): bits(""), fitness(0.0f){};
# 	chromo_typ(string bts, float ftns): bits(bts), fitness(ftns){}
# };
#
#
# /////////////////////////////////prototypes/////////////////////////////////////////////////////
#
# void    PrintGeneSymbol(int val);
# string  GetRandomBits(int length);
# int     BinToDec(string bits);
# void    PrintChromo(string bits);
# void    PrintGeneSymbol(int val);
# int     ParseBits(string bits, int* buffer);
# void    Mutate(string &bits);
# void    Crossover(string &offspring1, string &offspring2);
#
#

class Genetics:
    # TODO move this over config file (maybe YAML?)
    def __init__(self, chromosome_factory):
        self._chromosome_factory = chromosome_factory
        self._population = []
        self._create_original_population()

    CROSSOVER_RATE = 0.7
    MUTATION_RATE = 0.01
    POPULATION_SIZE = 100
    MAX_ALLOWABLE_GENERATIONS = 400

    def _create_original_population(self):
        for index in xrange(self.POPULATION_SIZE):
            self._population.append(self._chromosome_factory.create_random_chromosome())

    def run(self):
        for generation in xrange(self.MAX_ALLOWABLE_GENERATIONS):
            current_winner, total_fitness = self._get_winner_and_total_fitness()
            print("{} (generation {})".format(current_winner, generation))
            # if current_winner.get_fitness >= 0.999:
            #     break
            new_population = []
            while len(new_population) < self.POPULATION_SIZE:
                chromosome1 = self.roulette_selection(total_fitness).get_bits()
                chromosome2 = self.roulette_selection(total_fitness).get_bits()

                if random.random() < self.CROSSOVER_RATE:
                    chromosome1, chromosome2 = self.crossover(chromosome1, chromosome2)

                new_population.append(self._chromosome_factory.create_chromosome(self.mutate(chromosome1)))
                new_population.append(self._chromosome_factory.create_chromosome(self.mutate(chromosome2)))
            self._population = new_population

    def _get_winner_and_total_fitness(self):
        total_fitness = 0
        current_winner = self._population[0]
        for chromosome in self._population:
            fitness = chromosome.get_fitness()
            total_fitness += fitness
            if fitness > current_winner.get_fitness():
                current_winner = chromosome
        return current_winner, total_fitness

    @classmethod
    def mutate(cls, chromosome):
        new_chromosome = ''
        for bit in chromosome:
            if random.random() < cls.MUTATION_RATE:
                if bit == '0':
                    new_chromosome += '1'
                else:
                    new_chromosome += '0'
            else:
                new_chromosome += bit
        return new_chromosome

    @staticmethod
    def crossover(chromosome1, chromosome2):
        crossover_point = random.randint(0, len(chromosome1))
        new_chromosome1 = chromosome1[0:crossover_point] + chromosome2[crossover_point:len(chromosome1)]
        new_chromosome2 = chromosome2[0:crossover_point] + chromosome1[crossover_point:len(chromosome1)]
        return new_chromosome1, new_chromosome2

    def roulette_selection(self, total_fitness):
        random_value = random.random() * total_fitness
        for chromosome in self._population:
            random_value -= chromosome.get_fitness()
            if random_value < 0:
                return chromosome


