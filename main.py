import pygame,random
import sys

class Personagem:
    def __init__(self, nome, classe, hp, ataque, defesa, habilidade, velocidade):
        self.nome = nome
        self.classe = classe
        self.hp = hp
        self.ataque = ataque 
        self.defesa = defesa
        self.habilidade= habilidade
        self.velocidade = velocidade
    
    def atacar (self, inimigo):
        dano = self.ataque - self.defesa
        if dano > 0:
            inimigo.hp -= dano
            print(f"{self.nome} atacou {inimigo.nome} e causou {dano}!")

        def usar_habilidade(self, alvo = None):
            if self.habilidade:
                self.habilidade.ativar(alvo)

class habilidade_desc:
    def __init__ (self,nome, desc, efeito ):
        self.nome = nome
        self.desc = desc
        self.efeito = efeito
    def ativar (self, alvo):
        self.efeito (alvo)

    def luz_purificadora(alvo):
        cura = 2
        alvo.hp += cura
        print(f"{alvo.nome} é curado em {cura} HP!")

    def sombra_veloz(personagem):
        personagem.ataque += 2
        print(f"{personagem.nome} esta mais FORTEE!")

    def armadilha_reluzente(inimigo):
        dano = 3
        inimigo.hp -= dano
        print(f"Armadilha ativa! {inimigo.nome} sofre {dano} de dano!")

    def manto_da_escuridão(aliados):
        for aliado in aliados:
            aliado.ataque -= 2
            print("A precisão dos aliados diminui!")

    def golpe_pesado(inimigo):
        dano = 25
        inimigo.hp -= dano
        print(f"{inimigo.nome} sofre um golpe pesado e perde {dano} HP!")


class Botao():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, TELA):
		if self.image is not None:
			TELA.blit(self.image, self.rect)
		TELA.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def mudacor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
               

# personagens com habilidades
lia = Personagem("Lua", "Mágica", hp=20, ataque=5, defesa=2,
                 habilidade=habilidade_desc("Luz Purificadora", "Cura aliados", habilidade_desc.luz_purificadora), velocidade=1)

karo = Personagem("Karo", "Físico", hp=25, ataque=5, defesa=4,
                  habilidade=habilidade_desc("Sombra Veloz", "Aumenta velocidade de ataque", habilidade_desc.sombra_veloz), velocidade=2)

mira = Personagem("Mira", "Técnica", hp=15, ataque=4, defesa=2,
                  habilidade=habilidade_desc("Armadilha Reluzente", "Causa dano ao inimigo", habilidade_desc.armadilha_reluzente), velocidade=1)

eclipse = Personagem("Eclipse", "Mágica", hp=30, ataque=5, defesa=6,
                     habilidade=habilidade_desc("Manto da Escuridão", "Diminui precisão dos aliados", habilidade_desc.manto_da_escuridão), velocidade=2)

golem = Personagem("Golem de Sombra", "Físico", hp=30, ataque=4, defesa=5,
                   habilidade=habilidade_desc("Golpe Pesado", "Causa dano massivo", habilidade_desc.golpe_pesado), velocidade=2)

pygame.init()
TELA = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Sombra da Lua")

# Background da tela
imagem = pygame.image.load("tela de login.jpg")

def get_font(size):
    return pygame.font.Font("font.ttf", size)

# Botão de personagem
class caracteristicaBot:
    def __init__(self, name, pos, font):
        self.name = name
        self.rect = pygame.Rect(pos[0], pos[1], 200, 80)
        self.color = "White"
        self.selected = False
        self.font = font

    def desenho(self, TELA):
        pygame.draw.rect(TELA, self.color, self.rect, 0 if self.selected else 2)
        text_surface = self.font.render(self.name, True, "Black")
        text_rect = text_surface.get_rect(center=self.rect.center)
        TELA.blit(text_surface, text_rect)

    def handle_click(self):
        if not self.selected:
            self.selected = True
            self.color = "Green"
        else:
            self.selected = False
            self.color = "White"

# Função de seleção de personagens
def selecionar_personagens():
    character1 = caracteristicaBot("", (300, 250), get_font(35))
    character2 = caracteristicaBot("Karo", (300, 350), get_font(35))
    character3 = caracteristicaBot("Mira", (300, 450), get_font(35))
    characters = [character1, character2, character3]
    selected_count = 0

    while True:
        TELA.fill("black")

        SELECIONAR_TEXT = get_font(45).render("Selecione 2 personagens:", True, "White")
        SELECIONAR_RECT = SELECIONAR_TEXT.get_rect(center=(TELA.get_width() // 2, 150))
        TELA.blit(SELECIONAR_TEXT, SELECIONAR_RECT)

        CONFIRMAR_BUTTON = Botao(image=None, pos=(TELA.get_width() // 2, 600),
                                 text_input="CONFIRMAR", font=get_font(50), base_color="White", hovering_color="Green")

        CONFIRMAR_BUTTON.mudacor(pygame.mouse.get_pos())
        CONFIRMAR_BUTTON.update(TELA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONFIRMAR_BUTTON.checkForInput(pygame.mouse.get_pos()) and selected_count == 2:
                    print("Personagens selecionados confirmados!")
                    return
                for character in characters:
                    if character.rect.collidepoint(event.pos):
                        if character.selected:
                            character.handle_click()
                            selected_count -= 1
                        elif selected_count < 2:
                            character.handle_click()
                            selected_count += 1

        for character in characters:
            character.desenho(TELA)

        pygame.display.update()

# Função de opções
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        TELA.fill("white")

        OPTIONS_TEXT = get_font(45).render("NAO TEMOS OPÇOES AQUI.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(TELA.get_width() // 2, 260))
        TELA.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Botao(image=None, pos=(TELA.get_width() // 2, 460),
                             text_input="VOLTAR", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.mudacor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(TELA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Menu principal
def main_menu():
    while True:
        TELA.blit(imagem, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(TELA.get_width() // 2, 100))

        PLAY_BUTTON = Botao(image=pygame.image.load("usuais/Play Rect.png"), pos=(TELA.get_width() // 2, 250),
                            text_input="JOGAR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Botao(image=pygame.image.load("usuais/Options Rect.png"), pos=(TELA.get_width() // 2, 400),
                               text_input="OPÇÕES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Botao(image=pygame.image.load("usuais/Quit Rect.png"), pos=(TELA.get_width() // 2, 550),
                            text_input="SAIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        TELA.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.mudacor(MENU_MOUSE_POS)
            button.update(TELA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    selecionar_personagens()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Inicializa o menu principal
main_menu()
