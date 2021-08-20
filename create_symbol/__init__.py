from otree.api import *
import random
from sklearn.metrics import cohen_kappa_score, adjusted_rand_score
import itertools

doc = """
Your app description
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


def make_imgcat_path(num):
    imgcatpath_list = []
    for _ in range(num):
        imgcatpath_list.append("img{}_cat".format(_))
    return imgcatpath_list

def make_draggableimg_html_list(img_num, path_list, height, width):
    img_html_list = []
    for da in range(img_num):
        img_html_list.append(
            "<img src = \"{}\" class=\"item\" draggable=\"true\" id=\"{}\" height=\"{}px\" width=\"{}px\"/>".format(path_list[da], da, height, width)
        )
    return img_html_list


def make_img_html_list(img_num, path_list, height, width, id_name):
    img_html_list = []
    for a in range(img_num):
        img_html_list.append(
            "<img src = \"{}\" height=\"{}px\" width=\"{}px\" id=\"{}{}\"/>".format(path_list[a], height, width, id_name, a)
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

def make_name_html_list(name_num, path_list, height, width):
    img_html_list = []
    for b in range(name_num):
        img_html_list.append(
            "<img src=\"{}\" height=\"{}px\" width=\"{}px\">".format(path_list[b], height, width)
        )
    return img_html_list

class Constants(BaseConstants):
    name_in_url = 'create_symbol'
    players_per_group = 2
    num_rounds = 40
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

    stimuliimg_html_list = make_img_html_list(40, imgpath_list, 70, 70, "stimuli")
    logimg_html_list = make_img_html_list(40, imgpath_list, 30, 30, "logimg")
    choicename_html_list = make_name_html_list(6, namepath_list, 70, 70)
    logname_html_list = make_name_html_list(6, namepath_list, 30, 30)

    imgcatpath_list = make_imgcat_path(40)
    accept_choice = ["×", "○"]

    correct_cat_list = make_correct_list(6, 10, 4)
    goal_ari = 0.9


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    s_choice0 = models.StringField(initial="99")
    s_choice1 = models.StringField(initial="99")
    s_choice2 = models.StringField(initial="99")
    s_choice3 = models.StringField(initial="99")
    s_choice4 = models.StringField(initial="99")

    accept0 = models.IntegerField(initial=2)
    accept1 = models.IntegerField(initial=2)
    accept2 = models.IntegerField(initial=2)
    accept3 = models.IntegerField(initial=2)
    accept4 = models.IntegerField(initial=2)

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

    kappa = models.FloatField()
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
        "id_in_group", "round_number", "kappa", "ari",
        "accept0", "accept1", "accept2", "accept3", "accept4",
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
            p.id_in_group, p.round_number, p.kappa, p.ari,
            p.accept0, p.accept1, p.accept2, p.accept3, p.accept4, 
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
class Instruction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class ShowRole(Page):
    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            player.participant.loghtml_list =[]
            logstart = "<p>実験開始</p>"
            logbar = "<p>↓↓↓↓↓↓↓↓↓↓</p><br>"
            player.participant.loghtml_list.append(logstart)
            player.participant.loghtml_list.append(logbar)
        return {
            "round_num" : player.round_number,
            "role" : player.role(),
            }


class Speaker(Page):
    form_model = 'player'
    form_fields = [
        "name_order", 
        "box0_children", "box1_children", "box2_children",
        "box3_children", "box4_children", "box5_children",
        "s_choice0", "s_choice1", "s_choice2", "s_choice3", "s_choice4",
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
        player.participant.img_choice = []
        player.participant.showed_imgs = []
        player.participant.showed_imgs4log = []
        box0_defaultimgs = []
        box1_defaultimgs = []
        box2_defaultimgs = []
        box3_defaultimgs = []
        box4_defaultimgs = []
        box5_defaultimgs = []
        default_name_list = []
        for p in range(len(player.participant.default_nameorder)):
                default_name_list.append(Constants.namehtml_list[player.participant.default_nameorder[p]])

        if player.role() == "speaker":
            for id in img_choice:
                player.participant.img_choice.append(id)
                player.participant.showed_imgs.append(Constants.stimuliimg_html_list[id])
                player.participant.showed_imgs4log.append(Constants.logimg_html_list[id])

            if player.participant.box0_items[0] == 999:
                box0_defaultimgs.append("999")
            else:
                for j in range(len(player.participant.box0_items)):
                    box0_defaultimgs.append(Constants.imghtml_list[player.participant.box0_items[j]])
                    
            if player.participant.box1_items[0] == 999:
                box1_defaultimgs.append("999")
            else:
                for k in range(len(player.participant.box1_items)):
                    box1_defaultimgs.append(Constants.imghtml_list[player.participant.box1_items[k]])
        
            if player.participant.box2_items[0] == 999:
                box2_defaultimgs.append("999")
            else:
                for l in range(len(player.participant.box2_items)):
                    box2_defaultimgs.append(Constants.imghtml_list[player.participant.box2_items[l]])
        
            if player.participant.box3_items[0] == 999:
                box3_defaultimgs.append("999")
            else:
                for m in range(len(player.participant.box3_items)):
                    box3_defaultimgs.append(Constants.imghtml_list[player.participant.box3_items[m]])
        
            if player.participant.box4_items[0] == 999:
                box4_defaultimgs.append("999")
            else:
                for n in range(len(player.participant.box4_items)):
                    box4_defaultimgs.append(Constants.imghtml_list[player.participant.box4_items[n]])
        
            if player.participant.box5_items[0] == 999:
                box5_defaultimgs.append("999")
            else:
                for o in range(len(player.participant.box5_items)):
                    box5_defaultimgs.append(Constants.imghtml_list[player.participant.box5_items[o]])
           
        return {
            "showed_imgs" : player.participant.showed_imgs,
            "choice_names" : Constants.choicename_html_list,
            "default_name_list" : default_name_list,
            "box0_defaultimgs" : box0_defaultimgs,
            "box1_defaultimgs" : box1_defaultimgs,
            "box2_defaultimgs" : box2_defaultimgs,
            "box3_defaultimgs" : box3_defaultimgs,
            "box4_defaultimgs" : box4_defaultimgs,
            "box5_defaultimgs" : box5_defaultimgs,
            "img_category_list" : player.participant.img_category_list,
            "loghtml_list" : player.participant.loghtml_list,           
        }
    
    @staticmethod
    def js_vars(player):
        default_name_value = "sym" + str(player.participant.default_nameorder[0]) + "," +\
            "sym" + str(player.participant.default_nameorder[1]) + "," +\
                "sym" + str(player.participant.default_nameorder[2]) + "," +\
                    "sym" + str(player.participant.default_nameorder[3]) + "," +\
                        "sym" + str(player.participant.default_nameorder[4]) + "," +\
                            "sym" + str(player.participant.default_nameorder[5])
        other_player = player.get_others_in_group()[0]
        if player.role() == "speaker":
            img_choice = player.participant.img_choice
        else:
            img_choice = other_player.participant.img_choice

        return dict(
            img_category_list=player.participant.img_category_list,
            imgcatpath_list=Constants.imgcatpath_list,
            default_name_list=player.participant.default_nameorder,
            default_name_value=default_name_value,
            img_choice=img_choice,
            role=player.role(),
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
        for q in range(40):
            player.participant.img_category_list[q] = int(cat_list[q])
        
        player.participant.default_nameorder = []
        n_list = player.name_order.split(",")
        for name in n_list:
            player.participant.default_nameorder.append(int(name[-1]))        
        if player.box0_children == "999":
            player.participant.box0_items = [999,]
        else:
            player.participant.box0_items = []
            player.participant.box0_items = [int(b0i) for b0i in player.box0_children.split(",")]
        if player.box1_children == "999":
            player.participant.box1_items = [999,]
        else:
            player.participant.box1_items = []
            player.participant.box1_items = [int(b1i) for b1i in player.box1_children.split(",")]
        if player.box2_children == "999":
            player.participant.box2_items = [999,]
        else:
            player.participant.box2_items = []
            player.participant.box2_items = [int(b2i) for b2i in player.box2_children.split(",")]
        if player.box3_children == "999":
            player.participant.box3_items = [999,]
        else:
            player.participant.box3_items = []
            player.participant.box3_items = [int(b3i) for b3i in player.box3_children.split(",")]
        if player.box4_children == "999":
            player.participant.box4_items = [999,]
        else:
            player.participant.box4_items = []
            player.participant.box4_items = [int(b4i) for b4i in player.box4_children.split(",")]
        if player.box5_children == "999":
            player.participant.box5_items = [999,]
        else:
            player.participant.box5_items = []
            player.participant.box5_items = [int(b5i) for b5i in player.box5_children.split(",")]

class Debug(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "s_choice0" : player.s_choice0,
            "s_choice1" : player.s_choice1,
            "s_choice2" : player.s_choice2,
            "s_choice3" : player.s_choice3,
            "s_choice4" : player.s_choice4,
            "box0_items" : player.participant.box0_items,
            "box1_items" : player.participant.box1_items,
            "box2_items" : player.participant.box2_items,
            "box3_items" : player.participant.box3_items,
            "box4_items" : player.participant.box4_items,
            "box5_items" : player.participant.box5_items,
            }




class Listener(Page):
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
    def is_displayed(player: Player):
        return player.role() == 'listener'

    @staticmethod
    def vars_for_template(player: Player):
        box0_defaultimgs = []
        box1_defaultimgs = []
        box2_defaultimgs = []
        box3_defaultimgs = []
        box4_defaultimgs = []
        box5_defaultimgs = []
        default_name_list = []
        for p in range(len(player.participant.default_nameorder)):
            default_name_list.append(Constants.namehtml_list[player.participant.default_nameorder[p]])
        if player.role() == "listener":
            other_player = player.get_others_in_group()[0]
            showed_imgs = other_player.participant.showed_imgs

            if player.participant.box0_items[0] == 999:
                box0_defaultimgs.append("999")
            else:
                for j in range(len(player.participant.box0_items)):
                    box0_defaultimgs.append(Constants.imghtml_list[player.participant.box0_items[j]])
        
            
            if player.participant.box1_items[0] == 999:
                box1_defaultimgs.append("999")
            else:
                for k in range(len(player.participant.box1_items)):
                    box1_defaultimgs.append(Constants.imghtml_list[player.participant.box1_items[k]])
        
            if player.participant.box2_items[0] == 999:
                box2_defaultimgs.append("999")
            else:
                for l in range(len(player.participant.box2_items)):
                    box2_defaultimgs.append(Constants.imghtml_list[player.participant.box2_items[l]])
        
            if player.participant.box3_items[0] == 999:
                box3_defaultimgs.append("999")
            else:
                for m in range(len(player.participant.box3_items)):
                    box3_defaultimgs.append(Constants.imghtml_list[player.participant.box3_items[m]])
        
            if player.participant.box4_items[0] == 999:
                box4_defaultimgs.append("999")
            else:
                for n in range(len(player.participant.box4_items)):
                    box4_defaultimgs.append(Constants.imghtml_list[player.participant.box4_items[n]])
        
            if player.participant.box5_items[0] == 999:
                box5_defaultimgs.append("999")
            else:
                for o in range(len(player.participant.box5_items)):
                    box5_defaultimgs.append(Constants.imghtml_list[player.participant.box5_items[o]])

            others_choice_list = [
                Constants.choicename_html_list[int(other_player.s_choice0)],
                Constants.choicename_html_list[int(other_player.s_choice1)],
                Constants.choicename_html_list[int(other_player.s_choice2)],
                Constants.choicename_html_list[int(other_player.s_choice3)],
                Constants.choicename_html_list[int(other_player.s_choice4)],
            ]
        else:
            showed_imgs = player.participant.showed_imgs
            others_choice_list = [
                Constants.choicename_html_list[int(player.s_choice0)],
                Constants.choicename_html_list[int(player.s_choice1)],
                Constants.choicename_html_list[int(player.s_choice2)],
                Constants.choicename_html_list[int(player.s_choice3)],
                Constants.choicename_html_list[int(player.s_choice4)],
            ]
        
        return {
            "showed_imgs" : showed_imgs,
            "others_choice_list" : others_choice_list,
            "default_name_list" : default_name_list,
            "box0_defaultimgs" : box0_defaultimgs,
            "box1_defaultimgs" : box1_defaultimgs,
            "box2_defaultimgs" : box2_defaultimgs,
            "box3_defaultimgs" : box3_defaultimgs,
            "box4_defaultimgs" : box4_defaultimgs,
            "box5_defaultimgs" : box5_defaultimgs,
            "img_category_list" : player.participant.img_category_list,
            "loghtml_list" : player.participant.loghtml_list,            
        }
    
    @staticmethod
    def js_vars(player):
        default_name_value = "sym" + str(player.participant.default_nameorder[0]) + "," +\
            "sym" + str(player.participant.default_nameorder[1]) + "," +\
                "sym" + str(player.participant.default_nameorder[2]) + "," +\
                    "sym" + str(player.participant.default_nameorder[3]) + "," +\
                        "sym" + str(player.participant.default_nameorder[4]) + "," +\
                            "sym" + str(player.participant.default_nameorder[5])

        other_player = player.get_others_in_group()[0]
        if player.role() == "listener":
            img_choice = other_player.participant.img_choice
        else:
            img_choice = player.participant.img_choice

        return dict(
            img_category_list=player.participant.img_category_list,
            imgcatpath_list=Constants.imgcatpath_list,
            default_name_list=player.participant.default_nameorder,
            default_name_value=default_name_value,
            img_choice=img_choice,
            role=player.role(),
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
        for q in range(40):
            player.participant.img_category_list[q] = int(cat_list[q])

        other_player = player.get_others_in_group()[0]
        if player.participant.img_category_list[other_player.participant.img_choice[0]] == int(other_player.s_choice0):
            player.accept0 = 1
        else:
            player.accept0 = 0
        if player.participant.img_category_list[other_player.participant.img_choice[1]] == int(other_player.s_choice1):
            player.accept1 = 1
        else:
            player.accept1 = 0
        if player.participant.img_category_list[other_player.participant.img_choice[2]] == int(other_player.s_choice2):
            player.accept2 = 1
        else:
            player.accept2 = 0
        if player.participant.img_category_list[other_player.participant.img_choice[3]] == int(other_player.s_choice3):
            player.accept3 = 1
        else:
            player.accept3 = 0
        if player.participant.img_category_list[other_player.participant.img_choice[4]] == int(other_player.s_choice4):
            player.accept4 = 1
        else:
            player.accept4 = 0

        player.participant.default_nameorder = []
        n_list = player.name_order.split(",")
        for name in n_list:
            player.participant.default_nameorder.append(int(name[-1]))        
        if player.box0_children == "999":
            player.participant.box0_items = [999,]
        else:
            player.participant.box0_items = []
            player.participant.box0_items = [int(b0i) for b0i in player.box0_children.split(",")]
        if player.box1_children == "999":
            player.participant.box1_items = [999,]
        else:
            player.participant.box1_items = []
            player.participant.box1_items = [int(b1i) for b1i in player.box1_children.split(",")]
        if player.box2_children == "999":
            player.participant.box2_items = [999,]
        else:
            player.participant.box2_items = []
            player.participant.box2_items = [int(b2i) for b2i in player.box2_children.split(",")]
        if player.box3_children == "999":
            player.participant.box3_items = [999,]
        else:
            player.participant.box3_items = []
            player.participant.box3_items = [int(b3i) for b3i in player.box3_children.split(",")]
        if player.box4_children == "999":
            player.participant.box4_items = [999,]
        else:
            player.participant.box4_items = []
            player.participant.box4_items = [int(b4i) for b4i in player.box4_children.split(",")]
        if player.box5_children == "999":
            player.participant.box5_items = [999,]
        else:
            player.participant.box5_items = []
            player.participant.box5_items = [int(b5i) for b5i in player.box5_children.split(",")]


class WaitForSpeaker(WaitPage):
    titel_text = "「話し手」の入力を待っています"
    body_text = "あなたは「聞き手」です。「話し手」の入力をお待ち下さい。"
    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'listener'


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            other_player = player.get_others_in_group()[0]
            player.kappa = max(
                cohen_kappa_score(cl, player.participant.img_category_list) for cl in Constants.correct_cat_list
                )
            player.ari = adjusted_rand_score(
                group.get_players()[0].participant.img_category_list,
                group.get_players()[1].participant.img_category_list
            )
            loghead = "<p>ラウンド{}</p>".format(player.round_number)
            log1 = "<p>表示された画像（左から順に1,2,3,4,5番）：</p>"
            log_divhead = "<div style=\"display: flex;\">"
            log_divtail = "</div>"
            logtail = "<p>------------------------------------------------------------</p><br>"
            if player.role() == 'speaker':
                log0 = "<p>あなたの役割：「話し手」</p>"
                imgs_this_round = player.participant.showed_imgs4log
                log2 = "<p>あなたの選んだ記号（左から順に1,2,3,4,5番に対する記号）：</p>"
                log3 = "<p>相手がその記号を受け入れたかどうか（左から順に1,2,3,4,5番への答え）：</p>"
                log4 = "<p>{}, {}, {}, {}, {}<\p><br><br><br>".format(
                    Constants.accept_choice[other_player.accept0],
                    Constants.accept_choice[other_player.accept1],
                    Constants.accept_choice[other_player.accept2],
                    Constants.accept_choice[other_player.accept3],
                    Constants.accept_choice[other_player.accept4],
                    )
                player.participant.loghtml_list.append(loghead)
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
                player.participant.loghtml_list.append(logtail)
            else:
                log0 = "<p>あなたの役割：「聞き手」</p>"
                imgs_this_round = other_player.participant.showed_imgs4log
                log2 = "<p>相手の選んだ記号（左から順に1,2,3,4,5番に対する記号）：</p>"
                log3 = "<p>あなたがその記号を受け入れたかどうか（左から順に1,2,3,4,5番への答え）：</p>"
                log4 = "<p>{}, {}, {}, {}, {}<\p>".format(
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
                player.participant.loghtml_list.append(Constants.logname_html_list[int(other_player.s_choice0)])
                player.participant.loghtml_list.append(Constants.logname_html_list[int(other_player.s_choice1)])
                player.participant.loghtml_list.append(Constants.logname_html_list[int(other_player.s_choice2)])
                player.participant.loghtml_list.append(Constants.logname_html_list[int(other_player.s_choice3)])
                player.participant.loghtml_list.append(Constants.logname_html_list[int(other_player.s_choice4)])
                player.participant.loghtml_list.append(log_divtail)
                player.participant.loghtml_list.append(log3)
                player.participant.loghtml_list.append(log4)
                player.participant.loghtml_list.append(logtail)


class EndOfRound(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            "round_num" : player.round_number,
            "kappa" : player.kappa,
            "ari" : player.ari,
            "loghtml_list" : player.participant.loghtml_list,
            "box0_items" : player.participant.box0_items,
            "box1_items" : player.participant.box1_items,
            "box2_items" : player.participant.box2_items,
            "box3_items" : player.participant.box3_items,
            "box4_items" : player.participant.box4_items,
            "box5_items" : player.participant.box5_items,
        }


class EarlyFinish(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.ari >= Constants.goal_ari
    
    @staticmethod
    def vars_for_template(player: Player):
        player.participant.final_round_num = player.round_number
        player.participant.final_kappa = player.kappa
        player.participant.final_ari = player.ari
        return {"loghtml_list" : player.participant.loghtml_list,}
    
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if player.ari >= Constants.goal_ari:
            return upcoming_apps[0]


class LateFinish(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    
    @staticmethod
    def vars_for_template(player: Player):
        player.participant.final_round_num = player.round_number
        player.participant.final_kappa = player.kappa
        player.participant.final_ari = player.ari
        return {"loghtml_list" : player.participant.loghtml_list,}
    
    def app_after_this_page(player, upcoming_apps):
        return upcoming_apps[0]


page_sequence = [
    Instruction,
    ShowRole,
    Speaker,
    WaitForSpeaker,
    Debug,
    Listener,
    ResultsWaitPage,
    EndOfRound,
    EarlyFinish,
    LateFinish,
    ]
