#!/usr/bin/env python3

import math

class RDD:
	def __init__(self, iterator):
		self.data = iterator
		
	def collect(self):
		return self.data
		
	def first(self):
		return self.data[0]
		
	def top(self, num):
		return self.data[0:num]
		
	def persist(self):
		return self
	
	def cache(self):
		return self
		
	def map(self, func):
		return RDD([func(x) for x in self.data])
		
	def reduce(self, func):
		s = self.data[0]
		for x in self.data[1:]:
			s = func(s,x)
		return s
		
	def mapPartitions(self, func, n = 10):
		l = len(self.data)
		num = math.ceil(float(l)/n)
		return RDD([func(self.data[i*num : min((i+1)*num,l)]) for i in range(n)])	
		

def parallelize(iterator):
	return RDD(iterator)
	

	
