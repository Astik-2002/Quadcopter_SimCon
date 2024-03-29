# -*- coding: utf-8 -*-
"""
author: John Bass
email: john.bobzwik@gmail.com
license: MIT
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from numpy import sin, cos
from numpy.linalg import norm


# Normalize quaternion, or any vector
def vectNormalize(q):
    return q/norm(q)


# Quaternion multiplication
def quatMultiply(q, p):
    Q = np.array([[q[0], -q[1], -q[2], -q[3]],
                  [q[1],  q[0], -q[3],  q[2]],
                  [q[2],  q[3],  q[0], -q[1]],
                  [q[3], -q[2],  q[1],  q[0]]])
    return Q@p


# Inverse quaternion
def inverse(q):
    qinv = np.array([q[0], -q[1], -q[2], -q[3]])/norm(q)
    return qinv

def hat_map(vec):
    """Return that hat map of a vector
    
    Inputs: 
        vec - 3 element vector

    Outputs:
        skew - 3,3 skew symmetric matrix

    """
    vec = np.squeeze(vec)
    skew = np.array([
                    [0, -vec[2], vec[1]],
                    [vec[2], 0, -vec[0]],
                    [-vec[1], vec[0], 0]])

    return skew

def vee_map(skew):
    """Return the vee map of a vector

    """

    vec = 1/2 * np.array([skew[2,1] - skew[1,2],
                          skew[0,2] - skew[2,0],
                          skew[1,0] - skew[0,1]])

    return vec
