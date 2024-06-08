import time
import pygame
import pygame.locals as pl
import socket
from tkinter import messagebox

import game

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mahjong - Menu')

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)  # 淡蓝色

# 定义字体
font = pygame.font.Font('SmileySans-Oblique.ttf', 36)  # 标题字体
input_font = pygame.font.Font('SmileySans-Oblique.ttf', 24)  # 输入框字体
info_font = pygame.font.Font('SmileySans-Oblique.ttf', 28)  # 关于界面字体

# 全局变量
ip_input = None
port_input = None
name_input = None

connected_socket = None


def reset_pygame():
    global SCREEN_WIDTH, SCREEN_HEIGHT, screen, WHITE, BLACK, GRAY, LIGHT_BLUE, font, input_font, info_font
    # 设置窗口大小和标题
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Mahjong - Menu')

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
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.color = GRAY

    def draw(self, screen):
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
        self.txt_surface = input_font.render(text, True, self.color)  # 使用较小的字体
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
                    print(self.text)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = input_font.render(self.text, True, self.color)  # 使用较小的字体

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


def draw_label(text, x, y):
    label = font.render(text, True, BLACK)
    screen.blit(label, (x, y))


def draw_title(text, x, y):
    title_font = pygame.font.Font('SmileySans-Oblique.ttf', 48)  # 大字体
    title = title_font.render(text, True, BLACK)
    screen.blit(title, (x, y))


def test_connection():
    global ip_input, port_input
    print("测试连接")
    ip = ip_input.text
    port = int(port_input.text)

    try:
        # 创建套接字并连接到指定的 IP 地址和端口
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        start_time = time.time()  # 开始计时
        s.connect((ip, port))
        end_time = time.time()  # 结束计时

        latency = (end_time - start_time) * 1000  # 计算延迟，单位为毫秒

        # 发送消息
        message = "test\n"
        s.sendall(message.encode())

        # 接收回复
        data = str(s.recv(1024).decode()).split("\n")[0].split("\r")[0]
        print(data)

        # 关闭连接
        s.close()

        if data == "MahjongGame":
            messagebox.showinfo(title="Check Success", message=f"Check Success\nLatency: {latency:.2f} ms")

    except socket.timeout:
        messagebox.showerror(title="Connection Timeout", message="Connection timeout. Please check the IP and port.")

    except Exception as e:
        messagebox.showerror(title="Connection Error", message=str(e))


def start_multi_player():
    global current_screen
    current_screen = 'wait'


def confirm_name():
    global current_screen, connected_socket
    # 在此处添加确认名称后的处理逻辑
    if len(name_input.text) == 0 or "_" in name_input.text:
        messagebox.showerror(title="Name Error", message="Name should not be null or include '_'.")
        return
    else:
        pass

    print(f"Player name confirmed: {name_input.text}")
    global ip_input, port_input
    ip = ip_input.text
    port = int(port_input.text)

    try:
        # 创建套接字并连接到指定的 IP 地址和端口
        connected_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connected_socket.settimeout(3)
        connected_socket.connect((ip, port))

        # 发送消息
        message = "ready\n"
        connected_socket.sendall(message.encode())

        # 接收回复
        data = str(connected_socket.recv(1024).decode()).split("\n")[0].split("\r")[0]
        print(data)

        # 发送名称
        message = name_input.text + "\n"
        connected_socket.sendall(message.encode())

        # 接收回复
        data = str(connected_socket.recv(1024).decode()).split("\n")[0].split("\r")[0]
        print(data)

        if data == "sys_ready":
            g = game.Game()
            if g.game_loop(connected_socket):
                connected_socket = None
            reset_pygame()

    except socket.timeout:
        messagebox.showerror(title="Connection Timeout", message="Connection timeout. Please check the IP and port.")

    except Exception as e:
        messagebox.showerror(title="Connection Error", message=str(e))


def show_about():
    global current_screen
    current_screen = 'about'


def back_to_menu():
    global current_screen
    current_screen = 'menu'


def start_game():
    global current_screen
    current_screen = 'in_game'


def main():
    clock = pygame.time.Clock()
    global current_screen
    current_screen = 'menu'

    title_x, title_y = 275, 50  # 大标题位置
    ip_label_x, ip_label_y = 150, 150
    port_label_x, port_label_y = 150, 200
    input_box_x = 300

    global ip_input, port_input, name_input
    ip_input = InputBox(input_box_x, 150, 200, 40, '127.0.0.1')
    port_input = InputBox(input_box_x, 200, 200, 40, '2013')
    name_input = InputBox(input_box_x, 250, 200, 40, '')

    test_button = Button('Test Connect', 300, 250, 200, 50, test_connection)
    multi_player_button = Button('Login Server', 300, 310, 200, 50, start_multi_player)
    about_button = Button('About', 300, 430, 200, 50, show_about)

    back_button = Button('Back', 300, 500, 200, 50, back_to_menu)
    confirm_name_button = Button('Confirm Name', 300, 370, 200, 50, confirm_name)

    input_boxes = [ip_input, port_input]
    menu_buttons = [test_button, multi_player_button, about_button]
    wait_buttons = [name_input, confirm_name_button]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pl.QUIT:
                running = False
            if current_screen == 'menu':
                for box in input_boxes:
                    box.handle_event(event)
                for button in menu_buttons:
                    button.handle_event(event)
            elif current_screen == 'about':
                back_button.handle_event(event)
            elif current_screen == 'wait':
                name_input.handle_event(event)
                back_button.handle_event(event)
                confirm_name_button.handle_event(event)
            elif current_screen == 'in_game':
                back_button.handle_event(event)

        screen.fill(LIGHT_BLUE)  # 设置背景为淡蓝色

        if current_screen == 'menu':
            draw_title('Mahjong Game', title_x, title_y)  # 绘制大标题
            draw_label('IP Address', ip_label_x, ip_label_y)
            draw_label('Port', port_label_x, port_label_y)

            for box in input_boxes:
                box.draw(screen)
            for button in menu_buttons:
                button.draw(screen)
        elif current_screen == 'about':
            about_text = [
                "Mahjong Game",
                "This is a mahjong game client.",
                "You need to connect to our server to play."
            ]
            for i, line in enumerate(about_text):
                text_surface = info_font.render(line, True, BLACK)
                screen.blit(text_surface, (100, 150 + i * 40))
            back_button.draw(screen)
        elif current_screen == 'wait':
            draw_title('Waiting Room', title_x, title_y)
            draw_label('Your Name', ip_label_x, ip_label_y + 100)
            name_input.draw(screen)
            confirm_name_button.draw(screen)
            back_button.draw(screen)
        elif current_screen == 'in_game':
            draw_title('Game in Progress', title_x, title_y)
            back_button.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
    if connected_socket is not None:
        message = "sys_bye\n"
        connected_socket.sendall(message.encode())
        connected_socket.close()
