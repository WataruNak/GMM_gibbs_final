from otree.api import *
import random
from sklearn.metrics import cohen_kappa_score, adjusted_rand_score
import itertools

doc = """
https://qiita.com/naoki-funawatari/items/c78630b85f5f7fe21d19 drag_and_drop
https://www.otreehub.com/projects/otree-snippets/ otree sortable_example
https://qiita.com/AVELWP/items/536c797a63c081cf7bc0 sortable document ja
https://github.com/SortableJS/Sortable sortable git
https://qiita.com/t-iguchi/items/20dc31d5e004d7145634 js in django
"""

def make_correct_list(label_num, item_num, correct_cat_num):
    numlists = []
    correct_lists = []
    for ln in range(label_num):
        numlist = [ln] * item_num
        numlists.append(numlist)
    for nl in itertools.permutations(numlists, correct_cat_num):
        correctlist = list(itertools.chain.from_iterable(nl))
        correct_lists.append(correctlist)
    return correct_lists

def make_draggableimg_html_list(img_num, path_list, height, width):
    img_html_list = []
    for da in range(img_num):
        img_html_list.append(
            "<img src = \"{}\" class=\"item\" draggable=\"true\" id=\"{}\" height=\"{}px\" width=\"{}px\"/>".format(path_list[da], da, height, width)
        )
    return img_html_list

def make_draggablename_html_list(name_num, path_list, height, width):
    img_html_list = []
    for db in range(name_num):
        img_html_list.append(
            "<li draggable=\"true\" id=\"name{}\" data-id=\"sym{}\"><img src=\"{}\" height=\"{}px\" width=\"{}px\"></li>".format(
                db, db, path_list[db], height, width)
        )
    return img_html_list


