from otree.api import *
import random
from sklearn.metrics import cohen_kappa_score, adjusted_rand_score

doc = """
Your app description
"""

def make_imgcat_path(num):
    imgcatpath_list = []
    for _ in range(num):
        imgcatpath_list.append("img{}_cat".format(_))
    return imgcatpath_list

def make_img_html_list(height, width):
    img_html_list = [
        "<img src = \"https://imgur.com/wqnOMfy.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/LHJYfxo.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/9Xa4VnX.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/D91W1KT.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/J35mb8e.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/IC9TPNn.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/cJQIb6k.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/2rj1L4f.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/CeGed6S.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/u28iEnb.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/N1rDlYe.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/4uFfzbw.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/ATEBW84.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/OUEAyTS.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/oLE2TWf.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/xiGpQvF.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/NnOAzoD.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/0wGJ58N.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/nitf5Sq.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/dwXrpvH.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/K8sGXHa.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/XejnHhh.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/yFw1I6M.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/iuGyxnS.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/zysvnS8.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/jv5EHuP.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/fqjlV3Y.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/2NYuf1e.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/jy5MPbW.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/7Rf9TKU.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/BgSfDLZ.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/3sfX7Mr.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/6R8GCoP.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/A5ju4zJ.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/QF9ee5p.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/vW5QaBq.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/NcY47LO.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/GDI9kz8.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/OmiMBXk.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        "<img src = \"https://imgur.com/in0lSLH.jpg\" height=\"{}px\" width=\"{}px\"/>".format(height, width),
        ]
    return img_html_list
    
def make_name_html_list(height, width):
    img_html_list = [
        "<img src=\"https://imgur.com/a1HYfcA.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/xMBZ0Dg.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/Xh5Scyo.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/PBZ3YNV.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/dmiNF4h.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        "<img src=\"https://imgur.com/RdWIiGo.png\" height=\"{}px\" width=\"{}px\">".format(height, width),
        ]
    return img_html_list

