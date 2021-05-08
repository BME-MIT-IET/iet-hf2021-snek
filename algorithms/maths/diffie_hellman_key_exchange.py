from algorithms.maths import (
    prime_check,
    find_primitive_root,
)
from random import randint

"""
Diffie-Hellman key exchange is the method that enables
two entities (in here, Alice and Bob), not knowing each other,
to share common secret key through not-encrypted communication network.
This method use the property of one-way function (discrete logarithm)
For example, given a, b and n, it is easy to calculate x
that satisfies (a^b) ≡ x (mod n).
However, it is very hard to calculate x that satisfies (a^x) ≡ b (mod n).
For using this method, large prime number p and its primitive root a must be given.
"""

def alice_private_key(p):
    """Alice determine her private key
    in the range of 1 ~ p-1.
    This must be kept in secret"""
    return randint(1, p-1)


def alice_public_key(a_pr_k, a, p):
    """Alice calculate her public key
    with her private key.
    This is open to public"""
    return pow(a, a_pr_k) % p


def bob_private_key(p):
    """Bob determine his private key
    in the range of 1 ~ p-1.
    This must be kept in secret"""
    return randint(1, p-1)


def bob_public_key(b_pr_k, a, p):
    """Bob calculate his public key
    with his private key.
    This is open to public"""
    return pow(a, b_pr_k) % p
    

def alice_shared_key(b_pu_k, a_pr_k, p):
    """ Alice calculate secret key shared with Bob,
    with her private key and Bob's public key.
    This must be kept in secret"""
    return pow(b_pu_k, a_pr_k) % p


def bob_shared_key(a_pu_k, b_pr_k, p):
    """ Bob calculate secret key shared with Alice,
    with his private key and Alice's public key.
    This must be kept in secret"""
    return pow(a_pu_k, b_pr_k) % p


def diffie_hellman_key_exchange(a, p, option = None):
    if (option != None):
        option = 1
        """ Print explanation of process
        when option parameter is given """
    if (prime_check(p) == False):
        print("%d is not a prime number" % p)
        return False
        """p must be large prime number"""
    else:
        try:
            p_root_list = find_primitive_root(p)
            p_root_list.index(a)
        except ValueError:
            print("%d is not a primitive root of %d" % (a, p))
            return False
            """ a must be primitive root of p """
        
        a_pr_k = alice_private_key(p)
        a_pu_k = alice_public_key(a_pr_k, a, p)
        
        
        b_pr_k = bob_private_key(p)
        b_pu_k = bob_public_key(b_pr_k, a, p)
        
        if (option == 1):
            print ("Private key of Alice = %d" % a_pr_k)
            print ("Public key of Alice = %d" % a_pu_k)
            print ("Private key of Bob = %d" % b_pr_k)
            print ("Public key of Bob = %d" % b_pu_k)

        """ In here, Alice send her public key to Bob,
        and Bob also send his public key to Alice."""

        a_sh_k = alice_shared_key(b_pu_k, a_pr_k, p)
        b_sh_k = bob_shared_key(a_pu_k, b_pr_k, p)
        print ("Shared key calculated by Alice = %d" % a_sh_k)
        print ("Shared key calculated by Bob = %d" % b_sh_k)
        
        return (a_sh_k == b_sh_k)
