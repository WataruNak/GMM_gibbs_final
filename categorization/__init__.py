from otree.api import *
import random

doc = """
https://qiita.com/naoki-funawatari/items/c78630b85f5f7fe21d19 drag_and_drop
https://www.otreehub.com/projects/otree-snippets/ otree sortable_example
https://qiita.com/AVELWP/items/536c797a63c081cf7bc0 sortable document ja
https://github.com/SortableJS/Sortable sortable git
https://qiita.com/t-iguchi/items/20dc31d5e004d7145634 js in django
"""

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
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Categorize(Page):
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
        player.participant.img_category_list = []
        player.participant.img_category_list.append(player.img0_cat)
        player.participant.img_category_list.append(player.img1_cat)
        player.participant.img_category_list.append(player.img2_cat)
        player.participant.img_category_list.append(player.img3_cat)
        player.participant.img_category_list.append(player.img4_cat)
        player.participant.img_category_list.append(player.img5_cat)
        player.participant.img_category_list.append(player.img6_cat)
        player.participant.img_category_list.append(player.img7_cat)
        player.participant.img_category_list.append(player.img8_cat)
        player.participant.img_category_list.append(player.img9_cat)
        player.participant.img_category_list.append(player.img10_cat)
        player.participant.img_category_list.append(player.img11_cat)
        player.participant.img_category_list.append(player.img12_cat)
        player.participant.img_category_list.append(player.img13_cat)
        player.participant.img_category_list.append(player.img14_cat)
        player.participant.img_category_list.append(player.img15_cat)
        player.participant.img_category_list.append(player.img16_cat)
        player.participant.img_category_list.append(player.img17_cat)
        player.participant.img_category_list.append(player.img18_cat)
        player.participant.img_category_list.append(player.img19_cat)
        player.participant.img_category_list.append(player.img20_cat)
        player.participant.img_category_list.append(player.img21_cat)
        player.participant.img_category_list.append(player.img22_cat)
        player.participant.img_category_list.append(player.img23_cat)
        player.participant.img_category_list.append(player.img24_cat)
        player.participant.img_category_list.append(player.img25_cat)
        player.participant.img_category_list.append(player.img26_cat)
        player.participant.img_category_list.append(player.img27_cat)
        player.participant.img_category_list.append(player.img28_cat)
        player.participant.img_category_list.append(player.img29_cat)
        player.participant.img_category_list.append(player.img30_cat)
        player.participant.img_category_list.append(player.img31_cat)
        player.participant.img_category_list.append(player.img32_cat)
        player.participant.img_category_list.append(player.img33_cat)
        player.participant.img_category_list.append(player.img34_cat)
        player.participant.img_category_list.append(player.img35_cat)
        player.participant.img_category_list.append(player.img36_cat)
        player.participant.img_category_list.append(player.img37_cat)
        player.participant.img_category_list.append(player.img38_cat)
        player.participant.img_category_list.append(player.img39_cat)

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
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "dict" : player.participant.img2category,
            "box0_children" : player.box0_children,
            "box1_children" : player.box1_children,
            "box2_children" : player.box2_children,
            "box3_children" : player.box3_children,
            "box4_children" : player.box4_children,
            "box5_children" : player.box5_children,
        }


page_sequence = [Introduction, Categorize, ResultsWaitPage, Results]
