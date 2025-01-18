class Memory:
    def __init__(self):
        self.memory = []

    def remember(self, user_input, bot_response):
        self.memory.append((user_input, bot_response))

    def get_memory(self):
        return self.memory[-5:]  # Get the last 5 exchanges for context