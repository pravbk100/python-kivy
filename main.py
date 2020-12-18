from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition
from kivy.lang import Builder
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.image import Image
# from kivy.core.window import Window
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.audio import SoundLoader, Sound
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.storage.dictstore import DictStore
import random
from os.path import join
from kivy import kivy_home_dir

# Window.size = (1080, 1920)

# dict lists ----------------------------------------------------------------
ani_dicts = {1: 'DOG', 2: 'COW', 3: 'CAT', 4: 'BEE', 5: 'OWL', 6: 'RAT', 7: 'PIG', 8: 'FOX', 9: 'BAT', 10: 'LION', 11: 'WOLF', 12: 'GOAT', 13: 'DEER', 14: 'FROG', 15: 'PANDA', 16: 'SEAL', 17: 'ORCA', 18: 'DOVE', 19: 'CROW', 20: 'ANTS', 21: 'ZEBRA', 22: 'SHEEP', 23: 'HORSE', 24: 'TIGER', 25: 'SNAKE', 26: 'OTTER', 27: 'CAMEL', 28: 'DONKEY', 29: 'CHEETAH', 30: 'SWAN', 31: 'HYENA', 32: 'LLAMA', 33: 'PARROT', 34: 'BISON', 35: 'RABBIT', 36: 'EAGLE', 37: 'GOOSE', 38: 'JACKAL', 39: 'PIGEON', 40: 'GORILLA', 41: 'GIRAFFE', 42: 'JAGUAR', 43: 'WALRUS', 44: 'COYOTE', 45: 'BEAVER', 46: 'BUFFALO', 47: 'COUGAR', 48: 'WOMBAT', 49: 'SPIDER', 50: 'DOLPHIN', 51: 'LEOPARD', 52: 'GOPHER', 53: 'MONKEY', 54: 'ELEPHANT', 55: 'PEACOCK', 56: 'RACCOON', 57: 'PENGUIN', 58: 'OSTRICH', 59: 'MEERKAT', 60: 'SPARROW', 61: 'PANTHER', 62: 'PORCUPINE', 63: 'REDPANDA', 64: 'SQUIRREL', 65: 'OPOSSUM', 66: 'CROCODILE', 67: 'CHIPMUNK', 68: 'POLARBEAR', 69: 'ARMADILLO', 70: 'ANACONDA', 71: 'KANGAROO', 72: 'BLACKBEAR', 73: 'CHIMPANZEE', 74: 'MONGOOSE', 75: 'RHINOCEROS', 76: 'GRIZZLYBEAR', 77: 'HEDGEHOG', 78: 'KOALABEAR', 79: 'ORANGUTAN', 80: 'HIPPOPOTAMUS', 81: 'HUMPBACKWHALE', 82: 'SCIMITARORYX'}
fru_dicts = {1: 'LIME', 2: 'MANGO', 3: 'FIG', 4: 'PEAR', 5: 'GUAVA', 6: 'PLUM', 7: 'PEACH', 8: 'YUZU', 9: 'APPLE',
             10: 'PAPAYA', 11: 'ORANGE', 12: 'LEMON', 13: 'BANANA', 14: 'GRAPES', 15: 'DURIAN', 16: 'CHERRY',
             17: 'COCONUT', 18: 'QUINCE', 19: 'APRICOT', 20: 'SOURSOP', 21: 'CUCUMBER', 22: 'AVOCADO', 23: 'TAMARIND',
             24: 'PINEAPPLE', 25: 'WATERMELON', 26: 'STARFRUIT', 27: 'JACKFRUIT', 28: 'STRAWBERRY', 29: 'KIWIFRUIT',
             30: 'RASPBERRY', 31: 'GRAPEFRUIT', 32: 'BLUEBERRY', 33: 'PASSIONFRUIT', 34: 'BLACKBERRY', 35: 'PERSIMMON',
             36: 'PINEBERRY', 37: 'MULBERRY', 38: 'KUMQUAT', 39: 'GOOSEBERRY', 40: 'DRAGONFRUIT'}
