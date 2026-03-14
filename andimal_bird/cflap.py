import pygame
import random

class Bird:
    def __init__(self, x, y, image):
        # store starting position so we can reset easily
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.vy = 0                          # vertical velocity
        self.gravity = 0.5
        self.jump_force = -9
        self.image = pygame.transform.scale(image, (50, 50))
        self.alive = True

    def jump(self):
        if self.alive:
            self.vy = self.jump_force

    def update(self):
        if not self.alive:
            return
        self.vy += self.gravity              # gravity pulls down
        self.y += self.vy

        # hit ceiling or floor
        if self.y < 0 or self.y > 590:
            self.alive = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, int(self.y)))

    def get_rect(self):
        # slightly smaller than image so collisions feel fair
        return pygame.Rect(self.x + 5, self.y + 5, 40, 40)

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.vy = 0
        self.alive = True


class Pipe:
    WIDTH = 60
    GAP = 160
    SPEED = 3

    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(120, 400)  # centre of the gap
        self.scored = False                     # so we only count score once

    def update(self):
        self.x -= self.SPEED

    def draw(self, screen):
        top_height = self.gap_y - self.GAP // 2
        bot_y      = self.gap_y + self.GAP // 2

        # top pipe
        pygame.draw.rect(screen, (0, 180, 0), (self.x, 0, self.WIDTH, top_height))
        # bottom pipe
        pygame.draw.rect(screen, (0, 180, 0), (self.x, bot_y, self.WIDTH, 640))

    def is_off_screen(self):
        return self.x < -self.WIDTH

    def collides_with(self, bird_rect):
        top_rect = pygame.Rect(self.x, 0,          self.WIDTH, self.gap_y - self.GAP // 2)
        bot_rect = pygame.Rect(self.x, self.gap_y + self.GAP // 2, self.WIDTH, 640)
        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect)

    def bird_passed(self, bird_x):
        # returns True the exact frame the bird crosses the pipe centre
        if not self.scored and self.x + self.WIDTH < bird_x:
            self.scored = True
            return True
        return False


class Game:
    PIPE_SPAWN_INTERVAL = 90   # frames between new pipes

    def __init__(self, screen, clock, bg, character_image):
        self.screen = screen
        self.clock = clock
        self.bg = bg
        self.bird = Bird(80, 300, character_image)
        self.pipes = []
        self.score = 0
        self.frame = 0
        self.state = 'playing'               # 'playing' or 'dead'
        self.font = pygame.font.SysFont(None, 48)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                is_space = (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)
                is_click = (event.type == pygame.MOUSEBUTTONDOWN)
                if is_space or is_click:
                    if self.state == 'playing':
                        self.bird.jump()
                    elif self.state == 'dead':
                        self.reset()

    def update(self):
        if self.state != 'playing':
            return

        self.bird.update()

        # spawn pipes on a timer
        self.frame += 1
        if self.frame % self.PIPE_SPAWN_INTERVAL == 0:
            self.pipes.append(Pipe(640))

        # update pipes, check score + collision
        for pipe in self.pipes:
            pipe.update()
            if pipe.bird_passed(self.bird.x):
                self.score += 1
            if pipe.collides_with(self.bird.get_rect()):
                self.bird.alive = False

        # remove off-screen pipes
        self.pipes = [p for p in self.pipes if not p.is_off_screen()]

        if not self.bird.alive:
            self.state = 'dead'

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        c="ok"

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.bird.draw(self.screen)

        # score
        score_surf = self.font.render(str(self.score), True, (255, 255, 255))
        self.screen.blit(score_surf, (160, 40))

        # game over overlay
        if self.state == 'dead':
            msg = self.font.render('GAME OVER ', True, (200, 0, 0))
            self.screen.blit(msg, (50, 280))
            
            

    def reset(self):
        self.bird.reset()
        self.pipes = []
        self.score = 0
        self.frame = 0
        self.state = 'playing'

    def run(self):
        while self.state != "dead":
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)