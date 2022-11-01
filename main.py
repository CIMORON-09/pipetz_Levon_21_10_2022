import random

import wrap
spisok_harikov = []
udalenie=0
wrap.world.create_world(600,600)
wrap.add_sprite_dir("sprite")
skolko=0
first = wrap.sprite.add_text("1.Если ты нажмешь Space то все шарики остановятся", 260, 30, text_color=[5, 55, 125])
second = wrap.sprite.add_text("2.Если ты нажмешь Del то все шарики удалтся ", 250, 60, text_color=[5, 55, 125])
wrap.sprite.add_text("3.Cколько шариков на экрне", 135, 100, text_color=[5, 55, 125])
kolvo_harikov = wrap.sprite.add_text("0", 280,100, text_color=[5, 55, 125])


@wrap.always(delay=3000)
def risovka_kvadratov():
    otvet=random.randint(1,3)
    if otvet==1:
        otvet="edad"

    if otvet==3:
        otvet="zeleniy"
    if otvet==2 :
        otvet="siniy"
    koordinatx=random.randint(50,550)
    koordinaty=random.randint(50,550)
    razmer=random.randint(5,27)

    kvadrat_1 = wrap.sprite.add("lol", koordinatx, koordinaty,otvet)
    wrap.sprite.set_size(kvadrat_1,razmer,razmer)
    speedx_1=random.randint(1,5)
    speedx_2=random.randint(-5,-1)
    speedxgriki=[speedx_1,speedx_2]

    speedy_1 = random.randint(1,5)
    speedy_2 = random.randint(-5,-1)
    speedygriki=[speedy_1,speedy_2]

    speedx=random.choice(speedxgriki)
    speedy=random.choice(speedygriki)

    ss = {"id": kvadrat_1, "speedx":speedx,  "speedy":speedy }



    spisok_harikov.append(ss)
@wrap.on_key_down(wrap.K_p)
def udalenie_nadpisey():
    global udalenie
    udalenie+=1

@wrap.on_key_down(wrap.K_p)
def info():
    global udalenie , first , seecond

    if udalenie % 2 == 0:
        wrap.sprite.hide(first)
        wrap.sprite.hide(second)

    if udalenie % 2 ==1:
        wrap.sprite.show(first)
        wrap.sprite.show(second)



@wrap.on_key_down(wrap.K_SPACE)
def ostanovka():
    global skolko
    skolko+=1
    print("dssc")



@wrap.on_key_down(wrap.K_d)
def udalenie_sharikov():
    global spisok_harikov
    for did in spisok_harikov:

        wrap.sprite.remove(did["id"])
    spisok_harikov.clear()
    print("regfd")




@wrap.always(delay=10)
def rrrrrr():
    global speedy,speedx,spisok_harikov,skolko,kolvo_harikov

    if skolko % 2 == 1:
        return

    skolko_elementov=len(spisok_harikov)

    wrap.sprite_text.set_text(kolvo_harikov,str(skolko_elementov))


    for did in   spisok_harikov:
        wrap.sprite.move(did["id"], did["speedx"], did ["speedy"])

        bottom=wrap.sprite.get_bottom(did["id"])
        right=wrap.sprite.get_right(did["id"])
        left=wrap.sprite.get_left(did["id"])
        top=wrap.sprite.get_top(did["id"])

        if top<0:
            wrap.sprite.move_top_to(did["id"],0)
            did["speedy"] = -did["speedy"]

        if bottom > 600:
            wrap.sprite.move_bottom_to(did["id"], 600)
            did["speedy"] = -did["speedy"]

        if right >600:
            wrap.sprite.move_right_to(did["id"],600)
            did["speedx"]=-did["speedx"]
        if left < 0:
            wrap.sprite.move_left_to(did["id"],0)
            did["speedx"]=-did["speedx"]




import wrap_py
wrap_py.app.start()