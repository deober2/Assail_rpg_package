from PIL import Image
import os

# Get the directory of the current file
dir_path = os.path.dirname(os.path.realpath(__file__))

WATER_TEXTURE = Image.open(os.path.join(dir_path, "WaterBackground.png"))
TREE_TEXTURE = Image.open(os.path.join(dir_path,"TreeBackground.png"))
GRASS_TEXTURE = Image.open(os.path.join(dir_path,"GrassBackground.png"))
ROCK_TEXTURE = Image.open(os.path.join(dir_path,"RockBackground.png"))
DIRT_TEXTURE = Image.open(os.path.join(dir_path,"DirtBackground.png"))
KNIGHT_TEXTURE = Image.open(os.path.join(dir_path,"knight.png"))
MAGE_TEXTURE = Image.open(os.path.join(dir_path,"mage.png"))
FIRE = Image.open(os.path.join(dir_path,"fire.png"))
FORWARD_SLASH = Image.open(os.path.join(dir_path,"forward_slash.png"))
BACK_SLASH = Image.open(os.path.join(dir_path,"back_slash.png"))
VERTICAL_SHOT = Image.open(os.path.join(dir_path,"shot_vertical.png"))
HORIZONTAL_SHOT = Image.open(os.path.join(dir_path,"shot_horizontal.png"))
FIRE_COLUMN_1 = Image.open(os.path.join(dir_path,"fire_column_1.png"))
FIRE_COLUMN_2 = Image.open(os.path.join(dir_path,"fire_column_2.png"))
SELECT_BOX_WHITE = Image.open(os.path.join(dir_path,"select_box_white.png"))
BONES = Image.open(os.path.join(dir_path,"bones.png"))
