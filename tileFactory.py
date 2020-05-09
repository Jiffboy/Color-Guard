import tile
import emptyTile
import redTile
import blueTile
import greenTile
import roadTile

def getTile(tileType, x, y, size):
    if tileType == "empty":
        return emptyTile.EmptyTile(x, y, size)
    elif tileType == "red":
        return redTile.RedTile(x, y, size)
    elif tileType == "blue":
        return blueTile.BlueTile(x, y, size)
    elif tileType == "green":
        return greenTile.GreenTile(x, y, size)
    elif tileType == "road":
        return roadTile.RoadTile(x, y, size)
    else:
        return tile.Tile(x, y, size)
