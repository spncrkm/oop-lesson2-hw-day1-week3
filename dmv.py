class Vehicle:

    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    
    def update_owner(self, new_owner):
        self.owner = new_owner

        