veg_dicts = {1: 'PEAS', 2: 'TOMATO', 3: 'CORN', 4: 'MINT', 5: 'YAM', 6: 'CHIVE', 7: 'CHILLY', 8: 'BEAN', 9: 'TARO',
             10: 'KALE', 11: 'GINGER', 12: 'GARLIC', 13: 'LEEK', 14: 'POTATO', 15: 'ONION', 16: 'TURNIP', 17: 'CELERY',
             18: 'CABBAGE', 19: 'SPINACH', 20: 'CARROT', 21: 'LETTUCE', 22: 'PUMPKIN', 23: 'PARSNIP', 24: 'CUCUMBER',
             25: 'EGGPLANT', 26: 'SQUASH', 27: 'CAPSICUM', 28: 'BROCCOLI', 29: 'BEETROOT', 30: 'SWEETPOTATO',
             31: 'WHITERADISH', 32: 'CORIANDER', 33: 'CHAYOTE', 34: 'CAULIFLOWER', 35: 'MUSHROOM', 36: 'GREENONION',
             37: 'RADICCHIO', 38: 'REDRADISH', 39: 'BITTERGOURD', 40: 'ARTICHOKE', 41: 'BRUSSELSPROUT', 42: 'ZUCCHINI'}
# dict list end -------------------------------------------------------------

adicts = ani_dicts

# this is to save dicts------------------------------------------------------
user_data_dir = App().user_data_dir
savedict = DictStore(join(user_data_dir, "SavedState"))
if savedict.exists('ani_d'):
    svd_anilst = savedict.get('ani_d')['ani_dicts']
else:
    savedict.put('ani_d', ani_dicts=1)
    svd_anilst = 1
if savedict.exists('fru_d'):
    svd_frulst = savedict.get('fru_d')['fru_dicts']
else:
    savedict.put('fru_d', fru_dicts=1)
    svd_frulst = 1
if savedict.exists('veg_d'):
    svd_veglst = savedict.get('veg_d')['veg_dicts']
else:
    savedict.put('veg_d', veg_dicts=1)
    svd_veglst = 1
#print(svd_anilst,svd_frulst,svd_veglst)
# save dicts end ------------------------------------------------------------

start_list = 1

# sounds --------------------------------------------------------------------
sound = SoundLoader.load('spellebg.wav')
butaud = SoundLoader.load('butaud.wav')
fail = SoundLoader.load('fail.wav')
success = SoundLoader.load('succss.wav')
sound.loop = True
sound.state = 'stop'
fail.volume = 0
success.volume = 0
fail.play()
success.play()


# sounds end ----------------------------------------------------------------

class Home(ScreenManager):
    data = ObjectProperty(None)
    pass


# st screen start ----------------------------------------------------------------
class StSc(Screen):
    def __init__(self, **kwargs):
        super(StSc, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start)

    def on_start(self, *args):
        global sound
        self.ids.imid.size = 0, 0
        animation = Animation(size=(100, 100), t='out_bounce')
        sound.play()
        animation.start(self.ids.imid)
        if self.manager.current != "FirstSc":
            Clock.schedule_once(self.callbackfun, 1)

    def callbackfun(self, dt):
        # print(self.manager.current)
        # print(self.manager.next())
        self.manager.current = self.manager.next()


# st screen end -------------------------------------------------------------------

