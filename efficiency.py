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
         return crypt.crypt(text.encode('utf8'),'$1$HUSKIES!$')

unique_pass = set()
print unique_pass
for chain in table['chains']:
        value = chain['start']
        unique_pass.add(value)
        while value != chain['end']:
                value = reduce(MD5(value))
                unique_pass.add(value)
                print len(unique_pass)

length = len(unique_pass)
eff = length/(128*65536)
print eff