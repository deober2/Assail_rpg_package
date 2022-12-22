from numpy import random
from PIL import Image
from assail.resources.image_loading import *
import io


def generate_battle(
    oldBattleMap=[],
    buildNewBattleMap=True,
    baseTexture=0,
    newTexture=2,
    percentNewTexture=60,
    tile_height=14,
    tile_width=25,
) -> list[list[int]]:
    """Method to procedurally Generate a battleMap (an mxn grid of integers representing individual tile textures).
    Can pass an existing battleMap and generate on top of the old map, or generate a completely new map.

    Parameters
    ----------
    oldBattleMap : list[List[int]], optional
        existing battleMap that you wish to write on top of. Default is an empty list
    buildNewBattleMap : bool, optional
        Whether or not to generate a completely new map. Pair True with empty oldBattleMap, or False with filled oldBattleMap, by default True
    baseTexture : int, optional
        defines the base texture to fill the initial map. Refers to one of the textures defined above, by default 0
    newTexture : int, optional
        defines the new texture to draw on top of the existing battle map. Refers to one of the textures defined above, by default 2
    percentNewTexture : int, optional
        defines the percentage of the map that newTexture should occupy, by default 60

    Returns
    -------
    battleMap : list[List[int]]
        Matrix of integers representing the battle map. Each integer represents a texture.
    """
    print("Generating Battle Map")
    # Build a matrix to represent each gridpoint
    if buildNewBattleMap:
        battleMap = []
        for y in range(tile_height):
            battleMap.append([])
            for x in range(tile_width):
                battleMap[y].append(baseTexture)
    else:
        battleMap = oldBattleMap
        del oldBattleMap

    # Deposit new textures on the base texture
    location = [
        random.randint(0, len(battleMap)),
        random.randint(0, len(battleMap[0])),
    ]
    battleMap[location[0]][location[1]] = newTexture
    newTextureCount = 1

    # Random walk algorithm to generate grid spaces
    print("Beginning random Walk")
    while (100 * newTextureCount / (tile_width * tile_height)) < percentNewTexture:
        move = random.randint(-1, 2)
        direction = random.randint(0, 2)
        if direction == 0:
            move = [0, move]
        else:
            move = [move, 0]

        newCoord = [location[0] + move[0], location[1] + move[1]]
        try:
            # print(newCoord)
            if (
                newCoord[0] > -1
                and newCoord[1] > -1
                and newCoord[0] < len(battleMap)
                and newCoord[1] < len(battleMap[0])
            ):
                location = newCoord
                # print(newCoord)
                if battleMap[location[0]][location[1]] != newTexture:
                    battleMap[location[0]][location[1]] = newTexture
                    newTextureCount += 1
                    # print("generated. percent "+ str(100 * newTextureCount / (tile_height * tile_width))+ "\n"  )
        except:
            pass
    return battleMap


def battle_map_to_image(battle_map: list[list[int]]) -> Image:
    """Takes a battle map (matrix of integers) and converts it to an image.

    Parameters
    ----------
    battleMap : list[List[int]]
        Matrix of integers representing the battle map. Each integer represents a texture.

    Returns
    -------
        buffer : Image buffer data. Call buffer.getvalue() to get the image data.
    """
    # Access all elemental tile images
    small_images = [
        WATER_TEXTURE,
        TREE_TEXTURE,
        GRASS_TEXTURE,
        ROCK_TEXTURE,
        DIRT_TEXTURE,
    ]

    # Store the dimensions of the small images
    small_image_width = small_images[0].size[0]
    small_image_height = small_images[0].size[1]

    # Create a blank image with the desired dimensions in pixels
    width = len(battle_map[0]) * small_image_width
    height = len(battle_map) * small_image_height
    large_image = Image.new("RGB", (width, height))

    # Paste the small images onto the large image according to the matrix
    for i, row in enumerate(battle_map):
        for j, value in enumerate(row):
            small_image = small_images[value]
            large_image.paste(
                small_image, (j * small_image_width, i * small_image_height)
            )

    # Save the large image to a memory buffer
    # buffer = io.BytesIO()
    # large_image.save(buffer, format="PNG")

    # Return the image
    return large_image
