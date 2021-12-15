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


def custom_export(players):
    yield [
        "session",
        "participant_code",
        "id_in_group",
        "final_round_num",
        "final_c_kappa,",
        "final_ip_kappa",
        "final_ari"
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code,
            p.id_in_group,
            p.final_round_num,
            p.final_c_kappa,
            p.final_ip_kappa,
            p.final_ari,
            ]


class Constants(BaseConstants):
    name_in_url = 'final_result'
    players_per_group = None
    num_rounds = 1
    easy_dataset = [
        "https://imgur.com/Ok16AOf.jpg","https://imgur.com/E1tzbHT.jpg","https://imgur.com/TIYwSme.jpg","https://imgur.com/LxXzOcT.jpg",
        "https://imgur.com/JaIDNbN.jpg","https://imgur.com/HzhseCT.jpg","https://imgur.com/yDAAcfa.jpg","https://imgur.com/0QLNi4i.jpg",
        "https://imgur.com/u3uGowS.jpg","https://imgur.com/qnRjZh4.jpg",
        "https://imgur.com/TFK2ZGm.jpg","https://imgur.com/RaeqdvY.jpg","https://imgur.com/O3OebCR.jpg","https://imgur.com/9iWwWM1.jpg",
        "https://imgur.com/mJbqCYe.jpg","https://imgur.com/AofkRCU.jpg","https://imgur.com/GbqH1rT.jpg","https://imgur.com/14n5Njk.jpg",
        "https://imgur.com/biwO9BY.jpg","https://imgur.com/oAAjKTi.jpg",
        "https://imgur.com/aEo3RDS.jpg","https://imgur.com/6DNh3zy.jpg","https://imgur.com/NjIBgAk.jpg","https://imgur.com/J4xYRZl.jpg",
        "https://imgur.com/QR2edYY.jpg","https://imgur.com/ef6tKlM.jpg","https://imgur.com/K7uRcI7.jpg","https://imgur.com/2J8HGUW.jpg",
        "https://imgur.com/oePD1MJ.jpg","https://imgur.com/oePD1MJ.jpg"
        ]

    medium_dataset = [
        "https://imgur.com/oVrfxZw.jpg","https://imgur.com/TkW80Ck.jpg","https://imgur.com/GtymY98.jpg","https://imgur.com/7FGU28E.jpg",
        "https://imgur.com/3g3TFbH.jpg","https://imgur.com/YLcHzhf.jpg","https://imgur.com/erk07Pi.jpg","https://imgur.com/y9FXwvs.jpg",
        "https://imgur.com/aXt6xf1.jpg","https://imgur.com/LScSBWQ.jpg",
        "https://imgur.com/uZrmYFn.jpg","https://imgur.com/Zgsza4K.jpg","https://imgur.com/VhXqX1n.jpg","https://imgur.com/tYhIHr1.jpg",
        "https://imgur.com/bu5P0gG.jpg","https://imgur.com/tdUO3lT.jpg","https://imgur.com/RIe5q7d.jpg","https://imgur.com/yCAO7Ro.jpg",
        "https://imgur.com/eNdE7J9.jpg","https://imgur.com/1JfUNup.jpg",
        "https://imgur.com/gEtMtJ0.jpg","https://imgur.com/YfgQPsC.jpg","https://imgur.com/EZbWMPw.jpg","https://imgur.com/h3cBOKh.jpg",
        "https://imgur.com/sJuxYOJ.jpg","https://imgur.com/kxtLzmv.jpg","https://imgur.com/0x3U7Xj.jpg","https://imgur.com/1af1D9h.jpg",
        "https://imgur.com/IjzowZ2.jpg","https://imgur.com/K7NcZ3S"
        ]

    difficult_dataset = [
        "https://imgur.com/f7SqLNo.jpg","https://imgur.com/rBlF4mu.jpg","https://imgur.com/0WqM7kB.jpg","https://imgur.com/27A6jU2.jpg",
        "https://imgur.com/e7kfVeV.jpg","https://imgur.com/LUjj2px.jpg",
        "https://imgur.com/zgHZAP9.jpg","https://imgur.com/X9EE4u0.jpg","https://imgur.com/0PXQXGd.jpg","https://imgur.com/HOMn4V6.jpg",
        "https://imgur.com/znWBdLv.jpg","https://imgur.com/ZWYsTZP.jpg","https://imgur.com/VKydSuN.jpg","https://imgur.com/75B7TQR.jpg",
        "https://imgur.com/4dpcXkf.jpg","https://imgur.com/M81tl9O.jpg","https://imgur.com/lM4WQ5p.jpg","https://imgur.com/rRcgod4.jpg",
        "https://imgur.com/vdaoN97.jpg","https://imgur.com/ZzEYWUp.jpg","https://imgur.com/iwhyjOw.jpg",
        "https://imgur.com/ajWV0KL.jpg","https://imgur.com/XkUx41x.jpg","https://imgur.com/CB9XFGX.jpg","https://imgur.com/I1hgaCt.jpg",
        "https://imgur.com/F3EpQIU.jpg","https://imgur.com/RKN9hEI.jpg","https://imgur.com/dGwAswt.jpg","https://imgur.com/tR5f11p.jpg",
        "https://imgur.com/SsNAYPz.jpg"
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
