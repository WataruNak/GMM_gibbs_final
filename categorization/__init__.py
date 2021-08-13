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


class Constants(BaseConstants):
    name_in_url = 'categorization'
    players_per_group = 2
    num_rounds = 1
    imghtml_list = [
        "<img src = \"https://imgur.com/wqnOMfy.jpg\" class=\"item\" draggable=\"true\" id=\"0\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/LHJYfxo.jpg\" class=\"item\" draggable=\"true\" id=\"1\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/9Xa4VnX.jpg\" class=\"item\" draggable=\"true\" id=\"2\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/D91W1KT.jpg\" class=\"item\" draggable=\"true\" id=\"3\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/J35mb8e.jpg\" class=\"item\" draggable=\"true\" id=\"4\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/IC9TPNn.jpg\" class=\"item\" draggable=\"true\" id=\"5\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/cJQIb6k.jpg\" class=\"item\" draggable=\"true\" id=\"6\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/2rj1L4f.jpg\" class=\"item\" draggable=\"true\" id=\"7\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/CeGed6S.jpg\" class=\"item\" draggable=\"true\" id=\"8\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/u28iEnb.jpg\" class=\"item\" draggable=\"true\" id=\"9\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/N1rDlYe.jpg\" class=\"item\" draggable=\"true\" id=\"10\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/4uFfzbw.jpg\" class=\"item\" draggable=\"true\" id=\"11\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/ATEBW84.jpg\" class=\"item\" draggable=\"true\" id=\"12\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/OUEAyTS.jpg\" class=\"item\" draggable=\"true\" id=\"13\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/oLE2TWf.jpg\" class=\"item\" draggable=\"true\" id=\"14\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/xiGpQvF.jpg\" class=\"item\" draggable=\"true\" id=\"15\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/NnOAzoD.jpg\" class=\"item\" draggable=\"true\" id=\"16\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/0wGJ58N.jpg\" class=\"item\" draggable=\"true\" id=\"17\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/nitf5Sq.jpg\" class=\"item\" draggable=\"true\" id=\"18\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/dwXrpvH.jpg\" class=\"item\" draggable=\"true\" id=\"19\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/K8sGXHa.jpg\" class=\"item\" draggable=\"true\" id=\"20\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/XejnHhh.jpg\" class=\"item\" draggable=\"true\" id=\"21\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/yFw1I6M.jpg\" class=\"item\" draggable=\"true\" id=\"22\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/iuGyxnS.jpg\" class=\"item\" draggable=\"true\" id=\"23\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/zysvnS8.jpg\" class=\"item\" draggable=\"true\" id=\"24\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/jv5EHuP.jpg\" class=\"item\" draggable=\"true\" id=\"25\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/fqjlV3Y.jpg\" class=\"item\" draggable=\"true\" id=\"26\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/2NYuf1e.jpg\" class=\"item\" draggable=\"true\" id=\"27\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/jy5MPbW.jpg\" class=\"item\" draggable=\"true\" id=\"28\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/7Rf9TKU.jpg\" class=\"item\" draggable=\"true\" id=\"29\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/BgSfDLZ.jpg\" class=\"item\" draggable=\"true\" id=\"30\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/3sfX7Mr.jpg\" class=\"item\" draggable=\"true\" id=\"31\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/6R8GCoP.jpg\" class=\"item\" draggable=\"true\" id=\"32\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/A5ju4zJ.jpg\" class=\"item\" draggable=\"true\" id=\"33\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/QF9ee5p.jpg\" class=\"item\" draggable=\"true\" id=\"34\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/vW5QaBq.jpg\" class=\"item\" draggable=\"true\" id=\"35\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/NcY47LO.jpg\" class=\"item\" draggable=\"true\" id=\"36\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/GDI9kz8.jpg\" class=\"item\" draggable=\"true\" id=\"37\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/OmiMBXk.jpg\" class=\"item\" draggable=\"true\" id=\"38\" height=\"50px\" width=\"50px\"/>",
        "<img src = \"https://imgur.com/in0lSLH.jpg\" class=\"item\" draggable=\"true\" id=\"39\" height=\"50px\" width=\"50px\"/>",
        ]
    namehtml_list = [
        "<li draggable=\"true\" id=\"name0\" data-id=\"sym0\"><img src=\"https://imgur.com/a1HYfcA.png\" height=\"100px\" width=\"100px\"></li>",
        "<li draggable=\"true\" id=\"name1\" data-id=\"sym1\"><img src=\"https://imgur.com/xMBZ0Dg.png\" height=\"100px\" width=\"100px\"></li>",
        "<li draggable=\"true\" id=\"name2\" data-id=\"sym2\"><img src=\"https://imgur.com/Xh5Scyo.png\" height=\"100px\" width=\"100px\"></li>",
        "<li draggable=\"true\" id=\"name3\" data-id=\"sym3\"><img src=\"https://imgur.com/PBZ3YNV.png\" height=\"100px\" width=\"100px\"></li>",
        "<li draggable=\"true\" id=\"name4\" data-id=\"sym4\"><img src=\"https://imgur.com/dmiNF4h.png\" height=\"100px\" width=\"100px\"></li>",
        "<li draggable=\"true\" id=\"name5\" data-id=\"sym5\"><img src=\"https://imgur.com/RdWIiGo.png\" height=\"100px\" width=\"100px\"></li>",
        ]
    
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
        "round_number",
        "id_in_group",
        "stimuli_id",
        "selected_category",
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code,
            p.round_number,
            p.id_in_group,
            p.stimuli_id,
            p.selected_category,
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
        if timeout_happened:
            if player.img0_cat == "99":
                player.img0_cat = str(random.randint(0, 5))
            if player.img1_cat == "99":
                player.img1_cat = str(random.randint(0, 5))
            if player.img2_cat == "99":
                player.img2_cat = str(random.randint(0, 5))
            if player.img3_cat == "99":
                player.img3_cat = str(random.randint(0, 5))
            if player.img4_cat == "99":
                player.img4_cat = str(random.randint(0, 5))
            if player.img5_cat == "99":
                player.img5_cat = str(random.randint(0, 5))
            if player.img6_cat == "99":
                player.img6_cat = str(random.randint(0, 5))
            if player.img7_cat == "99":
                player.img7_cat = str(random.randint(0, 5))
            if player.img8_cat == "99":
                player.img8_cat = str(random.randint(0, 5))
            if player.img9_cat == "99":
                player.img9_cat = str(random.randint(0, 5))
            if player.img10_cat == "99":
                player.img10_cat = str(random.randint(0, 5))
            if player.img11_cat == "99":
                player.img11_cat = str(random.randint(0, 5))
            if player.img12_cat == "99":
                player.img12_cat = str(random.randint(0, 5))
            if player.img13_cat == "99":
                player.img13_cat = str(random.randint(0, 5))
            if player.img14_cat == "99":
                player.img14_cat = str(random.randint(0, 5))
            if player.img15_cat == "99":
                player.img15_cat = str(random.randint(0, 5))
            if player.img16_cat == "99":
                player.img16_cat = str(random.randint(0, 5))
            if player.img17_cat == "99":
                player.img17_cat = str(random.randint(0, 5))
            if player.img18_cat == "99":
                player.img18_cat = str(random.randint(0, 5))
            if player.img19_cat == "99":
                player.img19_cat = str(random.randint(0, 5))
            if player.img20_cat == "99":
                player.img20_cat = str(random.randint(0, 5))
            if player.img21_cat == "99":
                player.img21_cat = str(random.randint(0, 5))
            if player.img22_cat == "99":
                player.img22_cat = str(random.randint(0, 5))
            if player.img23_cat == "99":
                player.img23_cat = str(random.randint(0, 5))
            if player.img24_cat == "99":
                player.img24_cat = str(random.randint(0, 5))
            if player.img25_cat == "99":
                player.img25_cat = str(random.randint(0, 5))
            if player.img26_cat == "99":
                player.img26_cat = str(random.randint(0, 5))
            if player.img27_cat == "99":
                player.img27_cat = str(random.randint(0, 5))
            if player.img28_cat == "99":
                player.img28_cat = str(random.randint(0, 5))
            if player.img29_cat == "99":
                player.img29_cat = str(random.randint(0, 5))
            if player.img30_cat == "99":
                player.img30_cat = str(random.randint(0, 5))
            if player.img31_cat == "99":
                player.img31_cat = str(random.randint(0, 5))
            if player.img32_cat == "99":
                player.img32_cat = str(random.randint(0, 5))
            if player.img33_cat == "99":
                player.img33_cat = str(random.randint(0, 5))
            if player.img34_cat == "99":
                player.img34_cat = str(random.randint(0, 5))
            if player.img35_cat == "99":
                player.img35_cat = str(random.randint(0, 5))
            if player.img36_cat == "99":
                player.img36_cat = str(random.randint(0, 5))
            if player.img37_cat == "99":
                player.img37_cat = str(random.randint(0, 5))
            if player.img38_cat == "99":
                player.img38_cat = str(random.randint(0, 5))
            if player.img39_cat == "99":
                player.img39_cat = str(random.randint(0, 5))


        player.participant.img_category_list = []
        player.participant.img_category_list.append(int(player.img0_cat))
        player.participant.img_category_list.append(int(player.img1_cat))
        player.participant.img_category_list.append(int(player.img2_cat))
        player.participant.img_category_list.append(int(player.img3_cat))
        player.participant.img_category_list.append(int(player.img5_cat))
        player.participant.img_category_list.append(int(player.img6_cat))
        player.participant.img_category_list.append(int(player.img7_cat))
        player.participant.img_category_list.append(int(player.img8_cat))
        player.participant.img_category_list.append(int(player.img9_cat))
        player.participant.img_category_list.append(int(player.img10_cat))
        player.participant.img_category_list.append(int(player.img11_cat))
        player.participant.img_category_list.append(int(player.img12_cat))
        player.participant.img_category_list.append(int(player.img13_cat))
        player.participant.img_category_list.append(int(player.img14_cat))
        player.participant.img_category_list.append(int(player.img15_cat))
        player.participant.img_category_list.append(int(player.img16_cat))
        player.participant.img_category_list.append(int(player.img17_cat))
        player.participant.img_category_list.append(int(player.img18_cat))
        player.participant.img_category_list.append(int(player.img19_cat))
        player.participant.img_category_list.append(int(player.img20_cat))
        player.participant.img_category_list.append(int(player.img21_cat))
        player.participant.img_category_list.append(int(player.img22_cat))
        player.participant.img_category_list.append(int(player.img23_cat))
        player.participant.img_category_list.append(int(player.img24_cat))
        player.participant.img_category_list.append(int(player.img25_cat))
        player.participant.img_category_list.append(int(player.img26_cat))
        player.participant.img_category_list.append(int(player.img27_cat))
        player.participant.img_category_list.append(int(player.img28_cat))
        player.participant.img_category_list.append(int(player.img29_cat))
        player.participant.img_category_list.append(int(player.img30_cat))
        player.participant.img_category_list.append(int(player.img31_cat))
        player.participant.img_category_list.append(int(player.img32_cat))
        player.participant.img_category_list.append(int(player.img33_cat))
        player.participant.img_category_list.append(int(player.img34_cat))
        player.participant.img_category_list.append(int(player.img35_cat))
        player.participant.img_category_list.append(int(player.img36_cat))
        player.participant.img_category_list.append(int(player.img37_cat))
        player.participant.img_category_list.append(int(player.img38_cat))
        player.participant.img_category_list.append(int(player.img39_cat))

        player.participant.default_nameorder = []

        n_list = player.name_order.split(",")
        for name in n_list:
            player.participant.default_nameorder.append(int(name[-1]))
        
        if player.box0_children == "999":
            player.participant.box0_items = [999,]
        else:
            b0list = player.box0_children.split(",")
            for b0i in b0list:
                player.participant.box0_items = []
                player.participant.box0_items.append(int(b0i))

        if player.box1_children == "999":
            player.participant.box1_items = [999,]
        else:
            b1list = player.box1_children.split(",")
            for b1i in b1list:
                player.participant.box1_items = []
                player.participant.box1_items.append(int(b1i))
        
        if player.box2_children == "999":
            player.participant.box2_items = [999,]
        else:
            b2list = player.box2_children.split(",")
            for b2i in b2list:
                player.participant.box2_items = []
                player.participant.box2_items.append(int(b2i))
        
        if player.box3_children == "999":
            player.participant.box3_items = [999,]
        else:
            b3list = player.box3_children.split(",")
            for b3i in b3list:
                player.participant.box3_items = []
                player.participant.box3_items.append(int(b3i))
        
        if player.box4_children == "999":
            player.participant.box4_items = [999,]
        else:
            b4list = player.box4_children.split(",")
            for b4i in b4list:
                player.participant.box4_items = []
                player.participant.box4_items.append(int(b4i))
        
        if player.box5_children == "999":
            player.participant.box5_items = [999,]
        else:
            b5list = player.box5_children.split(",")
            for b5i in b5list:
                player.participant.box5_items = []
                player.participant.box5_items.append(int(b5i))



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
        }


page_sequence = [
    Introduction,
    Instruction,
    Categorize,
    ResultsWaitPage,
    EarlyFinish,
    Results
    ]
