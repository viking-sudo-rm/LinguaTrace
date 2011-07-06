import tracer #heart of the package
import mutations #module containing built-in premade mutations

"""

A simple example that attempts to reconstruct a word from the past based on a more recent cognate. Note that this specific example is not at all accutate because the 'lolmut' mutation that is used is completely made up.

"""

test = tracer.LinguaTrace(500,"hello") #create an instance of the LinguaTrace object, providing the lexical item as a string and its date (500 CE)

lolmut = tracer.newmutation(mutations.lolmut,400) #create a mutation out of the function lolmut in the mutations module and set the date of the mutation to 400 CE

test.mutate(lolmut) #apply the mutation; for best results, apply mutations in chronological order

print test.getearliest() #get the earliest form of the lexical item held in the LinguaTrace object (in this case, the form in the year 400 CE)
print test.get(330) #get the form of the lexical item in the year 330 CE