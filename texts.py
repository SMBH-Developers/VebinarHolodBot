from aiogram.utils import markdown
from string import Template
import datetime

from times import get_month


start_message = f"""
Здравствуйте!✨

Здесь вы сможете зарегистрироваться на вебинар "{markdown.hbold('7 Шагов к яркой и уверенной жизни')}", узнать больше об Анастасии, а также {markdown.hbold('получить подарок "100 Ресурсных  действия"')}❤️

Но для начала давайте познакомимся, как Вас зовут?
"""

main_menu = """
Рады Вас приветствовать в боте Анастасии Холод!😌

Скоро я проведу мастер-класс на котором мы поговорим про то, как найти дело жизни и обрести психологический комфорт. 

Для регистрации на вебинар Вам нужно нажать на кнопку ниже👇

Чтобы получить дополнительную информацию, выберите интересующий Вас пункт.
"""


menu_registration = f"""
🎁После регистрации Вы можете получить от меня подарок "Личный Социальный код"  

Это инструмент, который может подсказать, как конкретно Вам строить отношения с окружающими, чтобы развиваться в жизни уверенно.
"""

menu_present = f"""
{markdown.hbold('Гайд по простым действиям, направленный на поднятие настроения, запаса бодрости и мотивации')}🎯
"""


def menu_about_web() -> str:
    current_datetime = datetime.datetime.now()
    date = f"{current_datetime.day} {get_month(current_datetime.month)}"

    if current_datetime.hour >= 19:
        next_day = current_datetime + datetime.timedelta(days=1)
        date = f"{next_day.day} {get_month(next_day.month)}"

    menu_about_web = f"""
Наш внутренний мир - это сложный механизм, и чтобы он хорошо работал, надо учитывать все 7 слоев психики и комплексно подходить к их развитию 👇

{markdown.hitalic(f'{date} в 19:00 я предлагаю познакомиться с ними ближе на моем мастер-классе "7 шагов к уверенной и легкой жизни"')}

{markdown.hbold('Я расскажу, как запустить изменения в своей жизни комплексно - на каждом из 7 уровней.')}

За этот год больше 1000 участников моих практик смогли преодолеть тревогу, приобрести навыки управления собственной реальностью и увеличили свой ежемесячный доход в среднем на 20 тыс рублей.

Прямо сейчас Вы можете перейти по кнопке и оставить заявку на бесплатное участие!

🎁После регистрации Вы можете получить от меня подарок "Личный Социальный код"  

Это инструмент, который может подсказать, как конкретно Вам строить отношения с окружающими, чтобы развиваться в жизни уверенно.

На мастер-классе мы проведем авторскую практику по психологической настройке на твою идеальную жизнь.
"""
    return menu_about_web


menu_about_anastasia = f"""
❓{markdown.hbold('Почему стоит учиться у Анастасии Холод?')}

— 10 лет опыта  психологических практик, женские семинары

— Более 10 лет назад начала разрабатывать и проводить первые психологические тренинги

— 4 года наставник по бизнесу для начинающих предпринимателей.

— 2 млн рублей месячного дохода в собственном опыте предпринимательской деятельности

— 8 лет психологического образования, от классической до трансперсональной психотерапии

— Human Design сертифицированный специалист по системе, позволяющей раскрывать уникальные таланты любого человека, «Дизайн человека»🎨
"""

hour_after_registration = """
Время важных событий и решений✨

Как найти дело жизни и обрести психологический комфорт, я буду рассказывать на бесплатном мастер-классе «7 шагов к уверенной и яркой жизни»

Важное напоминание, мы начинаем в 19:00 по Москве.

Попасть к нам можно будет по этой ссылке — https://course.soul-aca.ru/7steps_in

На мастер-классе я подробно расскажу, как понять себя и что делать, чтобы цели достигались.

Давайте вместе исследуем Ваш запрос, мечты и цели, чтобы реализовать истинные таланты

Если Вы все еще не зарегистрировались, то самое время это сделать по кнопке ниже
"""#TODO hearts


def an_hour_before_web(name: str):
    text = f"""
Вебинар скоро начинается😌

{markdown.quote_html(name.title())}, если вы уже зарегистрировались на мастер-класс, то вам осталось найти удобное место и ждать старта

Мы начинаем ровно через час.

Подключайтесь по этой ссылке — https://course.soul-aca.ru/7steps_in

А для тех, кто по какой-то причине пропустил или не успел зарегистрироваться, можете сделать это по кнопке ниже👇
"""
    return text


the_next_day = """
Если по какой-то причине, Вы вчера не были на мастер-классе, то Вы многое пропустили😌

Мы обсудили 7 уровней изменений, которые способны преобразить Вашу жизнь, вот часть из них:

— Материальное направление
— Энергетический уровень
— Ментальный уровень

К счастью, сегодня будет доступен повтор , в 19:00 по Москве

Вот ссылка для входа — https://course.soul-aca.ru/7steps_in

Мы начинаем через час !
"""