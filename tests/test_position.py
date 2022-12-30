from pychess.position import Position


def test_position_create_from_entry():
    expected_result = (4, 4)

    p = Position.from_entry('5', 'e')
    result = (p.x, p.y)

    assert result == expected_result


def test_position_create():
    expected_result = (5, 5)

    p = Position(5, 5)
    result = (p.x, p.y)
    assert result == expected_result
