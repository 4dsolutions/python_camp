all_sprites = [  ]
stage.set_background_color("white")

# sprite = codesters.Text("text")
score = codesters.Text("", 0, 200)
score.set_text_size(40)
# Any font family supported by the browser
# options may include "Arial", "Times", "Courier", "Palatino", "Garamond",
# "Bookman", "Verdana", "Georgia", "Comic Sans MS", "Trebuchet MS", "Arial Black", "Impact"
score.set_text_font("Impact")
hits = 0

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def make_new():
    if len(all_sprites) > 0:
        # pick one to clone
        any_sprite = random.choice(all_sprites)
        new_sprite = any_sprite.clone()
        new_sprite.set_size(0.2)
    else:
        # start from scratch
        virus = "https://www.spc.int/sites/default/files/styles/featured_image/public/featuredimages/blog/2020-02/Covid-19-coronavirus-spc%20pacific%20community%20cps%20communaut%C3%A9%20du%20pacifique%20sant%C3%A9%20health%20jip%C3%A9%20le%20bars.jpg"
        # virus = "meteor1"
        new_sprite = codesters.Sprite(virus, 400, 400)
        new_sprite.hide()
        new_sprite.set_size(0.2)
        new_sprite.goto(0,0)
    # move in some random direction
    xspeed = random.randint(-3,3)
    yspeed = random.randint(-3,3)
    new_sprite.set_x_speed(xspeed)
    new_sprite.set_y_speed(yspeed)
    # add to list
    all_sprites.append(new_sprite)

def remove_old():
    if len(all_sprites)>0:
        any_sprite = random.choice(all_sprites)
        all_sprites.remove(any_sprite)
        stage.remove_sprite(any_sprite)

def turn():
    # take control
    # how often to make new versus
    # remove old?  Play with settings
    if roll_dice() <  10:
        make_new()
    if roll_dice() >= 11:
        remove_old()

stage.event_interval(turn, 0.5)

URL = "https://images-na.ssl-images-amazon.com/images/I/61B-bmUeRbL._AC_SL1000_.jpg"
player = codesters.Sprite(URL, -200, -200)
player.set_size(0.1)

def left_key():
    player.move_left(20)

def right_key():
    player.move_right(20)

def up_key():
    player.move_up(20)

def down_key():
    player.move_down(20)

def collision(sprite, hit_sprite):
    global hits
    hits = hits + 1
    score.set_text(hits)
    if hit_sprite in all_sprites:
        all_sprites.remove(hit_sprite)
        stage.remove_sprite(hit_sprite)

stage.event_key("right", right_key)
stage.event_key("left", left_key)
stage.event_key("up", up_key)
stage.event_key("down", down_key)

player.event_collision(collision)
