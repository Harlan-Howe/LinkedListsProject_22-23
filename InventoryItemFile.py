from enum import Enum

class InventoryType(Enum):
    HEALING = 1
    MEELEE = 2
    MAGIC = 3
    SWAG = 4

InventoryTypeEmojis = {InventoryType.HEALING: "❤️‍", InventoryType.MEELEE: "🗡", InventoryType.MAGIC: "🪄", InventoryType.SWAG: "💰"}

class InventoryItem:
    # Notice that the parameters can have default values - that is, if you don't tell the method what you want
    #    item name to be, it will fill in "generic item" automatically; otherwise, it will use what you give it.
    #    This is in lieu of overloading methods, which python does not allow.
    def __init__(self,      item_name: str = "generic item",
                            item_type: InventoryType = InventoryType.SWAG,
                           item_power: int = 0):
        self.name = item_name
        self.type = item_type
        self.power = item_power


    def __eq__(self, other):
        """
        overloaded "equals" operator - i.e., we are writing our own version of "==" when comparing this class to another.
        :param other:
        :return: whether these two items have equivalent items.
        """
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.type == other.type and self.power == other.power
        else:
            raise TypeError("Attempted to compare an Inventory item to a non-Inventory item.")

    def __lt__(self, other):
        """
        overloaded "less than" operator - i.e., we are writing our own version of "<" when comparing this class to another.
        :param other:
        :return:  whether the first item is "less than" the other item
        """
        if isinstance(other,InventoryItem):
            if self.type != other.type:
                return self.type < other.type
            else:
                if self.power != other.power:
                    return self.power < other.power
                else:
                    return self.name < other.name
        else:
            raise TypeError("Attempted to compare an Inventory item to a non-Inventory item.")

    def __gt__(self, other):
        """
        overloaded "greater than" operator - i.e., we are writing our own version of "<" when comparing this class to another.
        :param other:
        :return:  whether the first item is "less than" the other item
        """
        if isinstance(other, InventoryItem):
            if self.type != other.type:
                return self.type > other.type
            else:
                if self.power != other.power:
                    return self.power > other.power
                else:
                    return self.name > other.name
        else:
            raise TypeError("Attempted to compare an Inventory item to a non-Inventory item.")

    def __str__(self):
        """
        this is the equivalent to Java's toString() method for the user.
        :return: a string describing this Inventory Item
        """
        return f"({InventoryTypeEmojis[self.type]}: level {self.power} \"{self.name}\")"

    def __repr__(self):
        """
        this is the equivalent to Java's toString method for debugging purposes.
        :return: a detailed string describing this Inventory Item
        """
        return self.__str__() # in this case, they're the same.