class Constants(BaseConstants):
    name_in_url = 'create_symbol'
    players_per_group = 2
    num_rounds = 40
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

    stimuliimg_html_list = make_img_html_list(70, 70)
    logimg_html_list = make_img_html_list(30, 30)
    choicename_html_list = make_name_html_list(70, 70)
    logname_html_list = make_name_html_list(30, 30)

    imgcatpath_list = make_imgcat_path(40)
    accept_choice = ["×", "○"]

    pred_cat_list = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    s_choice0 = models.StringField(
        initial="99",
        label="1番目の画像",
        choices=[
            ["0", "1番の記号"],
            ["1", "2番の記号"],
            ["2", "3番の記号"],
            ["3", "4番の記号"],
            ["4", "5番の記号"],
            ["5", "6番の記号"],
            ],
        widget = widgets.RadioSelectHorizontal,
    )
    s_choice1 = models.StringField(
        initial="99",
        label="2番目の画像",
        choices=[
            ["0", "1番の記号"],
            ["1", "2番の記号"],
            ["2", "3番の記号"],
            ["3", "4番の記号"],
            ["4", "5番の記号"],
            ["5", "6番の記号"],
            ],
        widget = widgets.RadioSelectHorizontal,
    )
    s_choice2 = models.StringField(
        initial="99",
        label="3番目の画像",
        choices=[
            ["0", "1番の記号"],
            ["1", "2番の記号"],
            ["2", "3番の記号"],
            ["3", "4番の記号"],
            ["4", "5番の記号"],
            ["5", "6番の記号"],
            ],
        widget = widgets.RadioSelectHorizontal,
    )
    s_choice3 = models.StringField(
        initial="99",
        label="4番目の画像",
        choices=[
            ["0", "1番の記号"],
            ["1", "2番の記号"],
            ["2", "3番の記号"],
            ["3", "4番の記号"],
            ["4", "5番の記号"],
            ["5", "6番の記号"],
            ],
        widget = widgets.RadioSelectHorizontal,
    )
    s_choice4 = models.StringField(
        initial="99",
        label="5番目の画像",
        choices=[
            ["0", "1番の記号"],
            ["1", "2番の記号"],
            ["2", "3番の記号"],
            ["3", "4番の記号"],
            ["4", "5番の記号"],
            ["5", "6番の記号"],
            ],
        widget = widgets.RadioSelectHorizontal,
    )

    accept0 = models.IntegerField(
        initial=2,
        label="1番目の画像",
        choices=[[0, "受け入れない"], [1, "受け入れる"]],
        widget = widgets.RadioSelect,
    )

    accept1 = models.IntegerField(
        initial=2,
        label="2番目の画像",
        choices=[[0, "受け入れない"], [1, "受け入れる"]],
        widget = widgets.RadioSelect,
    )

    accept2 = models.IntegerField(
        initial=2,
        label="3番目の画像",
        choices=[[0, "受け入れない"], [1, "受け入れる"]],
        widget = widgets.RadioSelect,
    )

    accept3 = models.IntegerField(
        initial=2,
        label="4番目の画像",
        choices=[[0, "受け入れない"], [1, "受け入れる"]],
        widget = widgets.RadioSelect,
    )

    accept4 = models.IntegerField(
        initial=2,
        label="5番目の画像",
        choices=[[0, "受け入れない"], [1, "受け入れる"]],
        widget = widgets.RadioSelect,
    )

    name_order = models.StringField()
    img0_cat = models.StringField()
    img1_cat = models.StringField()
    img2_cat = models.StringField()
    img3_cat = models.StringField()
    img4_cat = models.StringField()
    img5_cat = models.StringField()
    img6_cat = models.StringField()
    img7_cat = models.StringField()
    img8_cat = models.StringField()
    img9_cat = models.StringField()
    img10_cat = models.StringField()
    img11_cat = models.StringField()
    img12_cat = models.StringField()
    img13_cat = models.StringField()
    img14_cat = models.StringField()
    img15_cat = models.StringField()
    img16_cat = models.StringField()
    img17_cat = models.StringField()
    img18_cat = models.StringField()
    img19_cat = models.StringField()
    img20_cat = models.StringField()
    img21_cat = models.StringField()
    img22_cat = models.StringField()
    img23_cat = models.StringField()
    img24_cat = models.StringField()
    img25_cat = models.StringField()
    img26_cat = models.StringField()
    img27_cat = models.StringField()
    img28_cat = models.StringField()
    img29_cat = models.StringField()
    img30_cat = models.StringField()
    img31_cat = models.StringField()
    img32_cat = models.StringField()
    img33_cat = models.StringField()
    img34_cat = models.StringField()
    img35_cat = models.StringField()
    img36_cat = models.StringField()
    img37_cat = models.StringField()
    img38_cat = models.StringField()
    img39_cat = models.StringField()

    box0_children = models.StringField()
    box1_children = models.StringField()
    box2_children = models.StringField()
    box3_children = models.StringField()
    box4_children = models.StringField()
    box5_children = models.StringField()

    ari = models.FloatField()


    def role(self):
        if self.round_number % 2 == 1:
            if self.id_in_group % 2 == 1:
                return 'speaker'
            if self.id_in_group % 2 == 0:
                return 'listener'
        else:
            if self.id_in_group % 2 == 1:
                return 'listener'
            if self.id_in_group % 2 == 0:
                return 'speaker'


def custom_export(players):
    yield [
        "session",
        "participant_code",
        "round_number",
        "id_in_group",
        "img_id",
        "send_choice",
        "accept",
        "rename_choice",
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code,
            p.round_number,
            p.id_in_group,
            p.test_id,
            p.send_choice,
            p.accept,
            p.rename_choice
            ]



# PAGES
class Instruction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class ShowRole(Page):
    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            player.participant.loghtml_list =["<p>実験開始</p><br>",]
        return {
            "role" : player.role(),
            }


