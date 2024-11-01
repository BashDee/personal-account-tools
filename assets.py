class Assets:
    """Assets"""

    def __init__(self):
        self.assets = {}
        self.user_actions = {}

    def add_asset(self, user, id, name, value):
        self.assets[id] = {'name': name, 'value': value}
        if user not in self.user_actions:
            self.user_actions