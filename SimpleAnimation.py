"""import pygame

# 初期化
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Animation")

# 色の定義
WHITE = (255, 255, 255)

# 円の設定
x, y = 100, HEIGHT // 2
radius = 30
speed = 5
direction = 1
color = [255, 0, 0]

# メインループ
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 円の移動
    x += speed * direction
    if x + radius > WIDTH or x - radius < 0:
        direction *= -1  # 反転
    
    # 色を変化させる
    color[0] = (color[0] + 2) % 256
    color[1] = (color[1] + 3) % 256
    color[2] = (color[2] + 5) % 256
    
    # 円を描画
    pygame.draw.circle(screen, color, (x, y), radius)
    
    # 画面更新
    pygame.display.flip()
    clock.tick(60)  # 60FPS

pygame.quit()"""
import pygame

# 初期化
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Animation")

# 色の定義
WHITE = (255, 255, 255)

# 円1の設定
x1, y1 = 100, HEIGHT // 2
radius1 = 30
speed1 = 5
direction1 = 1
color1 = [255, 0, 0]
# 円2の設定
x2, y2 = 100, HEIGHT // 2
radius2 = 30
speed2 = 5
direction2 = 1
color2 = [255, 0, 0]
# 円3の設定
x3=0
y3 =600
radius3 = 30
#speed3 = 5
#direction3 = 1
velocity=[5,-20]
accel=(0,0.5)
color3 = [255, 0, 0]
# メインループ
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 円1の移動
    x1 += speed1 * direction1
    if x1 + radius1 > WIDTH or x1 - radius1 < 0:
        direction1 *= -1  # 反転
    #円2の移動
    x2 += speed2 * direction2
    y2 += speed2 * direction2
    if x2 + radius2 > WIDTH or x2 - radius2 < 0 or y2 + radius2 > WIDTH or y2 - radius2 < -10:
        direction2 *= -1  # 反転
    #円3の移動
    #x3 += speed2 * direction2
    #y2 += speed2 * direction2
    velocity[0]+=accel[0]
    x3+=velocity[0]
    velocity[1]+=accel[1]
    y3+=velocity[1]
    if x3>800:
        x3=0
    if y3>600:
        velocity[1]=-20
    """if x2 + radius2 > WIDTH or x2 - radius2 < 0 or y2 + radius2 > WIDTH or y2 - radius2 < -10:
        direction2 *= -1  # 反転"""
    
    # 円1の色を変化させる
    color1[0] = (color1[0] + 2) % 256
    color1[1] = (color1[1] + 3) % 256
    color1[2] = (color1[2] + 5) % 256
    # 円2の色を変化させる
    color2[0] = (color2[0] + 2) % 256
    color2[1] = (color2[1] + 3) % 256
    color2[2] = (color2[2] + 5) % 256
    # 円3の色を変化させる
    color3[0] = (color3[0] + 2) % 256
    color3[1] = (color3[1] + 3) % 256
    color3[2] = (color3[2] + 5) % 256
    
    # 円1を描画
    pygame.draw.circle(screen, color1, (x1, y1), radius1)
    # 円2を描画
    pygame.draw.circle(screen, color2, (x2, y2), radius2)
    # 円1を描画
    pygame.draw.circle(screen, color3, (x3, y3), radius3)
    
    # 画面更新
    pygame.display.flip()
    clock.tick(60)  # 60FPS

pygame.quit()

