import json
import re
import sys

from math  import log10
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.compat import jobconf_from_env

N= 3


class proj1(MRJob):
    def mapper(self, _, line):
        year = line[:4]
        words = line[9:]

        words = re.split("[ *$&#/\t\n\f\"\'\\,.:;?!\[\](){}<>~\-_]", words.lower())

        for word in words:
            yield word + "," + str(year), 1
            yield word + ",*", 1

    def combiner(self, key, count):
        yield (key), sum(count)

    def reducer_init(self):
        self.marginal = 0 
        
        
    def reducer(self, key, count):
        w1, w2 = key.split(",", 1)
        if w2 == "*":
            self.marginal =sum(count)
        else:
            counts = sum(count)
            yield w1, (w2, counts)
            
    SORT_VALUES = True
            
    JOBCONF = {
        'mapreduce.map.output.key.field.separator':',',
        'mapreduce.job.reduces':2,
        'mapreduce.partition.keypartitioner.options':'-k1,1'
    }

    def TF_IDF(self, word, year_count):
        num = 0
        year = []
        freq = []
        for f in year_count:
            year.append(f[0])
            freq.append(f[1])
            num += 1

        IDF = log10(N / num)
        
        for i in range(len(year)):
            yield (word,IDF),(year[i],freq[i])

    def output(self, w_IDF, year_f):
        word, IDF = w_IDF[0],w_IDF[1]
        year=[]
        tfidf=[]
        for i in year_f:
            year.append(i[0])
            tfidf.append(i[1]*IDF)
        for i in range(len(year)):
            yield word,year[i]+','+str(tfidf[i]) 
        #year,freq=year_f[0],year_f[1]
        #word=w_IDF[0]
        #IDF=float(w_IDF[1])
        #tf_idf = IDF * float(year_f[1])
        #yield word, IDF

    SORT_VALUES = True
            
    JOBCONF = {
        'mapreduce.map.output.key.field.separator':',',
        'mapreduce.job.reduces':2,
        'mapreduce.partition.keypartitioner.options':'-k1,1'
    }
    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                combiner=self.combiner,
                reducer_init=self.reducer_init,
                reducer=self.reducer
            ),
            MRStep(
                 reducer=self.TF_IDF
            ),
            MRStep(
                reducer=self.output
           )
        ]

if __name__ == '__main__':
    proj1.run()
