'''
Algoritmo para o jogo 2048:
1. Definir uma matriz 4x4 preenchida por zeros.
2. Gerar um número aleatório (2 ou 4) e colocá-lo em uma posição aleatória da matriz.
3. Definir a grid do jogo usando a biblioteca Pygame.
4. Sempre que o jogador fizer um movimento (para cima, para baixo, para a esquerda ou para a direita):
    a. Mover os números na direção do movimento, combinando os números iguais (somando-os) e preenchendo os espaços vazios com zeros.
    b. Gerar um novo número aleatório (2 ou 4) e colocá-lo em uma posição aleatória da matriz.
    c. Verificar se o jogo terminou (se não houver mais movimentos possíveis).
5. Exibir a matriz atualizada na tela usando Pygame, com cada número representado por um quadrado colorido.
6. Repetir os passos 4 e 5 até que o jogo termine.
7. O jogo termina quando não houver mais movimentos possíveis ou o jogador alcançar o número 2048 em algum quadrado.
'''

import pygame
import random
import sys
import os 
import time

pygame.init()

tamanho_grid = 4
tamanho_celula = 100
tamanho_tela = tamanho_grid * tamanho_celula
tela = pygame.display.set_mode((tamanho_tela, tamanho_tela))
fps = 60


pygame.display.set_caption("2048")
fonte = pygame.font.Font(None, 40)
clock = pygame.time.Clock()


matriz = [[0 for i in range(tamanho_grid)] for j in range(tamanho_grid)]

def gerar_numero():
    numero = random.choice([2, 4])
    while True:
        linha = random.randint(0, tamanho_grid - 1)
        coluna = random.randint(0, tamanho_grid - 1)
        if matriz[linha][coluna] == 0:
            matriz[linha][coluna] = numero
            break

def mover_para_cima():
    matriz_antes = [linha[:] for linha in matriz]
    for coluna in range(tamanho_grid):
        merged = [False] * tamanho_grid
        for linha in range(1, tamanho_grid):
            if matriz[linha][coluna] != 0:
                for k in range(linha, 0, -1):
                    if matriz[k-1][coluna] == 0:
                        matriz[k-1][coluna] = matriz[k][coluna]
                        matriz[k][coluna] = 0
                    elif matriz[k-1][coluna] == matriz[k][coluna] and not merged[k-1]:
                        matriz[k-1][coluna] *= 2
                        matriz[k][coluna] = 0
                        merged[k-1] = True
                        break
                    else:
                        break
    return matriz != matriz_antes

def mover_para_baixo():
    matriz_antes = [linha[:] for linha in matriz]
    for coluna in range(tamanho_grid):
        merged = [False] * tamanho_grid
        for linha in range(tamanho_grid - 1, -1, -1):
            if matriz[linha][coluna] != 0:
                for k in range(linha, tamanho_grid - 1):
                    if matriz[k+1][coluna] == 0:
                        matriz[k+1][coluna] = matriz[k][coluna]
                        matriz[k][coluna] = 0
                    elif matriz[k+1][coluna] == matriz[k][coluna] and not merged[k+1]:
                        matriz[k+1][coluna] *= 2
                        matriz[k][coluna] = 0
                        merged[k+1] = True
                        break
                    else:
                        break
    return matriz != matriz_antes

def mover_para_esquerda():
    matriz_antes = [linha[:] for linha in matriz]
    for linha in range(tamanho_grid):
        merged = [False] * tamanho_grid
        for coluna in range(1, tamanho_grid):
            if matriz[linha][coluna] != 0:
                for k in range(coluna, 0, -1):
                    if matriz[linha][k-1] == 0:
                        matriz[linha][k-1] = matriz[linha][k]
                        matriz[linha][k] = 0
                    elif matriz[linha][k-1] == matriz[linha][k] and not merged[k-1]:
                        matriz[linha][k-1] *= 2
                        matriz[linha][k] = 0
                        merged[k-1] = True
                        break
                    else:
                        break
    return matriz != matriz_antes

def mover_para_direita():
    matriz_antes = [linha[:] for linha in matriz]
    for linha in range(tamanho_grid):
        merged = [False] * tamanho_grid
        for coluna in range(tamanho_grid - 1, -1, -1):
            if matriz[linha][coluna] != 0:
                for k in range(coluna, 3):
                    if matriz[linha][k+1] == 0:
                        matriz[linha][k+1] = matriz[linha][k]
                        matriz[linha][k] = 0
                    elif matriz[linha][k+1] == matriz[linha][k] and not merged[k+1]:
                        matriz[linha][k+1] *= 2
                        matriz[linha][k] = 0
                        merged[k+1] = True
                        break
                    else:
                        break
    return matriz != matriz_antes

def verificar_derrota():
    for linha in range(tamanho_grid):
        for coluna in range(tamanho_grid):
            if matriz[linha][coluna] == 0:
                return False
            if (coluna > 0 and matriz[linha][coluna] == matriz[linha][coluna - 1]) or (coluna < 3 and matriz[linha][coluna] == matriz[linha][coluna + 1]):
                return False
            if (linha > 0 and matriz[linha][coluna] ==  matriz[linha - 1][coluna]) or (linha < 3 and matriz[linha][coluna] == matriz[linha + 1][coluna]):
                return False
    return True

def verificar_vitoria():
    for linha in range(tamanho_grid):
        for coluna in range(tamanho_grid):
            if matriz[linha][coluna] == 2048:
                return True
    return False

cores = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

def desenhar_matriz( ):
    for linha in range(tamanho_grid):
        for coluna in range(tamanho_grid):
            valor = matriz[linha][coluna]
            cor = cores.get(valor, (60, 58, 50))
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
            if valor != 0:
                texto = fonte.render(str(valor), True, (0, 0, 0))
                texto_rect = texto.get_rect(center=(coluna * tamanho_celula + tamanho_celula // 2, linha * tamanho_celula + tamanho_celula // 2))
                tela.blit(texto, texto_rect)

gerar_numero()

def main():
    jogando = True
    while jogando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    if mover_para_cima():
                        gerar_numero()
                elif evento.key == pygame.K_DOWN:
                    if mover_para_baixo():
                        gerar_numero()
                elif evento.key == pygame.K_LEFT:
                    if mover_para_esquerda():
                        gerar_numero()
                elif evento.key == pygame.K_RIGHT:
                    if mover_para_direita():
                        gerar_numero()
        tela.fill((0, 0, 0))
        tela.fill((187, 173, 160))
        desenhar_matriz()
        pygame.display.flip()
        clock.tick(fps)

        if verificar_vitoria():
            texto_vitoria = fonte.render("Parabéns! Você venceu!", True, (0, 255, 0))
            texto_rect = texto_vitoria.get_rect(center=(tamanho_tela // 2, tamanho_tela // 2))
            tela.blit(texto_vitoria, texto_rect)
            pygame.display.flip()
            time.sleep(3)
            print("Parabéns! Você venceu!")
            jogando = False
        elif verificar_derrota():
            print("Game Over! Você perdeu!")
            texto_derrota = fonte.render("Game Over! Você perdeu!", True, (255, 0, 0))
            texto_rect = texto_derrota.get_rect(center=(tamanho_tela // 2, tamanho_tela // 2))
            tela.blit(texto_derrota, texto_rect)
            pygame.display.flip()
            time.sleep(3)
            jogando = False
main()
pygame.quit()