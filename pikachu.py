URL = "https://vignette.wikia.nocookie.net/school-daze/images/4/4c/Pikachu-PNG-HD.png"
sprite = codesters.Sprite(URL)

sprite.set_size(0.5) # half the size

for loop in range(5):
    sprite.show()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sprite.go_to(x, y)
    stage.wait(.5)
    sprite.stamp()
    sprite.hide()
