import pygame
pygame.init()

engine = None
default_width = 1280
default_height = 720

class Engine:
    def __init__(self, game_title):
        global engine

        engine = self
        self.active_objs = []

        self.background_drawables = []
        self.drawables = []
        self.ui_drawables = []

        from core.camera import create_screen
        self.clear_color = (30, 150, 240)

        self.screen = create_screen(default_width, default_height, game_title)
        self.stages = {}
        self.current_stage = None

    def register(self, stage_name, func):
        self.stages[stage_name] = func

    def switch_to(self, stage_name):
        self.reset()
        self.current_stage = stage_name
        func = self.stages[stage_name]
        print(f"Switching to {self.current_stage}")
        func()

    def run(self):
        from core.input import keys_down

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    keys_down.add(event.key)
                elif event.type == pygame.KEYUP:
                    keys_down.remove(event.key)

            for a in self.active_objs:
                a.update()

            self.screen.fill(self.clear_color)

            for d in self.background_drawables:
                d.draw(self.screen)

            for d in self.drawables:
                d.draw(self.screen)

            for d in self.ui_drawables:
                d.draw(self.screen)

            pygame.display.flip()

            pygame.time.delay(17)

        pygame.quit()

    def reset(self):
        from components.physics import reset_physics
        reset_physics()
        self.active_objs.clear()
        self.background_drawables.clear()
        self.drawables.clear()
        self.ui_drawables.clear()