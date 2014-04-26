from __future__ import division


import math
import itertools

def normalize(theta, start=0):
    """ normalize(theta, start)

    Normalize an angle to be in the range [0, 2pi]
    """
    if theta < float("inf"):
        while theta >= start + 2 * math.pi:
            theta -= 2 * math.pi
        while theta < start:
            theta += 2 * math.pi
        return theta
    else:
        return float("inf")


def addangles(alpha, beta):
    return normalize(alpha + beta, start=0)


def subangles(alpha, beta):
    delta = 0
    if alpha < float("inf") and beta < float("inf"):
        alpha = normalize(alpha, start=0)
        beta = normalize(beta, start=0)

        delta = alpha - beta
        if alpha > beta:
            while delta > math.pi:
                delta -= 2 * math.pi
        elif beta > alpha:
            while delta < -math.pi:
                delta += 2 * math.pi
    else:
        delta = float("inf")

    return delta


def average_angles(angles):
    """ average_angle(angles)
    Compute the average of a number of angles
    using circular statistics mean

    Parameters
    --------------
    angles : list container of angles

    Returns
    ----------
    theta_bar : average angle
    """

    if len(angles) == 0:
        return 0.0

    num = sum([math.sin(theta) for theta in angles])
    den = sum([math.cos(theta) for theta in angles])

    theta_bar = math.atan2(num/len(angles), den/len(angles))

    return theta_bar


def weighted_average_angles(angles, weights):
    """ weighted_average_angle(angles)
    Compute the weighted average of a number of angles
    using circular statistics mean

    Parameters
    --------------
    angles : list container of angles
    weights : list container of weights

    Returns
    ----------
    theta_bar : average angle
    """
    if len(angles) == 0:
        return 0.0

    if len(angles) != len(weights):
        raise ValueError('Input lists {0} and {1} have different lengths'.format(angles, weights))

    num = sum([weight * math.sin(theta) for theta, weight in itertools.izip(angles, weights)])
    den = sum([weight * math.cos(theta) for theta, weight in itertools.izip(angles, weights)])

    theta_bar = math.atan2(num/len(angles), den/len(angles))

    return theta_bar


def map_to(angle, amin, amax):
    pass
