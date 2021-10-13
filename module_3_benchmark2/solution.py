class KeyCodeDoorLock:

    count = 0

    def __init__(self, code):
        self.code = code
        self.locked = True
        self.hard_lock = False

    def enter_code(self, entry):
        self.entry = entry
        if self.entry == self.code:
            if self.hard_lock == False:
                self.locked = False
                self.count -= self.count
            else:
                self.locked = True
        elif self.entry != self.code:
            self.count += 1
            if self.count >= 3:
                self.hard_lock = True

    def reset(self, new_code):
        if self.locked == False:
            self.new_code = new_code
            self.code = self.new_code
            self.locked = True

    def is_locked(self):
        return self.locked

    def is_hard_locked(self):
        return self.hard_lock

    def lock(self):
        self.locked = True