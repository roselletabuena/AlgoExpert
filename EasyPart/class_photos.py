def classPhotos(redShirtsHeights, blueShirtHeights):
    redShirtsHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorInFirstRow = 'RED' if redShirtsHeights[0] < blueShirtHeights[0] else 'BLUE'

    for idx in range(len(redShirtsHeights)):
        redShirtsHeight = redShirtsHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFirstRow == 'RED':
            if redShirtsHeight >= blueShirtHeight:
                return False
        else: 
            if blueShirtHeight >= redShirtsHeight:
                return False


    return True


redShirts = [5, 8, 1, 3, 4]
blueShirts = [6, 4, 2, 4, 5]

print(classPhotos(redShirts, blueShirts))