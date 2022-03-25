from otree.api import *


doc = """
SPQ-B
AQ
 1か2なら1点 : 2, 4, 5, 6, 7, 9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41, 42, 43, 45, 46
 残りは3か4なら1点
ASRS
"""


class Constants(BaseConstants):
    name_in_url = 'brief_questionnaires'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #SPQ-B
    spq_b_1 = models.IntegerField(
        label="他人は私のことを、少し変わった突飛な人だと思っている",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_2 = models.IntegerField(
        label="姿は見えないが、私のまわりに人がいると感じたり、見えない力が存在すると感じたりしたことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_3 = models.IntegerField(
        label="私の変な癖や習慣について、人にいろいろ言われる",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_4 = models.IntegerField(
        label="私が考えていることを、他の人にわかられてしまうと確信したことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_5 = models.IntegerField(
        label="ありふれた物や出来事が、私のための特別な合図であるらしいと気づいたことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_6 = models.IntegerField(
        label="私のことをとても変人だと思っている人もいる",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_7 = models.IntegerField(
        label="友達と一緒の時でも、用心しないといけないと感じることがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_8 = models.IntegerField(
        label="私の話はとらえどころがなくてわかりにくいと思っている人もいる",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_9 = models.IntegerField(
        label="他人が言ったりしたりすることの中に、脅しや嫌がらせが隠されていると感じることがしばしばある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_10 = models.IntegerField(
        label="買い物をしているとき、他の人たちが私に注意を向けているような気がする",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_11 = models.IntegerField(
        label="知らない人たちと話をしなければならない時には、とても居心地が悪い",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_12 = models.IntegerField(
        label="占星術・未来予知・UFO・ESP(超感覚的知覚)・第六感などを体験したことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_13 = models.IntegerField(
        label="ときどき、人とは違う言葉の使い方をすることがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_14 = models.IntegerField(
        label="自分のことについて、他人に教えすぎないのが一番よいと思う",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_15 = models.IntegerField(
        label="社交の場では、あまり目立たないようにしている方である",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_16 = models.IntegerField(
        label="ふだんなら気づかないような遠くの物音を聞いて、びっくりしたことがある",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_17 = models.IntegerField(
        label="話している時、相手と目を合わせないようにしがちである",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_18 = models.IntegerField(
        label="他の人とは親しくなれないと感じる",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_19 = models.IntegerField(
        label="私はふつうとは違う、変わった人間である",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_20 = models.IntegerField(
        label="言いたいことを人に明確に伝えるのは、私には難しい",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_21 = models.IntegerField(
        label="よく知らない人たちに話しかけるのはとても緊張する",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
    spq_b_22 = models.IntegerField(
        label="感情を表に出さない方である",
        choices = [
            [1, "はい"],
            [0, "いいえ"]
        ],
        widget=widgets.RadioSelectHorizontal
    )
            
    #AQ
    aq_1 = models.IntegerField(
        label="何かをするときには、一人でするよりも他の人といっしょにする方が好きだ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_2 = models.IntegerField(
        label="同じやりかたを何度もくりかえし用いることが好きだ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_3 = models.IntegerField(
        label="何かを想像するとき、映像（イメージ）を簡単に思い浮かべることができる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_4 = models.IntegerField(
        label="ほかのことがぜんぜん気にならなくなる（目に入らなくなる）くらい、何かに没頭してしまうことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_5 = models.IntegerField(
        label="他の人が気がつかないような小さい物音に気がつくことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_6 = models.IntegerField(
        label="車のナンバーや時刻表の数字などの一連の数字や、特に意味のない情報に注目する（こだわる）ことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_7 = models.IntegerField(
        label="自分ではていねいに話したつもりでも、話し方が失礼だと周囲の人から言われることがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_8 = models.IntegerField(
        label="小説などの物語を読んでいるとき、登場人物がどのような人か（外見など）について簡単にイメージすることができる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_9 = models.IntegerField(
        label="日付についてのこだわりがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_10 = models.IntegerField(
        label="パーティや会合などで、いろいろな人の会話についていくことが簡単にできる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_11 = models.IntegerField(
        label="自分がおかれている社会的な状況（自分の立場）がすぐにわかる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_12 = models.IntegerField(
        label="ほかの人は気がつかないような細かいことに、すぐに気づくことが多い。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_13 = models.IntegerField(
        label="パーティなどよりも、図書館に行く方が好きだ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_14 = models.IntegerField(
        label="作り話には、すぐに気がつく（すぐわかる）。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_15 = models.IntegerField(
        label="モノよりも人間の方に魅力を感じる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_16 = models.IntegerField(
        label="それをそうすることができないとひどく混乱して（パニックになって）しまうほど、何かに強い興味を持つことがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_17 = models.IntegerField(
        label="他の人と、雑談などのような社交的な会話を楽しむことができる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_18 = models.IntegerField(
        label="自分が話をしているときには、なかなか他の人に横から口をはさませない。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_19 = models.IntegerField(
        label="数字に対するこだわりがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_20 = models.IntegerField(
        label="小説などを読んだり、テレビでドラマなどを観ているとき、登場人物の意図をよく理解できないことがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_21 = models.IntegerField(
        label="小説のようなフィクションを読むのは、あまり好きではない。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_22 = models.IntegerField(
        label="新しい友人を作ることは、むずかしい。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_23 = models.IntegerField(
        label="いつでも、ものごとの中に何らかのパターン（型や決まりなど）のようなものに気づく。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_24 = models.IntegerField(
        label="博物館に行くよりも、劇場に行く方が好きだ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_25 = models.IntegerField(
        label="自分の目標が妨害されても、混乱することはない。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_26 = models.IntegerField(
        label="会話をどのように進めたらいいのか、わからなくなってしまうことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_27 = models.IntegerField(
        label="誰かと話しをしているときに、相手の話の‘言外の意味’を理解することは容易である。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_28 = models.IntegerField(
        label="細部よりも全体像に注意が向くことが多い。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_29 = models.IntegerField(
        label="電話番号をおぼえるのは苦手だ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_30 = models.IntegerField(
        label="状況（部屋の様子やものなど）や人間の外見（服装や髪型）などが、いつもとちょっと違っているくらいでは、すぐには気がつかないことが多い。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_31 = models.IntegerField(
        label="自分の話を聞いている相手が退屈しているときには、どのように話をすればいいかわかっている。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_32 = models.IntegerField(
        label="同時に２つ以上のことをするのは、かんたんである。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_33 = models.IntegerField(
        label="電話で話をしているとき、自分が話をするタイミングがわからないことがある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_34 = models.IntegerField(
        label="自分から進んで何かをすることは楽しい。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_35 = models.IntegerField(
        label="冗談がわからないことがよくある。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_36 = models.IntegerField(
        label="相手の顔を見れば、その人が考えていることや感じていることがわかる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_37 = models.IntegerField(
        label="じゃまが入って何かを中断されても、すぐにそれまでやっていたことに戻ることができる。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_38 = models.IntegerField(
        label="人と雑談のような社交的な会話をすることが得意だ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_39 = models.IntegerField(
        label="同じことを何度も繰り返していると、周囲の人からよく言われる。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_40 = models.IntegerField(
        label="子どものころ、友達といっしょに、よく‘○○ごっこ’（ごっこ遊び）をして遊んでいた。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_41 = models.IntegerField(
        label="特定の種類のものについての（車について、鳥について、植物についてのような）情報を集めることが好きだ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_42 = models.IntegerField(
        label="あること（もの）を、他の人がどのように感じるかを想像するのは苦手だ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_43 = models.IntegerField(
        label="自分がすることはどんなことでも慎重に計画するのが好きだ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_44 = models.IntegerField(
        label="社交的な場面（機会）は楽しい。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_45 = models.IntegerField(
        label="他の人の考え（意図）を理解することは苦手だ。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_46 = models.IntegerField(
        label="新しい場面（状況）に不安を感じる。",
        choices = [
            [1, "1"],
            [1, "2"],
            [0, "3"],
            [0, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_47 = models.IntegerField(
        label="初対面の人と会うことは楽しい。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_48 = models.IntegerField(
        label="社交的である。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_49 = models.IntegerField(
        label="人の誕生日をおぼえるのは苦手だ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    aq_50 = models.IntegerField(
        label="子どもと‘○○ごっこ’をして遊ぶのがとても得意だ。",
        choices = [
            [0, "1"],
            [0, "2"],
            [1, "3"],
            [1, "4"]
            ],
        widget=widgets.RadioSelectHorizontal
    )
    
    #ASRS
    asrs_1 = models.IntegerField(
        label="つまらない、あるいは難しい仕事をする際に、不注意な間違いをすることが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_2 = models.IntegerField(
        label="長時間座っていなければならない時に、手足をそわそわと動かしたり、もぞもぞしたりすることが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_3 = models.IntegerField(
        label="つまらない、あるいは単調な作業をする際に、注意を集中し続けることが、困難なことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_4 = models.IntegerField(
        label="会議などの着席していなければいけない状況で、席を離れてしまうことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_5 = models.IntegerField(
        label="直接話しかけられているにもかかわらず、話に注意を払うことが困難なことはどれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_6 = models.IntegerField(
        label="落ち着かない、あるいはソワソワした感じが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_7 = models.IntegerField(
        label="物事を行うにあたって、難所は乗り越えたのに、詰めが甘くて仕上げるのが困難だったことが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_8 = models.IntegerField(
        label="時間に余裕があっても、一息ついたり、ゆったりとくつろぐことが困難なことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_9 = models.IntegerField(
        label="計画性を要する作業を行う際に、作業を順序だてるのが困難だったことが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_10 = models.IntegerField(
        label="まるで何かに駆り立てられるかのように過度に活動的になったり、何かせずにいられなくなることが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_11 = models.IntegerField(
        label="じっくりと考える必要のある課題に取り掛かるのを避けたり、遅らせたりすることが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_12 = models.IntegerField(
        label="社交的な場面でしゃべりすぎてしまうことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_13 = models.IntegerField(
        label="家や職場に物を置き忘れたり、物をどこに置いたかわからなくなって探すのに苦労したことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_14 = models.IntegerField(
        label="会話を交わしている相手が話し終える前に会話をさえぎってしまったことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_15 = models.IntegerField(
        label="外からの刺激や雑音で気が散ってしまうことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_16 = models.IntegerField(
        label="順番待ちしなければいけない場合に、順番を待つことが困難なことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_17 = models.IntegerField(
        label="約束や、しなければいけない用事を忘れたことが、どのくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    asrs_18 = models.IntegerField(
        label="忙しくしている人の邪魔をしてしまうことが、どれくらいの頻度でありますか。",
        choices = [0, 1, 2, 3, 4],
        widget=widgets.RadioSelectHorizontal
    )
    
def custom_export(players):
    yield [
        "session",
        "participant_code", "started_time",
        "spq_b_1", "spq_b_2", "spq_b_3", "spq_b_4", "spq_b_5",
        "spq_b_6", "spq_b_7", "spq_b_8", "spq_b_9", "spq_b_10",
        "spq_b_11", "spq_b_12", "spq_b_13", "spq_b_14", "spq_b_15",
        "spq_b_16", "spq_b_17", "spq_b_18", "spq_b_19", "spq_b_20",
        "spq_b_21", "spq_b_22",
        "aq_1", "aq_2", "aq_3", "aq_4", "aq_5",
        "aq_6", "aq_7", "aq_8", "aq_9", "aq_10",
        "aq_11", "aq_12", "aq_13", "aq_14", "aq_15",
        "aq_16", "aq_17", "aq_18", "aq_19", "aq_20",
        "aq_21", "aq_22", "aq_23", "aq_24", "aq_25",
        "aq_26", "aq_27", "aq_28", "aq_29", "aq_30",
        "aq_31", "aq_32", "aq_33", "aq_34", "aq_35",
        "aq_36", "aq_37", "aq_38", "aq_39", "aq_40",
        "aq_41", "aq_42", "aq_43", "aq_44", "aq_45",
        "aq_46", "aq_47", "aq_48", "aq_49", "aq_50",
        "asrs_1", "asrs_2", "asrs_3", "asrs_4", "asrs_5",
        "asrs_6", "asrs_7", "asrs_8", "asrs_9", "asrs_10",
        "asrs_11", "asrs_12", "asrs_13", "asrs_14", "asrs_15",
        "asrs_16", "asrs_17", "asrs_18",
        ]
    for p in players:
        participant = p.participant
        session = p.session
        yield [
            session.code,
            participant.code, participant.time_started_utc,
            p.spq_b_1, p.spq_b_2, p.spq_b_3, p.spq_b_4, p.spq_b_5,
            p.spq_b_6, p.spq_b_7, p.spq_b_8, p.spq_b_9, p.spq_b_10,
            p.spq_b_11, p.spq_b_12, p.spq_b_13, p.spq_b_14, p.spq_b_15,
            p.spq_b_16, p.spq_b_17, p.spq_b_18, p.spq_b_19, p.spq_b_20,
            p.spq_b_21, p.spq_b_22,
            p.aq_1, p.aq_2, p.aq_3, p.aq_4, p.aq_5,
            p.aq_6, p.aq_7, p.aq_8, p.aq_9, p.aq_10,
            p.aq_11, p.aq_12, p.aq_13, p.aq_14, p.aq_15,
            p.aq_16, p.aq_17, p.aq_18, p.aq_19, p.aq_20,
            p.aq_21, p.aq_22, p.aq_23, p.aq_24, p.aq_25,
            p.aq_26, p.aq_27, p.aq_28, p.aq_29, p.aq_30,
            p.aq_31, p.aq_32, p.aq_33, p.aq_34, p.aq_35,
            p.aq_36, p.aq_37, p.aq_38, p.aq_39, p.aq_40,
            p.aq_41, p.aq_42, p.aq_43, p.aq_44, p.aq_45,
            p.aq_46, p.aq_47, p.aq_48, p.aq_49, p.aq_50,
            p.asrs_1, p.asrs_2, p.asrs_3, p.asrs_4, p.asrs_5,
            p.asrs_6, p.asrs_7, p.asrs_8, p.asrs_9, p.asrs_10,
            p.asrs_11, p.asrs_12, p.asrs_13, p.asrs_14, p.asrs_15,
            p.asrs_16, p.asrs_17, p.asrs_18,
            ]

# PAGES
class Introduction(Page):
    pass

class SPQ_B(Page):
    form_model = 'player'
    form_fields = [
        "spq_b_1", "spq_b_2", "spq_b_3", "spq_b_4", "spq_b_5",
        "spq_b_6", "spq_b_7", "spq_b_8", "spq_b_9", "spq_b_10",
        "spq_b_11", "spq_b_12", "spq_b_13", "spq_b_14", "spq_b_15",
        "spq_b_16", "spq_b_17", "spq_b_18", "spq_b_19", "spq_b_20",
        "spq_b_21", "spq_b_22"
    ]

class AQ(Page):
    form_model = 'player'
    form_fields = [
        "aq_1", "aq_2", "aq_3", "aq_4", "aq_5",
        "aq_6", "aq_7", "aq_8", "aq_9", "aq_10",
        "aq_11", "aq_12", "aq_13", "aq_14", "aq_15",
        "aq_16", "aq_17", "aq_18", "aq_19", "aq_20",
        "aq_21", "aq_22", "aq_23", "aq_24", "aq_25",
        "aq_26", "aq_27", "aq_28", "aq_29", "aq_30",
        "aq_31", "aq_32", "aq_33", "aq_34", "aq_35",
        "aq_36", "aq_37", "aq_38", "aq_39", "aq_40",
        "aq_41", "aq_42", "aq_43", "aq_44", "aq_45",
        "aq_46", "aq_47", "aq_48", "aq_49", "aq_50"
        ]

class ASRS(Page):
    form_model = 'player'
    form_fields = [
        "asrs_1", "asrs_2", "asrs_3", "asrs_4", "asrs_5",
        "asrs_6", "asrs_7", "asrs_8", "asrs_9", "asrs_10",
        "asrs_11", "asrs_12", "asrs_13", "asrs_14", "asrs_15",
        "asrs_16", "asrs_17", "asrs_18"
        ]

class Finish(Page):
    pass


page_sequence = [
    Introduction,
    SPQ_B,
    AQ,
    ASRS,
    Finish
    ]
