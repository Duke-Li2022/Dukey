import pygame
import pygame.locals as pl
import threading
import socket_connect
from tkinter import messagebox

# 初始化 Pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)  # 淡蓝色

# 定义字体
font = pygame.font.Font('SmileySans-Oblique.ttf', 36)  # 标题字体
input_font = pygame.font.Font('SmileySans-Oblique.ttf', 24)  # 输入框字体
info_font = pygame.font.Font('SmileySans-Oblique.ttf', 28)  # 关于界面字体

# 牌图片文件夹
TILES_FOLDER = "tiles"

# 牌图片字典
tiles_images = {
    "一条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo1.png"), (50, 70)),
    "二条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo2.png"), (50, 70)),
    "三条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo3.png"), (50, 70)),
    "四条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo4.png"), (50, 70)),
    "五条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo5.png"), (50, 70)),
    "六条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo6.png"), (50, 70)),
    "七条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo7.png"), (50, 70)),
    "八条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo8.png"), (50, 70)),
    "九条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo9.png"), (50, 70)),
    "一万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character1.png"), (50, 70)),
    "二万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character2.png"), (50, 70)),
    "三万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character3.png"), (50, 70)),
    "四万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character4.png"), (50, 70)),
    "五万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character5.png"), (50, 70)),
    "六万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character6.png"), (50, 70)),
    "七万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character7.png"), (50, 70)),
    "八万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character8.png"), (50, 70)),
    "九万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character9.png"), (50, 70)),
    "一筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot1.png"), (50, 70)),
    "二筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot2.png"), (50, 70)),
    "三筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot3.png"), (50, 70)),
    "四筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot4.png"), (50, 70)),
    "五筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot5.png"), (50, 70)),
    "六筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot6.png"), (50, 70)),
    "七筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot7.png"), (50, 70)),
    "八筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot8.png"), (50, 70)),
    "九筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot9.png"), (50, 70)),
    "发财": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/DragonGreen.png"), (50, 70)),
    "红中": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/DragonRed.png"), (50, 70)),
    "白板": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/DragonWhite.png"), (50, 70)),
    "东风": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/WindEast.png"), (50, 70)),
    "南风": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/WindSouth.png"), (50, 70)),
    "西风": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/WindWest.png"), (50, 70)),
    "北风": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/WindNorth.png"), (50, 70)),
    "暗牌": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Unclear.png"), (50, 70)),
}

small_images = {
    "一条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo1.png"), (40, 56)),
    "二条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo2.png"), (40, 56)),
    "三条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo3.png"), (40, 56)),
    "四条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo4.png"), (40, 56)),
    "五条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo5.png"), (40, 56)),
    "六条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo6.png"), (40, 56)),
    "七条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo7.png"), (40, 56)),
    "八条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo8.png"), (40, 56)),
    "九条": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Bamboo9.png"), (40, 56)),
    "一万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character1.png"), (40, 56)),
    "二万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character2.png"), (40, 56)),
    "三万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character3.png"), (40, 56)),
    "四万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character4.png"), (40, 56)),
    "五万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character5.png"), (40, 56)),
    "六万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character6.png"), (40, 56)),
    "七万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character7.png"), (40, 56)),
    "八万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character8.png"), (40, 56)),
    "九万": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Character9.png"), (40, 56)),
    "一筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot1.png"), (40, 56)),
    "二筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot2.png"), (40, 56)),
    "三筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot3.png"), (40, 56)),
    "四筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot4.png"), (40, 56)),
    "五筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot5.png"), (40, 56)),
    "六筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot6.png"), (40, 56)),
    "七筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot7.png"), (40, 56)),
    "八筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot8.png"), (40, 56)),
    "九筒": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Dot9.png"), (40, 56)),
    "发财": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/DragonGreen.png"), (40, 56)),
    "红中": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/DragonRed.png"), (40, 56)),
    "白板": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/DragonWhite.png"), (40, 56)),
    "东风": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/WindEast.png"), (40, 56)),
    "南风": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/WindSouth.png"), (40, 56)),
    "西风": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/WindWest.png"), (40, 56)),
    "北风": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/WindNorth.png"), (40, 56)),
    "暗牌": pygame.transform.scale(pygame.image.load(f"{TILES_FOLDER}/Unclear.png"), (40, 56)),
}


