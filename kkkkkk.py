import wrap
wrap.world.create_world(600,600)
wrap.add_sprite_dir("sprite")

kvadrat_1 = wrap.sprite.add("lol", 300, 100, "edad", )
ss={"id":kvadrat_1,"speedx":1}
kvadrat_2 = wrap.sprite.add("lol", 200, 100, "edad", )
yog={"id":kvadrat_2,"speedx":3}
kvadrat_3 = wrap.sprite.add("lol", 100, 100, "edad", )
oo={"id":kvadrat_3,"speedx":4}

eee=[]

eee.append(ss)
eee.append(yog)
eee.append(oo)
@wrap.always
def ghhhj():
    for did in eee:
        did_aydi=did["id"]
        did_speedx=did["speedx"]


        wrap.sprite.move(did_aydi,did_speedx,0)

import wrap_py
wrap_py.app.start()