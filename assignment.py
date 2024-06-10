
# buckets = dict()
# def hash(arg):
#     return arg*len(arg)
# def insert(key, value):
#     idx = hash(key) % len(buckets)
#     buckets[idx] = [key,value]
# def lookup(key):
#     idx = hash(key) % len(buckets)
#     return buckets[idx][1]
# def remove(key):
#     idx = buckets(key) % len(buckets)
#     buckets[idx] = None

# PART 1 
class HashTable:
    def __init__(self, capacity, load=.75) -> None:
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.load = load
    
    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  
                return
        bucket.append((key, value))
        self.size +=1
            
    def get(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for k,v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket = bucket.remove(bucket[i])
                self.size -= 1
                return 
        
        return None


#PART 2



with open('tesxt.txt', 'r') as file:
    test = file.read()


count = dict()
words = test.split()
for word in words: 
    word = word.lower()
    if word: 
        curr_count = count.get(word,0)
        count[word] = curr_count + 1
for word, number in count.items():
    print(f"'{word}': {count}")


#top 10 words
top = sorted(count.items(), key=lambda x: x[1], reverse=True)

top10 = top[:10]
for k,v in top10:
    print(k,v)

# ANALYSIS

'''
- Time complexity: worst case scenario for all functions are o(n) and average case is o(1) because there can be instances where the function needs to traverse through the whole bucket. However, the average case is o(n) which is why hash tables are efficient. 

- Space complexity: space complexicity is o(n) as this this is number of key value pairs that are in the hash table. 

- This was an interesting way to understand and utilize dictionaries. The complexicity for me came when I had to deal with capacity and setting up the class: it has been a while. I decided to handle the collisions within the class itself rather than have it as a seprate function, as it was more inituitive, and was able to incorporate that into the existing function. 

- It was interesting to learn the underscore and how it could be used within the class. I itially followed the in class presentation, but there were many holes as most resources used classes. 

Sources: 
https://www.geeksforgeeks.org/implementation-of-hash-table-in-python-using-separate-chaining/

https://youcademy.org/word-freqency-counter-using-hash-table/

https://www.tutorialspoint.com/data_structures_algorithms/hash_data_structure.htm
'''