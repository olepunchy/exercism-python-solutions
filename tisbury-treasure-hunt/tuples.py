def get_coordinate(record):
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """
    coord = (coordinate[0], coordinate[1])
    return coord


def compare_records(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """
    azra_coords = azara_record[1]
    rui_x_coord = rui_record[1][0]
    rui_y_coord = rui_record[1][1]
    rui_coords = f"{rui_x_coord}{rui_y_coord}"
    return azra_coords == rui_coords


def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """
    match = compare_records(azara_record, rui_record)
    if match:
        treasure = azara_record[0]
        coords = azara_record[1]
        name = rui_record[0]
        rui_x_coord = rui_record[1][0]
        rui_y_coord = rui_record[1][1]
        rui_coords = (rui_x_coord, rui_y_coord)
        quadrant = rui_record[2]
        return (treasure, coords, name, rui_coords, quadrant)

    return "not a match"


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    report = ""
    for record in combined_record_group:
        treasure = record[0]
        name = record[2]
        coords = record[3]
        quadrant = record[4]
        location = (treasure, name, coords, quadrant)
        report += f"{location}\n"

    return report