class Speaker(Page):
    form_model = 'player'
    form_fields = [
        "s_choice0", "s_choice1", "s_choice2", "s_choice3", "s_choice4",
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
    def is_displayed(player: Player):
        return player.role() == 'speaker'

    @staticmethod
    def vars_for_template(player: Player):
        img_choice = random.sample(range(0,40,1), k=(5))
        player.subsession.showed_imgs = []
        player.subsession.showed_imgs4log = []
        for id in img_choice:
            player.subsession.showed_imgs.append(Constants.stimuliimg_html_list[img_choice[id]])
            player.subsession.showed_imgs4log.append(Constants.logimg_html_list[img_choice[id]])
        
        box0_defaultimgs = []
        if player.participant.box0_items[0] == 999:
            box0_defaultimgs.append("999")
        else:
            for j in range(len(player.participant.box0_items)):
                box0_defaultimgs.append(Constants.imghtml_list[player.participant.box0_items[j]])
        
        box1_defaultimgs = []
        if player.participant.box1_items[0] == 999:
            box1_defaultimgs.append("999")
        else:
            for k in range(len(player.participant.box1_items)):
                box1_defaultimgs.append(Constants.imghtml_list[player.participant.box1_items[k]])
        
        box2_defaultimgs = []
        if player.participant.box2_items[0] == 999:
            box2_defaultimgs.append("999")
        else:
            for l in range(len(player.participant.box2_items)):
                box2_defaultimgs.append(Constants.imghtml_list[player.participant.box2_items[l]])
        
        box3_defaultimgs = []
        if player.participant.box3_items[0] == 999:
            box3_defaultimgs.append("999")
        else:
            for m in range(len(player.participant.box3_items)):
                box3_defaultimgs.append(Constants.imghtml_list[player.participant.box3_items[m]])
        
        box4_defaultimgs = []
        if player.participant.box4_items[0] == 999:
            box4_defaultimgs.append("999")
        else:
            for n in range(len(player.participant.box4_items)):
                box4_defaultimgs.append(Constants.imghtml_list[player.participant.box4_items[n]])
        
        box5_defaultimgs = []
        if player.participant.box5_items[0] == 999:
            box5_defaultimgs.append("999")
        else:
            for o in range(len(player.participant.box5_items)):
                box5_defaultimgs.append(Constants.imghtml_list[player.participant.box5_items[o]])
        
        default_name_list = []
        for p in range(len(player.participant.default_nameorder)):
            default_name_list.append(Constants.namehtml_list[p])
        
        other_players = player.get_others_in_group()
        
        
        return {
            "showed_imgs" : player.subsession.showed_imgs,
            "choice_names" : Constants.choicename_html_list,
            "default_name_list" : default_name_list,
            "box0_defaultimgs" : box0_defaultimgs,
            "box1_defaultimgs" : box1_defaultimgs,
            "box2_defaultimgs" : box2_defaultimgs,
            "box3_defaultimgs" : box3_defaultimgs,
            "box4_defaultimgs" : box4_defaultimgs,
            "box5_defaultimgs" : box5_defaultimgs,
            "img_category_list" : player.participant.img_category_list,
            "loghtml_list" : player.participant.log_html_list,           
        }
    
    @staticmethod
    def js_vars(player):
        default_name_value = "sym" + str(player.participant.default_nameorder[0]) + "," +\
            "sym" + str(player.participant.default_nameorder[1]) + "," +\
                "sym" + str(player.participant.default_nameorder[2]) + "," +\
                    "sym" + str(player.participant.default_nameorder[3]) + "," +\
                        "sym" + str(player.participant.default_nameorder[4]) + "," +\
                            "sym" + str(player.participant.default_nameorder[5])
        return dict(
            img_category_list=player.participant.img_category_list,
            imgcatpath_list=Constants.imgcatpath_list,
            default_name_list=player.participant.default_name_list,
            default_name_value=default_name_value
        )
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.img_category_list[0] = int(player.img0_cat)
        player.participant.img_category_list[1] = int(player.img1_cat)
        player.participant.img_category_list[2] = int(player.img2_cat)
        player.participant.img_category_list[3] = int(player.img3_cat)
        player.participant.img_category_list[4] = int(player.img4_cat)
        player.participant.img_category_list[5] = int(player.img5_cat)
        player.participant.img_category_list[6] = int(player.img6_cat)
        player.participant.img_category_list[7] = int(player.img7_cat)
        player.participant.img_category_list[8] = int(player.img8_cat)
        player.participant.img_category_list[9] = int(player.img9_cat)
        player.participant.img_category_list[10] = int(player.img10_cat)
        player.participant.img_category_list[11] = int(player.img11_cat)
        player.participant.img_category_list[12] = int(player.img12_cat)
        player.participant.img_category_list[13] = int(player.img13_cat)
        player.participant.img_category_list[14] = int(player.img14_cat)
        player.participant.img_category_list[15] = int(player.img15_cat)
        player.participant.img_category_list[16] = int(player.img16_cat)
        player.participant.img_category_list[17] = int(player.img17_cat)
        player.participant.img_category_list[18] = int(player.img18_cat)
        player.participant.img_category_list[19] = int(player.img19_cat)
        player.participant.img_category_list[20] = int(player.img20_cat)
        player.participant.img_category_list[21] = int(player.img21_cat)
        player.participant.img_category_list[22] = int(player.img22_cat)
        player.participant.img_category_list[23] = int(player.img23_cat)
        player.participant.img_category_list[24] = int(player.img24_cat)
        player.participant.img_category_list[25] = int(player.img25_cat)
        player.participant.img_category_list[26] = int(player.img26_cat)
        player.participant.img_category_list[27] = int(player.img27_cat)
        player.participant.img_category_list[28] = int(player.img28_cat)
        player.participant.img_category_list[29] = int(player.img29_cat)
        player.participant.img_category_list[30] = int(player.img30_cat)
        player.participant.img_category_list[31] = int(player.img31_cat)
        player.participant.img_category_list[32] = int(player.img32_cat)
        player.participant.img_category_list[33] = int(player.img33_cat)
        player.participant.img_category_list[34] = int(player.img34_cat)
        player.participant.img_category_list[35] = int(player.img35_cat)
        player.participant.img_category_list[36] = int(player.img36_cat)
        player.participant.img_category_list[37] = int(player.img37_cat)
        player.participant.img_category_list[38] = int(player.img38_cat)
        player.participant.img_category_list[39] = int(player.img39_cat)

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


class Listener(Page):
    form_model = 'player'
    form_fields = [
        "accept0", "accept1", "accept2", "accept3", "accept4",
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
    def is_displayed(player: Player):
        return player.role() == 'speaker'

    @staticmethod
    def vars_for_template(player: Player):
        box0_defaultimgs = []
        if player.participant.box0_items[0] == 999:
            box0_defaultimgs.append("999")
        else:
            for j in range(len(player.participant.box0_items)):
                box0_defaultimgs.append(Constants.imghtml_list[player.participant.box0_items[j]])
        
        box1_defaultimgs = []
        if player.participant.box1_items[0] == 999:
            box1_defaultimgs.append("999")
        else:
            for k in range(len(player.participant.box1_items)):
                box1_defaultimgs.append(Constants.imghtml_list[player.participant.box1_items[k]])
        
        box2_defaultimgs = []
        if player.participant.box2_items[0] == 999:
            box2_defaultimgs.append("999")
        else:
            for l in range(len(player.participant.box2_items)):
                box2_defaultimgs.append(Constants.imghtml_list[player.participant.box2_items[l]])
        
        box3_defaultimgs = []
        if player.participant.box3_items[0] == 999:
            box3_defaultimgs.append("999")
        else:
            for m in range(len(player.participant.box3_items)):
                box3_defaultimgs.append(Constants.imghtml_list[player.participant.box3_items[m]])
        
        box4_defaultimgs = []
        if player.participant.box4_items[0] == 999:
            box4_defaultimgs.append("999")
        else:
            for n in range(len(player.participant.box4_items)):
                box4_defaultimgs.append(Constants.imghtml_list[player.participant.box4_items[n]])
        
        box5_defaultimgs = []
        if player.participant.box5_items[0] == 999:
            box5_defaultimgs.append("999")
        else:
            for o in range(len(player.participant.box5_items)):
                box5_defaultimgs.append(Constants.imghtml_list[player.participant.box5_items[o]])
        
        default_name_list = []
        for p in range(len(player.participant.default_nameorder)):
            default_name_list.append(Constants.namehtml_list[p])
        
        other_players = player.get_others_in_group()
        
        
        return {
            "showed_imgs" : player.subsession.showed_imgs,
            "choice_names" : Constants.choicename_html_list,
            "default_name_list" : default_name_list,
            "others_choice0" : other_players[0].s_choice0,
            "others_choice1" : other_players[0].s_choice1,
            "others_choice2" : other_players[0].s_choice2,
            "others_choice3" : other_players[0].s_choice3,
            "others_choice4" : other_players[0].s_choice4,
            "box0_defaultimgs" : box0_defaultimgs,
            "box1_defaultimgs" : box1_defaultimgs,
            "box2_defaultimgs" : box2_defaultimgs,
            "box3_defaultimgs" : box3_defaultimgs,
            "box4_defaultimgs" : box4_defaultimgs,
            "box5_defaultimgs" : box5_defaultimgs,
            "img_category_list" : player.participant.img_category_list,
            "loghtml_list" : player.participant.log_html_list,            
        }
    
    @staticmethod
    def js_vars(player):
        default_name_value = "sym" + str(player.participant.default_nameorder[0]) + "," +\
            "sym" + str(player.participant.default_nameorder[1]) + "," +\
                "sym" + str(player.participant.default_nameorder[2]) + "," +\
                    "sym" + str(player.participant.default_nameorder[3]) + "," +\
                        "sym" + str(player.participant.default_nameorder[4]) + "," +\
                            "sym" + str(player.participant.default_nameorder[5])
        return dict(
            img_category_list=player.participant.img_category_list,
            imgcatpath_list=Constants.imgcatpath_list,
            default_name_list=player.participant.default_name_list,
            default_name_value=default_name_value
        )
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.img_category_list[0] = int(player.img0_cat)
        player.participant.img_category_list[1] = int(player.img1_cat)
        player.participant.img_category_list[2] = int(player.img2_cat)
        player.participant.img_category_list[3] = int(player.img3_cat)
        player.participant.img_category_list[4] = int(player.img4_cat)
        player.participant.img_category_list[5] = int(player.img5_cat)
        player.participant.img_category_list[6] = int(player.img6_cat)
        player.participant.img_category_list[7] = int(player.img7_cat)
        player.participant.img_category_list[8] = int(player.img8_cat)
        player.participant.img_category_list[9] = int(player.img9_cat)
        player.participant.img_category_list[10] = int(player.img10_cat)
        player.participant.img_category_list[11] = int(player.img11_cat)
        player.participant.img_category_list[12] = int(player.img12_cat)
        player.participant.img_category_list[13] = int(player.img13_cat)
        player.participant.img_category_list[14] = int(player.img14_cat)
        player.participant.img_category_list[15] = int(player.img15_cat)
        player.participant.img_category_list[16] = int(player.img16_cat)
        player.participant.img_category_list[17] = int(player.img17_cat)
        player.participant.img_category_list[18] = int(player.img18_cat)
        player.participant.img_category_list[19] = int(player.img19_cat)
        player.participant.img_category_list[20] = int(player.img20_cat)
        player.participant.img_category_list[21] = int(player.img21_cat)
        player.participant.img_category_list[22] = int(player.img22_cat)
        player.participant.img_category_list[23] = int(player.img23_cat)
        player.participant.img_category_list[24] = int(player.img24_cat)
        player.participant.img_category_list[25] = int(player.img25_cat)
        player.participant.img_category_list[26] = int(player.img26_cat)
        player.participant.img_category_list[27] = int(player.img27_cat)
        player.participant.img_category_list[28] = int(player.img28_cat)
        player.participant.img_category_list[29] = int(player.img29_cat)
        player.participant.img_category_list[30] = int(player.img30_cat)
        player.participant.img_category_list[31] = int(player.img31_cat)
        player.participant.img_category_list[32] = int(player.img32_cat)
        player.participant.img_category_list[33] = int(player.img33_cat)
        player.participant.img_category_list[34] = int(player.img34_cat)
        player.participant.img_category_list[35] = int(player.img35_cat)
        player.participant.img_category_list[36] = int(player.img36_cat)
        player.participant.img_category_list[37] = int(player.img37_cat)
        player.participant.img_category_list[38] = int(player.img38_cat)
        player.participant.img_category_list[39] = int(player.img39_cat)

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



class WaitForSpeaker(WaitPage):
    titel_text = "「話し手」の入力を待っています"
    body_text = "あなたは「聞き手」です。「話し手」が名前を決めるまでお待ち下さい。"
    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'listener'


class WaitForListener(WaitPage):
    titel_text = "「聞き手」の入力を待っています"
    body_text = "「聞き手」があなたのつけた名前を受け入れるかどうかを決めています。入力があるまでお待ち下さい。"
    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'speaker'


class EndOfRound(Page):
    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.get_players()
        player.subsession.kappa = cohen_kappa_score(
            all_players[0].participant.img_category_list,
            all_players[1].participant.img_category_list
            )
        player.ari = adjusted_rand_score(
            Constants.pred_cat_list,
            player.participant.img_category_list
        )

        imgs_this_round = player.subsession.showed_imgs4log
        other_players = player.get_others_in_group()
        if player.role() == 'speaker':
            log0 = "<p>あなたの役割：「話し手」</p>"
            log1 = "<p>表示された画像（左から順に1,2,3,4,5番）：</p>"
            log_divhead = "<div style=\"display: flex;\">"
            log_divtail = "</div>"
            log2 = "<p>あなたの選んだ記号（左から順に1,2,3,4,5番に対する記号）：</p>"
            log3 = "<p>相手がその記号を受け入れたかどうか（左から順に1,2,3,4,5番への答え）：</p>"
            log4 = "<p>{}, {}, {}, {}, {}<\p><br><br><br>".format(
                Constants.accept_choice[other_players[0].accept0],
                Constants.accept_choice[other_players[0].accept1],
                Constants.accept_choice[other_players[0].accept2],
                Constants.accept_choice[other_players[0].accept3],
                Constants.accept_choice[other_players[0].accept4],
                )
            player.participant.loghtml_list.append(log0)
            player.participant.loghtml_list.append(log1)
            player.participant.loghtml_list.append(log_divhead)
            for img_tr in imgs_this_round:
                player.participant.loghtml_list.append(img_tr)
            player.participant.loghtml_list.append(log_divtail)
            player.participant.loghtml_list.append(log2)
            player.participant.loghtml_list.append(log_divhead)
            player.participant.loghtml_list.append(Constants.logname_html_list[int(player.s_choice0)])
            player.participant.loghtml_list.append(Constants.logname_html_list[int(player.s_choice1)])
            player.participant.loghtml_list.append(Constants.logname_html_list[int(player.s_choice2)])
            player.participant.loghtml_list.append(Constants.logname_html_list[int(player.s_choice3)])
            player.participant.loghtml_list.append(Constants.logname_html_list[int(player.s_choice4)])
            player.participant.loghtml_list.append(log_divtail)
            player.participant.loghtml_list.append(log3)
            player.participant.loghtml_list.append(log4)
        else:
            log0 = "<p>あなたの役割：「聞き手」</p>"
            log1 = "<p>表示された画像（左から順に1,2,3,4,5番）：</p>"
            log_divhead = "<div style=\"display: flex;\">"
            log_divtail = "</div>"
            log2 = "<p>相手の選んだ記号（左から順に1,2,3,4,5番に対する記号）：</p>"
            log3 = "<p>あなたがその記号を受け入れたかどうか（左から順に1,2,3,4,5番への答え）：</p>"
            log4 = "<p>{}, {}, {}, {}, {}<\p><br><br><br>".format(
                Constants.accept_choice[player.accept0],
                Constants.accept_choice[player.accept1],
                Constants.accept_choice[player.accept2],
                Constants.accept_choice[player.accept3],
                Constants.accept_choice[player.accept4],
                )
            player.participant.loghtml_list.append(log0)
            player.participant.loghtml_list.append(log1)
            player.participant.loghtml_list.append(log_divhead)
            for img_tr in imgs_this_round:
                player.participant.loghtml_list.append(img_tr)
            player.participant.loghtml_list.append(log_divtail)
            player.participant.loghtml_list.append(log2)
            player.participant.loghtml_list.append(log_divhead)
            player.participant.loghtml_list.append(Constants.logname_html_list[int(other_players[0].s_choice0)])
            player.participant.loghtml_list.append(Constants.logname_html_list[int(other_players[0].s_choice1)])
            player.participant.loghtml_list.append(Constants.logname_html_list[int(other_players[0].s_choice2)])
            player.participant.loghtml_list.append(Constants.logname_html_list[int(other_players[0].s_choice3)])
            player.participant.loghtml_list.append(Constants.logname_html_list[int(other_players[0].s_choice4)])
            player.participant.loghtml_list.append(log_divtail)
            player.participant.loghtml_list.append(log3)
            player.participant.loghtml_list.append(log4)
        return {
            "kappa" : player.subsession.kappa,
        }



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
            "dict1" : player.participant.img2category,
            "dict2" : player.participant.img2name,
        }


page_sequence = [
    Instruction,
    ShowRole,
    Speaker,
    WaitForSpeaker,
    Listener,
    WaitForListener,
    EndOfRound,
    ResultsWaitPage,
    Results
    ]
