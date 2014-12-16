import crypt
import json
import string
with open("/home/hash-chain/table.json") as f:
        json_data = json.load(f)
        hash_chains = json_data['chains']
def reduce(text_to_hash):
        tmp = text_to_hash[-8:]
        result = ""
        for i in tmp[::-1]:
                result += chr(ord(i)%26 + ord('a'))
        print result
        return result
def hash_this(text):
         return crypt.crypt(text,'$1$HUSKIES!$')

text_to_hash = raw_input("enter the hash")
reduction = reduce(text_to_hash)
s=0
k=0
while s<1:
        print(k)
        for chain in hash_chains:
                if reduction == chain['end']:
                        start = chain['start']
                        print chain['start']
                        print chain['end']
                        s+=1
                        break
                else:
                        s=0
        tmp = hash_this(reduction)
        reduction=reduce(tmp)
        k+=1
hash_tmp=hash_this(start)
while text_to_hash != hash_tmp:
        password= reduce(hash_tmp)
        hash_tmp = hash_this(password)
print password