import csv
import random

NEURON = [3, 7, 3]
TRAIN_PERCENT = 0.8
TEST_PERCENT = 0.4
SETOSA = "Iris-setosa"
VERSICOLOR = "Iris-versicolor"
VIRGINICA = "Iris-virginica"

# The class for a single neural network
class NeuralNetwork():

	# The initial loading of data, and setting of class variables.
	# This function runs on the creation of a new neural network.
	def __init__(self, PATH):

		with open(PATH) as database_file:
			iris_database = list(csv.reader(database_file))
		for row in iris_database:
			row[4] = [SETOSA, VERSICOLOR, VIRGINICA].index(row[4])
			row[:4] = [float(row[j]) for j in range(len(row))]

		random.shuffle(iris_database)
		training_data = []
		testing_data = []

		# Assignming some portion of data to train
		for i in iris_database:
			random_num = random.random()
			if (random_num < TRAIN_PERCENT):
				training_data.append(i)
			
		# Assignming some portion of data to test
		for i in iris_database:
			random_num = random.random()
			if (random_num < TEST_PERCENT):
				testing_data.append(i)



		# Putting the iris data into according testing and training lists
		self.train_info = [info[:4] for info in training_data]
		self.test_info  = [info[:4] for info in testing_data]

		# Putting the iris class into according testing and training lists
		self.train_class = [iris_class[4] for iris_class in training_data]
		self.test_class  = [iris_class[4] for iris_class in testing_data]

		self.neur1   = ([0 for i in range(NEURON[1])])
		self.neur2   = ([0 for i in range(NEURON[2])])

		self.weight1 = []
		for i in range(NEURON[0]):
			sub_array = []
			for j in range(NEURON[1]):
				sub_array.append(2 * (random.random() - 0.5))
			self.weight1.append(sub_array)
		
		self.weight2 = []
		for i in range(NEURON[1]):
			sub_array = []
			for j in range(NEURON[2]):
				sub_array.append(2 * (random.random() - 0.5))
			self.weight2.append(sub_array)









