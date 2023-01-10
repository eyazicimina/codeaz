from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class SmartBinaryClassifier( object ):
	def __init__(self, dataFrame: pd.DataFrame, target: str):
		self.dataFrame = dataFrame
		self.target = target
		self.splitted = False

	def shuffle(self):
		self.dataFrame = self.dataFrame.sample(frac = 1.0)

	def sampleN(self, n: int = 10000):
		self.dataFrame = self.dataFrame.sample(n = n)

	def sampleRatio(self, fraction: float = 0.5):
		self.dataFrame = self.dataFrame.sample(frac = fraction)

	def splitInto2ByCriteria(self, column: str, criteria: object):
		self.splitted = True
		self.dataFrameA = self.dataFrame[ self.dataFrame[column] == criteria]
		self.dataFrameB = self.dataFrame[ self.dataFrame[column] != criteria]

	def splitIntoTrainTest(self, ratio: float = 0.70, rebalance: float = 0.5):
		if self.splitted == False:
			#: Split into two
			limit = int(ratio * len(self.dataFrame))
			self.train = self.dataFrame[: limit]
			self.test = self.dataFrame[limit:]

			#: If rebalancing is needed
			if not (rebalance == None or rebalance == 0.0):
				#: Divide into 2
				ones = self.train[self.train[self.target] == 1]
				zeros = self.train[self.train[self.target] == 0]

				# Find the small one
				mean = self.train[self.target].mean()

				#: Rebalance
				if mean < 0.5:
					zeros = zeros.sample(frac = rebalance)
				else:
					ones = ones.sample(frac = rebalance)

				#: Merge
				self.train = pd.concat( [ones, zeros] )
				self.train = self.train.sample( frac = 1.0)

		else:
			limit = int( ratio * len(self.dataFrameA) )
			self.trainA = self.dataFrameA[ : limit ]
			self.testA = self.dataFrameA[ limit: ]

			#: TODO, rebalance

			limit = int( ratio * len(self.dataFrameB) )
			self.trainB = self.dataFrameB[ : limit ]
			self.testB = self.dataFrameB[ limit: ]

	def train(self) -> dict:
		#: Declare variables
		output = {}
		#: If only one
		if self.splitted == False:
			self.model = RandomForestClassifier(max_depth=6, random_state=0)
			#: Split the x,y
			trainy = self.train[ self.target ]
			trainx = self.train.drop( columns = [self.target])
			#: Split the x,y
			testy = self.test[ self.target ]
			testx = self.test.drop( columns = [self.target])
			#: Train the model
			self.model.fit( trainx, trainy )
			#: Get the results
			output[ 'accuracy' ] = self.model.score( testx, testy )
			output[ 'f1score' ] = f1_score( testy, self.model.predict( testx ) )
		else:
			# TODO: for multiple classifiers
			pass

		#: Returns the output
		return output


# 1 Load the dataset
# 2 Feature representation
# 3 Feature mining
# 4 == CLASS
# 4.a ====> sample
# 4.b ====> shuffle
# 4.c ====> train/test split
# 4.d ====> re-balancing
# 4.e ====> split into two category
# 4.f ====> train





path = "/home/mina5/Desktop/codeacedemy/"
df = pd.read_csv(path + "week6-quiz1.csv")

