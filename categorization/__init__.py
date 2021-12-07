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

def make_imgcat_path(num):
    imgcatpath_list = []
    for _ in range(num):
        imgcatpath_list.append("img{}_cat".format(_))
    return imgcatpath_list

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
            "<img src = \"{}\" class=\"item\" draggable=\"true\" id=\"{}\" height=\"{}px\" width=\"{}px\">".format(path_list[da], da, height, width)
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
    num_rounds = 60
    imgpath_list = [
        "https://imgur.com/c27avQk.jpg","https://imgur.com/WWwUJ3H.jpg","https://imgur.com/smEbdXU.jpg","https://imgur.com/BIBHIx8.jpg",
        "https://imgur.com/8dUYe80.jpg","https://imgur.com/WQb3adx.jpg","https://imgur.com/4YoAZKD.jpg","https://imgur.com/FK3nedQ.jpg",
        "https://imgur.com/UXUe1P5.jpg","https://imgur.com/YF7pyfv.jpg","https://imgur.com/pI7e19V.jpg","https://imgur.com/wQQS0vp.jpg",
        "https://imgur.com/2mzG1Z4.jpg","https://imgur.com/wBlXTXe.jpg","https://imgur.com/yRvUFc2.jpg","https://imgur.com/QnTabih.jpg",
        "https://imgur.com/P0lS9Rt.jpg","https://imgur.com/5Tq3F9y.jpg","https://imgur.com/uVbdt9m.jpg","https://imgur.com/0vcyIVT.jpg",
        "https://imgur.com/RdnKdk7.jpg","https://imgur.com/DnQ5V0i.jpg","https://imgur.com/CaMFEft.jpg","https://imgur.com/PdlK46v.jpg",
        "https://imgur.com/fd3wsHj.jpg","https://imgur.com/v8o0KXI.jpg","https://imgur.com/GPuAaQK.jpg","https://imgur.com/h01dH1M.jpg",
        "https://imgur.com/Lyo5oHo.jpg","https://imgur.com/0oIZVUQ.jpg","https://imgur.com/CRafgcZ.jpg","https://imgur.com/wzorH2u.jpg",
        "https://imgur.com/xMpP47O.jpg","https://imgur.com/IdmTxuR.jpg","https://imgur.com/irNZoWH.jpg","https://imgur.com/ramZYq9.jpg",
        "https://imgur.com/A5BIv1n.jpg","https://imgur.com/fJqy1Vw.jpg","https://imgur.com/2dLFQW5.jpg","https://imgur.com/60A8YR8.jpg",
        "https://imgur.com/TTLMf8j.jpg","https://imgur.com/eSdxiLg.jpg","https://imgur.com/u4digfM.jpg","https://imgur.com/FJ5W1oN.jpg",
        "https://imgur.com/45sKDoN.jpg","https://imgur.com/XC4Z4bB.jpg","https://imgur.com/3efZBys.jpg","https://imgur.com/Ee7SzDc.jpg",
        "https://imgur.com/5I6U5br.jpg","https://imgur.com/OmKIiqk.jpg","https://imgur.com/q4z3OLw.jpg","https://imgur.com/FICZpGt.jpg",
        "https://imgur.com/x16qbtH.jpg","https://imgur.com/7xn4I0i.jpg","https://imgur.com/yUYU300.jpg","https://imgur.com/4tY7w92.jpg",
        "https://imgur.com/mqFMhzF.jpg","https://imgur.com/U16Jxoc.jpg","https://imgur.com/NPVutC3.jpg","https://imgur.com/c033ge1.jpg"
        ]

    namepath_list = [
    "https://imgur.com/a2Q74iy.png","https://imgur.com/k9q8sBE.png","https://imgur.com/GWYaBNN.png",
    ]
    
    imgcatpath_list = make_imgcat_path(60)
    imghtml_list = make_draggableimg_html_list(60, imgpath_list, 50, 50)
    namehtml_list = make_draggablename_html_list(3, namepath_list, 100, 100)
    
    correct_cat_list = make_correct_list(3, 20, 3)
    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    name_order = models.StringField(initial="sym0,sym1,sym2")
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
    img40_cat = models.StringField(initial="99")
    img41_cat = models.StringField(initial="99")
    img42_cat = models.StringField(initial="99")
    img43_cat = models.StringField(initial="99")
    img44_cat = models.StringField(initial="99")
    img45_cat = models.StringField(initial="99")
    img46_cat = models.StringField(initial="99")
    img47_cat = models.StringField(initial="99")
    img48_cat = models.StringField(initial="99")
    img49_cat = models.StringField(initial="99")
    img50_cat = models.StringField(initial="99")
    img51_cat = models.StringField(initial="99")
    img52_cat = models.StringField(initial="99")
    img53_cat = models.StringField(initial="99")
    img54_cat = models.StringField(initial="99")
    img55_cat = models.StringField(initial="99")
    img56_cat = models.StringField(initial="99")
    img57_cat = models.StringField(initial="99")
    img58_cat = models.StringField(initial="99")
    img59_cat = models.StringField(initial="99")

    box0_children = models.StringField(default="999")
    box1_children = models.StringField(default="999")
    box2_children = models.StringField(default="999")

    c_kappa = models.FloatField()