# 1st screen start ----------------------------------------------------------------
class FirstSc(Screen):

    def on_pre_enter(self, *args):
        # print('hi')
        # print(savedict.get('ani_d'))
        # print(savedict.get('fru_d'))
        # print(savedict.get('veg_d'))
        # print('hi')
        global sound, success, fail, butaud, adicts, ani_dicts, fru_dicts, veg_dicts, start_list, svd_anilst, svd_frulst, svd_veglst
        if sound.state == 'play':
            self.ids.aa.source = 'musicon.png'
        else:
            self.ids.aa.source = 'musicoff.png'
        if adicts == ani_dicts and svd_anilst > 1:
            self.ids.acon.size_hint = (.5, 0.08)
            self.ids.acon.disabled = False
        elif adicts == fru_dicts and svd_frulst > 1:
            self.ids.acon.size_hint = (.5, 0.08)
            self.ids.acon.disabled = False
        elif adicts == veg_dicts and svd_veglst > 1:
            self.ids.acon.size_hint = (.5, 0.08)
            self.ids.acon.disabled = False
        else:
            self.ids.acon.size_hint = (0, 0)
            self.ids.acon.disabled = True

    def audio(self):
        global sound, success, fail, butaud
        a = 'musicon.png'
        b = 'musicoff.png'
        if sound.state == 'stop':
            sound.play()
            fail.volume = 1
            success.volume = 1
            butaud.volume = 1
            self.ids.aa.source = a
        else:
            sound.stop()
            fail.volume = 0
            success.volume = 0
            butaud.volume = 0
            self.ids.aa.source = b

    def on_presStart(self):
        global start_list
        self.ids.ac.color = (.9, 1, .9, 1)
        self.ids.ac.size_hint = .497, .277
        start_list = 1

    def on_relStart(self):
        self.ids.ac.color = (1, 1, 1, 1)
        self.ids.ac.size_hint = .5, .28

    def on_presConStart(self):
        global adicts, ani_dicts, fru_dicts, veg_dicts, start_list, svd_anilst, svd_frulst, svd_veglst
        global start_list
        self.ids.acon.color = (.9, 1, .9, 1)
        self.ids.acon.size_hint = .45, .08
        if adicts == ani_dicts:
            start_list = svd_anilst
        elif adicts == fru_dicts:
            start_list = svd_frulst
        elif adicts == veg_dicts:
            start_list = svd_veglst

    def on_relConStart(self):
        global adicts, ani_dicts, fru_dicts, veg_dicts, start_list, svd_anilst, svd_frulst, svd_veglst
        self.ids.acon.color = (1, 1, 1, 1)
        self.ids.acon.size_hint = .5, .08
        if adicts == ani_dicts:
            if start_list == 83:
                self.parent.current = "end"
            else:
                self.parent.current = "2nd"
        elif adicts == fru_dicts:
            if start_list == 41:
                self.parent.current = "end"
            else:
                self.parent.current = "2nd"
        elif adicts == veg_dicts:
            if start_list == 43:
                self.parent.current = "end"
            else:
                self.parent.current = "2nd"
#        print('a')
#        print(svd_anilst, svd_frulst, svd_veglst)
#        print('a')

    def soundplay(self):
        global butaud
        butaud.play()


# 1st screen end ----------------------------------------------------------------

# custbutt start ----------------------------------------------------------------

class ImBut(ButtonBehavior, Image):
    pass


# custbutt end ------------------------------------------------------------------

