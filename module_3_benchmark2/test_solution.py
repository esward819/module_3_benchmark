from solution import KeyCodeDoorLock

def test_initial_state():
    lock = KeyCodeDoorLock("1234")
    assert lock.is_locked() is True
    assert lock.is_hard_locked() is False

def test_unlocking():
    lock = KeyCodeDoorLock("1234")
    assert lock.is_locked() is True
    lock.enter_code("1234")
    assert lock.is_locked() is False

def test_different_code():
    lock = KeyCodeDoorLock("hello")
    assert lock.is_locked() is True
    lock.enter_code("hello")
    assert lock.is_locked() is False

def test_hard_locking():
    lock = KeyCodeDoorLock("1234")
    lock.enter_code("1")
    assert lock.is_hard_locked() is False
    lock.enter_code("2")
    assert lock.is_hard_locked() is False
    lock.enter_code("3")
    assert lock.is_hard_locked() is True


def test_cannot_unlock_after_hard_locking():
    lock = KeyCodeDoorLock("1234")
    lock.enter_code("1")
    assert lock.is_hard_locked() is False
    lock.enter_code("2")
    assert lock.is_hard_locked() is False
    lock.enter_code("3")
    assert lock.is_hard_locked() is True
    lock.enter_code("1234")
    assert lock.is_locked() is True
    assert lock.is_hard_locked() is True

def test_unlocking_resets_fail_count():
    lock = KeyCodeDoorLock("1234")
    lock.enter_code("1")
    assert lock.is_hard_locked() is False
    lock.enter_code("2")
    assert lock.is_hard_locked() is False
    lock.enter_code("1234")
    assert lock.is_hard_locked() is False
    lock.enter_code("1")
    assert lock.is_hard_locked() is False
    lock.enter_code("2")
    assert lock.is_hard_locked() is False
    lock.enter_code("3")
    assert lock.is_hard_locked() is True

def test_resetting():
    lock = KeyCodeDoorLock("1234")
    lock.enter_code("1234")
    lock.reset("4321")
    assert lock.is_locked() is True
    lock.enter_code("4321")
    assert lock.is_locked() is False

def test_cannot_reset_locked():
    lock = KeyCodeDoorLock("1234")
    lock.reset("4321")
    assert lock.is_locked() is True
    lock.enter_code("4321")
    assert lock.is_locked() is True


def test_locking():
    lock = KeyCodeDoorLock("1234")
    lock.enter_code("1234")
    lock.lock()
    assert lock.is_locked() is True