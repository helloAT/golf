def menu(level):
    if level == 0:
        textSize(150)
        textAlign(CENTER)
        text("Golf", width / 2, height / 4)
        rectMode(CENTER)
        rect(width / 2, height / 2, 150, 75)
        textSize(50)
        fill(0)
        text("Play!", width / 2, height / 2 + 15)
        fill(255)
