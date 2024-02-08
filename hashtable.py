class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function_1(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return ((1731 * key + 520123) % 524287) % self.size

    def hash_function_3(self, key):
        return hash(key) % self.size

    def insert(self, key, command_num, string):
        index = None
        if command_num == 1:
            index = self.hash_function_1(key)
        elif command_num == 2:
            index = self.hash_function_2(key)
        elif command_num == 3:
            index = self.hash_function_3(key)

        if index is not None:
            self.table[index].insert(0, string)

    def delete(self, string):
        for slot in self.table:
            if string in slot:
                slot.remove(string)


hash_table = Hashtable(32)


def process_commands(commands, hash_function):
    hash_type = int(hash_function)
    for command in commands:
        if command.startswith("del "):
            string_to_delete = command[4:]
            hash_table.delete(string_to_delete)
        else:
            key = sum(ord(char) for char in command)
            hash_table.insert(key, hash_type, command)


def generate_table():
    table = {}
    for i, slot in enumerate(hash_table.table):
        table[i] = slot
    return table