class Constants(BaseConstants):
    name_in_url = 'categorization'
    players_per_group = 2
    num_rounds = 1
    imgpath_list = [
        "https://imgur.com/wqnOMfy.jpg","https://imgur.com/LHJYfxo.jpg","https://imgur.com/9Xa4VnX.jpg","https://imgur.com/D91W1KT.jpg",
        "https://imgur.com/J35mb8e.jpg","https://imgur.com/IC9TPNn.jpg","https://imgur.com/cJQIb6k.jpg","https://imgur.com/2rj1L4f.jpg",
        "https://imgur.com/CeGed6S.jpg","https://imgur.com/u28iEnb.jpg","https://imgur.com/N1rDlYe.jpg","https://imgur.com/4uFfzbw.jpg",
        "https://imgur.com/ATEBW84.jpg","https://imgur.com/OUEAyTS.jpg","https://imgur.com/oLE2TWf.jpg","https://imgur.com/xiGpQvF.jpg",
        "https://imgur.com/NnOAzoD.jpg","https://imgur.com/0wGJ58N.jpg","https://imgur.com/nitf5Sq.jpg","https://imgur.com/dwXrpvH.jpg",
        "https://imgur.com/K8sGXHa.jpg","https://imgur.com/XejnHhh.jpg","https://imgur.com/yFw1I6M.jpg","https://imgur.com/iuGyxnS.jpg",
        "https://imgur.com/zysvnS8.jpg","https://imgur.com/jv5EHuP.jpg","https://imgur.com/fqjlV3Y.jpg","https://imgur.com/2NYuf1e.jpg",
        "https://imgur.com/jy5MPbW.jpg","https://imgur.com/7Rf9TKU.jpg","https://imgur.com/BgSfDLZ.jpg","https://imgur.com/3sfX7Mr.jpg",
        "https://imgur.com/6R8GCoP.jpg","https://imgur.com/A5ju4zJ.jpg","https://imgur.com/QF9ee5p.jpg","https://imgur.com/vW5QaBq.jpg",
        "https://imgur.com/NcY47LO.jpg","https://imgur.com/GDI9kz8.jpg","https://imgur.com/OmiMBXk.jpg","https://imgur.com/in0lSLH.jpg",
    ]

    namepath_list = [
        "https://imgur.com/a1HYfcA.png","https://imgur.com/xMBZ0Dg.png","https://imgur.com/Xh5Scyo.png",
        "https://imgur.com/PBZ3YNV.png","https://imgur.com/dmiNF4h.png","https://imgur.com/RdWIiGo.png",
        ]
    
    imghtml_list = make_draggableimg_html_list(40, imgpath_list, 50, 50)
    namehtml_list = make_draggablename_html_list(6, namepath_list, 100, 100)
    
    correct_cat_list = make_correct_list(6, 10, 4)
    goal_ari = 0.9
    


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    name_order = models.StringField(initial="sym0,sym1,sym2,sym3,sym4,sym5")
    img0_cat = models.StringField(initial="99")
    img1_cat = models.StringField(initial="99")
    img2_cat = models.StringField(initial="99")
    img3_cat = models.StringField(initial="99")
    img4_cat = models.StringField(initial="99")
    img5_cat = models.StringField(initial="99")
    img6_cat = models.StringField(initial="99")
    img7_cat = models.StringField(initial="99")
    img8_cat = models.StringField(initial="99")
    img9_cat = models.StringField(initial="99")
    img10_cat = models.StringField(initial="99")
    img11_cat = models.StringField(initial="99")
    img12_cat = models.StringField(initial="99")
    img13_cat = models.StringField(initial="99")
    img14_cat = models.StringField(initial="99")
    img15_cat = models.StringField(initial="99")
    img16_cat = models.StringField(initial="99")
    img17_cat = models.StringField(initial="99")
    img18_cat = models.StringField(initial="99")
    img19_cat = models.StringField(initial="99")
    img20_cat = models.StringField(initial="99")
    img21_cat = models.StringField(initial="99")
    img22_cat = models.StringField(initial="99")
    img23_cat = models.StringField(initial="99")
    img24_cat = models.StringField(initial="99")
    img25_cat = models.StringField(initial="99")
    img26_cat = models.StringField(initial="99")
    img27_cat = models.StringField(initial="99")
    img28_cat = models.StringField(initial="99")
    img29_cat = models.StringField(initial="99")
    img30_cat = models.StringField(initial="99")
    img31_cat = models.StringField(initial="99")
    img32_cat = models.StringField(initial="99")
    img33_cat = models.StringField(initial="99")
    img34_cat = models.StringField(initial="99")
    img35_cat = models.StringField(initial="99")
    img36_cat = models.StringField(initial="99")
    img37_cat = models.StringField(initial="99")
    img38_cat = models.StringField(initial="99")
    img39_cat = models.StringField(initial="99")

    box0_children = models.StringField(default="999")
    box1_children = models.StringField(default="999")
    box2_children = models.StringField(default="999")
    box3_children = models.StringField(default="999")
    box4_children = models.StringField(default="999")
    box5_children = models.StringField(default="999")

    kappa = models.FloatField()
    ari = models.FloatField()


def custom_export(players):
    yield [
        "session",
        "participant_code",
        "id_in_group", "kappa", "ari",
        "img0_cat", "img1_cat", "img2_cat", "img3_cat", "img4_cat",
        "img5_cat", "img6_cat", "img7_cat", "img8_cat", "img9_cat",
        "img10_cat", "img11_cat", "img12_cat", "img13_cat", "img14_cat",
        "img15_cat", "img16_cat", "img17_cat", "img18_cat", "img19_cat",
        "img20_cat", "img21_cat", "img22_cat", "img23_cat", "img24_cat",
        "img25_cat", "img26_cat", "img27_cat", "img28_cat", "img29_cat",
        "img30_cat", "img31_cat", "img32_cat", "img33_cat", "img34_cat",
        "img35_cat", "img36_cat", "img37_cat", "img38_cat", "img39_cat",
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code,
            p.id_in_group, p.kappa, p.ari,
            p.img0_cat, p.img1_cat, p.img2_cat, p.img3_cat, p.img4_cat,
            p.img5_cat, p.img6_cat, p.img7_cat, p.img8_cat, p.img9_cat,
            p.img10_cat, p.img11_cat, p.img12_cat, p.img13_cat, p.img14_cat,
            p.img15_cat, p.img16_cat, p.img17_cat, p.img18_cat, p.img19_cat,
            p.img20_cat, p.img21_cat, p.img22_cat, p.img23_cat, p.img24_cat,
            p.img25_cat, p.img26_cat, p.img27_cat, p.img28_cat, p.img29_cat,
            p.img30_cat, p.img31_cat, p.img32_cat, p.img33_cat, p.img34_cat,
            p.img35_cat, p.img36_cat, p.img37_cat, p.img38_cat, p.img39_cat,
            ]