def reset_game():
    global WHITE, BLACK, GRAY, LIGHT_BLUE, font, input_font, info_font
    # 定义颜色
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    LIGHT_BLUE = (173, 216, 230)  # 淡蓝色

    # 定义字体
    font = pygame.font.Font('SmileySans-Oblique.ttf', 36)  # 标题字体
    input_font = pygame.font.Font('SmileySans-Oblique.ttf', 24)  # 输入框字体
    info_font = pygame.font.Font('SmileySans-Oblique.ttf', 28)  # 关于界面字体


class Button:
    def __init__(self, x, y, width, height, callback, image=None, text=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.image = image
        self.text = text
        self.color = GRAY

    def draw(self, screen):
        if self.image:
            image_rect = self.image.get_rect(center=self.rect.center)
            screen.blit(self.image, image_rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            text_surf = font.render(self.text, True, BLACK)
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = text
        self.txt_surface = input_font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = BLACK if self.active else GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = input_font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_text(self):
        return self.text

    def clear_text(self):
        self.text = ''
        self.txt_surface = input_font.render(self.text, True, self.color)


class Game:
    def __init__(self):
        self.last_discarded = ""
        self.players = ["0-0", "0-0", "0-0", "0-0"]
        self.current_player_name = "0"
        reset_game()
        self.running = True
        self.current_screen = 'wait'

        self.find_turn_later = 0
        self.s = socket_connect.SocketConnect()

        # 设置窗口大小和标题
        SCREEN_WIDTH = 1200
        SCREEN_HEIGHT = 900
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Mahjong - Game')

        self.game_thread = None
        self.messages = []

        # 消息输入框和发送按钮
        self.message_input_box = InputBox(650, 700, 370, 40)
        self.send_button = Button(920, 750, 100, 40, self.send_message, text='Send')

        # 游戏状态
        self.hand_tiles = []
        self.id = 0
        self.hand_tiles_number = [0, 0, 0, 0]
        self.clear_tiles = [[], [], [], []]
        self.hand_buttons = []
        self.clear_buttons = []
        self.current_turn = False
        self.discard_pile = []
        self.able_list = []
        self.action_buttons = []

    def draw_title(self, text, x, y):
        title_font = pygame.font.Font('SmileySans-Oblique.ttf', 48)  # 大字体
        title = title_font.render(text, True, BLACK)
        self.screen.blit(title, (x, y))

    def back_to_menu(self):
        self.s.send("sys_bye")
        self.s.stop()
        self.running = False

    def start_game(self):
        self.current_screen = 'in_game'

    def check_for_messages(self):
        while self.running:
            message = self.s.read()
            if message:
                self.handle_message(message)

    def handle_message(self, message):
        if message.startswith("msg_"):
            self.messages.append(message[4:])
        if message.startswith("sys_game_start"):
            self.s.send("show_user")
            self.current_screen = 'in_game'
        elif message.startswith("sys_users_"):
            self.players = message.split("_")[2:-1]
            if self.find_turn_later != 0:
                for i in self.players:
                    if int(i[0]) == self.find_turn_later:
                        self.current_player_name = i
                        self.create_clear_tiles()
                        break
        elif message.startswith("sys_id_"):
            self.id = int(message.split("_")[2])
            print(self.id)
        elif message.startswith("sys_turn_"):
            find = False
            for i in self.players:
                if int(i[0]) == int(message.split("_")[2]):
                    self.current_player_name = i
                    self.create_clear_tiles()
                    find = True
                    break
            if not find:
                self.find_turn_later = int(message.split("_")[2])
        elif message.startswith("sys_drop"):
            self.handle_drop_command()
        elif message.startswith("sys_discard_"):
            self.last_discarded = message.split("_")[2]
        elif message.startswith("sys_get_"):
            tile = message.split("_")[2]
            self.hand_tiles.append(tile)
            self.create_hand_buttons()
        elif message.startswith("sys_hand_"):
            tiles = message.split("_")[2:-1]
            self.hand_tiles = tiles
            self.create_hand_buttons()
        elif message.startswith("sys_recent_"):
            self.discard_pile = message.split("_")[2:-1]
        elif message.startswith("sys_clear_"):
            t_user_num = int(message.split("_")[2]) - 1
            t_unclear_num = int(message.split("_")[3]) - 1
            t_clear_tiles = message.split("_")[4:-1]
            self.clear_tiles[t_user_num] = t_clear_tiles
            self.hand_tiles_number[t_user_num] = t_unclear_num
            self.create_clear_tiles()
        elif message.startswith("sys_able_list_"):
            self.able_list = message.split("_")[3:-1]
            self.create_action_buttons()
        elif message.startswith("sys_able_pung"):
            self.create_specific_action_buttons('碰')
        elif message.startswith("sys_able_clear_kong"):
            self.create_specific_action_buttons('明杠')
        elif message.startswith("sys_able_chow"):
            self.create_specific_action_buttons('吃')
        elif message.startswith("sys_able_hu"):
            self.create_specific_action_buttons('胡')
        elif message.startswith("sys_able_unclear_kong"):
            self.create_specific_action_buttons('暗杠')
        elif message.startswith("sys_err"):
            print("Error from server: ", message)
            messagebox.showerror(title="Error", message=message)
        elif message.startswith("sys_winner_"):
            winner_id = int(message.split("_")[2])
            print(f"Player {winner_id} won!")
            messagebox.showinfo(title="Game Over", message=f"Player {winner_id} won!")
        elif message.startswith("sys_score_"):
            score = message.split("_")[2]
            print(f"Score: {score}")
            messagebox.showinfo(title="Game Score", message=f"Score: {score}")

    def handle_drop_command(self):
        self.current_turn = True

    def create_hand_buttons(self):
        self.hand_buttons = []
        x = 100
        y = 800
        for tile in self.hand_tiles:
            image = tiles_images.get(tile)
            if image:
                button = Button(x, y, 50, 70, lambda t=tile: self.drop_tile(t), image=image)
                self.hand_buttons.append(button)
            else:
                button = Button(x, y, 50, 70, lambda t=tile: self.drop_tile(t), text=tile)
                self.hand_buttons.append(button)
            x += 60
        self.create_clear_tiles()

    def nothing_to_do(self):
        pass

    def create_clear_tiles(self):
        self.clear_buttons = []
        x_l = [90, 1080, 1000, 100]
        y_l = [740, 820, 100, 50]
        x_p = [45, 0, -45, 0]
        y_p = [0, -60, 0, 60]
        x_d = [0, 45, 0, -45]
        y_d = [0, 0, -60, 0]
        x_n = [590, 1000, 600, 120]
        y_n = [700, 450, 120, 450]
        n = self.id
        for p in range(4):
            m = (3 + n - p) % 4
            x = x_l[m]
            y = y_l[m]
            for tile in self.clear_tiles[p]:
                image = small_images.get(tile)
                if image:
                    button = Button(x, y, 40, 56, self.nothing_to_do, image=image)
                    self.clear_buttons.append(button)
                else:
                    button = Button(x, y, 40, 56, self.nothing_to_do, text=tile)
                    self.clear_buttons.append(button)
                x += x_p[m]
                y += y_p[m]
            if m != 0:
                x = x_l[m] + x_d[m]
                y = y_l[m] + y_d[m]
                for i in range(self.hand_tiles_number[p]):
                    image = small_images.get("暗牌")
                    if image:
                        button = Button(x, y, 40, 56, self.nothing_to_do, image=image)
                        self.clear_buttons.append(button)
                    else:
                        button = Button(x, y, 40, 56, self.nothing_to_do, text="暗牌")
                        self.clear_buttons.append(button)
                    x += x_p[m]
                    y += y_p[m]
            if int(self.current_player_name[0]) == p + 1:
                button = Button(x_n[m], y_n[m], 45, 40, self.nothing_to_do, text="X")
            else:
                button = Button(x_n[m], y_n[m], 45, 30, self.nothing_to_do, text="P" + self.players[p][0])
            self.clear_buttons.append(button)
        x = 140
        y = 240
        for i in range(len(self.discard_pile)):
            image = small_images.get(self.discard_pile[i])
            if image:
                button = Button(x, y, 40, 56, self.nothing_to_do, image=image)
                self.clear_buttons.append(button)
            else:
                button = Button(x, y, 40, 56, self.nothing_to_do, text=self.discard_pile[i])
                self.clear_buttons.append(button)
            x += 43
            if i % 12 == 11:
                x = 140
                y += 60

    def create_action_buttons(self):
        self.action_buttons = [
            Button(50, 350, 200, 50, lambda: self.send_action('1'), text='Action'),
            Button(300, 350, 200, 50, lambda: self.send_action('0'), text='Skip')
        ]

    def create_specific_action_buttons(self, action):
        self.action_buttons = [
            Button(50, 350, 200, 50, lambda: self.send_action('1'), text=action),
            Button(300, 350, 200, 50, lambda: self.send_action('0'), text='Skip')
        ]

    def drop_tile(self, tile):
        if self.current_turn:
            self.s.send(tile)
            self.current_turn = False

    def send_message(self):
        message = self.message_input_box.get_text()
        if message:
            self.s.send("m" + message)
            self.message_input_box.clear_text()

    def send_action(self, action):
        self.s.send(action)
        self.action_buttons = []
        self.able_list = []

    def game_loop(self, connected_socket):
        self.s.start(connected_socket)
        clock = pygame.time.Clock()
        self.current_screen = 'wait'

        title_x, title_y = 275, 50  # 大标题位置

        back_button = Button(450, 500, 200, 50, self.back_to_menu, text='Back')

        # 启动线程检测消息
        self.game_thread = threading.Thread(target=self.check_for_messages)
        self.game_thread.daemon = True
        self.game_thread.start()

        while self.running:
            for event in pygame.event.get():
                if event.type == pl.QUIT:
                    self.running = False
                    return False
                elif self.current_screen == 'wait':
                    back_button.handle_event(event)
                    self.message_input_box.handle_event(event)
                    self.send_button.handle_event(event)
                elif self.current_screen == 'in_game':
                    self.message_input_box.handle_event(event)
                    self.send_button.handle_event(event)
                    for button in self.hand_buttons:
                        button.handle_event(event)
                    for button in self.action_buttons:
                        button.handle_event(event)

            self.screen.fill(LIGHT_BLUE)  # 设置背景为淡蓝色

            if self.current_screen == 'wait':
                self.draw_title('Waiting Room', title_x, title_y)
                back_button.draw(self.screen)
                self.message_input_box.draw(self.screen)
                self.send_button.draw(self.screen)
                self.draw_messages()
            elif self.current_screen == 'in_game':
                self.draw_game()
                self.message_input_box.draw(self.screen)
                self.send_button.draw(self.screen)
                self.draw_messages()
                for button in self.hand_buttons:
                    button.draw(self.screen)
                for button in self.clear_buttons:
                    button.draw(self.screen)
                for button in self.action_buttons:
                    button.draw(self.screen)

            pygame.display.flip()
            clock.tick(30)

        return True

    def draw_game(self):
        # 绘制当前状态
        turn_text = "Current turn: " + self.current_player_name
        turn_surf = font.render(turn_text, True, BLACK)
        self.screen.blit(turn_surf, (140, 120))

        # 绘制玩家列表
        player_list_text = "Players: " + " , ".join(self.players)
        player_list_surf = info_font.render(player_list_text, True, BLACK)
        self.screen.blit(player_list_surf, (100, 1))

        # 绘制最近的弃牌
        last_discard_text = "Recent discarded: " + self.last_discarded
        discard_surf = font.render(last_discard_text, True, BLACK)
        self.screen.blit(discard_surf, (140, 160))

        # 绘制弃牌堆
        discard_pile_text = "Discard Pile: "
        discard_surf = info_font.render(discard_pile_text, True, BLACK)
        self.screen.blit(discard_surf, (140, 200))

        # 绘制可用操作列表
        if self.able_list:
            able_list_text = "Able actions: " + ", ".join(self.able_list)
            able_surf = info_font.render(able_list_text, True, BLACK)
            self.screen.blit(able_surf, (50, 400))

    def draw_messages(self):
        y = 650
        for message in self.messages[-8:]:  # 显示最近的8条消息
            msg_surf = info_font.render(message, True, BLACK)
            self.screen.blit(msg_surf, (650, y))
            y -= 35
