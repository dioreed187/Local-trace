class LocationSharingApp:
    def __init__(self):
        self.users = {}

    def add_user(self, username, ghost_mode=False):
        self.users[username] = {'visible': not ghost_mode, 'location': (0, 0)}

    def update_location(self, username, new_location):
        if username in self.users:
            self.users[username]['location'] = new_location

    def set_ghost_mode(self, username, enabled):
        if username in self.users:
            self.users[username]['visible'] = not enabled

    def get_visible_users(self):
        return {username: data['location'] for username, data in self.users.items() if data['visible']}

    def share_location(self, username):
        if username in self.users:
            return self.users[username]['location'] if self.users[username]['visible'] else 'User is in ghost mode.'


# Example usage:
app = LocationSharingApp()
app.add_user('Alice', ghost_mode=True)
app.add_user('Bob')
app.update_location('Bob', (10, 20))
print(app.get_visible_users())  # Should only show Bob's location
print(app.share_location('Alice'))  # Should indicate ghost mode