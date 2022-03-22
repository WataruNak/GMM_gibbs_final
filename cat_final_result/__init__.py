from otree.api import *


doc = """
Your app description
"""

def make_html_list(img_num, path_list, height, width):
    img_html_list = []
    for a in range(img_num):
        img_html_list.append(
            "<img src=\"{}\" draggable=\"false\" height=\"{}px\" width=\"{}px\">".format(path_list[a], height, width)
        )
    return img_html_list


class Constants(BaseConstants):
    name_in_url = 'cat_final_result'
    players_per_group = None
    num_rounds = 1
    easy_dataset = [
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

    medium_dataset = [
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

    difficult_dataset = [
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
    namepath_list = [
    "https://imgur.com/a2Q74iy.png","https://imgur.com/k9q8sBE.png","https://imgur.com/GWYaBNN.png",
    ]
    e_img_html_list = make_html_list(30, easy_dataset, 50, 50)
    m_img_html_list = make_html_list(30, medium_dataset, 50, 50)
    d_img_html_list = make_html_list(30, difficult_dataset, 50, 50)
    name_html_list = make_html_list(3, namepath_list, 50, 50)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# PAGES
class FinalResults(Page):
    @staticmethod
    def vars_for_template(player: Player):
        e_dict = {}
        m_dict = {}
        d_dict = {}
        for e_id in player.participant.e_stimuli_id_list:
            e_dict[Constants.e_img_html_list[e_id]] = player.participant.e_img_category_list[e_id]
        for m_id in player.participant.m_stimuli_id_list:
            m_dict[Constants.m_img_html_list[m_id]] = player.participant.m_img_category_list[m_id]
        for d_id in player.participant.d_stimuli_id_list:
            d_dict[Constants.d_img_html_list[d_id]] = player.participant.d_img_category_list[d_id]
        e_score = int(player.participant.e_ari * 100)
        m_score = int(player.participant.m_ari * 100)
        d_score = int(player.participant.d_ari * 100)
        
        return {
            "e_score": e_score,
            "m_score": m_score,
            "d_score": d_score,
            "e_dict" : e_dict,
            "m_dict" : m_dict,
            "d_dict" : d_dict,
            "name0" : Constants.name_html_list[0],
            "name1" : Constants.name_html_list[1],
            "name2" : Constants.name_html_list[2],
        }

page_sequence = [FinalResults]
