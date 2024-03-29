ADD_PIC_TEXT = "🖼 Добавить"

ADD_PIC_SEND_PHOTO = "🏖 Отправьте фотографию берега"

ADD_PIC_SEND_PHOTO_ERROR = "❗️Необходимо отправить *фотографию*"
ADD_PIC_SEND_GEO_TAG_ERROR = "❗️Необходимо отправить *геолокацию*"
ADD_PIC_SEND_ABOUT_ERROR = "❗️Необходимо отправить *текст*"

ADD_PIC_SEND_GEO_TAG = (
    "📍 Отправьте свою геолокацию\n_(Что бы определить местонахождение берега)_"
)

ADD_PIC_SEND_ABOUT = "📝 Напишите какое-нибудь замечание\n_(Если нужно)_"

ADD_PIC_SEND_DESTRUCTION = """🔸 Оцените на глаз насколько берег разрушен.
*Необходимо ввести число (процент)*
Далее, число будет проверено нейросетью.
_(Пример ввода: 15)_"""

ADD_PIC_ERROR_INT_DESTRUCTION = "🔴 Необходимо указать целое число.\n_(Например: 30)_"

ADD_PIC_READY = """🟢 Ваша заявка принята.

📍 Местоположение: {geo_tag}
📝 Описание: {about}
🔸 Разрушенность: {destruction}%
"""

ADD_PIC_ERROR = "🔴 Ошибка при добавлении вашей заявки\n{error}"

ADD_PIC_NOT_COASTAL = """
✅ Мы не можем подтвердить, что это действительно берег.\
Поэтому изображение будет дополнительно проверено модератором перед его размещением на карте.

Статус проверки доступен в разделе «📚 Добавленные».

📍 Отправьте свою геолокацию. _(Что бы определить местонахождение берега)_
"""
