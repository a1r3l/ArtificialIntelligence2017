import nltk
import collections
import os
import codecs

class Most_common():

	def __init__(self, n,path):
		self.counts = None
		self.readAndMake(n,path)

	def readAndMake(self,n,path):	
		for filename in os.listdir(path):
			f = codecs.open(path + filename,"r",encoding="utf-8")
			text = f.read()
			words = nltk.word_tokenize(text)
			words = [word for word in words if word.isalpha()]
			if not self.counts:
				self.counts = collections.Counter(words)
			else:
				self.counts += collections.Counter(words)
			f.close()
		self.counts = [str(word[0]) for word in self.counts.most_common(int(n))]