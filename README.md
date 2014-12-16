hash-chain
==========
An insider has leaked three password hashes for system accounts on the project server.
aoun        $1$HUSKIES!$v/mh7SBLm8/3SBL6w0Z9M1
curry       $1$HUSKIES!$xk2VnxpJYAGOxEl0W8uEP0
ryder       $1$HUSKIES!$R9bstTQ9eG2Pzql0cq7kd/

PASSWORD RECOVERY

Your first task is to recover the corresponding passwords for those accounts using the pre-computed table of hash chains. 
This JSON file contains the start and end values for each chain, the salt known to be used 
for these three acounts, and the length k for each chain. The hash function H is MD5, while the reduction R for a hash value 
of length m is"

R(x)=r(xm),…,r(xm−7)
where

r(x)=(x mod 26)+ ‘a’
That is, R takes the last eight characters of a hash value in reverse, and for each character x produces the x mod 26 lowercase ASCII letter.

Use the recovered passwords to log into each account on the project server and collect the secret located in the home directory.

HASH TABLE EFFICIENCY

The provided table contains a number of collisions that reduces its theoretical maximum coverage of the password space c=n×k, 
where n is the number of chains. Compute the table’s actual coverage of the password space c′ and its efficiency c′/c.