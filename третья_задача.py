import os
import sys

import pygame
import requests

spn1 = 0.002
spn2 = 0.002
x, y = 37.530887, 55.703118
step = 0.001
map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={spn1},{spn2}&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
speed = 0.001
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True


def rebield():
    global map_request, response, map_file
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={spn1},{spn2}&l=map"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                spn1 += speed
                spn2 += speed
                rebield()
            elif event.key == pygame.K_UP:
                y += step
                rebield()
            elif event.key == pygame.K_DOWN:
                y -= step
                rebield()
            elif event.key == pygame.K_LEFT:
                x -= step
                rebield()
            elif event.key == pygame.K_RIGHT:
                x += step
                rebield()
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()

os.remove(map_file)
