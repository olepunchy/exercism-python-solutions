def create_inventory(items):
    """
    Create an inventory dictionary from a list of items.

    The string value of the item becomes the dictionary key.
    The number of times the string appears in items becomes
    the value, an integer representation of how many times.

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    items_dict = {}
    for item in items:

        found = False
        for key in items_dict.keys():

            if key == item:
                items_dict[item] += 1
                found = True

        if not found:
            items_dict[item] = 1

    return items_dict


def add_items(inventory, items):
    """
    Increment the value (count) for a key for each occurence in items

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    if not bool(inventory):
        inventory = {}
        for item in items:
            if item in inventory:
                inventory[item] += 1

            else:
                inventory[item] = 1

        return inventory

    else:
        for item in items:
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """
    For each item found in items, decrement the value of item in inventory.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """
    Remove an item from inventory if it exists.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory):
    """
    Return the inventory in tuple form. Skip any items with a value of zero.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = []
    for item in inventory:
        if inventory[item] <= 0:
            continue

        inventory_tuple = (item, inventory[item])
        inventory_list.append(inventory_tuple)

    return inventory_list
