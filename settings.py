from os import environ

SESSION_CONFIGS = [
    dict(
        name='CategorizeGame_only',
        display_name="CategorizeGame",
        app_sequence=[
            'introduction_only',
            'categorization_easy',
            'categorization_mid',
            'categorization_difficult',
            'cat_final_result'],
        num_demo_participants=1,
    ),
    dict(
        name='Questionnaire_only',
        display_name="Questionnaire_only",
        app_sequence=['questionnaires'],
        num_demo_participants=1,
    ),
    dict(
        name='categorize_and_full_questionnaire',
        display_name="Game and full questionnaire",
        app_sequence=[
            'informed_consent',
            'introduction_only',
            'categorization_easy',
            'categorization_mid',
            'categorization_difficult',
            'cat_final_result',
            'questionnaires'
            ],
        num_demo_participants=110,
    ),
    dict(
        name='categorize_and_brief_questionnaire',
        display_name="Game and brief questionnaire",
        app_sequence=[
            'informed_consent',
            'introduction_only',
            'categorization_easy',
            'categorization_mid',
            'categorization_difficult',
            'cat_final_result',
            'brief_questionnaires'
            ],
        num_demo_participants=1,
    ),
    # dict(
    #     name='public_goods',
    #     app_sequence=['public_goods'],
    #     num_demo_participants=3,
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    "e_img_category_list", "e_stimuli_id_list", "e_default_nameorder", "e_imghtml_order",
    "e_box0_items", "e_box1_items", "e_box2_items", "e_ari", "e_count",
    "m_img_category_list", "m_stimuli_id_list", "m_default_nameorder", "m_imghtml_order",
    "m_box0_items", "m_box1_items", "m_box2_items", "m_ari", "m_count",
    "d_img_category_list", "d_stimuli_id_list", "d_default_nameorder", "d_imghtml_order",
    "d_box0_items", "d_box1_items", "d_box2_items", "d_ari", "d_count",
    "img_choice", "showed_imgs", "showed_imgs4log", "stimuli_img_order", "loghtml_list",
    "final_round_num", "final_ip_kappa", "final_c_kappa", "final_ari",
    "keycode"
    ]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3953047406988'

ROOMS = [
    dict(
        name='categorize_and_questionnaire',
        display_name='待機ページ'
    ),
]