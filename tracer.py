#class holding various versions of string

class LinguaTrace:
	def __init__(self,date,final):
		self.strings = {date:final}
		self.final = date,final
	def latest(self):
		lowest = self.final[0]
		val = self.final[1]
		for date,s in self.strings.iteritems():
			if date < lowest:
				lowest = date
				val = s
		return lowest,val
	def getearliest(self):
		return self.latest()[1]
	def get(self,date):
		lastdate = self.final[0]
		val = self.final[1]
		for d,s in self.strings.iteritems():
			if d > date and d < lastdate:
				lastdate = d
				val = s
		return val
	def mutate(self,func):
		res = func(*self.latest())
		self.strings[res[0]] = res[1]

#generator to turn a normal function into a compatible mutation

def newmutation(func,date):
	def gen(d,s):
		if d > date: return date,func(s)
		return date,s
	return gen