from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire ",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration ",
        callback_data="registration"
    )
    profile_button = InlineKeyboardButton(
        "My Profile ",
        callback_data="my_profile"
    )
    view_profile_button = InlineKeyboardButton(
        "View Profiles ",
        callback_data="random_profile"
    )
    reference_menu_button = InlineKeyboardButton(
        "Reference Menu ",
        callback_data="reference_menu"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(profile_button)
    markup.add(view_profile_button)
    markup.add(reference_menu_button)
    return markup



async def start_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Python ",
        callback_data="python"
    )
    mojo_button = InlineKeyboardButton(
        "Mojo ",
        callback_data="mojo"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup

async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "LIKE ",
        callback_data=f"like_{owner_tg_id}"
    )
    mojo_button = InlineKeyboardButton(
        "DISLIKE ",
        callback_data="random_profile"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    python_button = InlineKeyboardButton(
        "Update ",
        callback_data=f"update_profile"
    )
    mojo_button = InlineKeyboardButton(
        "Delete ",
        callback_data="delete_profile"
    )
    markup.add(python_button)
    markup.add(mojo_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Link 🔗",
        callback_data="reference_link"
    )

    markup.add(link_button)
    return markup


