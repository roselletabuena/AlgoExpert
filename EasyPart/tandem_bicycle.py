# O(nlog(n)) time | O(1) space

def tandemBicycle(redShirtsSpeeds, blueShirtSpeeds, fastest):
    redShirtsSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest: 
        reverseArrayInPlace(redShirtsSpeeds)

    totalSpeed = 0
    for idx in range(len(redShirtsSpeeds)):
        rider1 = redShirtsSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
        totalSpeed += max(rider1, rider2)

    return totalSpeed


def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end += 1