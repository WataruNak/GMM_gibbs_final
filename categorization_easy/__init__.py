from otree.api import *
import random
from sklearn.metrics import cohen_kappa_score, adjusted_rand_score
import itertools

doc = """
This is an "Easy" level test.
https://qiita.com/naoki-funawatari/items/c78630b85f5f7fe21d19 drag_and_drop
https://www.otreehub.com/projects/otree-snippets/ otree sortable_example
https://qiita.com/AVELWP/items/536c797a63c081cf7bc0 sortable document ja
https://github.com/SortableJS/Sortable sortable git
https://qiita.com/t-iguchi/items/20dc31d5e004d7145634 js in django
git push -u origin main or heroku main
heroku create app-name
heroku addons:create heroku-postgresql:hobby-dev
heroku run otree resetdb

draggable_name : false
"""

def make_imgcat_path(num):
    imgcatpath_list = []
    for _ in range(num):
        imgcatpath_list.append("img{}_cat".format(_))
    return imgcatpath_list

def make_correct_list(item_num_list):
    correct_lists = []
    for ln in range(3):
        for _ in range(item_num_list[ln]):
            correct_lists.append(ln)
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
            "<li draggable=\"false\" id=\"name{}\" data-id=\"sym{}\"><img src=\"{}\" height=\"{}px\" width=\"{}px\"></li>".format(
                db, db, path_list[db], height, width)
        )
    return img_html_list


class Constants(BaseConstants):
    name_in_url = 'categorization_easy'
    players_per_group = None
    num_rounds = 30
    imgpath_list = [
        "https://imgur.com/ZZzLzPi.jpg","https://imgur.com/dvXxCel.jpg","https://imgur.com/icA4YgN.jpg","https://imgur.com/54CnHrG.jpg",
        "https://imgur.com/4B0vzv1.jpg","https://imgur.com/DgifDgs.jpg","https://imgur.com/8VZJBiq.jpg","https://imgur.com/F8V4XM6.jpg",
        "https://imgur.com/i2OwITT.jpg","https://imgur.com/BfYgkFZ.jpg",
        "https://imgur.com/ZcPHQV1.jpg","https://imgur.com/MPsWg32.jpg","https://imgur.com/qZXRbyM.jpg","https://imgur.com/pdWD2ah.jpg",
        "https://imgur.com/0cD8UPF.jpg","https://imgur.com/agMr7gt.jpg","https://imgur.com/V7n1vcD.jpg","https://imgur.com/cd3sVrx.jpg",
        "https://imgur.com/czNAM1L.jpg","https://imgur.com/4cgc2rK.jpg",
        "https://imgur.com/7VWclM5.jpg","https://imgur.com/ZT9llfe.jpg","https://imgur.com/9s7WbZX.jpg","https://imgur.com/n1FFbbS.jpg",
        "https://imgur.com/MqS4s6L.jpg","https://imgur.com/K2r0jrv.jpg","https://imgur.com/yl49vYJ.jpg","https://imgur.com/yXwWV9M.jpg",
        "https://imgur.com/BvLXAoO.jpg","https://imgur.com/uDQDTOG.jpg"
        ]

    namepath_list = [
    "https://imgur.com/a2Q74iy.png","https://imgur.com/k9q8sBE.png","https://imgur.com/GWYaBNN.png",
    ]
    
    imgcatpath_list = make_imgcat_path(num_rounds)
    imghtml_list = make_draggableimg_html_list(num_rounds, imgpath_list, 50, 50)
    namehtml_list = make_draggablename_html_list(3, namepath_list, 100, 100)
    
    correct_cat_list = make_correct_list([10, 10, 10])