def custom_export(players):
    yield [
        "session",
        "participant_code",
        "id_in_group", "c_kappa", "ip_kappa", "ari",
        "img0_cat", "img1_cat", "img2_cat", "img3_cat", "img4_cat",
        "img5_cat", "img6_cat", "img7_cat", "img8_cat", "img9_cat",
        "img10_cat", "img11_cat", "img12_cat", "img13_cat", "img14_cat",
        "img15_cat", "img16_cat", "img17_cat", "img18_cat", "img19_cat",
        "img20_cat", "img21_cat", "img22_cat", "img23_cat", "img24_cat",
        "img25_cat", "img26_cat", "img27_cat", "img28_cat", "img29_cat",
        "img30_cat", "img31_cat", "img32_cat", "img33_cat", "img34_cat",
        "img35_cat", "img36_cat", "img37_cat", "img38_cat", "img39_cat",
        "img40_cat", "img41_cat", "img42_cat", "img43_cat", "img44_cat",
        "img45_cat", "img46_cat", "img47_cat", "img48_cat", "img49_cat",
        "img50_cat", "img51_cat", "img52_cat", "img53_cat", "img54_cat",
        "img55_cat", "img56_cat", "img57_cat", "img58_cat", "img59_cat",
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code,
            p.id_in_group, p.c_kappa, p.ip_kappa, p.ari,
            p.img0_cat, p.img1_cat, p.img2_cat, p.img3_cat, p.img4_cat,
            p.img5_cat, p.img6_cat, p.img7_cat, p.img8_cat, p.img9_cat,
            p.img10_cat, p.img11_cat, p.img12_cat, p.img13_cat, p.img14_cat,
            p.img15_cat, p.img16_cat, p.img17_cat, p.img18_cat, p.img19_cat,
            p.img20_cat, p.img21_cat, p.img22_cat, p.img23_cat, p.img24_cat,
            p.img25_cat, p.img26_cat, p.img27_cat, p.img28_cat, p.img29_cat,
            p.img30_cat, p.img31_cat, p.img32_cat, p.img33_cat, p.img34_cat,
            p.img35_cat, p.img36_cat, p.img37_cat, p.img38_cat, p.img39_cat,
            p.img40_cat, p.img41_cat, p.img42_cat, p.img43_cat, p.img44_cat,
            p.img45_cat, p.img46_cat, p.img47_cat, p.img48_cat, p.img49_cat,
            p.img50_cat, p.img51_cat, p.img52_cat, p.img53_cat, p.img54_cat,
            p.img55_cat, p.img56_cat, p.img57_cat, p.img58_cat, p.img59_cat,
            ]

# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class ddtest(Page):
    pass