# sec sc start ------------------------------------------------------------------
class SecSc(Screen):

    def on_pre_enter(self, *args):
        global sound, success, fail, butaud, adicts, ani_dicts, fru_dicts, veg_dicts, start_list, svd_anilst, svd_frulst, svd_veglst
        self.a = start_list
        self.all_dicts = adicts
        self.stri = self.all_dicts[self.a]
        self.normal_list = list(self.stri)
        self.rand_list = list.copy(self.normal_list)
        random.shuffle(self.rand_list)
        self.ids.imid.source = self.stri + ".png"
        px = 0
        if len(self.rand_list) <= 10 and len(self.rand_list) > 4:
            px = .058
        elif len(self.rand_list) > 10:
            px = .072
        elif len(self.rand_list) == 3:
            px = .225
        elif len(self.rand_list) == 4:
            px = .14
        py = (.2, .245)[len(self.rand_list) > 10]
        sy = (.1, .07)[len(self.rand_list) > 10]
        sx = sy + .05
        spX = .17
        self.buttons = []
        for i, j in enumerate(self.rand_list):
            # self.buttons.append(ImBut(source='categ.png',text=j,on_press=self.o_p))
            self.buttons.append(
                Factory.ImButb(text=j, size_hint=(sx, sy), pos_hint={"x": px, "y": py}, on_press=self.o_p))
            self.ids.grid.add_widget(self.buttons[i])
            px += spX
            if len(self.rand_list) <= 10:
                if i == 4 and len(self.rand_list) == 6:
                    px = .399
                    py -= .11
                elif i == 4 and len(self.rand_list) == 7:
                    px = .315
                    py -= .11
                elif i == 4 and len(self.rand_list) == 8:
                    px = .2275
                    py -= .11
                elif i == 4 and len(self.rand_list) == 9:
                    px = .12
                    py -= .11
                elif i == 4 and len(self.rand_list) == 10:
                    px = .0559
                    py -= .11
            else:
                if i == 4 and len(self.rand_list) == 11:
                    px = .073
                    py -= .08
                elif i == 4 and len(self.rand_list) == 12:
                    px = .073
                    py -= .08
                elif i == 4 and len(self.rand_list) == 13:
                    px = .073
                    py -= .08
                elif i == 4 and len(self.rand_list) == 14:
                    px = .073
                    py -= .08
                elif i == 4 and len(self.rand_list) == 15:
                    px = .073
                    py -= .08
                elif i == 9 and len(self.rand_list) == 11:
                    px = .412
                    py -= .08
                elif i == 9 and len(self.rand_list) == 12:
                    px = .325
                    py -= .08
                elif i == 9 and len(self.rand_list) == 13:
                    px = .243
                    py -= .08
                elif i == 9 and len(self.rand_list) == 14:
                    px = .15
                    py -= .08
                elif i == 9 and len(self.rand_list) == 15:
                    px = .072
                    py -= .08
        if sound.state == 'play':
            fail.volume = 1
            success.volume = 1
            butaud.volume = 1
            self.ids.mon.source = 'musicon.png'
        else:
            self.ids.mon.source = 'musicoff.png'
            fail.volume = 0
            success.volume = 0
            butaud.volume = 0

    def ansanimate(self):
        success.play()
        self.ids.corr_ans.size = 0, 0
        animation = Animation(size=(500, 500), t='out_bounce')
        animation.start(self.ids.corr_ans)

    def wr_ansanimate(self):
        fail.play()
        self.ids.wr_ans.size = 0, 0
        animation = Animation(size=(500, 500), t='out_bounce')
        animation.start(self.ids.wr_ans)

    def o_p(self, instance):
        a = self.ids.spltxt.text
        if instance.on_press:
            self.butaudi()
            instance.back_color = (1, 1, 1, .7)
            instance.disabled = True
        self.ids.spltxt.text = a + str(instance.text)
        if len(self.ids.spltxt.text) == len(self.stri):
            if self.ids.spltxt.text == self.stri:
                self.ansanimate()
                Clock.schedule_once(self.delayy, 2)
            else:
                self.ids.wrbg.opacity = .9
                self.wr_ansanimate()
                Clock.schedule_once(self.wr_screen, 2)

    def delayy(self, dt):
        global sound, success, fail, butaud, adicts, ani_dicts, fru_dicts, veg_dicts, start_list, svd_anilst, svd_frulst, svd_veglst
        start_list += 1
        if self.all_dicts == ani_dicts:
            savedict.put('ani_d', ani_dicts=start_list)
            svd_anilst = start_list
        elif self.all_dicts == veg_dicts:
            savedict.put('veg_d', veg_dicts=start_list)
            svd_veglst = start_list
        elif self.all_dicts == fru_dicts:
            savedict.put('fru_d', fru_dicts=start_list)
            svd_frulst = start_list
#        print(svd_anilst, svd_frulst, svd_veglst)
#        print(savedict.get('ani_d'), savedict.get('fru_d'), savedict.get('veg_d'))
        self.parent.current = "3rd"

    def wr_screen(self, dt):
        self.manager.transition = FadeTransition(duration=.8)
        self.parent.current = "3rd"
        self.manager.transition = SlideTransition(direction='left')

    def on_leave(self, *args):
        self.ids.spltxt.text = ''
        self.ids.corr_ans.size = 0, 0
        self.ids.wr_ans.size = 0, 0
        self.ids.wrbg.opacity = 0
        for i, j in enumerate(self.rand_list):
            self.ids.grid.remove_widget(self.buttons[i])

    def butloop(self):
        global sound, success, fail, butaud
        if sound.state == 'stop':
            sound.play()
            fail.volume = 1
            success.volume = 1
            butaud.volume = 1
            self.ids.mon.source = 'musicon.png'
        else:
            sound.stop()
            fail.volume = 0
            success.volume = 0
            butaud.volume = 0
            self.ids.mon.source = 'musicoff.png'

    def butaudi(self):
        butaud.play()


# sec screen ends---------------------------------------------------------------------