"""
mean = [[70, 190], [70, 110], [150, 110]]
cov = [
    [[256, 0], [0, 256]],
    [[256, 0], [0, 256]],
    [[256, 0], [0, 256]],
    ]

new_dataset = [
        "https://imgur.com/ZZzLzPi.jpg","https://imgur.com/dvXxCel.jpg","https://imgur.com/icA4YgN.jpg","https://imgur.com/54CnHrG.jpg",
        "https://imgur.com/4B0vzv1.jpg","https://imgur.com/DgifDgs.jpg","https://imgur.com/8VZJBiq.jpg","https://imgur.com/F8V4XM6.jpg",
        "https://imgur.com/i2OwITT.jpg","https://imgur.com/BfYgkFZ.jpg",
        "https://imgur.com/ZcPHQV1.jpg","https://imgur.com/MPsWg32.jpg","https://imgur.com/qZXRbyM.jpg","https://imgur.com/pdWD2ah.jpg",
        "https://imgur.com/0cD8UPF.jpg","https://imgur.com/agMr7gt.jpg","https://imgur.com/V7n1vcD.jpg","https://imgur.com/cd3sVrx.jpg",
        "https://imgur.com/czNAM1L.jpg","https://imgur.com/4cgc2rK.jpg",
        "https://imgur.com/7VWclM5.jpg","https://imgur.com/ZT9llfe.jpg","https://imgur.com/9s7WbZX.jpg","https://imgur.com/n1FFbbS.jpg",
        "https://imgur.com/MqS4s6L.jpg","https://imgur.com/K2r0jrv.jpg","https://imgur.com/yl49vYJ.jpg","https://imgur.com/yXwWV9M.jpg",
        "https://imgur.com/BvLXAoO.jpg","https://imgur.com/uDQDTOG.jpg"
        ]

circle = [
    "https://imgur.com/2v96Nsz.jpg","https://imgur.com/o00ZR5n.jpg","https://imgur.com/gN8wVFP.jpg","https://imgur.com/CFnriY9.jpg",
    "https://imgur.com/eOykFKN.jpg","https://imgur.com/v7CrjSU.jpg","https://imgur.com/RWQm2rR.jpg","https://imgur.com/UrHdEWO.jpg",
    "https://imgur.com/UrHdEWO.jpg","https://imgur.com/9iu6bEv.jpg",
    "https://imgur.com/oFhKVpB.jpg","https://imgur.com/RhjO157.jpg","https://imgur.com/AU809mF.jpg","https://imgur.com/NgkPdaz.jpg",
    "https://imgur.com/h5E1W8L.jpg","https://imgur.com/cS75xgN.jpg","https://imgur.com/795sB1f.jpg","https://imgur.com/dZAsMeP.jpg",
    "https://imgur.com/46uFVaN.jpg","https://imgur.com/8053M8w.jpg",
    "https://imgur.com/FSbrUrq.jpg","https://imgur.com/Cdo4t1e.jpg","https://imgur.com/IZr4MNc.jpg","https://imgur.com/Q1GUep3.jpg",
    "https://imgur.com/Jv5lEGD.jpg","https://imgur.com/Uu39IuD.jpg","https://imgur.com/m3CosMY.jpg","https://imgur.com/NoMBW1m.jpg",
    "https://imgur.com/o6xLXDK.jpg","https://imgur.com/EFR9FgA.jpg"
    ]

level2 = [
    "https://imgur.com/PL0CoPZ.jpg","https://imgur.com/foh6Ibq.jpg","https://imgur.com/BjD5uEp.jpg","https://imgur.com/z5FTEN3.jpg",
    "https://imgur.com/RZRUxrT.jpg","https://imgur.com/izXDHXX.jpg","https://imgur.com/dsAQraw.jpg","https://imgur.com/qdzH3Vg.jpg",
    "https://imgur.com/fFuUJ4v.jpg","https://imgur.com/7vbSeWK.jpg",
    "https://imgur.com/Sc1Lv0t.jpg","https://imgur.com/m1R1YSU.jpg","https://imgur.com/6PB8fed.jpg","https://imgur.com/9xCx3sn.jpg",
    "https://imgur.com/55kIIjk.jpg","https://imgur.com/dXOW7el.jpg","https://imgur.com/ZLtz0Fx.jpg","https://imgur.com/W32mzJj.jpg",
    "https://imgur.com/WzJCz4p.jpg","https://imgur.com/XeRy4wv.jpg",
    "https://imgur.com/JZYPEOl.jpg","https://imgur.com/rYBg9Cx.jpg","https://imgur.com/2TIu1Q7.jpg","https://imgur.com/6GH1yve.jpg",
    "https://imgur.com/u7So8Jt.jpg","https://imgur.com/MZpbYY8.jpg","https://imgur.com/1bwVxIx.jpg","https://imgur.com/lH8u5LI.jpg",
    "https://imgur.com/yRlUQR9.jpg","https://imgur.com/xAkNIXr.jpg"
    ]

easy_id_list = [10,11,27,14,15,0,3,6,16,17,19,1,8,7,25,24,26,18,2,4,20,22,9,28,29,13,21,5,23,12]
circle_id_list = [10,11,27,14,15,0,3,6,16,17,19,1,8,7,25,24,26,18,2,4,20,22,9,28,29,13,21,5,23,12]
level2_id_list = [12,22,26,17,10,7,5,2,24,21,3,4,15,11,6,0,25,29,27,1,9,8,28,20,23,14,19,16,18,13]

"""


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

    box0_children = models.StringField(default="999")
    box1_children = models.StringField(default="999")
    box2_children = models.StringField(default="999")

    c_ari = models.FloatField()
    count = models.IntegerField(initial=0)


