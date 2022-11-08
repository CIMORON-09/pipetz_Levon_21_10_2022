import random

import wrap

spisok_harikov = []
udalenie = 0
wrap.world.create_world(600, 600)
wrap.add_sprite_dir("sprite")
skolko = 0
nazhali=1
up=1
right=1

first = wrap.sprite.add_text("1.Если ты нажмешь Space то все шарики остановятся", 260, 30, text_color=[5, 55, 125])
second = wrap.sprite.add_text("2.Если ты нажмешь Del то все шарики удалтся ", 250, 60, text_color=[5, 55, 125])
third=wrap.sprite.add_text("3.Cколько шариков на экрне", 135, 90, text_color=[5, 55, 125])
fourth=wrap.sprite.add_text("4.Eсли ты нажмешь 1 то включится обычный режим полета",300, 120, text_color=[5, 55, 125])
fifth=wrap.sprite.add_text("5.Eсли ты нажмешь 2 то включится необычный полет шариков",300, 150, text_color=[5, 55, 125])
sixth=wrap.sprite.add_text("6.Если нажмешь p то все надписи исчезнут",300, 180, text_color=[5, 55, 125])

kolvo_harikov = wrap.sprite.add_text("0", 280, 90, text_color=[5, 55, 125])

wrap.sprite.move_left_to(first,0)
wrap.sprite.move_left_to(second,0)
wrap.sprite.move_left_to(third,0)
wrap.sprite.move_left_to(fourth,0)
wrap.sprite.move_left_to(fifth,0)
wrap.sprite.move_left_to(sixth,0)




@wrap.always(delay=1000)
def risovka_kvadratov():
    otvet = random.randint(1, 3)
    if otvet == 1:
        otvet = "edad"

    if otvet == 3:
        otvet = "zeleniy"
    if otvet == 2:
        otvet = "siniy"
    koordinatx = random.randint(50, 550)
    koordinaty = random.randint(50, 550)
    razmer = random.randint(5, 27)

    kvadrat_1 = wrap.sprite.add("lol", koordinatx, koordinaty, otvet)
    wrap.sprite.set_size(kvadrat_1, razmer, razmer)

    speedx_1 = random.randint(1, 5)
    speedx_2 = random.randint(-5, -1)
    speedxgriki = [speedx_1, speedx_2]

    speedy_1 = random.randint(1, 5)
    speedy_2 = random.randint(-5, -1)
    speedygriki = [speedy_1, speedy_2]

    speedx = random.choice(speedxgriki)
    speedy = random.choice(speedygriki)

    ss = {"id": kvadrat_1, "speedx": speedx, "speedy": speedy,"speedx2":-2,"speedy2": -2 }

    spisok_harikov.append(ss)
    print("ppp")




@wrap.on_key_down(wrap.K_p)
def info():
    global udalenie, first, seecond
    udalenie += 1

    if udalenie % 2 == 0:
        wrap.sprite.hide(first)
        wrap.sprite.hide(second)
        wrap.sprite.hide(third)
        wrap.sprite.hide(fourth)
        wrap.sprite.hide(fifth)
        wrap.sprite.hide(sixth)
        wrap.sprite.hide(kolvo_harikov)

    if udalenie % 2 == 1:
        wrap.sprite.show(kolvo_harikov)
        wrap.sprite.show(first)
        wrap.sprite.show(second)
        wrap.sprite.show(third)
        wrap.sprite.show(fourth)
        wrap.sprite.show(fifth)
        wrap.sprite.show(sixth)





@wrap.always(delay=10)
def rrrrrr():
    global speedy, speedx, skolko, kolvo_harikov, nazhali,right,up

    if skolko % 2 == 1:
        return


    if  nazhali==1  :
        for did in spisok_harikov:
            wrap.sprite.move(did["id"], did["speedx"], did["speedy"])
        otbivka()


    # if right==0 and up==0:








    if nazhali == 2:
        for did in spisok_harikov:
            wrap.sprite.move(did["id"], did["speedx2"], did["speedy2"])
        otbivka()

    skolko_elementov = len(spisok_harikov)
    wrap.sprite_text.set_text(kolvo_harikov, str(skolko_elementov))




def otbivka():
    for did in spisok_harikov:


        bottom = wrap.sprite.get_bottom(did["id"])

        right = wrap.sprite.get_right(did["id"])

        left = wrap.sprite.get_left(did["id"])

        top = wrap.sprite.get_top(did["id"])

        if top < 0:
            wrap.sprite.move_top_to(did["id"], 0)
            did["speedy"] = -did["speedy"]

        if bottom > 600:
            wrap.sprite.move_bottom_to(did["id"], 600)
            did["speedy"] = -did["speedy"]

        if right > 600:
            wrap.sprite.move_right_to(did["id"], 600)
            did["speedx"] = -did["speedx"]

        if left < 0:
            wrap.sprite.move_left_to(did["id"], 0)
            did["speedx"] = -did["speedx"]












# сменяем траекторию полета шариков
@wrap.on_key_down()
def goggga(keys):
    global nazhali
    if wrap.K_1 in keys:
        nazhali = 1

    if wrap.K_2 in keys:
        nazhali = 2




# удаляем все шарики с экрана
@wrap.on_key_down(wrap.K_d)
def udalenie_sharikov():
    global spisok_harikov
    for did in spisok_harikov:
        wrap.sprite.remove(did["id"])
    spisok_harikov.clear()
    print("regfd")


# останавливаем движение шариков
@wrap.on_key_down(wrap.K_SPACE)
def ostanovka():
    global skolko
    skolko += 1
    print("dssc")

@wrap.on_key_down(wrap.K_UP,wrap.K_DOWN,wrap.K_LEFT,wrap.K_RIGHT)
def vibor_ugla_poleta_harika(key):
    global up,right

    if wrap.K_UP==key:
        up=1

    if wrap.K_DOWN==key:
        up=0

    if wrap.K_RIGHT==key:
        right=1

    if wrap.K_LEFT==key:
        right=0

import wrap_py

wrap_py.app.start()