# third screen starts-----------------------------------------------------------------
class ThirdSc(Screen):

    def on_pre_enter(self, *args):
        global sound, success, fail, butaud, adicts, ani_dicts, fru_dicts, veg_dicts, start_list, svd_anilst, svd_frulst, svd_veglst
        self.a = start_list
        self.all_dicts = adicts
        self.stri = self.all_dicts[self.a]
        self.normal_list = list(self.stri)
        self.rand_list = list.copy(self.normal_list)
        random.shuffle(self.rand_list)
        self.ids.imid.source = self.stri + ".png"
        px = 0
        if len(self.rand_list) <= 10 and len(self.rand_list) > 4:
            px = .058
        elif len(self.rand_list) > 10:
            px = .072
        elif len(self.rand_list) == 3:
            px = .225
        elif len(self.rand_list) == 4:
            px = .14
        py = (.2, .245)[len(self.rand_list) > 10]
        sy = (.1, .07)[len(self.rand_list) > 10]
        sx = sy + .05
        spX = .17
        self.buttons = []
        for i, j in enumerate(self.rand_list):
            # self.buttons.append(ImBut(source='categ.png',text=j,on_press=self.o_p))
            self.buttons.append(
                Factory.ImButb(text=j, size_hint=(sx, sy), pos_hint={"x": px, "y": py}, on_press=self.o_p))
            self.ids.grid.add_widget(self.buttons[i])
            px += spX
            if len(self.rand_list) <= 10:
                if i == 4 and len(self.rand_list) == 6:
                    px = .399
                    py -= .11
                elif i == 4 and len(self.rand_list) == 7:
                    px = .315
                    py -= .11
                elif i == 4 and len(self.rand_list) == 8:
                    px = .2275
                    py -= .11
                elif i == 4 and len(self.rand_list) == 9:
                    px = .12
                    py -= .11
                elif i == 4 and len(self.rand_list) == 10:
                    px = .0559
                    py -= .11
            else:
                if i == 4 and len(self.rand_list) == 11:
                    px = .073
                    py -= .08
                elif i == 4 and len(self.rand_list) == 12:
                    px = .073
                    py -= .08
                elif i == 4 and len(self.rand_list) == 13:
                    px = .073
                    py -= .08
                elif i == 4 and len(self.rand_list) == 14:
                    px = .073
                    py -= .08
                elif i == 4 and len(self.rand_list) == 15:
                    px = .073
                    py -= .08
                elif i == 9 and len(self.rand_list) == 11:
                    px = .412
                    py -= .08
                elif i == 9 and len(self.rand_list) == 12:
                    px = .325
                    py -= .08
                elif i == 9 and len(self.rand_list) == 13:
                    px = .243
                    py -= .08
                elif i == 9 and len(self.rand_list) == 14:
                    px = .15
                    py -= .08
                elif i == 9 and len(self.rand_list) == 15:
                    px = .072
                    py -= .08
        if sound.state == 'play':
            self.ids.mon.source = 'musicon.png'
            fail.volume = 1
            success.volume = 1
            butaud.volume = 1
        else:
            self.ids.mon.source = 'musicoff.png'
            fail.volume = 0
            success.volume = 0
            butaud.volume = 0

    def ansanimate(self):
        success.play()
        self.ids.corr_ans.size = 0, 0
        animation = Animation(size=(500, 500), t='out_bounce')
        animation.start(self.ids.corr_ans)

    def wr_ansanimate(self):
        fail.play()
        self.ids.wr_ans.size = 0, 0
        animation = Animation(size=(500, 500), t='out_bounce')
        animation.start(self.ids.wr_ans)

    def o_p(self, instance):
        a = self.ids.spltxt.text
        if instance.on_press:
            self.butaudi()
            instance.back_color = (1, 1, 1, .7)
            instance.disabled = True
        self.ids.spltxt.text = a + str(instance.text)
        if len(self.ids.spltxt.text) == len(self.stri):
            if self.ids.spltxt.text == self.stri:
                self.ansanimate()
                Clock.schedule_once(self.delayy, 2)
            else:
                self.ids.wrbg.opacity = .9
                self.wr_ansanimate()
                Clock.schedule_once(self.wr_screen, 2)

    def delayy(self, dt):
        global sound, success, fail, butaud, adicts, ani_dicts, fru_dicts, veg_dicts, start_list, svd_anilst, svd_frulst, svd_veglst
        start_list += 1
        if self.all_dicts == ani_dicts:
            savedict.put('ani_d', ani_dicts=start_list)
            svd_anilst = start_list
        elif self.all_dicts == veg_dicts:
            savedict.put('veg_d', veg_dicts=start_list)
            svd_veglst = start_list
        elif self.all_dicts == fru_dicts:
            savedict.put('fru_d', fru_dicts=start_list)
            svd_frulst = start_list