def custom_export(players):
    yield [
        "session", "participant_code", "started_time", "c_ari", "e_count",
        "img0_cat", "img1_cat", "img2_cat", "img3_cat", "img4_cat",
        "img5_cat", "img6_cat", "img7_cat", "img8_cat", "img9_cat",
        "img10_cat", "img11_cat", "img12_cat", "img13_cat", "img14_cat",
        "img15_cat", "img16_cat", "img17_cat", "img18_cat", "img19_cat",
        "img20_cat", "img21_cat", "img22_cat", "img23_cat", "img24_cat",
        "img25_cat", "img26_cat", "img27_cat", "img28_cat", "img29_cat",
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code, participant.code, participant.time_started_utc, p.c_ari, participant.e_count,
            p.img0_cat, p.img1_cat, p.img2_cat, p.img3_cat, p.img4_cat,
            p.img5_cat, p.img6_cat, p.img7_cat, p.img8_cat, p.img9_cat,
            p.img10_cat, p.img11_cat, p.img12_cat, p.img13_cat, p.img14_cat,
            p.img15_cat, p.img16_cat, p.img17_cat, p.img18_cat, p.img19_cat,
            p.img20_cat, p.img21_cat, p.img22_cat, p.img23_cat, p.img24_cat,
            p.img25_cat, p.img26_cat, p.img27_cat, p.img28_cat, p.img29_cat,
            ]

# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Categorize(Page):
    form_model = 'player'
    form_fields = [
        "name_order", "count",
        "box0_children", "box1_children", "box2_children",
        "img0_cat", "img1_cat", "img2_cat", "img3_cat", "img4_cat",
        "img5_cat", "img6_cat", "img7_cat", "img8_cat", "img9_cat",
        "img10_cat", "img11_cat", "img12_cat", "img13_cat", "img14_cat",
        "img15_cat", "img16_cat", "img17_cat", "img18_cat", "img19_cat",
        "img20_cat", "img21_cat", "img22_cat", "img23_cat", "img24_cat",
        "img25_cat", "img26_cat", "img27_cat", "img28_cat", "img29_cat",
    ]

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            player.participant.e_stimuli_id_list = [10,11,27,14,15,0,3,6,16,17,19,1,8,7,25,24,26,18,2,4,20,22,9,28,29,13,21,5,23,12]
            player.participant.e_imghtml_order = []
            for j in range(Constants.num_rounds):
                player.participant.e_imghtml_order.append(Constants.imghtml_list[player.participant.e_stimuli_id_list[j]])
            player.participant.e_box0_items = [999]
            player.participant.e_box1_items = [999]
            player.participant.e_box2_items = [999]
            player.participant.e_default_nameorder = [0,1,2]
            player.participant.e_img_category_list = []
            for _ in range(Constants.num_rounds):
                player.participant.e_img_category_list.append(99)
            player.participant.e_count = 0
        
        showed_img = player.participant.e_imghtml_order[player.round_number-1]

        box0_defaultimgs = []
        box1_defaultimgs = []
        box2_defaultimgs = []
        if player.participant.e_box0_items[0] == 999:
            box0_defaultimgs.append("999")
        else:
            for j in range(len(player.participant.e_box0_items)):
                box0_defaultimgs.append(Constants.imghtml_list[player.participant.e_box0_items[j]])
                    
        if player.participant.e_box1_items[0] == 999:
            box1_defaultimgs.append("999")
        else:
            for k in range(len(player.participant.e_box1_items)):
                box1_defaultimgs.append(Constants.imghtml_list[player.participant.e_box1_items[k]])
        
        if player.participant.e_box2_items[0] == 999:
            box2_defaultimgs.append("999")
        else:
            for l in range(len(player.participant.e_box2_items)):
                box2_defaultimgs.append(Constants.imghtml_list[player.participant.e_box2_items[l]])

        default_name_list = []
        for p in range(len(player.participant.e_default_nameorder)):
                default_name_list.append(Constants.namehtml_list[player.participant.e_default_nameorder[p]])

        return {
            "showed_img" : showed_img,
            "round_num" : player.round_number,
            "name_order" : player.name_order,
            "imghtml_order" : player.participant.e_imghtml_order,
            "default_name_list" : default_name_list,
            "box0_defaultimgs" : box0_defaultimgs,
            "box1_defaultimgs" : box1_defaultimgs,
            "box2_defaultimgs" : box2_defaultimgs,
            "count" : player.participant.e_count
        }
    
    @staticmethod
    def js_vars(player):
        default_name_value = "sym" + str(player.participant.e_default_nameorder[0]) + "," +\
            "sym" + str(player.participant.e_default_nameorder[1]) + "," +\
                "sym" + str(player.participant.e_default_nameorder[2])
        return dict(
            num_rounds=Constants.num_rounds,
            this_roundnum = player.round_number,
            id_order=player.participant.e_stimuli_id_list,
            showed_img_id=player.participant.e_stimuli_id_list[player.round_number-1],
            default_name_value=default_name_value,
            imgcatpath_list=Constants.imgcatpath_list,
            img_category_list=player.participant.e_img_category_list,
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
        ]

        player.participant.e_img_category_list = []
        for imc in cat_list:
            player.participant.e_img_category_list.append(int(imc))
        player.participant.e_default_nameorder = []
        n_list = player.name_order.split(",")
        for name in n_list:
            player.participant.e_default_nameorder.append(int(name[-1]))
      
        if player.box0_children == "999":
            player.participant.e_box0_items = [999,]
        else:
            player.participant.e_box0_items = [int(b0i) for b0i in player.box0_children.split(",")]

        if player.box1_children == "999":
           player.participant.e_box1_items = [999,]
        else:
            player.participant.e_box1_items = [int(b1i) for b1i in player.box1_children.split(",")]
        
        if player.box2_children == "999":
            player.participant.e_box2_items = [999,]
        else:
            player.participant.e_box2_items = [int(b2i) for b2i in player.box2_children.split(",")]
        
        player.participant.e_count += player.count


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        player.c_ari = adjusted_rand_score(Constants.correct_cat_list, player.participant.e_img_category_list)
        player.participant.e_ari = player.c_ari
        score = int(player.c_ari * 100)
        return {
            "c_ari" : player.c_ari,
            "score" : score,
            "name_order" : player.name_order,
            "cats" : player.participant.e_img_category_list,
            "box0_children" : player.box0_children,
            "box1_children" : player.box1_children,
            "box2_children" : player.box2_children,
            "box0_items" : player.participant.e_box0_items,
            "box1_items" : player.participant.e_box1_items,
            "box2_items" : player.participant.e_box2_items,
        }


page_sequence = [
    Introduction,
    Categorize,
    Results
    ]
