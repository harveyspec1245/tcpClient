
def capital_case(x):
    return x.capitalize()


def test_capital_case() -> None:
    assert capital_case('semaphore') == 'Semaphore'
