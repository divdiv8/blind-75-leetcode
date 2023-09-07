def isAnagram(self, s: str, t: str) -> bool:
        #create a dictionary with letters and number of occurences for both s and t and equate them
        
      d=getdict(s)
      d1=getdict(t)
      return d==d1

        

def getdict(x:str):
    d={}
    for i in x:
        if len(d)==0:
            d.update({i:1})
            continue
        if d.get(i)==None:
            d.update({i:1})
        else:
            d.update({i:d.get(i)+1})
    return d
