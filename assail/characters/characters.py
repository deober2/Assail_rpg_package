import assail.resources.image_loading as il


# Movement dictionary to get movement vectors
userInput = ["l", "r", "u", "d"]
moveVec = [[0, -1], [0, 1], [1, 0], [-1, 0]]
moveDict = dict(zip(userInput, moveVec))
del userInput
del moveVec


# Archetype attack patterns
attackNames = ["melee", "mageBlast", "arrow"]
patterns = [
    [[1, 0]],
    [[3, 0], [3, 0], [2, 0], [4, 0], [3, -1], [3, 1]],
    [[2, 0], [1, 0], [3, 0]],
]
damages = [7, 3, 6]
animationNames = ["melee", "mageBlast", "arrowVert", "arrowHoriz"]
animations = [
    [il.FORWARD_SLASH, il.BACK_SLASH],
    [il.FIRE_COLUMN_1, il.FIRE_COLUMN_2],
    [il.VERTICAL_SHOT],
    [il.HORIZONTAL_SHOT],
]
attackPatternDict = dict(zip(attackNames, patterns))
attackAminationDict = dict(zip(animationNames, animations))
attackDamageDict = dict(zip(attackNames, damages))
del attackNames
del patterns
del animations
del animationNames
del damages


class creature:
    # Class representing moveable characters
    def __init__(
        self,
        name="noName",
        archetype="knight",
        battleMapLocation=[5, 10],
        team="blue",
        apMax=4,
        health=20,
        armorClass=10,
        attackName="melee",
    ):
        self.name = name
        self.archetype = archetype
        self.battleMapLocation = battleMapLocation
        self.team = team
        self.apMax = apMax
        self.apCurrent = apMax
        self.health = health
        self.texture = None
        self.armorClass = armorClass
        self.attackName = attackName
        self.living = True
        self.healthMax = None
        self.isPlayer = False

    def assign_attributes(self):
        if self.archetype == "knight":
            self.texture = il.KNIGHT_TEXTURE
            self.attackName = "melee"
        elif self.archetype == "mage":
            self.texture = il.MAGE_TEXTURE
            self.attackName = "mageBlast"
        self.attackPattern = attackPatternDict[self.attackName]
        self.armorClass = 5
        self.healthMax = 10

    def get_value(self):
        value = (
            self.healthMax
            + self.armorClass
            + attackDamageDict[self.attackName]
            * len(attackPatternDict[self.attackName])
        )
        return round(value**1.1)


class player(creature):
    def __init__(
        self,
        name="noName",
        archetype="knight",
        battleMapLocation=[5, 10],
        team="blue",
        apMax=4,
        health=20,
        teamMembers=[],
        money=1000,
    ):
        super().__init__(self)
        self.name = name
        self.archetype = archetype
        self.battleMapLocation = battleMapLocation
        self.team = team
        self.apMax = apMax
        self.apCurrent = apMax
        self.health = health
        self.texture = None
        self.teamMembers = teamMembers
        self.money = money
        self.attackName = None
        self.attackPattern = None
        self.living = True
        self.healthMax = None
        self.armorClass = None
        self.isPlayer = True