#        print(svd_anilst,svd_frulst,svd_veglst)
#        print(savedict.get('ani_d'),savedict.get('fru_d'),savedict.get('veg_d'))
        self.parent.current = "2nd"

    def wr_screen(self, dt):
        self.manager.transition = FadeTransition(duration=.8)
        self.parent.current = "2nd"
        self.manager.transition = SlideTransition(direction='left')

    def on_leave(self, *args):
        self.ids.spltxt.text = ''
        self.ids.corr_ans.size = 0, 0
        self.ids.wr_ans.size = 0, 0
        self.ids.wrbg.opacity = 0
        rembuts = self.buttons
        for i, j in enumerate(self.rand_list):
            self.ids.grid.remove_widget(self.buttons[i])

    def butloop(self):
        global sound, success, fail, butaud
        if sound.state == 'stop':
            sound.play()
            fail.volume = 1
            success.volume = 1
            butaud.volume = 1
            self.ids.mon.source = 'musicon.png'
        else:
            sound.stop()
            fail.volume = 0
            success.volume = 0
            butaud.volume = 0
            self.ids.mon.source = 'musicoff.png'
        pass

    def butaudi(self):
        butaud.play()


# third screen ends--------------------------------------------------------------

# cat sc start ------------------------------------------------------------------
class Category(Screen):
    global butaud

    def gotoaniFpage(self):
        global adicts
        global ani_dicts
        adicts = ani_dicts
        self.ids.cata.color = (1, 1, 1, 1)
        self.ids.cata.size_hint = .9, .11

    def onpressani(self):
        self.ids.cata.color = (1, 1, 2, .8)
        self.ids.cata.size_hint = .8, .11

    def gotoFruFpage(self):
        global adicts
        global ani_dicts
        adicts = fru_dicts
        self.ids.catb.color = (1, 1, 1, 1)
        self.ids.catb.size_hint = .9, .11

    def onpressfru(self):
        self.ids.catb.color = (1, 1, 2, .8)
        self.ids.catb.size_hint = .8, .11

    def gotoVegFpage(self):
        global adicts
        global ani_dicts
        adicts = veg_dicts
        self.ids.catc.color = (1, 1, 1, 1)
        self.ids.catc.size_hint = .9, .11

    def onpressveg(self):
        self.ids.catc.color = (1, 1, 2, .8)
        self.ids.catc.size_hint = .8, .11

    def butaudi(self):
        global sound, success, fail, butaud
        if sound.state == 'stop':
            butaud.volume = 0
            butaud.play()
        else:
            butaud.volume = 1
            butaud.play()


# Cat screen ends---------------------------------------------------------------

class EndSc(Screen):
    # def anim(self, instance):
    #     self.instance.size = (0,0)
    #     animation = Animation(size=(50, 50), t='out_bounce')
    #     animation.start(self.instance.size)
    pass


# classes end ------------------------------------------------------------------


