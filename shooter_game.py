from pygame import *
from random import randint
#Arka plan müziği
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

font.init()
font2 = font.Font(None,36)

#böyle resimlere ihtiyacımız var:
img_back = "galaxy.jpg" #oyunun arka planı
img_hero = "rocket.png" #kahraman
img_enemey = "ufo.png" 

score = 0
lost = 0


#sprite'lar için ebeveyn sınıfı
class GameSprite(sprite.Sprite):
 #Sınıf kurucusu
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Sınıf yapıcısını (Sprite) çağırın:
       sprite.Sprite.__init__(self)


       # Her sprite image - resim özelliğini depolamalıdır
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       # Her sprite, içine yazıldığı dikdörtgenin  rect özelliğini saklamalıdır
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #pencereye kahraman çizen yöntem
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#ana oyuncunun sınıfı
class Player(GameSprite):
   #Sprite'ı klavye oklarıyla kontrol etme yöntemi
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 # atış yöntemi (orada bir mermi oluşturmak için oyuncunun yerini kullanırız)
   def fire(self):
       pass

class Enemy(GameSprite):
    def update (self):
        self.rect.y += self.speed
        global lost

        if self.rect.y > win_height:
            self.rect.x = randint(80,win_width - 80)
            self.rect.y = 0
            lost = lost+1

#Bir pencere oluştur
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


#sozdayem spraytyvolume_up16 / 5.000Çeviri sonuçları# sprite oluştur 
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range (1,6):
    monster = Enemy(img_enemey,randint(80,win_width - 80),-40,80,50,randint(1,5))
    monsters.add(monster)
# "oyun bitti" değişkeni: True olduğunda, sprite ana döngüde çalışmayı durdurur
finish = False
#Ana oyun döngüsü:
run = True #bayrak pencereyi kapat düğmesiyle sıfırlanır
while run:
   #Kapat düğmesindeki olayı tıklayın
   for e in event.get():
       if e.type == QUIT:
           run = False


   if not finish:
       # arka planı güncelliyoruz
       window.blit(background,(0,0))
       

       text = font2.render("Score: "+ str(score),1,(255,255,255))
       window.blit(text,(10,20))
    


       #sprite hareketleri üretiyoruz
       ship.update()
       monsters.update()



       #Döngünün her yinelemesinde onları yeni bir konumda güncelliyoruz
       ship.reset()
       monsters.draw(window)


       display.update()
   #loop her 0,05 saniyede bir çalışır
   time.delay(50)