# PAGES
class Introduction(Page):
    pass

class Instruction(Page):
    pass

class Categorize(Page):
    timeout_seconds = 600
    form_model = 'player'
    form_fields = [
        "name_order", 
        "box0_children", "box1_children", "box2_children",
        "box3_children", "box4_children", "box5_children",
        "img0_cat", "img1_cat", "img2_cat", "img3_cat", "img4_cat",
        "img5_cat", "img6_cat", "img7_cat", "img8_cat", "img9_cat",
        "img10_cat", "img11_cat", "img12_cat", "img13_cat", "img14_cat",
        "img15_cat", "img16_cat", "img17_cat", "img18_cat", "img19_cat",
        "img20_cat", "img21_cat", "img22_cat", "img23_cat", "img24_cat",
        "img25_cat", "img26_cat", "img27_cat", "img28_cat", "img29_cat",
        "img30_cat", "img31_cat", "img32_cat", "img33_cat", "img34_cat",
        "img35_cat", "img36_cat", "img37_cat", "img38_cat", "img39_cat",
    ]

    @staticmethod
    def vars_for_template(player: Player):
        player.participant.stimuli_id_list = []
        player.participant.imghtml_order = []
        for n in range(40):
            player.participant.stimuli_id_list.append(n)
        random.shuffle(player.participant.stimuli_id_list)
        for j in range(40):
            player.participant.imghtml_order.append(Constants.imghtml_list[player.participant.stimuli_id_list[j]])
        return {
            "name_order" : player.name_order,
            "imghtml_order" : player.participant.imghtml_order,
            "namehtml_list" : Constants.namehtml_list,
        }
    
    @staticmethod
    def js_vars(player):
        return dict(
            id_order=player.participant.stimuli_id_list,
            name_order=player.name_order,
        )

    @staticmethod
    def before_next_page(player, timeout_happened):
        cat_list = [
            player.img0_cat, player.img1_cat, player.img2_cat, player.img3_cat, player.img4_cat,
            player.img5_cat, player.img6_cat, player.img7_cat, player.img8_cat, player.img9_cat,
            player.img10_cat, player.img11_cat, player.img12_cat, player.img13_cat, player.img14_cat,
            player.img15_cat, player.img16_cat, player.img17_cat, player.img18_cat, player.img19_cat,
            player.img20_cat, player.img21_cat, player.img22_cat, player.img23_cat, player.img24_cat,
            player.img25_cat, player.img26_cat, player.img27_cat, player.img28_cat, player.img29_cat,
            player.img30_cat, player.img31_cat, player.img32_cat, player.img33_cat, player.img34_cat,
            player.img35_cat, player.img36_cat, player.img37_cat, player.img38_cat, player.img39_cat,
        ]

        if timeout_happened:
            for pc in cat_list:
                if pc == "99":
                    pc = str(random.randint(0, 5))
            player.participant.box0_items = []
            player.participant.box1_items = []
            player.participant.box2_items = []
            player.participant.box3_items = []
            player.participant.box4_items = []
            player.participant.box5_items = []
            for pc2 in cat_list:
                if pc2 == "0":
                    player.participant.box0_items.append(int(pc2))
                if pc2 == "1":
                    player.participant.box1_items.append(int(pc2))
                if pc2 == "2":
                    player.participant.box2_items.append(int(pc2))
                if pc2 == "3":
                    player.participant.box3_items.append(int(pc2))
                if pc2 == "4":
                    player.participant.box4_items.append(int(pc2))
                if pc2 == "5":
                    player.participant.box5_items.append(int(pc2))
            
            if player.participant.box0_items == []:
                player.participant.box0_items = [999,]
            if player.participant.box1_items == []:
                player.participant.box1_items = [999,]
            if player.participant.box2_items == []:
                player.participant.box2_items = [999,]
            if player.participant.box3_items == []:
                player.participant.box3_items = [999,]
            if player.participant.box4_items == []:
                player.participant.box4_items = [999,]
            if player.participant.box5_items == []:
                player.participant.box5_items = [999,]
        
        else:
            player.participant.img_category_list = []
            for imc in cat_list:
                player.participant.img_category_list.append(int(imc))

            player.participant.default_nameorder = []

            n_list = player.name_order.split(",")
            for name in n_list:
                player.participant.default_nameorder.append(int(name[-1]))
        
            if player.box0_children == "999":
                player.participant.box0_items = [999,]
            else:
                player.participant.box0_items = [int(b0i) for b0i  in player.box0_children.split(",")]

            if player.box1_children == "999":
                player.participant.box1_items = [999,]
            else:
                player.participant.box1_items = [int(b1i) for b1i  in player.box1_children.split(",")]
        
            if player.box2_children == "999":
                player.participant.box2_items = [999,]
            else:
                player.participant.box2_items = [int(b2i) for b2i  in player.box2_children.split(",")]
        
            if player.box3_children == "999":
                player.participant.box3_items = [999,]
            else:
                player.participant.box3_items = [int(b3i) for b3i  in player.box3_children.split(",")]
        
            if player.box4_children == "999":
                player.participant.box4_items = [999,]
            else:
                player.participant.box4_items = [int(b4i) for b4i  in player.box4_children.split(",")]
        
            if player.box5_children == "999":
                player.participant.box5_items = [999,]
            else:
                player.participant.box5_items = [int(b5i) for b5i  in player.box5_children.split(",")]


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            player.kappa = max(
                cohen_kappa_score(cl, player.participant.img_category_list) for cl in Constants.correct_cat_list
                )
            player.ari = adjusted_rand_score(
                group.get_players()[0].participant.img_category_list,
                group.get_players()[1].participant.img_category_list
            )

class EarlyFinish(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.ari >= Constants.goal_ari
    
    @staticmethod
    def vars_for_template(player: Player):
        player.parcitipant.final_round_num = player.round_number
        player.parcitipant.final_kappa = player.kappa
        player.parcitipant.final_ari = player.ari
        return {
            "kappa" : player.kappa,
        }
    
    def app_after_this_page(self, upcoming_apps):
        player = self.player
        if player.whatever:
            return upcoming_apps[-1]

class Results(Page):    
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "kappa" : player.kappa,
            "ari" : player.ari,
            "box0_children" : player.box0_children,
            "box1_children" : player.box1_children,
            "box2_children" : player.box2_children,
            "box3_children" : player.box3_children,
            "box4_children" : player.box4_children,
            "box5_children" : player.box5_children,
            "box0_items" : player.participant.box0_items,
            "box1_items" : player.participant.box1_items,
            "box2_items" : player.participant.box2_items,
            "box3_items" : player.participant.box3_items,
            "box4_items" : player.participant.box4_items,
            "box5_items" : player.participant.box5_items,
        }


page_sequence = [
    Introduction,
    Instruction,
    Categorize,
    ResultsWaitPage,
    EarlyFinish,
    Results
    ]
