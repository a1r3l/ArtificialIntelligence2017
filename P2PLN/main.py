from outputWeka import OutputWeka
from most_common import Most_common

def init():
	path = './dataset/'
	n = raw_input("Number of most common words: ")
	common = Most_common(n,path)
	calcVect = OutputWeka(common.counts,n,path)

init()

