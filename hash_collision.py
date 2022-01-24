import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
    
    generated = {}
   
    #Collision finding code goes here
    while True:
        x = os.urandom(64)
        y = os.urandom(64)

        binary_x = format(int(hashlib.sha256(x).hexdigest(), 16), 'b')
        binary_y = format(int(hashlib.sha256(y).hexdigest(), 16), 'b')

        if x not in generated:
            binary_x = format(int(hashlib.sha256(x).hexdigest(), 16), 'b')
            generated[x] = binary_x

        if y not in generated:
            binary_y = format(int(hashlib.sha256(y).hexdigest(), 16), 'b')
            generated[y] = binary_y

        bin_x = generated[x]
        bin_y = generated[y]
        
        if bin_x[-k:] == bin_y[-k:]:
            break
    
    return( x, y )