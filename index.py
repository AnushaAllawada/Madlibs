from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager,Screen,NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Rectangle,Color
from kivy.core.window import Window
import random
#Window.size=(360,800)
class Pop_up(Popup):
    background_normal=''
    background_color=1,0.65, 1, 1   
class Pop_up_retry(Popup):
    background_normal=''
    background_color=1,0.65, 1, 1   
class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition=NoTransition()
    def genre(self):
        self.current="page2"
    def switching_back(self):
        self.current="page1"
    def input_page_adven(self):
         self.current="page3"
    def input_page_fairy(self):
         self.current="page4"
    def input_page_crime(self):
         self.current="page5"
    def input_page_fantacy(self):
         self.current="page6"
    def input_page_detective(self):
         self.current="page7"
    def input_page_comedy(self):
        self.current="page8"
    def back_to_genre(self):
        self.current="page2"
    def show(self):
        Pop_up().open()
    def show1(self):
        Pop_up_retry().open()
    def adventure(self):
        i=random.randint(1,5)
        if(i==1):
            self.ids.label1.text=f"Once upon a time, in a {self.ids.t1.text} land, there was a {self.ids.t2.text} who\n dreamed of finding the lost {self.ids.t3.text}. One day, they {self.ids.t4.text} into \nthe {self.ids.t5.text} forest.They encountered a {self.ids.t6.text} who gave them a\n {self.ids.t7.text} map. After days of  {self.ids.t8.text}, they finally found th\ntreasure hidden under a {self.ids.t9.text} tree. The {self.ids.t10.text} opened the\n treasure chest and found {self.ids.t11.text} {self.ids.t12.text} inside.Their adventure\n was {self.ids.t13.text}."
        if(i==2):
            self.ids.label1.text=f"In a {self.ids.t1.text} village, a young {self.ids.t2.text} discovered an old \n{self.ids.t3.text} that led to a secret cave. Armed with a {self.ids.t5.text} lantern, \nthey {self.ids.t4.text} into the darkness. Inside, they found a {self.ids.t6.text} \nguarding a {self.ids.t7.text} door. After solving a {self.ids.t10.text}, the door \nopened, revealing {self.ids.t11.text} {self.ids.t12.text}. The {self.ids.t10.text} \nbecame a hero and their discovery was {self.ids.t13.text}."
        if(i==3):
            self.ids.label1.text=f"A {self.ids.t1.text}  {self.ids.t2.text}  set sail to find a mysterious island. After\ndays of {self.ids.t8.text}  , they arrived at a {self.ids.t5.text}   shore. There, they \nmet a {self.ids.t3.text}   who told them about a {self.ids.t7.text}   treasure. They \n{self.ids.t4.text}   through the jungle and found a {self.ids.t6.text}   hidden in a\n cave. Inside, there were {self.ids.t11.text}   {self.ids.t12.text}  . The \n{self.ids.t10.text}   returned home, their adventure {self.ids.t13.text}."
        if(i==4):
            self.ids.label1.text=f"A {self.ids.t1.text} {self.ids.t2.text} ventured into an enchanted forest in search of a \n{self.ids.t3.text}. They {self.ids.t4.text} through {self.ids.t5.text} trees and \ndiscovered a {self.ids.t6.text} with {self.ids.t7.text} powers. After a long \n{self.ids.t8.text}, they found the {self.ids.t10.text} at the heart of the forest. It \nwas surrounded by {self.ids.t11.text} {self.ids.t12.text}. The {self.ids.t6.text} took \nthe {self.ids.t10.text} and felt {self.ids.t9.text}."
        if(i==5):
            self.ids.label1.text=f"A {self.ids.t1.text} {self.ids.t2.text} invented a time machine to visit the \n{self.ids.t3.text} era. They {self.ids.t4.text} into the past and found themselves in a \n{self.ids.t5.text} kingdom. There, they met a {self.ids.t6.text} who showed them a \n{self.ids.t7.text} artifact. After {self.ids.t8.text} through history, they returned to \ntheir time with {self.ids.t11.text} {self.ids.t12.text}. The {self.ids.t10.text} shared \ntheir story and it became {self.ids.t13.text}."
    def fairytale(self):
        i=random.randint(1,5)
        if(i==1):
            self.ids.label2.text=f" In a small {self.ids.f1.text}, a young girl {self.ids.f2.text} a {self.ids.f3.text}\n {self.ids.f4.text}.The girl often wandered into the nearby {self.ids.f5.text}. One day, she {self.ids.f6.text} deep\n into the{self.ids.f7.text} woods. There, she {self.ids.f9.text} a {self.ids.f8.text} in an old\n {self.ids.f10.text}.The book contained {self.ids.f11.text} spellsfor good deeds. The girl {self.ids.f12.text} the\n spells to help her{self.ids.f1.text}. Everyone in the {self.ids.f1.text} lived happily ever after."
        if(i==2):
            self.ids.label2.text=f" In a quaint {self.ids.f1.text}, a brave boy {self.ids.f2.text} a {self.ids.f3.text}\n {self.ids.f4.text}.She told him tales of a {self.ids.f5.text} filled with wonders. Curious, he {self.ids.f6.text}\n to the{self.ids.f7.text} place. He {self.ids.f9.text} a {self.ids.f8.text} hidden in an ancient\n {self.ids.f10.text}.The book held {self.ids.f11.text} secrets of the forest. The boy {self.ids.f12.text} the\nknowledge toprotect the {self.ids.f1.text}. His bravery was celebrated in the {self.ids.f1.text}."
        if(i==3):
            self.ids.label2.text=f" In a peaceful {self.ids.f1.text}, a kind woman {self.ids.f2.text} a {self.ids.f3.text}\n{self.ids.f4.text}.She heard about a {self.ids.f5.text} where dreams came true. She {self.ids.f6.text} into the\n {self.ids.f7.text} woods one day. There, she {self.ids.f9.text} a {self.ids.f8.text} inside a \nquaint {self.ids.f10.text}. The book revealed {self.ids.f11.text} treasures and spells. She \n{self.ids.f12.text} them to bring joy to her {self.ids.f1.text}. The{self.ids.f1.text}\n prospered under her care."
        if(i==4):
            self.ids.label2.text=f" In a distant {self.ids.f1.text}, a young prince {self.ids.f2.text} a {self.ids.f3.text}\n {self.ids.f4.text}. The prince loved exploring the {self.ids.f5.text} near his home. One day, he\n {self.ids.f6.text} to a{self.ids.f7.text} part of the woods. He {self.ids.f9.text} a \n{self.ids.f8.text} inside an old {self.ids.f10.text}.The book contained\n {self.ids.f11.text} spells for bravery. He {self.ids.f12.text} the spells to protect his\n {self.ids.f1.text}. The {self.ids.f1.text} thrived thanks to his courage."
        if(i==5):
            self.ids.label2.text=f" In a charming {self.ids.f1.text}, a curious girl {self.ids.f2.text} a {self.ids.f3.text}\n {self.ids.f4.text}. The witch spoke of a{self.ids.f5.text} full of secrets. Intrigued, she \n{self.ids.f6.text} to the {self.ids.f7.text} woods. She {self.ids.f9.text} a {self.ids.f8.text}\n in an abandoned {self.ids.f10.text}. The book held\n {self.ids.f11.text} spells of\n enchantment. The girl {self.ids.f12.text} the spells to enchant her {self.ids.f1.text}. The\n {self.ids.f1.text} became a place of wonder and magic."
    def crime(self):
        i=random.randint(1,5)
        if(i==1):
            self.ids.label3.text=f"In a bustling {self.ids.c1.text}, a rookie officer {self.ids.c2.text} a {self.ids.c3.text}\n{self.ids.c4.text}.They were assigned a {self.ids.c5.text} involving a missing person. They {self.ids.c6.text}\nthrough the {self.ids.c7.text} alleys in search of leads. There, they {self.ids.c9.text} a\n critical {self.ids.c8.text} near an abandoned {self.ids.c10.text}. The clue led them to\n a{self.ids.c11.text} room where the victim was kept. Together, they {self.ids.c12.text} the case \n and saved the day.The {self.ids.c1.text} celebrated their success."
        if(i==2):
            self.ids.label3.text=f"In a large {self.ids.c1.text}, a bank manager {self.ids.c2.text} a {self.ids.c3.text}\n {self.ids.c4.text}.They were investigating a high-profile {self.ids.c5.text} of robbery. They\n {self.ids.c6.text} to the {self.ids.c7.text} underworld to gather information. There,\n they {self.ids.c9.text} a vital {self.ids.c8.text} in the robber's {self.ids.c10.text}. The clue\n led them to the {self.ids.c11.text} stash of stolen money. The detective\n {self.ids.c12.text} the case and returned the money.\n"
        if(i==3):
            self.ids.label3.text=f"In a bustling {self.ids.c1.text}, a jeweler {self.ids.c2.text} a {self.ids.c3.text}\n {self.ids.c4.text}.A valuable necklace had been taken, launching a major {self.ids.c5.text}.\n They {self.ids.c6.text} through the {self.ids.c7.text} network of black-market\n dealers. There, they {self.ids.c9.text} an essential {self.ids.c8.text} in a shady\n dealer's {self.ids.c10.text}. The clue pointed to the necklace's {self.ids.c11.text}\n location. The detective {self.ids.c12.text} the mystery and recovered\n the jewels. The {self.ids.c1.text} celebrated their recovery.\nhe {self.ids.c1.text} praised their bravery."
        if(i==4):
            self.ids.label3.text=f"In a quiet {self.ids.c1.text}, an art dealer {self.ids.c2.text} a {self.ids.c3.text}\n {self.ids.c4.text}. Apriceless painting had been stolen, sparking a major {self.ids.c5.text}. They\n {self.ids.c6.text} to the {self.ids.c7.text} corners of the art world. There, they\n {self.ids.c9.text} a significant {self.ids.c8.text} hidden in a notorious thief's\n {self.ids.c10.text}. The clue revealed the painting's {self.ids.c11.text} location.\n The detective {self.ids.c12.text} the mystery and retrieved the artwork.\n The {self.ids.c1.text} was relieved and grateful."
        if(i==5):
            self.ids.label3.text=f"In a busy {self.ids.c1.text}, a concerned parent {self.ids.c2.text} a {self.ids.c3.text}\n {self.ids.c4.text}.Their child had gone missing, creating a high-stakes {self.ids.c5.text}. They\n{self.ids.c6.text} through the {self.ids.c7.text} parts of the {self.ids.c1.text}. There, they\n {self.ids.c9.text}a telling {self.ids.c8.text} in the kidnapper's {self.ids.c10.text}. The clue uncovered the\nchild's {self.ids.c11.text} location. The detective {self.ids.c12.text} the case and\nrescued the child. The {self.ids.c1.text} rejoiced at the happy reunion."
    def horror(self):
        i=random.randint(1,5)
        if(i==1):
            self.ids.label5.text=f" Once upon a time, in a dark {self.ids.d1.text}, there was a {self.ids.d2.text} who dreamed of\n finding the lost {self.ids.d3.text}. One day, they {self.ids.d4.text} into the enchanted\n{self.ids.d5.text}. They {self.ids.d8.text} a {self.ids.d6.text} {self.ids.d7.text} that led them to a {self.ids.d9.text}\n cave. In thecave, they found the {self.ids.d9.text} {self.ids.d10.text}. Their discovery was\n {self.ids.d11.text}, andthey never returned."
        if(i==2):
            self.ids.label5.text=f" Once upon a time, in a foggy {self.ids.d1.text}, there was a {self.ids.d2.text} who dreamed of\n findingthe lost {self.ids.d3.text}. One day, they {self.ids.d4.text} into the abandoned\n {self.ids.d1.tex5}. They{self.ids.d8.text} a mysterious {self.ids.d7.text} that led them to a {self.ids.d9.text} attic.\nIn the attic, theyfound the {self.ids.d9.text} {self.ids.t10.text}. Their joy was {self.ids.d11.text}, as they\n reunited with their toy."
        if(i==3):
            self.ids.label5.text=f" Once upon a time, in a stormy {self.ids.d1.text}, there was a sailor who {self.ids.d4.text} of\n findingthe lost {self.ids.d2.text}. One day, they {self.ids.d8.text} into the foggy {self.ids.d5.text}.\n They {self.ids.d12.text} a {self.ids.d6.text} map that led them to a {self.ids.d9.text} island.\nOn the island, they foundthe {self.ids.d9.text}{self.ids.d9.text}. Their adventure was {self.ids.d11.text}, and they\n sailed home safely."
        if(i==4):
            self.ids.label5.text=f" Once upon a time, in a haunted {self.ids.f1.text}, there was a villager who dreamed of\n finding the cursed {self.ids.f2.text}. One day, they {self.ids.f4.text} into the deserted\n {self.ids.f5.text}. They {self.ids.t8.text} a {self.ids.f6.text} {self.ids.f3.text} that led them to a\n {self.ids.f9.text} well. In the well, they found the {self.ids.f9.text} {self.ids.f10.text}. Their curse was\n {self.ids.f11.text}, and they could never leave."
        if(i==5):
            self.ids.label5.text=f" Once upon a time, in a quiet {self.ids.d1.text}, there was a {self.ids.d2.text} who dreamed of\n finding the lost {self.ids.d3.text}. One day, they {self.ids.d4.text} into the\n{self.ids.d6.text} {self.ids.d5.text}. They {self.ids.d8.text} a mysterious {self.ids.d7.text} that led them to a {self.ids.d9.text}\n room.In the room, they found the {self.ids.d9.text} {self.ids.d10.text}. Their knowledge was\n {self.ids.d11.text},and they became a famous scholar."
    def fantacy(self):
        i=random.randint(1,5)
        if(i==1):
            self.ids.label4.text=f"Once upon a time, in a {self.ids.fy1.text}, a princess {self.ids.fy2.text} a {self.ids.fy3.text}\n {self.ids.fy4.text}.One day, she {self.ids.fy6.text} into the {self.ids.fy7.text} {self.ids.fy5.text}. She\n {self.ids.fy9.text}a mystical {self.ids.fy8.text}. Following it, she uncovered a {self.ids.fy11.text}\n {self.ids.fy10.text}.Inside, she found the golden {self.ids.fy4.text} and {self.ids.fy12.text} immense power. Her\n kingdom prospered with the flower's magic. The people celebrated her bravery."
        if(i==2):
            self.ids.label4.text=f"In a distant {self.ids.fy1.text}, a brave knight {self.ids.fy2.text} a {self.ids.fy3.text}\n {self.ids.fy4.text}.Armed with courage, he {self.ids.fy6.text} into the fiery {self.ids.fy5.text}. He\n {self.ids.fy9.text} a {self.ids.fy8.text}. Using it, he {self.ids.fy12.text} a {self.ids.fy11.text}\n {self.ids.fy10.text}. Inside,he found the {self.ids.fy7.text} treasure and became a hero. The dragon's hoard brought peace\n and wealth to his {self.ids.fy1.text}. Songs were sung of his deeds."
        if(i==3):
            self.ids.label4.text=f"Far away in an {self.ids.fy1.text}, a young explorer {self.ids.fy2.text} a {self.ids.fy3.text}\n{self.ids.fy4.text}. With determination, she {self.ids.fy6.text} to the {self.ids.fy7.text} shore.\n She {self.ids.fy9.text} an ancient {self.ids.fy8.text}. Following it, she uncovered a\n {self.ids.fy11.text} {self.ids.fy10.text}. Inside, she found a sacred {self.ids.fy5.text} and\n {self.ids.fy12.text}great wisdom. Her discovery changed history forever. Her name was\n remembered in legends."
        if(i==4):
            self.ids.label4.text=f"Deep in a {self.ids.fy1.text}, a curious elf {self.ids.fy2.text} a {self.ids.fy3.text}\n {self.ids.fy4.text}.One day, he {self.ids.fy6.text} into the dense {self.ids.fy5.text}. He {self.ids.fy9.text} an\nold map.Following it, he discovered a {self.ids.fy11.text} {self.ids.fy10.text}. There, he met the\n {self.ids.fy7.text}\{self.ids.fy8.text} and {self.ids.fy12.text} its friendship. Together, they protected the\n {self.ids.fy1.text} for generations. The {self.ids.fy1.text} thrived under their care."
        if(i==5):
            self.ids.label4.text=f" In a mystical {self.ids.fy1.text}, a wise wizard {self.ids.fy2.text} for a {self.ids.fy3.text}\n {self.ids.fy4.text}. With spells, he {self.ids.fy6.text} to the ancient {self.ids.fy5.text}. He\n {self.ids.fy9.text} a magical {self.ids.fy8.text}. Using it, he a {self.ids.fy11.text}\n {self.ids.fy10.text}.Inside, he found the {self.ids.fy7.text} {self.ids.fy4.text} and\n {self.ids.fy12.text}\nits magic. The wizard's newfound power brought balance to the {self.ids.fy1.text}.\n The {self.ids.fy1.text} flourished under his guidance."
    def comedy(self):
        i=random.randint(1,5)
        if(i==1):
            self.ids.label6.text=f" The  {self.ids.C1.text} restaurant experience turned into a disaster when the waiter \naccidentally {self.ids.C2.text}our orders with a ({self.ids.C3.text}twist. They brought out \n{self.ids.C4.text} {self.ids.C5.text}, and we couldn't help but laugh. The chef \n{self.ids.C6.text} the main course and it ended up a  {self.ids.C7.text}[color] \n{self.ids.C8.text} dream. Despite this, we managed to eat {self.ids.C9.text} servings of the\n {self.ids.C10.text} dessert shaped like  {self.ids.C11.text} . In the chaos, we saw the manager\n  {self.ids.C12.text} ending  around the {self.ids.C13.text} trying to fix everything. Our bill \nincluded a charge for {self.ids.C14.text} that tasted {self.ids.C15.text}but we decided to \n {self.ids.C16.text} and exclaimed,  {self.ids.C18.text}."
        if(i==2):
            self.ids.label6.text=f" At the {self.ids.C1.text} the boss suddenly decided to {self.ids.C2.text} while wearing a \n{self.ids.C3.text} hat. This caused all the {self.ids.C4.text} stare{self.ids.C5.text} and\n whisper to each other. The intern accidentally {self.ids.C6.text} into the boss's office with a\n {self.ids.C7.text}  {self.ids.C8.text} They were asked to fetch {self.ids.C9.text} \n{self.ids.C10.text} pens from the supply closet, but ended up tripping over their own \n {self.ids.C11.text} while {self.ids.C12.text}. Chaos ensued, and everyone ended up in the \n {self.ids.C13.text} for an emergency meeting about the missing {self.ids.C14.text}. After a \n{self.ids.C15.text}  discussion, they decided to {self.ids.C16.text} and shout '{self.ids.C17.text}'."
        if(i==3):
            self.ids.label6.text=f" The {self.ids.C1.text} family reunion turned into a wild event when Uncle Ted tried to \n({self.ids.C2.text} on the dance floor with his {self.ids.C3.text} moves. Aunt Martha brought \nher famous {self.ids.C4.text} and insisted on serving them {self.ids.C5.text}. Cousin Billy\n {self.ids.C6.text} the family pet with a {self.ids.C7.text}  {self.ids.C8.text} costume, causing\n everyone to laugh for {self.ids.C9.text} minutes straight. Grandma surprised everyone by \nshowing off her {self.ids.C10.text} collection of {self.ids.C11.text} while the kids were busy\n {self.ids.C12.text} around the {self.ids.C13.text}. The highlight was when Uncle Ted \naccidentally sat on the {self.ids.C14.text}, prompting a {self.ids. C15.text} reaction from \neveryone. They all decided to {self.ids.C16.text} together and exclaimed, '{self.ids.C17.text}'!."
        if(i==4):
            self.ids.label6.text=f" The {self.ids.C1.text} vacation started off with a bang when Dad decided to {self.ids.C2.text}\n his snorkeling gear with a {self.ids.C3.text} twist. We packed our {self.ids.C4.text}  \n{self.ids.C5.text} but they got mixed up with Mom's {self.ids.C6.text}suitcase. At the beach, \nwe saw a {self.ids.C7.text}  {self.ids.C8.text}  digging for {self.ids.C9.text} buried \ntreasures. The hotel room had a {self.ids.C10.text} view of the {self.ids.C11.text}, and we\n spent our days {self.ids.C12.text} by the pool. One evening, we ventured to a local \n{self.ids.C13.text} and stumbled upon a {self.ids.C14.text} that looked {self.ids.C15.text}. We\n couldn't resist {self.ids.C16.text}, present tense] and ended the night with a loud '{self.ids.C17.text}'."
        if(i==5):
            self.ids.label6.text=f" The {self.ids.C1.text} birthday party became unforgettable when Grandma decided to\n {self.ids.C2.text} on the trampoline with her {self.ids.C3.text}moves. The cake was decorated \nwith {self.ids.C4.text} {self.ids.C5.text}, and Uncle Bob accidentally {self.ids.C6.text} the\n piñata into the neighbor's yard. Little Timmy found a {self.ids.C7.text} {self.ids.C8.text} \nhiding under the table and chased it for {self.ids.C9.text} minutes. We played \n{self.ids.C10.text} games involving {self.ids.C11.text}, and Mom was caught {self.ids.C12.text}\n in the bounce house. Later, we gathered in the backyard {self.ids.C13.text}\n to open presents, and Aunt Sally brought a {self.ids.C14.text} that looked\n {self.ids.C15.text}. We all couldn't help but {self.ids.C16.text}and shouted, '{self.ids.C17.text}'."
        
class madlib(App):
    def Exit(self):
        App.get_running_app().stop() 
        Window.close()
    def build(self):
        self.icon = 'start.png'
    def restart(self):
        self.root.clear_widgets()
        self.stop()
        return madlib().run()
madlib().run()