root_widget = Builder.load_string('''
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
Home:
    transition: FadeTransition()
    transition: SlideTransition()
    StSc:
    FirstSc:
    SecSc:
    ThirdSc:
    Category:
    EndSc:
<ImButb@Button>
    id: imbutb
    font_size: 0.65 * self.height
    background_normal: ''
    background_color: (0,0,0,0)
    back_color: (1,0,1,1)
    size_hint: (.15,.1)
    canvas.before:
        Color:
            rgba: self.back_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: (18,18)
<StSc>:
    name: 'st'
    FloatLayout:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'
        Image:
            id: imid
            source:"stbg.png"
            allow_stretch: True
            keep_ratio: False
<FirstSc>:
    name: '1st'
    FloatLayout:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'firstframe.png'
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'firstframe_low.png'
        ImBut:
            id: aa
            pos_hint: {"x":.79,"top":.125}
            source: 'musicon.png'
            size_hint: .15,.08
            on_press: 
                root.soundplay()           
            on_release:
                root.audio()
        ImBut:
            id: ab
            pos_hint: {"x":.06,"top":.125}
            source: 'categ.png'
            size_hint: .15,.08
            on_press: 
                root.soundplay()           
            on_release: 
                app.root.current = 'category'
                root.manager.transition.direction = 'right'
        ImBut:
            id: ac
            text: ''
            pos_hint: {"x":.25,"top":.58}
            source: 'startplay.png'
            size_hint: .5,.28       
            on_press: 
                root.soundplay()
                root.on_presStart()
            on_release:
                root.on_relStart() 
                app.root.current = '2nd'
                root.manager.transition.direction = 'left'
        ImBut:
            id: acon
            pos_hint: {'center_x': .5, 'center_y': .22}
            source: 'continue.png'
            size_hint: .5,.08      
            on_press: 
                root.soundplay()
                root.on_presConStart()
            on_release:
                root.on_relConStart()
                root.manager.transition.direction = 'left'
<SecSc>:
    name: '2nd'
    FloatLayout:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'imgfrm.png'
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'splfrm.png'
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'forback.png'
        Image:
            id: imid
            source:""
            allow_stretch: True
            keep_ratio: False
        ImBut:
            id: mon
            pos_hint: {"x":.82,"top":.08}
            source: ''
            size_hint: .13,.07
            on_press: root.butaudi()           
            on_release: root.butloop()
        ImBut:
            id: back
            pos_hint: {"x":.05,"top":.08}
            source: 'back.png'
            size_hint: .128,.07
            on_press: root.butaudi()        
            on_release: 
                app.root.current = '1st'
                root.manager.transition.direction = 'right'
        Label:
            id: spltxt
            text: ''
            font_size: root.width / 10
            pos_hint:{"y": -.093} 
        FloatLayout:
            id: grid
            cols:5
            size_hint: (1.06,1.06)
        Image:
            id: corr_ans
            size_hint:(None,None)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size: 0,0
            source:"welldone.png"
        Image:
            id: wrbg
            opacity:0
            source:"wrongbg.png"
        Image:
            id: wr_ans
            size_hint:(None,None)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size: 0,0
            source:"wrans.png"
    

<ThirdSc>:
    name: '3rd'
    FloatLayout:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'imgfrm.png'
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'splfrm.png'
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'forback.png'
        Image:
            id: imid
            source:""
            allow_stretch: True
            keep_ratio: False
        ImBut:
            id: mon
            pos_hint: {"x":.82,"top":.08}
            source: 'musicon.png'
            size_hint: .13,.07
            on_press: root.butaudi()           
            on_release: root.butloop()
        ImBut:
            id: back
            pos_hint: {"x":.05,"top":.08}
            source: 'back.png'
            size_hint: .128,.07
            on_press: root.butaudi()           
            on_release: 
                app.root.current = '1st'
                root.manager.transition.direction = 'right'
        Label:
            id: spltxt
            text: ''
            font_size: root.width / 10
            pos_hint:{"y": -.093} 
        FloatLayout:
            id: grid
            cols:5
            size_hint: (1.06,1.06)
        Image:
            id: corr_ans
            size_hint:(None,None)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size: 0,0
            source:"welldone.png"
        Image:
            id: wrbg
            opacity:0
            source:"wrongbg.png"
        Image:
            id: wr_ans
            size_hint:(None,None)
            pos_hint: {'center_x': .5, 'center_y': .5}
            size: 0,0
            source:"wrans.png"

<Category>:
    name: 'category'
    FloatLayout:
        orientation: 'vertical'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'
        ImBut:
            id: cata
            source: 'catsscreen_Ani.png'
            size_hint:(.9,.11)
            pos_hint: {'center_x': .5, 'center_y': .65} 
            on_press: 
                root.butaudi()
                root.onpressani()        
            on_release:
                root.gotoaniFpage()
                app.root.current = '1st'
                root.manager.transition.direction = 'left'
        ImBut:
            id: catb
            source: 'catsscreen_Fru.png'
            size_hint:(.9,.11)
            pos_hint: {'center_x': .5, 'center_y': .5} 
            on_press: 
                root.butaudi()
                root.onpressfru()        
            on_release:
                root.gotoFruFpage()
                app.root.current = '1st'
                root.manager.transition.direction = 'left'
        ImBut:
            id: catc
            source: 'catsscreen_Veg.png'
            size_hint:(.9,.11)
            pos_hint: {'center_x': .5, 'center_y': .35} 
            on_press: 
                root.butaudi()
                root.onpressveg()        
            on_release:
                root.gotoVegFpage()
                app.root.current = '1st'
                root.manager.transition.direction = 'left'
<EndSc>:
    name: 'end'
    FloatLayout:
        orientation: 'vertical'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg.png'
        Image:
            id: hur
            source: 'hurrah.png'
            pos_hint: {'center_x': .5, 'center_y': .5}
''')


class MyiApp(App):
    def build(self):
        return root_widget


MyiApp().run()
