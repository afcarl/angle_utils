from __future__ import division


import math

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


def average_angle(angles):
    """ average_angle(angles)
    Compute the average of a number of angles
    using circular statistics mean

    Parameters
    --------------
    angles : iterable container of angles

    Returns
    ----------
    theta_bar : average angle
    """

    if len(angles) == 0:
        return 0.0

    num, den = 0.0, 0.0
    for theta in angles:
        num += math.sin(theta)
        den += math.cos(theta)

    theta_bar = math.atan2(num/len(angles), den/len(angles))

    return theta_bar
