#coding:utf-8
import pygame

class Ship(object):
    """控制飞船的类"""

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  #加载飞船图片
        self.rect = self.image.get_rect() #得到飞船的矩形
        self.screen_rect = screen.get_rect() #得到屏幕的矩形

        #将每艘新飞船放在屏幕底部
        self.rect.centerx = self.screen_rect.centerx  #将飞船的矩形的x轴位置放在屏幕的x轴位置
        self.rect.bottom = self.screen_rect.bottom #将飞船放在屏幕底部
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        

