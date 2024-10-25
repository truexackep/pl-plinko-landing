
import asyncio
import json
import logging
import os
import re
import sqlite3
import sys
from datetime import datetime, timedelta
from os import getenv

import requests as requests
from aiogram import Bot, Dispatcher, Router, types, BaseMiddleware
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.utils.markdown import hbold
from aiohttp import web
from typing import Callable, Any, Awaitable, Union

# Подключение к базе данных SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    user_id INTEGER UNIQUE,
    name TEXT,
    username TEXT,
    register_time TEXT)
''')
conn.commit()


# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6774266370:AAHiqwzjbD30I4KoAOA5mCOP4Kaq1793pHI"
channel_id = "-1001702864568"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='bot.log')  # указываем имя файла для логов
logger = logging.getLogger(__name__)

# Добавляем обработчик для вывода в консоль
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
ADMIN = 5116638137

storage = MemoryStorage()

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher(logger=logger, storage=storage)
bot = Bot(TOKEN)

class SomeMiddleware(BaseMiddleware):
    album_data: dict = {}

    def __init__(self, latency: Union[int, float] = 0.01):
        self.latency = latency

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            message: Message,
            data: dict[str, Any]
    ) -> Any:
        if not message.media_group_id:
            await handler(message, data)
            return
        try:
            self.album_data[message.media_group_id].append(message)
        except KeyError:
            self.album_data[message.media_group_id] = [message]
            await asyncio.sleep(self.latency)

            data['_is_last'] = True
            data["album"] = self.album_data[message.media_group_id]
            await handler(message, data)

        if message.media_group_id and data.get("_is_last"):
            del self.album_data[message.media_group_id]
            del data['_is_last']


dp.message.middleware(SomeMiddleware())

class Settingss(StatesGroup):
    we = State()
    sh = State()
    sends = State()
app = web.Application()
async def handle_post_request(request):

    data = await request.read()
    data = data.decode('utf-8')  # Декодируем байтовый объект в строку UTF-8
    data = json.loads(data)
    subid = data.get('subid')
    chan_id = data.get('cid')
    result = await asyncio.create_task(generate_link(subid, chan_id))
    return web.Response(text=json.dumps({'link': result.invite_link}),  headers={
        'Access-Control-Allow-Origin': '*',  # Разрешаем доступ с любого источника
        'Access-Control-Allow-Methods': 'POST',  # Разрешаем только POST запросы
        'Access-Control-Allow-Headers': 'Content-Type',  # Разрешаем только Content-Type заголовок
    })

@dp.message(Settingss.sh)
async def handle_albums(message: Message, state: FSMContext,  album: list[Message] = None):
    # print(message.html_text)
    message_db = {'is_media': False, 'types': []}
    if album == None:
        if message.text:
            message_db['types'].append({'type': 'text', 'payload': message.html_text})

        if message.caption:
            message_db['types'].append({'type': 'text', 'payload': message.html_text})


        if message.photo:
            media_path = await save_file(message.photo[-1].file_id, 'photo')
            message_db['types'].append({'type': 'photo', 'payload': media_path})

    else:
        message_db['is_media'] = True

        if message.caption:
            message_db['types'].append({'type': 'text', 'payload': message.html_text})
        i = 0
        for msg in album:
            caption = ''
            if i == 0:
                caption = message.caption
            if msg.photo:
                file_id = msg.photo[-1].file_id
                media_path = await save_file(file_id, 'photo')
                message_db['types'].append({'type': 'photo', 'payload': media_path})
            else:
                obj_dict = msg.dict()
                file_id = obj_dict[msg.content_type]['file_id']
                media_path = await save_file(file_id, 'file')
                message_db['types'].append({'type': 'file', 'payload': media_path})
            i = i + 1

    cursor.execute("UPDATE settings SET value = '"+json.dumps(message_db)+"' WHERE id = 2;")
    conn.commit()

    await state.clear()

    await message.reply("Сообещние изменено")

@dp.message(Settingss.sends)
async def handle_albums(message: Message, state: FSMContext,  album: list[Message] = None):
    # print(message.html_text)
    message_db = {'is_media': False, 'types': []}
    if album == None:
        if message.text:
            message_db['types'].append({'type': 'text', 'payload': message.html_text})

        if message.caption:
            message_db['types'].append({'type': 'text', 'payload': message.html_text})


        if message.photo:
            media_path = await save_file(message.photo[-1].file_id, 'photo')
            message_db['types'].append({'type': 'photo', 'payload': media_path})

    else:
        message_db['is_media'] = True

        if message.caption:
            message_db['types'].append({'type': 'text', 'payload': message.html_text})
        i = 0
        for msg in album:
            caption = ''
            if i == 0:
                caption = message.caption
            if msg.photo:
                file_id = msg.photo[-1].file_id
                media_path = await save_file(file_id, 'photo')
                message_db['types'].append({'type': 'photo', 'payload': media_path})
            else:
                obj_dict = msg.dict()
                file_id = obj_dict[msg.content_type]['file_id']
                media_path = await save_file(file_id, 'file')
                message_db['types'].append({'type': 'file', 'payload': media_path})
            i = i + 1

    # cursor.execute("UPDATE settings SET value = '"+json.dumps(message_db)+"' WHERE id = 2;")
    # conn.commit()

    # await state.clear()
    post = {"structure": message_db}
    builder = InlineKeyboardBuilder()
    await state.set_data({"mes": message_db})
    builder.button(text=f"Запустить рассылку", callback_data=f"send_messages")

    if post['structure']['is_media']:
        media = []
        text = None
        for type in post['structure']['types']:
            if type['type'] == 'text':
                text = type['payload']
                break
        if text == None:
            text = ''
        i = 0
        tx = text
        for type in post['structure']['types']:
            if type['type'] == 'photo':
                media.append(types.InputMediaPhoto(media=FSInputFile(type['payload']), caption=tx,
                                                   parse_mode='html'))
                tx = ''
        # await bot.delete_message(chat_id=message.from_user.id, message_id=data.message.message_id)
        await bot.send_media_group(chat_id=message.from_user.id, media=media)
        await bot.send_message(chat_id=message.from_user.id,
                               text="Действие", reply_markup=builder.as_markup())


    else:
        text = None
        for type in post['structure']['types']:
            if type['type'] == 'text':
                text = type['payload']
                break
        if text == None:
            text = ''
        i = 0
        tx = text
        photo = None
        for type in post['structure']['types']:
            if type['type'] == 'photo':
                photo = FSInputFile(type['payload'])

        texts_and_links = extract_texts_and_links(tx)
        for link in texts_and_links:
            builder.button(text=link['text'], url=link['link'])
        tx = remove_patterns(tx)
        builder.adjust(1, 1)

        if photo == None:
            await bot.send_message(chat_id=message.from_user.id, text=tx, parse_mode='html',
                                   reply_markup=builder.as_markup())

        else:
            await bot.send_photo(chat_id=message.from_user.id, caption=tx, photo=photo,
                                 parse_mode='html', reply_markup=builder.as_markup())
    # await message.reply("Сообещние изменено")
def extract_texts_and_links(message):
    # Регулярное выражение для поиска шаблонов $btn (text:::ссылка)
    pattern = r'\$btn\s*\(([^:]+):::(.*?)\)'

    # Поиск всех совпадений в сообщении
    matches = re.findall(pattern, message)

    # Разделение найденных совпадений на тексты и ссылки
    texts_and_links = [{'text': match[0], 'link': match[1]} for match in matches]

    return texts_and_links


def remove_patterns(message):
    # Регулярное выражение для удаления строк с шаблонами $btn (text:::ссылка)
    pattern = r'\$btn\s*\([^:]+:::(.*?)\)\s*'
    # Замена найденных шаблонов на пустую строку
    cleaned_message = re.sub(pattern, '', message)

    return cleaned_message
async def save_file(file_id, file_type):
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_extension = os.path.splitext(file_path)[1]
    new_file_name = f"{file_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{file_extension}"
    new_file_path = os.path.join('media', new_file_name)

    await bot.download_file(file_path, new_file_path)

    return new_file_path


@dp.message(Settingss.we)
async def wait_sh(message: Message, state: FSMContext):
    try:
        seconds = int(message.text)
        cursor.execute(f"UPDATE settings SET value = '{seconds}' WHERE id = 1;")
        conn.commit()
        await state.clear()
        await bot.send_message(message.from_user.id, f"Автопринятие успешно изменено на {seconds} секунд.")
    except:
        await message.answer("Неизвестная ошибка")
@dp.message(Command('admin'))
async def send_menu(message: types.Message):
    await send_menu(message.from_user.id)


async def send_menu(chat_id, message_id = None):
    builder = ReplyKeyboardBuilder()
    builder.button(text="Основные настройки")
    builder.button(text="Запустить рассылку")

    if message_id == None:
        await bot.send_message(chat_id=chat_id, text="Меню", reply_markup=builder.as_markup())

async def send_menus(chat_id, message_id = None):
    cursor.execute('SELECT * FROM settings')
    settings = cursor.fetchall()
    approve_time = settings[0]
    hello_message = settings[1]
    builder = InlineKeyboardBuilder()
    tim = ''
    if approve_time[2] == '0':
        tim = 'сразу'
    else:
        tim = f"{approve_time[2]} сек."
    builder.button(text=f"Автопринятие юзера: {tim}", callback_data=f"time")

    builder.button(text=f"Приветственное сообщение", callback_data=f"hello_message")
    builder.adjust(1, 1)


    if message_id == None:
        await bot.send_message(chat_id=chat_id, text="Основные настройки:", reply_markup=builder.as_markup())
    else:
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Основные настройки:", reply_markup=builder.as_markup())


@dp.message()
async def menu(message: types.Message,  state: FSMContext):
    if message.text == "Запустить рассылку":
        builder = InlineKeyboardBuilder()
        builder.button(text=f"Назад", callback_data=f"back")
        builder.adjust(1, 1)
        await state.set_state(Settingss.sends)
        await bot.send_message(chat_id=message.from_user.id,
                                    text="Отправьте сообщение", reply_markup=builder.as_markup())
    if message.text == "Основные настройки":
        cursor.execute('SELECT * FROM settings')
        settings = cursor.fetchall()
        approve_time = settings[0]
        hello_message = settings[1]
        builder = InlineKeyboardBuilder()
        tim = ''
        if approve_time[2] == '0':
            tim = 'сразу'
        else:
            tim = f"{approve_time[2]} сек."
        builder.button(text=f"Автопринятие юзера: {tim}", callback_data=f"time")

        builder.button(text=f"Приветственное сообщение", callback_data=f"hello_message")
        builder.adjust(1, 1)

        await message.answer("Основные настройки:", reply_markup=builder.as_markup())

    # if message.text == "Приветственное сообщение":

async def send_messages(post, chat_id, message_id):
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    users = get_users()
    count = 0
    erorrs = 0
    message = await bot.send_message(chat_id=chat_id,         text = f"РАССЫЛКА\n\nОтправлено {count}/{len(users)}\nОшибок: {erorrs}.")

    for user in users:
        try:
            builder = InlineKeyboardBuilder()

            if post['structure']['is_media']:
                media = []
                text = None
                for type in post['structure']['types']:
                    if type['type'] == 'text':
                        text = type['payload']
                        break
                if text == None:
                    text = ''
                i = 0
                tx = text
                for type in post['structure']['types']:
                    if type['type'] == 'photo':
                        media.append(types.InputMediaPhoto(media=FSInputFile(type['payload']), caption=tx,
                                                           parse_mode='html'))
                        tx = ''
                # await bot.delete_message(chat_id=message.from_user.id, message_id=data.message.message_id)
                await bot.send_media_group(chat_id=user['user_id'], media=media)


            else:
                text = None
                for type in post['structure']['types']:
                    if type['type'] == 'text':
                        text = type['payload']
                        break
                if text == None:
                    text = ''
                i = 0
                tx = text
                photo = None
                for type in post['structure']['types']:
                    if type['type'] == 'photo':
                        photo = FSInputFile(type['payload'])

                texts_and_links = extract_texts_and_links(tx)
                for link in texts_and_links:
                    builder.button(text=link['text'], url=link['link'])
                tx = remove_patterns(tx)
                builder.adjust(1, 1)

                if photo == None:
                    await bot.send_message(chat_id=user['user_id'], text=tx, parse_mode='html',
                                           reply_markup=builder.as_markup())

                else:
                    await bot.send_photo(chat_id=user['user_id'], caption=tx, photo=photo,
                                         parse_mode='html', reply_markup=builder.as_markup())

            count = count + 1


        except Exception as e:
            print(e)
            erorrs = erorrs + 1

        text = f"РАССЫЛКА\n\nОтправлено {count}/{len(users)}\nОшибок: {erorrs}"
        await bot.edit_message_text(chat_id=chat_id, message_id=message.message_id, text=text)
        await asyncio.sleep(5)


@dp.callback_query()
async def on_query(data, state: FSMContext):
    if data.data == 'send_messages':
        dat =  await state.get_data()
        print(dat)
        await send_messages(post={'structure': dat['mes']}, chat_id=data.from_user.id, message_id=data.message.message_id)
        await state.clear()
        # post = {"structure": dat['mes']}

    if data.data == 'hello_message':
        builder = InlineKeyboardBuilder()

        cursor.execute('SELECT * FROM settings')
        settings = cursor.fetchall()
        hello_message = settings[1]
        post = {"structure": json.loads(hello_message[2])}
        builder.button(text=f"Изменить", callback_data=f"hello_set")
        builder.button(text=f"Назад", callback_data=f"baak")
        if hello_message[2] == None or hello_message[2] == '':
            text = "Сообщение не настроено"
        else:
            if post['structure']['is_media']:
                media = []
                text = None
                for type in post['structure']['types']:
                    if type['type'] == 'text':
                        text = type['payload']
                        break
                if text == None:
                    text = ''
                i = 0
                tx = text
                for type in post['structure']['types']:
                    if type['type'] == 'photo':
                        media.append(types.InputMediaPhoto(media=FSInputFile(type['payload']), caption=tx,
                                                           parse_mode='html'))
                        tx = ''
                await bot.delete_message(chat_id=data.from_user.id, message_id=data.message.message_id)
                await bot.send_media_group(chat_id=data.from_user.id, media=media)
                await bot.send_message(chat_id=data.from_user.id,
                                            text="Действие", reply_markup=builder.as_markup())


            else:
                text = None
                for type in post['structure']['types']:
                    if type['type'] == 'text':
                        text = type['payload']
                        break
                if text == None:
                    text = ''
                i = 0
                tx = text
                photo = None
                for type in post['structure']['types']:
                    if type['type'] == 'photo':
                        photo = FSInputFile(type['payload'])

                texts_and_links = extract_texts_and_links(tx)
                for link in texts_and_links:
                    builder.button(text=link['text'], url=link['link'])
                tx = remove_patterns(tx)
                builder.adjust(1, 1)

                if photo == None:
                    await bot.send_message(chat_id=data.from_user.id, text=tx, parse_mode='html', reply_markup=builder.as_markup())

                else:
                    await bot.send_photo(chat_id=data.from_user.id, caption=tx, photo=photo,
                                         parse_mode='html', reply_markup=builder.as_markup())

        # await bot.edit_message_text(chat_id=data.from_user.id, message_id=data.message.message_id,
        #                             text=text, reply_markup=builder.as_markup())

    if data.data == 'time':
        await state.clear()
        cursor.execute('SELECT * FROM settings')
        settings = cursor.fetchall()
        approve_time = settings[0]
        hello_message = settings[1]

        if approve_time[2] == '0':
            tim = 'сразу'
        else:
            tim = f"{approve_time[2]} сек."

        text = f"Текущее время автопринятия: {tim}"
        builder = InlineKeyboardBuilder()

        builder.button(text=f"Изменить", callback_data=f"change_approve")

        builder.button(text=f"Назад", callback_data=f"back")
        builder.adjust(1, 1)

        await bot.edit_message_text(chat_id=data.from_user.id, message_id=data.message.message_id,
                                    text=text, reply_markup=builder.as_markup())

    if data.data == 'hello_set':
        builder = InlineKeyboardBuilder()
        builder.button(text=f"Назад", callback_data=f"back")
        builder.adjust(1, 1)
        await state.set_state(Settingss.sh)

        try:
            await bot.edit_message_text(chat_id=data.from_user.id, message_id=data.message.message_id,
                                    text="Отправьте сообщение", reply_markup=builder.as_markup())
        except:
            await bot.delete_message(chat_id=data.from_user.id, message_id=data.message.message_id)
            await bot.send_message(chat_id=data.from_user.id,
                                        text="Отправьте сообщение", reply_markup=builder.as_markup())
    if data.data == "baak":
        await state.clear()
        await bot.delete_message(chat_id=data.from_user.id, message_id=data.message.message_id)
        await send_menus(chat_id=data.from_user.id, message_id=data.message.message_id)

    if data.data == "back":
        await state.clear()
        await send_menus(chat_id=data.from_user.id, message_id=data.message.message_id)


    if data.data == 'change_approve':
        text = f"Отправьте время автопринятия в секундах:\n\nПример сообщения: \n900\n\n**Если хотите чтобы бот принимал сразу то просто отправьте 0"
        builder = InlineKeyboardBuilder()

        builder.button(text=f"Назад", callback_data=f"time")
        builder.adjust(1, 1)
        await state.set_state(Settingss.we)
        await bot.edit_message_text(chat_id=data.from_user.id, message_id=data.message.message_id,
                                    text=text, reply_markup=builder.as_markup())
async def handle_options_request(request):
    response = web.Response()
    response.headers['Access-Control-Allow-Origin'] = '*'  # Разрешаем доступ из любого источника
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'  # Разрешаем методы POST и OPTIONS
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'  # Разрешаем заголовок Content-Type
    return response

async def generate_link(subid, chan_id):
    try:
        link = await bot.create_chat_invite_link(chan_id, creates_join_request=True, name=subid)
        return link
    except:
        logger.warning(f"handle flood error  " +subid)
        await bot.send_message(chat_id=ADMIN, text="Flood error  " +subid)

    # await bot.send_message(chat_id=5116638137, text=f"Received link: {link}")


app.router.add_post('/api/v2/link', handle_post_request)
app.router.add_options('/api/v2/link', handle_options_request)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    logger.info(f"Received start command from {message.from_user.username}")

    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.chat_join_request()
async def join(update: types.ChatJoinRequest):
    prepare = f"http://79.141.164.229/59e945d/postback?subid={update.invite_link.name}&status=lead&sub_id_1= " +str \
        (update.from_user.first_name ) +"&sub_id_2= " +str(update.from_user.last_name ) +"&sub_id_3= " +str \
        (update.from_user.username ) +"&sub_id_4= " +str(update.from_user.id ) +"&sub_id_25=Lead"
    response = requests.get(prepare)

    user_id = update.from_user.id
    name = update.from_user.full_name
    username = update.from_user.username
    register_time = rounded_current_time().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    approved = False
    cursor.execute('SELECT * FROM settings')
    settings = cursor.fetchall()
    # print(settings)
    approve_time = settings[0]
    if approve_time[2] == '0':
        approved = True
        await update.approve()
    if not user:
        cursor.execute('''
          INSERT INTO users (user_id, name, username, register_time, chid, approved)
          VALUES (?, ?, ?, ?, ?, ?)
          ''', (user_id, name, username, register_time, update.chat.id, approved))
        conn.commit()

    builder = InlineKeyboardBuilder()

    cursor.execute('SELECT * FROM settings')
    settings = cursor.fetchall()
    hello_message = settings[1]
    post = {"structure": json.loads(hello_message[2])}

    if post['structure']['is_media']:
        media = []
        text = None
        for type in post['structure']['types']:
            if type['type'] == 'text':
                text = type['payload']
                break
        if text == None:
            text = ''
        i = 0
        tx = text
        for type in post['structure']['types']:
            if type['type'] == 'photo':
                media.append(types.InputMediaPhoto(media=FSInputFile(type['payload']), caption=tx,
                                                   parse_mode='html'))
                tx = ''
        await bot.send_media_group(media=media)



    else:
        text = None
        for type in post['structure']['types']:
            if type['type'] == 'text':
                text = type['payload']
                break
        if text == None:
            text = ''
        i = 0
        tx = text
        photo = None
        for type in post['structure']['types']:
            if type['type'] == 'photo':
                photo = FSInputFile(type['payload'])

        texts_and_links = extract_texts_and_links(tx)
        for link in texts_and_links:
            builder.button(text=link['text'], url=link['link'])
        tx = remove_patterns(tx)
        builder.adjust(1, 1)

        if photo == None:
            await bot.send_message(chat_id=update.from_user.id, text=tx, parse_mode='html',
                                   reply_markup=builder.as_markup())

        else:
            await bot.send_photo(chat_id=update.from_user.id, caption=tx, photo=photo,
                                 parse_mode='html', reply_markup=builder.as_markup())

    # await update.answer()




#    await update.approve()

def rounded_current_time():
    now = datetime.now()
    if now.second < 30:
        return now.replace(second=0, microsecond=0)
    else:
        return (now + timedelta(minutes=1)).replace(second=0, microsecond=0)

@dp.message()
async def echo_handler(message: types.Message) -> None:
    url = "http://91.247.37.144/admin/?object=conversions.log"
    headers = {
        "Cookie": "states=v1eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6IjhkMTk0NjRiMTY3ZTZkMjljZTQ5NGFhYWRjNGJmNWZkIiwicGFzc3dvcmQiOiIlMjQyeSUyNDEwJTI0RVRscm96eW9Nai4yWnN2TGw4b2J0dTZwU3pKOVpNZHdYLjJDZXFHNDhqTlZYNDU4QmljemUiLCJ0aW1lc3RhbXAiOjE3MTQ1OTc3NTR9.AxMLCu0YqB8W_T_iYn4v-lxe027VP__RxZXPP2p4h3A; streamsView=true; streamsSharesVisible=false; keitaro=39s1lqaaorncjpc3eeh83skfv3; link=https://t.me/+5qSOoX1XfWJlZGMy; GN_USER_ID_KEY=6571c389-5f6d-4bfa-bb6f-2f3a8c7b06b3; _ga=GA1.1.152552950.1715338828; _ga_CKHN92FK43=GS1.1.1715338828.1.1.1715338853.35.0.0",
        "Content-Type": "application/json"
    }
    body = {
        "range": {
            "interval": "1_month_ago",
            "timezone": "Europe/Kyiv"
        },
        "columns": [
            "sub_id",
            "status",
            "sub_id_1",
            "sub_id_2",
            "sub_id_3",
            "sub_id_4",
            "sub_id_5"
        ],
        "metrics": [],
        "grouping": [],
        "filters": [],
        "sort": [
            {
                "name": "click_datetime",
                "order": "desc"
            }
        ],
        "summary": True,
        "limit": 10000,
        "offset": 0
    }
    print(message)
    response = requests.post(url, json=body, headers=headers)
    # result = response.json()
    # for lo in result['rows']:
    #     id = lo['sub_id_4']
    #     try:
    #         if id is not None and id != '' and int(id) == int(message.forward_from.id):
    #             await message.answer('Депозит отправлен  ' +lo['sub_id'])
    #             prepare = f"http://185.36.147.21/1001e1b/postback?subid= " +lo
    #                 ['sub_id' ] +"&status=sale&sub_id_25=Purchase"
    #             response = requests.get(prepare)
    #             return
    #             break
    #     except:
    #         await message.answer('Ошибка! У юзера скрытый аккаунт')
    #         return
    #
    # await message.answer('Данного юзера не найдено в базе')
def get_users():
    sel = f"select * from users"
    cursor.execute(sel)
    rows = cursor.fetchall()
    filtered = []
    for roww in rows:
        rrr = {'id': roww[0], 'user_id': roww[1], 'name': roww[2], 'username': roww[3], 'register_time': roww[4], 'chid': roww[5], 'approved': roww[6]}
        filtered.append(rrr)
    return filtered
async def send_scheduled_message():
    while True:
        cursor.execute('SELECT * FROM settings')
        settings = cursor.fetchall()
        approve_time = settings[0]
        secs = int(approve_time[2])
        users = get_users()
        for user in users:
            if user['approved'] == False:
                register_time = datetime.strptime(user['register_time'], '%Y-%m-%d %H:%M:%S')  # Замените формат на ваш
                adjusted_time = register_time + timedelta(seconds=secs)
                current_time = datetime.now()

                if current_time  >= adjusted_time:
                    try:
                        await bot.approve_chat_join_request(chat_id=user['chid'], user_id=user['user_id'])
                    except:
                        ""
                    cursor.execute(f"UPDATE users SET approved = true WHERE id = {user['id']};")
                    conn.commit()
                    print("approved")
        await asyncio.sleep(10)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=6778)
    await site.start()
    # And the run events dispatching
    loop = asyncio.get_event_loop()
    loop.create_task(send_scheduled_message())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


# import requests
#

#
#
#
#

