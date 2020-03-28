t0 ="""\
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>--<>-
<>-<>-<>-<>-<>-<>-<>-
"""

t1 ="""\
<>-<>-<>-<>-<>-<>-<>-
<>--<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
"""

t2 ="""\
<>-<>-<>-<>-<>--<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
<>-<>-<>-<>-<>-<>-<>-
"""

stage.set_background_color("black")
# sprite = codesters.Text("text", x, y)
sprite = codesters.Text(t0, 0, 0, 'mediumspringgreen')
# sprite = codesters.Text("text", x, y, "color")
# Any font family supported by the browser
# options may include "Arial", "Times", "Courier", "Palatino", "Garamond",
# "Bookman", "Verdana", "Georgia", "Comic Sans MS", "Trebuchet MS", "Arial Black", "Impact"
sprite.set_text_font("Comic Sans MS")
sprite.set_text_size(40)

for turn in range(100):
    t = random.choice((t0, t1, t2))
    sprite.set_text(t)
    stage.wait(0.2)
