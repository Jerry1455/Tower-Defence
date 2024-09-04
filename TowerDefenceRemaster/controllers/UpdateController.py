class UpdateController:
    def __init__(self):
        self.queue = []
    
    def register(self, entity):
        self.queue.append(entity)
    
    def update(self, screen):
        for entity in self.queue:
            entity.draw(screen)