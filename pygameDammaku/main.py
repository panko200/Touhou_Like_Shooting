import pygame as pg
import copy
import math
import random as rd

# PlayerCharacterクラスの定義 [ここから]

class PlayerCharacter:

  # コンストラクタ
  def __init__(self,name,init_pos,init_velocity,img_path,bullet_rate, bullet_type):
    self.pos  = pg.Vector2(init_pos)
    self.velocity = float(init_velocity)
    self.size = pg.Vector2(48,64)
    self.middle = pg.Vector2(self.size[0] / 2,self.size[1] / 2)
    self.Countermeasures = pg.Vector2(16,16)
    self.name = str(name)
    self.bullet_rate = bullet_rate
    self.sub_bullet_rate = 0
    self.bullet_type = bullet_type
    self.lv = 0
    img_raw = pg.image.load(img_path)
    self.__img_arr = []
    for i in range(3):
      p = pg.Vector2(24*i,0)
      tmp = img_raw.subsurface(pg.Rect(p,(24,32)))
      tmp = pg.transform.scale(tmp, self.size)
      self.__img_arr.append(tmp)
    self.__img_arr.append(self.__img_arr[1])

  def move_to(self,vec):
    self.pos += vec 

  def Charactor_bullet_fire(self, bullet_frame, sub_bullet_frame, bullet_player_ref, power):
    if(power <= 5):self.lv = 0
    elif(power <= 15):self.lv = 1
    elif(power <= 30):self.lv = 2
    elif(power <= 50):self.lv = 3
    elif(power <= 80):self.lv = 4
    elif(power < 120):self.lv = 5
    elif(power >= 120):self.lv = 6
    if self.lv == 0: 
      self.bullet_rate = 7
      self.sub_bullet_rate = 0
    elif self.lv == 1: 
      self.bullet_rate = 7
      self.sub_bullet_rate = 30
    elif self.lv == 2: 
      self.bullet_rate = 6
      self.sub_bullet_rate = 20
    elif self.lv == 3: 
      self.bullet_rate = 5
      self.sub_bullet_rate = 15
    elif self.lv == 4: 
      self.bullet_rate = 5
      self.sub_bullet_rate = 10
    elif self.lv == 5: 
      self.bullet_rate = 5
      self.sub_bullet_rate = 8
    elif self.lv == 6: 
      self.bullet_rate = 3
      self.sub_bullet_rate = 6
    #メイン武器
    if bullet_frame >= self.bullet_rate:
      new_pos = self.pos.copy()
      
      if self.name == "reimu":
        b_data = self.bullet_type["reimu_bullet1"]
        spawn_pos = new_pos + self.middle - pg.Vector2(b_data["size"].x / 2, 0)
        if self.lv <= 1:
          bullet_player_ref.append(bullet_player(spawn_pos, b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
        elif self.lv <= 4:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
        elif self.lv <= 5:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x - 20,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 20,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
        else:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x - 20,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 20,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x - 25,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 25,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))

      elif self.name == "marisa":
        b_data = self.bullet_type["marisa_bullet1"]
        spawn_pos = new_pos + self.middle - pg.Vector2(b_data["size"].x / 2, 0)
        if self.lv <= 0:
          bullet_player_ref.append(bullet_player(spawn_pos, b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
        elif self.lv <= 3:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
        else:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 10,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x - 20,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 20,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))

      bullet_frame = 0

    # サブ武器
    if self.lv >= 1 and sub_bullet_frame >= self.sub_bullet_rate:
      new_pos = self.pos.copy()

      if self.name == "reimu":
        b_data = self.bullet_type["reimu_bullet2"]
        spawn_pos = new_pos + self.middle - pg.Vector2(b_data["size"].x / 2, 0)
        if self.lv <= 2:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 15,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "homing"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 15,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "homing"))
        else:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 15,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "homing"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 15,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "homing"))
          bullet_player_ref.append(bullet_player((spawn_pos.x - 30,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "homing"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 30,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "homing"))

      elif self.name == "marisa":
        b_data = self.bullet_type["marisa_bullet2"]
        spawn_pos = new_pos + self.middle - pg.Vector2(b_data["size"].x / 2, 0)
        if self.lv <= 4:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 15,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 15,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
        else:
          bullet_player_ref.append(bullet_player((spawn_pos.x - 15,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 15,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x - 30,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
          bullet_player_ref.append(bullet_player((spawn_pos.x + 30,spawn_pos.y), b_data["vec"], b_data["img"], b_data["size"], b_data["damage"], b_data["img_len"], "straight"))
      
      sub_bullet_frame = 0
    return bullet_frame, sub_bullet_frame
  
  def change_bullet_rate(self, rate):
    self.bullet_rate = rate

  def get_dp(self):
    return self.pos * 1 - pg.Vector2(0,0.5)
  
  def get_img(self,frame):
    return self.__img_arr[frame//12%4]
  

# 自分の弾のクラスの定義
class bullet_player:
  def __init__(self,init_pos,init_velocity,img_raw,img_size,damage,img_len, behavior="straight"):
    self.pos = pg.Vector2(init_pos)
    self.speed = float(init_velocity)
    self.velocity_vec = pg.Vector2(0, -self.speed)
    self.size = pg.Vector2(img_size)
    self.middle = pg.Vector2(self.size[0] / 2,self.size[1] / 2)
    self.Countermeasures = pg.Vector2(img_size)
    self.damage = damage
    self.img_len = img_len
    self.behavior = behavior # "straight","homing"
    self.target = None
    self.__img_arr = []
    for i in range(self.img_len):
      p = pg.Vector2(img_size[0]*i,0)
      tmp = img_raw.subsurface(pg.Rect(p,img_size))
      tmp = pg.transform.scale(tmp, self.size)
      self.__img_arr.append(tmp)

  # 移動関数（敵リストを受け取るように変更）
  def move_to(self, enemies=None):
    
    # --- ホーミング弾の処理 ---
    if self.behavior == "homing":
        # まだターゲットがいない、またはターゲットが死んでたら、一番近い敵を探す
        if self.target is None or self.target not in enemies:
            min_dist = 10000
            self.target = None
            if enemies:
                for e in enemies:
                    dist = self.pos.distance_to(e.pos)
                    if dist < min_dist:
                        min_dist = dist
                        self.target = e
        
        if self.target:
            desired_vec = (self.target.pos - self.pos).normalize() * self.speed
            self.velocity_vec = self.velocity_vec.lerp(desired_vec, 0.2)
            if self.velocity_vec.length() > 0:
                self.velocity_vec = self.velocity_vec.normalize() * self.speed

    # --- 直進弾の処理 ---
    else:
        self.velocity_vec = pg.Vector2(0, -self.speed)

    self.pos += self.velocity_vec

  def get_dp(self):
    return self.pos * 1 - pg.Vector2(0,0.5)

  def get_img(self,frame):
    return self.__img_arr[frame//4%self.img_len]

# 敵キャラのクラスの定義
class enemyCharacter:
  def __init__(self,init_pos,init_hp,img_path,img_size,transform_path,bullet_path,img_len,bullet_catalog):
    self.pos = pg.Vector2(init_pos)
    self.origin = pg.Vector2(init_pos)
    self.hp = init_hp
    self.vel = pg.Vector2(0,0)
    if img_size == (24, 24):
        self.size = pg.Vector2(32, 32)
    else:
        self.size = pg.Vector2(img_size)
    self.middle = pg.Vector2(self.size[0] / 2,self.size[1] / 2)
    self.path = list(transform_path)
    self.bullet_catalog = bullet_catalog
    self.bullet_path = bullet_path
    self.bullet_pathindex = 0
    self.bullet_timer = 0
    self.pathindex = 0
    self.timer = 0
    self.img_len = img_len
    self.Countermeasures = pg.Vector2(img_size)
    img_raw = pg.image.load(img_path)
    self.__img_arr = []
    for i in range(img_len):
      p = pg.Vector2(img_size[0]*i,0)
      tmp = img_raw.subsurface(pg.Rect(p,img_size))
      tmp = pg.transform.scale(tmp, self.size)
      self.__img_arr.append(tmp)

  # 移動経路の設定
  def update(self):
    if self.pathindex < len(self.path):
      rel_x, rel_y, target_speed, ease = self.path[self.pathindex]
      target_pos = self.origin + pg.Vector2(rel_x, rel_y)

      # 目的地への理想の速度
      desired_vel = (target_pos - self.pos)
      if desired_vel.length() > 0:
          desired_vel = desired_vel.normalize() * target_speed

      # 今の速度を理想に近づける
      self.vel += (desired_vel - self.vel) * ease
      self.pos += self.vel

      if (self.pos - target_pos).length() < 10:
        self.pathindex += 1      
    self.finish_path = self.pathindex >= len(self.path)
  
  # 敵の弾の設定
  def bullet_update(self, target_pos, bullet_list_ref):
    if self.bullet_path == []:
      return
    b_cmd = self.bullet_path[self.bullet_pathindex]

    if self.bullet_timer < b_cmd["wait"]:
      self.bullet_timer += 1
      return
    
    # 待ち時間が終わった後の発射処理
    b_id = b_cmd["bullet"]
    current_bullet_info = self.bullet_catalog[b_id]
    
    # リストだったらランダム
    raw_speed = b_cmd["speed"]
    if isinstance(raw_speed, list):
      b_spd = rd.uniform(raw_speed[0], raw_speed[1])
    else:
      b_spd = raw_speed
    b_img = current_bullet_info["img"]
    b_size = pg.Vector2(current_bullet_info["size"])
    b_cou = current_bullet_info["countermeasures"]
    spawn_pos = self.pos + self.middle - pg.Vector2(b_size.x / 2, b_size.y / 2)

    

    if b_cmd["type"] == "single":
      raw_angle = b_cmd["angle"]
      if isinstance(raw_angle, list):
        angle = rd.uniform(raw_angle[0], raw_angle[1])
      else:
        angle = raw_angle
      b_vec = pg.Vector2(1,0).rotate(angle) * b_spd
      bullet_list_ref.append(bullet_enemy(spawn_pos, b_vec, b_img, b_size, b_cou))

    elif b_cmd["type"] == "aim":
      diff = target_pos - spawn_pos
      if diff.length() != 0:
        b_vec = diff.normalize() * b_spd
      else:
        b_vec = pg.Vector2(0, b_spd)
      bullet_list_ref.append(bullet_enemy(spawn_pos, b_vec, b_img, b_size, b_cou))

    elif b_cmd["type"] == "circle":
      count = b_cmd["count"]
      raw_offset = b_cmd["offset"]
      if isinstance(raw_offset, list):
        offset_angle = rd.uniform(raw_offset[0], raw_offset[1])
      else:
        offset_angle = raw_offset
      for i in range(count):
        angle = (360 / count) * i  + offset_angle
        b_vec = pg.Vector2(1,0).rotate(angle) * b_spd
        bullet_list_ref.append(bullet_enemy(spawn_pos, b_vec, b_img, b_size, b_cou))

    self.bullet_pathindex += 1
    self.bullet_timer = 0

    if self.bullet_pathindex >= len(self.bullet_path):
      self.bullet_pathindex = 0
 

  def get_finish_path(self):
    return self.finish_path

  def get_dp(self):
    return self.pos * 1 - pg.Vector2(0,0.5)
  
  def get_img(self,frame):
    return self.__img_arr[frame//12%self.img_len]

        
# 敵キャラの弾のクラスの定義
class bullet_enemy:
  def __init__(self,init_pos,init_velocity,img_raw,img_size,countermeasures):
    self.pos = pg.Vector2(init_pos)
    self.velocity = init_velocity
    self.size = pg.Vector2(img_size)
    self.middle = pg.Vector2(self.size[0] / 2,self.size[1] / 2)
    self.grazed = False 
    self.Countermeasures = pg.Vector2(countermeasures)
    self.__img_arr = []
    for i in range(2):
      p = pg.Vector2(img_size[0]*i,0)
      tmp = img_raw.subsurface(pg.Rect(p,img_size))
      tmp = pg.transform.scale(tmp, self.size)
      self.__img_arr.append(tmp)

  def move_to(self):
    self.pos += self.velocity

  def get_dp(self):
    return self.pos * 1 - pg.Vector2(0,0.5)

  def get_img(self,frame):
    return self.__img_arr[frame//12%2]

# アイテムのクラス定義
class item:
  def __init__(self,init_pos,init_velocity,img_raw,img_size,type):
    self.pos = pg.Vector2(init_pos)
    self.velocity = pg.Vector2(init_velocity)
    self.size = pg.Vector2(img_size)
    self.middle = pg.Vector2(self.size[0] / 2,self.size[1] / 2)
    self.Countermeasures = pg.Vector2(img_size)
    self.type = type
    self.__img_arr = []
    for i in range(1):
      p = pg.Vector2(img_size[0]*i,0)
      tmp = img_raw.subsurface(pg.Rect(p,img_size))
      tmp = pg.transform.scale(tmp, self.size)
      self.__img_arr.append(tmp)

  def move_to(self):
    self.velocity.x *= 0.975

    if self.velocity.y < 3:
      self.velocity.y += 0.2
        
    self.pos += self.velocity

  def get_dp(self):
    return self.pos * 1 - pg.Vector2(0,0.5)

  def get_img(self, frame):
    return self.__img_arr[frame//12%1]
    
def main():

  # 初期化処理
  map_s  = pg.Vector2(1024,768)

  clockspeed = 60
  pg.init() 
  pg.display.set_caption('東方風弾幕 ~Touhou_Like_Shooting~')
  disp_w = int(map_s.x)
  disp_h = int(map_s.y)
  screen = pg.display.set_mode((disp_w,disp_h))
  canmvscrwh = pg.Vector2(map_s.x/2,map_s.y)
  canmvscroffset = pg.Vector2(map_s.x/8,0)
  canmvscr = ([canmvscroffset.x, canmvscrwh.x + canmvscroffset.x],[canmvscroffset.y, canmvscrwh.y - canmvscroffset.y])
  canmvscrmiddle = pg.Vector2(canmvscrwh.x / 2 + canmvscroffset.x,canmvscrwh.y / 2 + canmvscroffset.y)
  clock  = pg.time.Clock()
  font   = pg.font.Font(None,15)
  font_title = pg.font.Font(None, 80)
  font_msg = pg.font.Font(None, 40)
  font_state = pg.font.SysFont("ＭＳ 明朝", 35)
  frame  = 0
  score = 0
  power = 0
  point = 0
  graze = 0
  exit_flag = False
  exit_code = '000'
  game_state = "Title"
  title_state = "NONE"
  title_select_num = 0
  option_select_num = 0
  pause_select_num = 0
  title_select = ["START","OPTION","QUIT"]
  option_select = ["player_life","bomb","60fps","default","quit"]
  pause_select = ["CONTINUE","RESTART","QUIT"]
  def_init_player_life = 2
  def_init_bomb = 3
  def_fps_fixed = True
  unrivaled_frame = 0 #無敵時間

  init_player_life = def_init_player_life
  init_bomb = def_init_bomb
  fps_fixed = def_fps_fixed
 
  # タイトル画面ロード
  title_image = pg.image.load("./pygameDammaku/data/img/ui/title.png").convert_alpha()

  # アイテムロード
  img_Power = pg.image.load("./pygameDammaku/data/img/item/Power.png").convert_alpha()
  img_Score = pg.image.load("./pygameDammaku/data/img/item/Score.png").convert_alpha()

  # アイテムの情報
  item_type = {"itemPower" : {"img":img_Power, "size":pg.Vector2(12,12)},
               "itemScore" : {"img":img_Score, "size":pg.Vector2(12,12)}}

  # 弾の画像ロード
  img_reimu_bullet1 = pg.image.load("./pygameDammaku/data/img/bullet/character/bulletreimu1.png")
  img_marisa_bullet1 = pg.image.load("./pygameDammaku/data/img/bullet/character/bulletmarisa1.png")
  img_reimu_bullet2 = pg.image.load("./pygameDammaku/data/img/bullet/character/bulletreimu2.png")
  img_marisa_bullet2 = pg.image.load("./pygameDammaku/data/img/bullet/character/bulletmarisa2.png")
  img_enemy1_bullet = pg.image.load("./pygameDammaku/data/img/bullet/enemy/enemy1.png")
  img_enemy2_bullet = pg.image.load("./pygameDammaku/data/img/bullet/enemy/enemy2.png")

  # 自機の弾の情報
  bullet_type = {"reimu_bullet1": {"img":img_reimu_bullet1, "vec":12, "size":pg.Vector2(8,32), "damage":6, "img_len":2},
                 "marisa_bullet1": {"img":img_marisa_bullet1, "vec":16, "size":pg.Vector2(16,16), "damage":5, "img_len":2},
                 "reimu_bullet2": {"img":img_reimu_bullet2, "vec":8, "size":pg.Vector2(16,16), "damage":5, "img_len":4},
                 "marisa_bullet2": {"img":img_marisa_bullet2, "vec":10, "size":pg.Vector2(16,32), "damage":8, "img_len":2}
                }

  # 敵の弾の情報
  bullet_catalog = {"enemy1_bullet": {"img":img_enemy1_bullet, "size":(16,16),"countermeasures":(4,4)},
                    "enemy2_bullet": {"img":img_enemy2_bullet, "size":(16,16),"countermeasures":(4,4)},}
  
  # 敵の動きパターン(相対目標X,相対目標Y,速さ,曲がりやすさ)
  enemy_path_test1 = [(0,100,2,0.1),
                      (100,0,1,0.02),
                      (100,-100,1,0.1)]
  
  enemy_path_test2 = [(100,100,3,0.04),
                      (0,200,2,0.04),
                      (-100,100,3,0.04),
                      (0,0,3,0.04)]
  
  enemy_path1 = [(0,250,2,0.02),
                 (-300,250,2,0.1)]
  
  enemy_path2 = [(0,250,2,0.02),
                 (300,250,2,0.1)]
  
  enemy_path3 = [(0,100,2,0.1),
                 (20,100,0.1,0.1),
                 (20,0,2,0.1)]
  
  enemy_path4_1 = [(0,250,2,0.02),
                 (-300,250,2,0.1)]
  
  enemy_path4_2 = [(0,250,2,0.02),
                 (300,250,2,0.1)]
  
  enemy_path5 = [(-60,150,2,0.02),
                 (-120,0,2,0.02)]
  
  enemy_path5_2 = [(60,150,2,0.02),
                 (120,0,2,0.02)]
  
  enemy_path6 = [(0,100,2,0.1),
                 (20,100,0.03,0.1),
                 (20,0,2,0.1)]
  
  enemy_path7 = [(0,100,2,0.1),
                 (50,100,0.07,0.1),
                 (50,0,2,0.1)]
  
  enemy_path8 = [(0,100,2,0.1),
                 (50,150,0.07,0.1),
                 (-40,90,0.07,0.1),
                 (-110,110,0.07,0.1),
                 (190,140,0.07,0.1),
                 (-50,80,0.07,0.1),
                 (90,120,0.07,0.1),
                 (-150,140,0.07,0.1),
                 (50,0,2,0.1)]
  
  # 敵の弾のパターン(雑魚敵)
  enemy_bullet_path_test1 = [
    {"type": "aim",    "wait": 60, "speed": 4, "bullet": "enemy1_bullet"},
  ]

  enemy_bullet_path_test2 = [
    {"type": "circle", "wait": 20, "speed": 3, "count": 16, "offset": 0,  "bullet": "enemy1_bullet"},
    {"type": "circle", "wait": 20, "speed": 3, "count": 16, "offset": 15,  "bullet": "enemy1_bullet"},
    {"type": "circle", "wait": 20, "speed": 3, "count": 16, "offset": 30,  "bullet": "enemy1_bullet"},
    {"type": "circle", "wait": 20, "speed": 3, "count": 16, "offset": 45,  "bullet": "enemy1_bullet"}
  ]
  
  enemy_bullet_path1 = []

  enemy_bullet_path2 = [{"type": "circle", "wait": 60, "speed": 2, "count": 8, "offset": 0,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 60, "speed": 2, "count": 8, "offset": 45,  "bullet": "enemy1_bullet"},]
  
  enemy_bullet_path3 = [{"type": "aim",    "wait": 120, "speed": 4, "bullet": "enemy2_bullet"},]

  enemy_bullet_path4 = [{"type": "single", "wait": 120, "speed": 5, "bullet": "enemy1_bullet", "angle": 90},
                        {"type": "single", "wait": 0, "speed": 5, "bullet": "enemy1_bullet", "angle": 110},
                        {"type": "single", "wait": 0, "speed": 5, "bullet": "enemy1_bullet", "angle": 70},
                        {"type": "aim",    "wait": 120, "speed": 4, "bullet": "enemy1_bullet"},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy1_bullet"},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy1_bullet"},]
  
  enemy_bullet_path5 = [{"type": "single", "wait": 30, "speed": 5, "bullet": "enemy2_bullet", "angle": 90},
                        {"type": "single", "wait": 0, "speed": 5, "bullet": "enemy2_bullet", "angle": 110},
                        {"type": "single", "wait": 0, "speed": 5, "bullet": "enemy2_bullet", "angle": 70},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},]
  
  enemy_bullet_path6 = [{"type": "circle", "wait": 60, "speed": 2, "count": 16, "offset": 0,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 5, "speed": 3, "count": 16, "offset": 22.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 5, "speed": 4, "count": 16, "offset": 45,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 5, "speed": 5, "count": 16, "offset": 67.5,  "bullet": "enemy1_bullet"},]
  
  enemy_bullet_path7 = [{"type": "circle", "wait": 120, "speed": 2, "count": 24, "offset": 0,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": 7.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": 15,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": 22.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": 30,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 24, "offset": 37.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": 45,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.4, "count": 24, "offset": 52.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.6, "count": 24, "offset": 60,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.8, "count": 24, "offset": 67.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4, "count": 24, "offset": 75,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4.2, "count": 24, "offset": 82.5,  "bullet": "enemy1_bullet"},]
  
  enemy_bullet_path8 = [{"type": "circle", "wait": 120, "speed": 1, "count": 24, "offset": 0,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.2, "count": 24, "offset": 7.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.4, "count": 24, "offset": 15,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.6, "count": 24, "offset": 22.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.8, "count": 24, "offset": 30,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2, "count": 24, "offset": 37.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": 45,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": 52.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": 60,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": 67.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 24, "offset": 75,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": 82.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 30, "speed": 1, "count": 24, "offset": 0,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.2, "count": 24, "offset": -7.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.4, "count": 24, "offset": -15,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.6, "count": 24, "offset": -22.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.8, "count": 24, "offset": -30,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2, "count": 24, "offset": -37.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": -45,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": -52.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": -60,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": -67.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 24, "offset": -75,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": -82.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 30, "speed": 1, "count": 24, "offset": 0,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.2, "count": 24, "offset": 7.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.4, "count": 24, "offset": 15,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.6, "count": 24, "offset": 22.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.8, "count": 24, "offset": 30,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2, "count": 24, "offset": 37.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": 45,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": 52.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": 60,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": 67.5,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 24, "offset": 75,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": 82.5,  "bullet": "enemy1_bullet"},]
  
  enemy_bullet_path9 = [{"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},]
  
  enemy_bullet_path10 =[{"type": "aim",    "wait": 60, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},]
  
  enemy_bullet_path11 = [{"type": "single", "wait": 30, "speed": 5, "bullet": "enemy2_bullet", "angle": [0, 180]},
                        {"type": "single", "wait": 0, "speed": 5, "bullet": "enemy2_bullet", "angle": [0, 180]},
                        {"type": "single", "wait": 0, "speed": 5, "bullet": "enemy2_bullet", "angle": [0, 180]},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",    "wait": 10, "speed": 4, "bullet": "enemy2_bullet"},]
  
  enemy_bullet_path12 = [{"type": "aim",   "wait": 120, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "aim",   "wait": 30, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "aim",   "wait": 30, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "aim",   "wait": 30, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy2_bullet", "angle": [0, 360]},
                        
                        {"type": "circle", "wait": 240, "speed": 1, "count": 36, "offset": 0,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.2, "count": 36, "offset": 2,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.4, "count": 36, "offset": 4,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.6, "count": 36, "offset": 6,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.8, "count": 36, "offset": 8,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2, "count": 36, "offset": 10,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 36, "offset": 12,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 36, "offset": 14,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 36, "offset": 16,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 36, "offset": 18,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 36, "offset": 20,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 36, "offset": 22,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 90, "speed": 1, "count": 36, "offset": 45,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.2, "count": 36, "offset": 43,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.4, "count": 36, "offset": 41,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.6, "count": 36, "offset": 39,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.8, "count": 36, "offset": 37,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2, "count": 36, "offset": 35,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 36, "offset": 33,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 36, "offset": 31,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 36, "offset": 29,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 36, "offset": 27,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 36, "offset": 25,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 36, "offset": 23,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 90, "speed": 1, "count": 36, "offset": 0,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.2, "count": 36, "offset": -2,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.4, "count": 36, "offset": -4,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.6, "count": 36, "offset": -6,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.8, "count": 36, "offset": -8,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2, "count": 36, "offset": -10,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 36, "offset": -12,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 36, "offset": -14,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 36, "offset": -16,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 36, "offset": -18,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 36, "offset": -20,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 36, "offset": -22,  "bullet": "enemy1_bullet"},
                        {"type": "circle", "wait": 90, "speed": 1, "count": 36, "offset": -45,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.2, "count": 36, "offset": -43,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.4, "count": 36, "offset": -41,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.6, "count": 36, "offset": -39,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 1.8, "count": 36, "offset": -37,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2, "count": 36, "offset": -35,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 36, "offset": -33,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 36, "offset": -31,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 36, "offset": -29,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 36, "offset": -27,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 36, "offset": -25,  "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 36, "offset": -23,  "bullet": "enemy2_bullet"},
                        
                        {"type": "aim",   "wait": 240, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "aim",   "wait": 1, "speed": 4, "bullet": "enemy2_bullet"},
                        
                        {"type": "circle", "wait": 120, "speed": 2, "count": 24, "offset": 0,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": 7.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": 15,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": 22.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": 30,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 24, "offset": 37.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": 45,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.4, "count": 24, "offset": 52.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.6, "count": 24, "offset": 60,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.8, "count": 24, "offset": 67.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4, "count": 24, "offset": 75,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4.2, "count": 24, "offset": 82.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 40, "speed": 2, "count": 24, "offset": 0,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": 7.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": 15,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": 22.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": 30,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 24, "offset": 37.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": 45,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.4, "count": 24, "offset": 52.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.6, "count": 24, "offset": 60,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.8, "count": 24, "offset": 67.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4, "count": 24, "offset": 75,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4.2, "count": 24, "offset": 82.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 40, "speed": 2, "count": 24, "offset": 0,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": 7.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": 15,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": 22.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": 30,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 24, "offset": 37.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": 45,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.4, "count": 24, "offset": 52.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.6, "count": 24, "offset": 60,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.8, "count": 24, "offset": 67.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4, "count": 24, "offset": 75,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4.2, "count": 24, "offset": 82.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 40, "speed": 2, "count": 24, "offset": 0,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": 7.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": 15,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": 22.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": 30,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3, "count": 24, "offset": 37.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": 45,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.4, "count": 24, "offset": 52.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.6, "count": 24, "offset": 60,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.8, "count": 24, "offset": 67.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4, "count": 24, "offset": 75,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 4.2, "count": 24, "offset": 82.5,  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},

                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},
                        {"type": "single", "wait": 1, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},{"type": "single", "wait": 0, "speed": [2, 6], "bullet": "enemy1_bullet", "angle": [0, 360]},

                        {"type": "circle", "wait": 120, "speed": 2, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.0, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.4, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 40, "speed": 2.0, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.2, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.4, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.6, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 2.8, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.0, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.2, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        {"type": "circle", "wait": 2, "speed": 3.4, "count": 24, "offset": [0,360],  "bullet": "enemy1_bullet"},{"type": "aim",   "wait": 0, "speed": 4, "bullet": "enemy2_bullet"},
                        ]

  # 敵の情報
  enemy1 = {"hp": 8, "img_path":"./pygameDammaku/data/img/enemy/Test1.png", "img_size": (16,16),"img_len":2}
  yousei0 = {"hp": 4, "img_path":"./pygameDammaku/data/img/enemy/yousei0.png", "img_size": (24,24),"img_len":1}
  yousei0_2 = {"hp": 12, "img_path":"./pygameDammaku/data/img/enemy/yousei0.png", "img_size": (24,24),"img_len":1}
  yousei1 = {"hp": 50, "img_path":"./pygameDammaku/data/img/enemy/yousei1.png", "img_size": (24,24),"img_len":1}
  yousei2 = {"hp": 16, "img_path":"./pygameDammaku/data/img/enemy/yousei2.png", "img_size": (24,24),"img_len":1}
  yousei2_2 = {"hp": 30, "img_path":"./pygameDammaku/data/img/enemy/yousei2.png", "img_size": (24,24),"img_len":1}
  yousei3 = {"hp": 300, "img_path":"./pygameDammaku/data/img/enemy/yousei3.png", "img_size": (24,24),"img_len":1}
  yousei3_0 = {"hp": 100, "img_path":"./pygameDammaku/data/img/enemy/yousei3.png", "img_size": (24,24),"img_len":1}
  yousei4 = {"hp": 10000, "img_path":"./pygameDammaku/data/img/enemy/yousei3.png", "img_size": (24,24),"img_len":1}

  # 出現スケジュール
  # spawn_f: 出現フレーム, x: 初期X座標, path: 使う移動データ
  init_enemy_schedule = [
    {"spawn_f": 120,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path1, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 120,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path2, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 140,  "x": canmvscrmiddle.x - 145 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path1, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 140,  "x": canmvscrmiddle.x + 145 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path2, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 160,  "x": canmvscrmiddle.x - 125 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path1, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 160,  "x": canmvscrmiddle.x + 125 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path2, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 180,  "x": canmvscrmiddle.x - 105 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path1, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 180,  "x": canmvscrmiddle.x + 105 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path2, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 200,  "x": canmvscrmiddle.x - 85 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path1, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 200,  "x": canmvscrmiddle.x + 85 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path2, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 220,  "x": canmvscrmiddle.x - 65 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path1, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 220,  "x": canmvscrmiddle.x + 65 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path2, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 240,  "x": canmvscrmiddle.x - 45 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path1, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 240,  "x": canmvscrmiddle.x + 45 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path2, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 260,  "x": canmvscrmiddle.x - 25 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path1, "bullet_path": enemy_bullet_path1},
    {"spawn_f": 260,  "x": canmvscrmiddle.x + 25 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path2, "bullet_path": enemy_bullet_path1},

    {"spawn_f": 360,  "x": canmvscrmiddle.x + 100 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 420,  "x": canmvscrmiddle.x - 145 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 480,  "x": canmvscrmiddle.x + 163 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 540,  "x": canmvscrmiddle.x - 48 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 600,  "x": canmvscrmiddle.x - 175 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 660,  "x": canmvscrmiddle.x + 16 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 360,  "x": canmvscrmiddle.x - 115 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 420,  "x": canmvscrmiddle.x + 84 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 480,  "x": canmvscrmiddle.x - 97 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 540,  "x": canmvscrmiddle.x + 144 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 600,  "x": canmvscrmiddle.x - 12 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 660,  "x": canmvscrmiddle.x - 78 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 720,  "x": canmvscrmiddle.x - 172 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 720,  "x": canmvscrmiddle.x + 97 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 780,  "x": canmvscrmiddle.x - 63 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},
    {"spawn_f": 780,  "x": canmvscrmiddle.x + 189 - 32 / 2, "enemy_info" : yousei2, "path": enemy_path3, "bullet_path": enemy_bullet_path2},

    {"spawn_f": 900,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 900,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 920,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 920,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 940,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 940,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 960,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 960,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 980,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 980,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1000,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1000,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1020,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1020,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},

    {"spawn_f": 1120,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1120,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1140,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1140,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1160,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1160,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1180,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1180,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1200,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1200,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1220,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1220,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1240,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1240,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},

    {"spawn_f": 1340,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1340,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1360,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1360,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1380,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1380,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1400,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1400,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1420,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1420,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1460,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1460,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1480,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1480,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_1, "bullet_path": enemy_bullet_path3},

    {"spawn_f": 1580,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1580,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1600,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1600,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1620,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1620,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1640,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1640,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1660,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1660,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1680,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1680,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1700,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},
    {"spawn_f": 1700,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path4_2, "bullet_path": enemy_bullet_path3},

    {"spawn_f": 1860,  "x": canmvscrmiddle.x - 145 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 1880,  "x": canmvscrmiddle.x + 46 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 1900,  "x": canmvscrmiddle.x - 155 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 1920,  "x": canmvscrmiddle.x - 123 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 1940,  "x": canmvscrmiddle.x + 12 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 1960,  "x": canmvscrmiddle.x + 56 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 1980,  "x": canmvscrmiddle.x - 67 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 2000,  "x": canmvscrmiddle.x - 91 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 2020,  "x": canmvscrmiddle.x + 195 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 2040,  "x": canmvscrmiddle.x - 26 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 2060,  "x": canmvscrmiddle.x + 79 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 2080,  "x": canmvscrmiddle.x + 91 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 2100,  "x": canmvscrmiddle.x + 42 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 2120,  "x": canmvscrmiddle.x - 121 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},
    {"spawn_f": 2140,  "x": canmvscrmiddle.x - 175 - 32 / 2, "enemy_info" : yousei2_2, "path": enemy_path3, "bullet_path": enemy_bullet_path4},

    {"spawn_f": 2300,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2300,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2320,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2320,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2340,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2340,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2360,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2360,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2380,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2380,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2400,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2400,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2420,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2420,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2440,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2440,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2460,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2460,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2600,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2600,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2620,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2620,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2640,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2640,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2660,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2660,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2680,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2680,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2700,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2700,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2720,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2720,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2740,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2740,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2760,  "x": canmvscrmiddle.x + 95 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},
    {"spawn_f": 2760,  "x": canmvscrmiddle.x + 60 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path5},

    {"spawn_f": 2900,  "x": canmvscrmiddle.x + 200 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},
    {"spawn_f": 2980,  "x": canmvscrmiddle.x + 150 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},
    {"spawn_f": 3060,  "x": canmvscrmiddle.x + 100 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},
    {"spawn_f": 3140,  "x": canmvscrmiddle.x + 50 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},
    {"spawn_f": 3220,  "x": canmvscrmiddle.x + 0 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},
    {"spawn_f": 3300,  "x": canmvscrmiddle.x - 50 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},
    {"spawn_f": 3380,  "x": canmvscrmiddle.x - 100 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},
    {"spawn_f": 3460,  "x": canmvscrmiddle.x - 150 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},
    {"spawn_f": 3540,  "x": canmvscrmiddle.x - 200 - 32 / 2, "enemy_info" : yousei1, "path": enemy_path3, "bullet_path": enemy_bullet_path6},

    {"spawn_f": 3700,  "x": canmvscrmiddle.x + 0 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path6, "bullet_path": enemy_bullet_path7},
    {"spawn_f": 4000,  "x": canmvscrmiddle.x + 150 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path6, "bullet_path": enemy_bullet_path7},
    {"spawn_f": 4000,  "x": canmvscrmiddle.x - 150 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path6, "bullet_path": enemy_bullet_path7},

    {"spawn_f": 4400,  "x": canmvscrmiddle.x + 0 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path7, "bullet_path": enemy_bullet_path8},
    {"spawn_f": 4700,  "x": canmvscrmiddle.x + 110 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path7, "bullet_path": enemy_bullet_path8},
    {"spawn_f": 4900,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path7, "bullet_path": enemy_bullet_path8},
    
    {"spawn_f": 5700,  "x": canmvscrmiddle.x - 0 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path7, "bullet_path": enemy_bullet_path9},
    {"spawn_f": 5800,  "x": canmvscrmiddle.x - 70 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path7, "bullet_path": enemy_bullet_path10},
    {"spawn_f": 5900,  "x": canmvscrmiddle.x + 70 - 32 / 2, "enemy_info" : yousei3, "path": enemy_path7, "bullet_path": enemy_bullet_path10},

    {"spawn_f": 6500,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6500,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6520,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6520,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6540,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6540,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6560,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6560,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6580,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6580,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6600,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6600,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6620,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6620,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6640,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6640,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},

    {"spawn_f": 6700,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6700,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6720,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6720,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6740,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6740,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6760,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6760,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6780,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6780,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6800,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6800,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6820,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6820,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6840,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6840,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},

    {"spawn_f": 6900,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6900,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6920,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6920,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6940,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6940,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6960,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6960,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6980,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 6980,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7000,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7000,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7020,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7020,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7040,  "x": canmvscrmiddle.x + 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7040,  "x": canmvscrmiddle.x + 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5, "bullet_path": enemy_bullet_path11},

    {"spawn_f": 7100,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7100,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7120,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7120,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7140,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7140,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7160,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7160,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7180,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7180,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7200,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7200,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7220,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7220,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7240,  "x": canmvscrmiddle.x - 165 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},
    {"spawn_f": 7240,  "x": canmvscrmiddle.x - 130 - 32 / 2, "enemy_info" : yousei0, "path": enemy_path5_2, "bullet_path": enemy_bullet_path11},

    {"spawn_f": 7500,  "x": canmvscrmiddle.x - 0 - 32 / 2, "enemy_info" : yousei4, "path": enemy_path8, "bullet_path": enemy_bullet_path12},
  ]
  #　発射レートフレーム
  bullet_frame = 0
  sub_bullet_frame = 0

  # 自キャラ移動関連
  cmd_move_low = 0 # 微調整移動コマンド
  cmd_tab = 0

  # 自キャラの生成・初期化
  reimu = PlayerCharacter("reimu",(canmvscrwh.x / 2 - (48 / 2)+ canmvscroffset.x,disp_h - canmvscrwh.y / 9),4,'./pygameDammaku/data/img/character/reimu.png',7,bullet_type)
  marisa = PlayerCharacter("marisa",(canmvscrwh.x / 2 - (48 / 2)+ canmvscroffset.x,disp_h - canmvscrwh.y / 9),6,'./pygameDammaku/data/img/character/marisa.png',7,bullet_type)

  # 出現する奴らをまとめておく
  Character = [reimu, marisa]
  Bullet_player = []
  Enemies = []
  Bullet_enemy = []
  Item = []

  def init_game():
    nonlocal frame, score, power, point, graze, unrivaled_frame, bullet_frame, sub_bullet_frame, player_life, bomb
    frame = 0
    score = 0
    power = 0
    point = 0
    graze = 0
    unrivaled_frame = 0
    bullet_frame = 0
    sub_bullet_frame = 0
    Enemies.clear()
    Bullet_enemy.clear()
    Bullet_player.clear()
    Item.clear()
    enemy_schedule = copy.deepcopy(init_enemy_schedule)
    Character[cmd_tab].pos = pg.Vector2(canmvscrwh.x / 2 - (48 / 2)+ canmvscroffset.x,disp_h - canmvscrwh.y / 9)
    player_life = init_player_life
    bomb = init_bomb
    return enemy_schedule
  
  # ゲームループ
  while not exit_flag:

    # システムイベントの検出
    events = pg.event.get() 
    for event in events:
      if event.type == pg.QUIT:
        exit_flag = True
        exit_code = '001'
    
    #---Title---
    if game_state == "Title":
      screen.fill(pg.Color("#555555"))
      #タイトル画面
      if title_state == "NONE":
        option_select_num = 0

        # 画像を中央に配置する計算
        title_rect = title_image.get_rect()
        title_rect.center = (disp_w // 2, disp_h // 3)
        screen.blit(title_image, title_rect)
        
        msg_s_start_str = "GAME PLAY"
        msg_s_option_str = "OPTION"
        msg_s_quit_str = "QUIT"

        msg_s_start = font_msg.render(msg_s_start_str, True, "WHITE")
        if title_select[title_select_num] == "START":msg_s_start = font_msg.render(msg_s_start_str, True, "RED")
        screen.blit(msg_s_start, (disp_w//2 - msg_s_start.get_width()//2, disp_h//2 + 50))
        msg_s_option = font_msg.render(msg_s_option_str, True, "WHITE")
        if title_select[title_select_num] == "OPTION":msg_s_option = font_msg.render(msg_s_option_str, True, "RED")
        screen.blit(msg_s_option, (disp_w//2 - msg_s_option.get_width()//2, disp_h//2 + 90))
        msg_s_quit = font_msg.render(msg_s_quit_str, True, "WHITE")
        if title_select[title_select_num] == "QUIT":msg_s_quit = font_msg.render(msg_s_quit_str, True, "RED")
        screen.blit(msg_s_quit, (disp_w//2 - msg_s_quit.get_width()//2, disp_h//2 + 130))
        
        for event in events:
          if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            if title_select_num > 0:title_select_num -= 1
          elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            if title_select_num < len(title_select) - 1:title_select_num += 1
          if event.type == pg.KEYDOWN and event.key == pg.K_z:
            if title_select[title_select_num] == "START":
              game_state = "Game"
              enemy_schedule = init_game()
            if title_select[title_select_num] == "OPTION":
              title_state = "OPTION"
            if title_select[title_select_num] == "QUIT":
              title_state = "QUIT"
      #オプション画面
      elif title_state == "OPTION":
        msg_option = font_msg.render("OPTION",True,"WHITE")
        screen.blit(msg_option,  (10, 10))
        for event in events:
          if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            title_state = "NONE"
          if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            if option_select_num > 0:option_select_num -= 1
          elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            if option_select_num < len(option_select) - 1:option_select_num += 1
          if event.type == pg.KEYDOWN and option_select[option_select_num] == "player_life":
            if event.key == pg.K_LEFT and init_player_life > 0:init_player_life -= 1
            elif event.key == pg.K_RIGHT and init_player_life < 4:init_player_life += 1
          if event.type == pg.KEYDOWN and option_select[option_select_num] == "bomb":
            if event.key == pg.K_LEFT and init_bomb > 0:init_bomb -= 1
            elif event.key == pg.K_RIGHT and init_bomb < 4:init_bomb += 1
          if event.type == pg.KEYDOWN and option_select[option_select_num] == "60fps":
            if event.key == pg.K_z: fps_fixed = not fps_fixed
          if event.type == pg.KEYDOWN and option_select[option_select_num] == "default":
            if event.key == pg.K_z:
              init_player_life = def_init_player_life
              init_bomb = def_init_bomb
              fps_fixed = def_fps_fixed
          if event.type == pg.KEYDOWN and option_select[option_select_num] == "quit":
            if event.key == pg.K_z:
              title_state = "NONE"
        
        msg_option_life_str = "Player"
        msg_option_life0_str = "0"
        msg_option_life1_str = "1"
        msg_option_life2_str = "2"
        msg_option_life3_str = "3"
        msg_option_life4_str = "4"
        msg_option_bomb_str = "Bomb"
        msg_option_bomb0_str = "0"
        msg_option_bomb1_str = "1"
        msg_option_bomb2_str = "2"
        msg_option_bomb3_str = "3"
        msg_option_bomb4_str = "4"
        msg_option_60fps_str = "Fixfps"
        msg_option_default_str = "Default"
        msg_option_life_num_str = str(init_player_life)
        msg_option_bomb_num_str = str(init_bomb)
        msg_option_60fps_num_str = str(fps_fixed)
        msg_option_quit_str = "Quit"

        msg_option_life = font_msg.render(msg_option_life_str, True, "WHITE")
        if option_select[option_select_num] == "player_life":msg_option_life = font_msg.render(msg_option_life_str, True, "ORANGE")
        screen.blit(msg_option_life, (disp_w//2, disp_h//2 + 50))
        
        msg_option_life0 = font_msg.render(msg_option_life0_str, True, "WHITE")
        screen.blit(msg_option_life0, (disp_w//2 + 100, disp_h//2 + 50))
        msg_option_life1 = font_msg.render(msg_option_life1_str, True, "WHITE")
        screen.blit(msg_option_life1, (disp_w//2 + 120, disp_h//2 + 50))
        msg_option_life2 = font_msg.render(msg_option_life2_str, True, "WHITE")
        screen.blit(msg_option_life2, (disp_w//2 + 140, disp_h//2 + 50))
        msg_option_life3 = font_msg.render(msg_option_life3_str, True, "WHITE")
        screen.blit(msg_option_life3, (disp_w//2 + 160, disp_h//2 + 50))
        msg_option_life4 = font_msg.render(msg_option_life4_str, True, "WHITE")
        screen.blit(msg_option_life4, (disp_w//2 + 180, disp_h//2 + 50))
        msg_option_life_num = font_msg.render(msg_option_life_num_str, True, "RED")
        screen.blit(msg_option_life_num, (disp_w//2 + 100 + (20*init_player_life), disp_h//2 + 50))

        msg_option_bomb = font_msg.render(msg_option_bomb_str, True, "WHITE")
        if option_select[option_select_num] == "bomb":msg_option_bomb = font_msg.render(msg_option_bomb_str, True, "ORANGE")
        screen.blit(msg_option_bomb, (disp_w//2, disp_h//2 + 90))

        msg_option_bomb0 = font_msg.render(msg_option_bomb0_str, True, "WHITE")
        screen.blit(msg_option_bomb0, (disp_w//2 + 100, disp_h//2 + 90))
        msg_option_bomb1 = font_msg.render(msg_option_bomb1_str, True, "WHITE")
        screen.blit(msg_option_bomb1, (disp_w//2 + 120, disp_h//2 + 90))
        msg_option_bomb2 = font_msg.render(msg_option_bomb2_str, True, "WHITE")
        screen.blit(msg_option_bomb2, (disp_w//2 + 140, disp_h//2 + 90))
        msg_option_bomb3 = font_msg.render(msg_option_bomb3_str, True, "WHITE")
        screen.blit(msg_option_bomb3, (disp_w//2 + 160, disp_h//2 + 90))
        msg_option_bomb4 = font_msg.render(msg_option_bomb4_str, True, "WHITE")
        screen.blit(msg_option_bomb4, (disp_w//2 + 180, disp_h//2 + 90))
        msg_option_bomb_num = font_msg.render(msg_option_bomb_num_str, True, "RED")
        screen.blit(msg_option_bomb_num, (disp_w//2 + 100 + (20*init_bomb), disp_h//2 + 90))

        msg_option_60fps = font_msg.render(msg_option_60fps_str, True, "WHITE")
        if option_select[option_select_num] == "60fps":msg_option_60fps = font_msg.render(msg_option_60fps_str, True, "ORANGE")
        screen.blit(msg_option_60fps, (disp_w//2, disp_h//2 + 130))

        msg_option_60fps_num = font_msg.render(msg_option_60fps_num_str, True, "WHITE")
        screen.blit(msg_option_60fps_num, (disp_w//2 + 100, disp_h//2 + 130))

        msg_option_default = font_msg.render(msg_option_default_str, True, "WHITE")
        if option_select[option_select_num] == "default":msg_option_default = font_msg.render(msg_option_default_str, True, "ORANGE")
        screen.blit(msg_option_default, (disp_w//2, disp_h//2 + 170))

        msg_option_quit = font_msg.render(msg_option_quit_str, True, "WHITE")
        if option_select[option_select_num] == "quit":msg_option_quit = font_msg.render(msg_option_quit_str, True, "ORANGE")
        screen.blit(msg_option_quit, (disp_w//2, disp_h//2 + 210))

              
      #終了
      elif title_state == "QUIT":
        exit_flag = True
        exit_code = '002'

      pg.display.update()
      if fps_fixed:clock.tick(clockspeed)
      frame += 1
      continue
    #---game---

    elif game_state == "Game":
      cmd_move_low = 0
      for event in events:
        # キー入力の受け取り処理
        if event.type == pg.KEYDOWN:
          #キャラクター切り替え
          if event.key == pg.K_q:
            Character[(cmd_tab-1) %2].pos = Character[cmd_tab].pos
            cmd_tab = ((cmd_tab + 1) % 2)
          if event.key == pg.K_ESCAPE:
            pause_screen = screen.copy()
            pause_select_num = 0
            game_state = "Pause"
            dark_overlay = pg.Surface((disp_w, disp_h))
            dark_overlay.set_alpha(255//4)
            dark_overlay.fill((0, 0, 0))
            pause_screen.blit(dark_overlay, (0, 0))
            continue
          if event.key == pg.K_x and bomb > 0:
            score += 1000 * len(Enemies)
            score += 50 * len(Bullet_enemy)
            Enemies.clear()
            Bullet_enemy.clear()
            bomb -= 1
      
      # 移動キー入力の受け取り処理
      move_dir = pg.Vector2(0,0)
      keys = pg.key.get_pressed()
      if keys[pg.K_UP]:
        move_dir.y -= 1
      if keys[pg.K_RIGHT]:
        move_dir.x += 1
      if keys[pg.K_DOWN]:
        move_dir.y += 1
      if keys[pg.K_LEFT]:
        move_dir.x -= 1
      if keys[pg.K_LSHIFT]:
        cmd_move_low = 1
      if keys[pg.K_z]:
        bullet_frame, sub_bullet_frame = Character[cmd_tab].Charactor_bullet_fire(bullet_frame, sub_bullet_frame, Bullet_player, power)

      # 微調整移動時の速度計算
      if cmd_move_low == 1:
        #　速度1/2
        velo_mult = 2
      else:
        velo_mult = 1

      # 弾の移動
      for i in Bullet_player[:]:
        i.move_to(Enemies)

      # 自機移動の処理
      if move_dir.length_squared() > 0:
        move_dir = move_dir.normalize()
        Character[cmd_tab].move_to(move_dir * Character[cmd_tab].velocity / velo_mult)
        # 移動後に、現在の座標を移動可能範囲の中に収める
        # X軸の制限
        min_x = canmvscr[0][0]
        max_x = canmvscr[0][1] - Character[cmd_tab].size.x
        if Character[cmd_tab].pos.x < min_x:
          Character[cmd_tab].pos.x = min_x
        if Character[cmd_tab].pos.x > max_x:
          Character[cmd_tab].pos.x = max_x
        # Y軸の制限
        min_y = canmvscr[1][0]
        max_y = canmvscr[1][1] - Character[cmd_tab].size.y
        if Character[cmd_tab].pos.y < min_y:
          Character[cmd_tab].pos.y = min_y
        if Character[cmd_tab].pos.y > max_y: 
          Character[cmd_tab].pos.y = max_y

      # 敵の登録
      for spawn_info in enemy_schedule[:]:
        if frame == spawn_info["spawn_f"]:
          Enemies.append(enemyCharacter((spawn_info["x"], -spawn_info["enemy_info"]["img_size"][1]),
                                        spawn_info["enemy_info"]["hp"],
                                        spawn_info["enemy_info"]["img_path"],
                                        spawn_info["enemy_info"]["img_size"],
                                        spawn_info["path"],
                                        spawn_info["bullet_path"],
                                        spawn_info["enemy_info"]["img_len"],
                                        bullet_catalog))
          enemy_schedule.remove(spawn_info)

      # 敵の弾の登録
      for be in Bullet_enemy[:]:
        be.move_to()
        if not((canmvscr[1][0] - be.size.y < be.pos.y < canmvscr[1][1]) and (canmvscr[0][0] - be.size.x < be.pos.x < canmvscr[0][1])):
          Bullet_enemy.remove(be)

      # 敵の当たり判定
      for e in Enemies[:]:
        e_rect = pg.Rect((e.pos + e.middle) - (e.Countermeasures / 2), e.Countermeasures)
        for b in Bullet_player[:]:
          b_rect = pg.Rect((b.pos + b.middle) - (b.Countermeasures / 2), b.Countermeasures)
          if e_rect.colliderect(b_rect):
            e.hp -= b.damage
            Bullet_player.remove(b)
            if e.hp <= 0:
              score += 1000
              r = rd.random()
              if r <= 0.33: pass
              else:
                if rd.randint(0, 1) == 0:itemtype = "itemPower"
                else: itemtype = "itemScore"
                Item.append(item((e.pos + e.middle), pg.Vector2(rd.uniform(-4,4),rd.uniform(-2,-4)), item_type[itemtype]["img"],item_type[itemtype]["size"],itemtype))
              if e in Enemies:
                Enemies.remove(e)
              break
              
      # アイテムの移動
      for it in Item[:]:
        it.move_to()
      
      # お古のgraze保存
      tmp_graze = graze
      tmp_point = point

      # 自機の当たり判定
      if unrivaled_frame == 0:
        c_rect = pg.Rect(Character[cmd_tab].pos + Character[cmd_tab].middle - (Character[cmd_tab].Countermeasures / 2), Character[cmd_tab].Countermeasures)
        for eb in Bullet_enemy[:]:
          eb_rect = pg.Rect((eb.pos + eb.middle) - (eb.Countermeasures / 2), eb.Countermeasures)
          eb_graze_rect = pg.Rect((eb.pos + eb.middle) - ((eb.Countermeasures + pg.Vector2(32,32)) / 2), eb.Countermeasures + pg.Vector2(32,32) )
          if c_rect.colliderect(eb_rect):
            player_life -= 1
            lost_power = rd.randint(5,10)
            lost_power = min(power,lost_power)
            power -= lost_power
            for p in range(lost_power):
              Item.append(item((Character[cmd_tab].pos + Character[cmd_tab].middle), pg.Vector2(rd.uniform(-4,4),rd.uniform(-2,-4)), item_type["itemPower"]["img"],item_type["itemPower"]["size"],"itemPower"))
            unrivaled_frame = 300
            Character[cmd_tab].pos = pg.Vector2(canmvscrwh.x / 2 - (48 / 2)+ canmvscroffset.x,disp_h - canmvscrwh.y / 9)
            if player_life < 0:
              game_state = "GameOver"
              continue
          else:
            if c_rect.colliderect(eb_graze_rect) and not eb.grazed:
              graze += 1
              eb.grazed = True
      c_rect = pg.Rect(Character[cmd_tab].pos + Character[cmd_tab].middle - (Character[cmd_tab].size / 2), Character[cmd_tab].size)
      for it in Item[:]:
        it_rect = pg.Rect((it.pos + it.middle) - (it.Countermeasures / 2), it.Countermeasures)
        if c_rect.colliderect(it_rect):
          if it.type == "itemPower" and power < 120:power += 1
          elif it.type == "itemScore":point += 1
          Item.remove(it)

      # grazeによるscore判定
      s_g = graze - tmp_graze
      score += 50 * s_g
      s_p = point - tmp_point
      score += 10000 * s_p

      #背景描画
      screen.fill(pg.Color("#555555"))

      # アイテムの描画

      for it in Item[:]:
        screen.blit(it.get_img(frame), it.get_dp())
        if it.pos.y > disp_h:
          Item.remove(it)

      # 自キャラの描画
      current_img = Character[cmd_tab].get_img(frame)
      if unrivaled_frame > 0:
          current_img.set_alpha(128)
      else:
          current_img.set_alpha(255)
      screen.blit(current_img, Character[cmd_tab].get_dp())

      # 自球の描画
      for i in Bullet_player[:]:
        screen.blit(i.get_img(frame), i.get_dp())
        if i.pos.y < -i.size.y:
          Bullet_player.remove(i)

      # 敵の描画
      for i in Enemies[:]:
        i.update()
        i.bullet_update(Character[cmd_tab].pos + Character[cmd_tab].middle, Bullet_enemy)
        screen.blit(i.get_img(frame),i.get_dp())
        if i.get_finish_path():
          Enemies.remove(i)
      
      # 敵の弾の描画
      for b in Bullet_enemy:
        screen.blit(b.get_img(frame), b.get_dp())

      # 画面外の背景描画
      screen.fill(pg.Color("BLACK"),(0,0,canmvscr[0][0],canmvscr[1][1]))
      screen.fill(pg.Color("BLACK"),(canmvscr[0][1],canmvscr[1][0],disp_w - canmvscr[0][1],canmvscr[1][1]))

      # スコアや残機表示
      current_fps = clock.get_fps()
      score_str = f"{score:09d}"
      fps_str = f'{current_fps:>.2f}fps'
      screen.blit(font_state.render(f"Score  {score_str}",True,"WHITE"),(700,100))
      screen.blit(font_state.render(f"Player {"★" * player_life}",True,"WHITE"),(700,170))
      screen.blit(font_state.render(f"Bomb   {"★" * bomb}",True,"WHITE"),(700,220))
      if power >= 120:
        screen.blit(font_state.render(f"Power  MAX!",True,"WHITE"),(700,300))
      else:
        screen.blit(font_state.render(f"Power  {power}",True,"WHITE"),(700,300))
      screen.blit(font_state.render(f"Graze  {graze}",True,"WHITE"),(700,350))
      screen.blit(font_state.render(f"Point  {point}",True,"WHITE"),(700,400))
      screen.blit(font_msg.render(f"{fps_str}",True,"WHITE"),(900,720))
      
      #フレーム加算
      frame += 1
      bullet_frame += 1
      sub_bullet_frame += 1
      if unrivaled_frame > 0:unrivaled_frame -= 1

      """
      # デバック情報の表示
      current_fps = clock.get_fps()
      fps_str = f'FPS: {current_fps:.2f}'
      frm_str = f'{frame:05}'
      screen.blit(font.render(frm_str,True,'WHITE'),(10,10))
      screen.blit(font.render(f'{Character[cmd_tab].pos}',True,'WHITE'),(10,20))
      screen.blit(font.render(f"select character {str(Character[cmd_tab].name)}",True,"WHITE"),(10,30))
      screen.blit(font.render(f"bullet amount {str(len(Bullet_player))}",True,"WHITE"),(10,40))
      screen.blit(font.render(f"bullet frame {str(bullet_frame)}",True,"WHITE"),(10,50)) 
      screen.blit(font.render(fps_str, True, 'WHITE'), (10, 60))
      screen.blit(font.render(f"enemy amount {str(len(Enemies))}",True,"WHITE"),(10,70))
      screen.blit(font.render(f"eb amount {str(len(Bullet_enemy))}",True,"WHITE"),(10,80))
      """

      # クリア判定
      if len(enemy_schedule) == 0 and len(Enemies) == 0:
          game_state = "GameClear"
          continue
      
      # 画面の更新と同期
      pg.display.update()
      if fps_fixed:clock.tick(clockspeed)
      continue
    
    #---pause---
    elif game_state == "Pause":
      screen.blit(pause_screen, (0,0))

      pg.draw.rect(screen,("#000000"),pg.Rect(disp_w // 2 - 150,disp_h // 2 - 100,300,200))

      for event in events:
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_ESCAPE:
            game_state = "Game"
          if event.key == pg.K_UP and pause_select_num > 0:pause_select_num -= 1
          elif event.key == pg.K_DOWN and pause_select_num < len(pause_select) - 1:pause_select_num += 1
          if event.key == pg.K_z and pause_select[pause_select_num] == "CONTINUE":
            game_state = "Game"
          if event.key == pg.K_z and pause_select[pause_select_num] == "RESTART":
            enemy_schedule = init_game()
            game_state = "Game"
          if event.key == pg.K_z and pause_select[pause_select_num] == "QUIT":
            game_state = "Title"
            

      msg_pause_str = "PAUSE"
      msg_pause_continue_str = "Continue"
      msg_pause_restert_str = "Restart"
      msg_pause_quit_str = "Quit"

      msg_pause = font_title.render(msg_pause_str, True, "WHITE")
      screen.blit(msg_pause, (disp_w//2 - msg_pause.get_width()//2, disp_h//2 -90))
      msg_pause_continue = font_msg.render(msg_pause_continue_str, True, "WHITE")
      if pause_select[pause_select_num] == "CONTINUE":msg_pause_continue = font_msg.render(msg_pause_continue_str, True, "RED")
      screen.blit(msg_pause_continue, (disp_w//2 - msg_pause_continue.get_width()//2, disp_h//2 -20))
      msg_pause_restert = font_msg.render(msg_pause_restert_str, True, "WHITE")
      if pause_select[pause_select_num] == "RESTART":msg_pause_restert = font_msg.render(msg_pause_restert_str, True, "RED")
      screen.blit(msg_pause_restert, (disp_w//2 - msg_pause_restert.get_width()//2, disp_h//2 +10))
      msg_pause_quit = font_msg.render(msg_pause_quit_str, True, "WHITE")
      if pause_select[pause_select_num] == "QUIT":msg_pause_quit = font_msg.render(msg_pause_quit_str, True, "RED")
      screen.blit(msg_pause_quit, (disp_w//2 - msg_pause_quit.get_width()//2, disp_h//2 +40))

      pg.display.update()
      if fps_fixed:clock.tick(clockspeed)
      continue

    #---gameover---
    elif game_state == "GameOver":
      screen.fill(pg.Color("#555555"))
      title_s = font_title.render("GameOver", True, "WHITE")
      screen.blit(title_s, (disp_w//2 - title_s.get_width()//2, disp_h//3))
      
      msg_gameover_score = font_msg.render(f"score {score}", True, "WHITE")
      screen.blit(msg_gameover_score, (disp_w//2 - msg_gameover_score.get_width()//2, disp_h//2))

      if (frame // 30) % 2 == 0:
        msg_s = font_msg.render("PRESS Z KEY TO TITLE", True, "YELLOW")
        screen.blit(msg_s, (disp_w//2 - msg_s.get_width()//2, disp_h//2 + 50))
      
      for event in events:
        if event.type == pg.KEYDOWN and event.key == pg.K_z:
          game_state = "Title"
      pg.display.update()
      if fps_fixed:clock.tick(clockspeed)
      frame += 1
      continue

    #---GameClear---
    elif game_state == "GameClear":
      screen.fill(pg.Color("#555555"))
      
      title_s = font_title.render("GAME CLEAR!!", True, "YELLOW")
      screen.blit(title_s, (disp_w//2 - title_s.get_width()//2, disp_h//3))
      
      msg_score = font_msg.render(f"Final Score: {score}", True, "WHITE")
      screen.blit(msg_score, (disp_w//2 - msg_score.get_width()//2, disp_h//2))

      if (frame // 30) % 2 == 0:
        msg_s = font_msg.render("PRESS Z KEY TO TITLE", True, "CYAN")
        screen.blit(msg_s, (disp_w//2 - msg_s.get_width()//2, disp_h//2 + 50))
      
      for event in events:
        if event.type == pg.KEYDOWN and event.key == pg.K_z:
          game_state = "Title"
          
      pg.display.update()
      if fps_fixed:clock.tick(clockspeed)
      frame += 1
      continue

  # ゲームループ [ここまで]
  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f'プログラムを「コード{code}」で終了しました。')