class Categorize(Page):
    form_model = 'player'
    form_fields = [
        "name_order", 
        "box0_children", "box1_children", "box2_children",
        "img0_cat", "img1_cat", "img2_cat", "img3_cat", "img4_cat",
        "img5_cat", "img6_cat", "img7_cat", "img8_cat", "img9_cat",
        "img10_cat", "img11_cat", "img12_cat", "img13_cat", "img14_cat",
        "img15_cat", "img16_cat", "img17_cat", "img18_cat", "img19_cat",
        "img20_cat", "img21_cat", "img22_cat", "img23_cat", "img24_cat",
        "img25_cat", "img26_cat", "img27_cat", "img28_cat", "img29_cat",
        "img30_cat", "img31_cat", "img32_cat", "img33_cat", "img34_cat",
        "img35_cat", "img36_cat", "img37_cat", "img38_cat", "img39_cat",
        "img40_cat", "img41_cat", "img42_cat", "img43_cat", "img44_cat",
        "img45_cat", "img46_cat", "img47_cat", "img48_cat", "img49_cat",
        "img50_cat", "img51_cat", "img52_cat", "img53_cat", "img54_cat",
        "img55_cat", "img56_cat", "img57_cat", "img58_cat", "img59_cat",
    ]

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            player.participant.stimuli_id_list = []
            player.participant.imghtml_order = []
            for n in range(60):
                player.participant.stimuli_id_list.append(n)
            random.shuffle(player.participant.stimuli_id_list)
            for j in range(60):
                player.participant.imghtml_order.append(Constants.imghtml_list[player.participant.stimuli_id_list[j]])
            player.participant.box0_items = [999]
            player.participant.box1_items = [999]
            player.participant.box2_items = [999]
            player.participant.default_nameorder = [0,1,2]
            player.participant.img_category_list = []
            for _ in range(60):
                player.participant.img_category_list.append(99)
        
        showed_img = player.participant.imghtml_order[player.round_number-1]

        box0_defaultimgs = []
        box1_defaultimgs = []
        box2_defaultimgs = []
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

        default_name_list = []
        for p in range(len(player.participant.default_nameorder)):
                default_name_list.append(Constants.namehtml_list[player.participant.default_nameorder[p]])

        return {
            "showed_img" : showed_img,
            "name_order" : player.name_order,
            "imghtml_order" : player.participant.imghtml_order,
            "default_name_list" : default_name_list,
            "box0_defaultimgs" : box0_defaultimgs,
            "box1_defaultimgs" : box1_defaultimgs,
            "box2_defaultimgs" : box2_defaultimgs,
        }
    
    @staticmethod
    def js_vars(player):
        default_name_value = "sym" + str(player.participant.default_nameorder[0]) + "," +\
            "sym" + str(player.participant.default_nameorder[1]) + "," +\
                "sym" + str(player.participant.default_nameorder[2])
        return dict(
            id_order=player.participant.stimuli_id_list,
            showed_img_id=player.participant.stimuli_id_list[player.round_number-1],
            default_name_value=default_name_value,
            imgcatpath_list=Constants.imgcatpath_list,
            img_category_list=player.participant.img_category_list,
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
            player.img40_cat, player.img41_cat, player.img42_cat, player.img43_cat, player.img44_cat,
            player.img45_cat, player.img46_cat, player.img47_cat, player.img48_cat, player.img49_cat,
            player.img50_cat, player.img51_cat, player.img52_cat, player.img53_cat, player.img54_cat,
            player.img55_cat, player.img56_cat, player.img57_cat, player.img58_cat, player.img59_cat,
        ]

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
            player.participant.box0_items = [int(b0i) for b0i in player.box0_children.split(",")]

        if player.box1_children == "999":
           player.participant.box1_items = [999,]
        else:
            player.participant.box1_items = [int(b1i) for b1i in player.box1_children.split(",")]
        
        if player.box2_children == "999":
            player.participant.box2_items = [999,]
        else:
            player.participant.box2_items = [int(b2i) for b2i in player.box2_children.split(",")]


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        player.c_kappa = max(
            cohen_kappa_score(cl, player.participant.img_category_list) for cl in Constants.correct_cat_list
            )
        return {
            "c_kappa" : player.c_kappa,
            "name_order" : player.name_order,
            "cats" : player.participant.img_category_list,
            "box0_children" : player.box0_children,
            "box1_children" : player.box1_children,
            "box2_children" : player.box2_children,
            "box0_items" : player.participant.box0_items,
            "box1_items" : player.participant.box1_items,
            "box2_items" : player.participant.box2_items,
        }


page_sequence = [
    Introduction,
    Instruction,
    Categorize,
    Results
    ]
