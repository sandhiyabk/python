class simplehashing:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
        self.probe='linear'
    def _hash(self,key):
        return key%self.size
    def set_probe(self,probe):
        if probe in ['linear','quadratic']:
            self.probe=probe
        else:
            return ValueError("probe type should be linear or quadratic")
    def insert(self,key,value):
        index=self._hash(key)
        for i in range(self.size):
            if self.table[index] is None or self.table[index][0]==key:
                self.table[index]=(key,value)
                return
            index=(index+(i if self.probe=='linear' else i*2))%self.size
    def search(self,key):
        index=self._hash(key)
        for i in range(self.size):
            if self.table[index] is None:
                return None
            if self.table[index][0]==key:
                return self.table[index][1]
            index=(index+(i if self.probe=='linear' else i*i))%self.size
        return None
simple=simplehashing(10)
print("linear probing:")
simple.set_probe('linear')
simple.insert(1,100)
simple.insert(1,200)
print(simple.search(1))
print("Quadratic probing:")
simple.set_probe('quadratic')
simple.insert(3,300)
print(simple.search(3))

    

    
