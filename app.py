#This Bot is made by Hussnain sK 
import os
import sys
import time
import json
import pickle
import random
import socket
import threading
import signal
import asyncio
import base64
import binascii
import re
import ssl
import urllib3
import jwt
import pytz
import aiohttp
import requests

from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from flask import Flask, jsonify, request
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from google.protobuf.timestamp_pb2 import Timestamp
from cfonts import render, say

from protobuf_decoder.protobuf_decoder import Parser
from xDL import *
from Pb2 import (
    DEcwHisPErMsG_pb2,
    MajoRLoGinrEs_pb2,
    PorTs_pb2,
    MajoRLoGinrEq_pb2,
    sQ_pb2,
    Team_msg_pb2
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ADMIN_UID = "16777590733"
GUEST_UID = "6071603503"
GUEST_PASSWORD = "F35F7E8DBB972368C28A89EBE92E5C2B74F4B6750AE46990B881918051FD4E33 = 'PK'

online_writer = None
whisper_writer = None
restart_requested = False
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
fast_spam_running = False
fast_spam_task = None
custom_spam_running = False
custom_spam_task = None
evo_fast_spam_running = False
evo_fast_spam_task = None
evo_custom_spam_running = False
evo_custom_spam_task = None
legendry_cycle_task = None
legendry_cycle_running = False
reject_spam_running = False
insquad = None
joining_team = False
reject_spam_task = None
lag_running = False
lag_task = None
evo_cycle_running = False
evo_cycle_task = None
auto_start_running = False
auto_start_teamcode = None
stop_auto = False
auto_start_task = None
start_spam_duration = 18
wait_after_match = 10
start_spam_delay = 0.1
spm_inv_task = None
spm_inv_running = False
emote_hijack = True
PACKET_DELAY_ULTRA_FAST = 0.2
SPAM_REQUESTS = 99
BADGE_REQUESTS = 5
exploit_running = False
exploit_instance = None

evo_emotes = {
    "1": "909000063",
    "2": "909000068",
    "3": "909000075",
    "4": "909040010",
    "5": "909000081",
    "6": "909039011",
    "7": "909000085",
    "8": "909000090",
    "9": "909000098",
    "10": "909035007",
    "11": "909042008",
    "12": "909041005",
    "13": "909033001",
    "14": "909038010",
    "15": "909038012",
    "16": "909045001",
    "17": "909049010",
    "18": "909051003"
}

EMOTE_MAP = {
    1: 909000063,
    2: 909000081,
    3: 909000075,
    4: 909000085,
    5: 909000134,
    6: 909000098,
    7: 909035007,
    8: 909051012,
    9: 909000141,
    10: 909034008,
    11: 909051015,
    12: 909041002,
    13: 909039004,
    14: 909042008,
    15: 909051014,
    16: 909039012,
    17: 909040010,
    18: 909035010,
    19: 909041005,
    20: 909051003,
    21: 909034001
}

LEGENDRY_EMOTE = {
    1: 909051013,
    2: 909051014,
    3: 909051015,
    4: 909051016,
    5: 909051017,
    6: 909051020,
    7: 909051021,
    8: 909051022,
    9: 909051023,
    10: 909052001,
    11: 909052002,
    12: 909052003,
    13: 909052004,
    14: 909052005,
    15: 909052006,
    16: 909052007,
    17: 909052008,
    18: 909052009,
    19: 909052010,
    20: 909052011,
    21: 909000037,
    22: 909000023
}

BADGE_VALUES = {
    "s1": 1048576,
    "s2": 32768,
    "s3": 2048,
    "s4": 64,
    "s5": 262144
}

def fixnum(num):
    num_str = str(num)
    return "[C]" + "[C]".join(num_str) + "[C]"

def format_date_with_month_name(date_str):
    try:
        for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y"):
            try:
                date_obj = datetime.strptime(date_str, fmt)
                return date_obj.strftime("%d %B %Y")
            except ValueError:
                continue
        return date_str
    except:
        return date_str

def dec_to_hex(decimal):
    hex_str = hex(decimal)[2:]
    return hex_str.upper() if len(hex_str) % 2 == 0 else '0' + hex_str.upper()

async def encrypt_packet(packet_hex, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    packet_bytes = bytes.fromhex(packet_hex)
    padded_packet = pad(packet_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded_packet)
    return encrypted.hex()

async def nmnmmmmn(packet_hex, key, iv):
    return await encrypt_packet(packet_hex, key, iv)

async def RoomJoin(room_id, password, key, iv):
    try:
        from Pb2.room_join_pb2 import join_room
        root = join_room()
        root.field_1 = 3
        root.field_2.field_1 = int(room_id)
        root.field_2.field_2 = str(password) if password else ""
        root.field_2.field_8.field_1 = "IDC3"
        root.field_2.field_8.field_2 = 149
        root.field_2.field_8.field_3 = "ME"
        root.field_2.field_9 = "\u0001\u0003\u0004\u0007\t\n\u000b\u0012\u000e\u0016\u0019 \u001d"
        root.field_2.field_10 = 1
        root.field_2.field_13 = 1
        root.field_2.field_14 = 1
        root.field_2.field_16 = "en"
        root.field_2.field_22.field_1 = 21
        packet_bytes = root.SerializeToString()
        packet_hex = packet_bytes.hex()
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = hex(packet_length)[2:].upper()
        if len(hex_length) % 2 != 0:
            hex_length = '0' + hex_length
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e15000000"
        final_packet_hex = header + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        return final_packet
    except Exception as e:
        return None

async def XRLeaveRoom(uid, key, iv):
    try:
        root = room_join_pb2.join_room()
        root.field_1 = 6
        nested_object = root.field_2
        nested_object.field_1 = int(uid)
        nested_object.field_8.field_1 = "IDC3"
        nested_object.field_8.field_2 = 149
        nested_object.field_8.field_3 = "BD"
        nested_object.field_9 = "\u0001\u0003\u0004\u0007\t\n\u000b\u0012\u000e\u0016\u0019 \u001d"
        nested_object.field_10 = 1
        nested_object.field_13 = 1
        nested_object.field_14 = 1
        nested_object.field_16 = "en"
        nested_object.field_22.field_1 = 21
        packet_hex = root.SerializeToString().hex()
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        packet_len_hex = await base_to_hex(packet_length)
        if len(packet_len_hex) == 2:
            header = "0e15000000"
        elif len(packet_len_hex) == 3:
            header = "0e1500000"
        elif len(packet_len_hex) == 4:
            header = "0e150000"
        elif len(packet_len_hex) == 5:
            header = "0e15000"
        final_packet = header + packet_len_hex + encrypted_packet
        return bytes.fromhex(final_packet)
    except Exception as e:
        return None

def get_idroom_by_idplayer(packet_hex):
    try:
        json_result = get_available_room(packet_hex)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        idroom = data['15']["data"]
        return idroom
    except Exception as e:
        return None

async def Look_Changer(bundle_id, key, iv, look_type=1, region="ind"):
    fields = {
        1: 88,
        2: {
            1: {
                1: bundle_id,
                2: look_type
            },
            2: 2
        }
    }
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    encrypted = await encrypt_packet(packet_hex, key, iv)
    header_length = len(encrypted) // 2
    header_length_hex = await DecodE_HeX(header_length)
    if region.lower() == "ind":
        packet_type = "0514"
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    if len(header_length_hex) == 2:
        final_header = f"{packet_type}000000"
    elif len(header_length_hex) == 3:
        final_header = f"{packet_type}00000"
    elif len(header_length_hex) == 4:
        final_header = f"{packet_type}0000"
    elif len(header_length_hex) == 5:
        final_header = f"{packet_type}000"
    else:
        final_header = f"{packet_type}000000"
    final_packet_hex = final_header + header_length_hex + encrypted
    return bytes.fromhex(final_packet_hex)

async def check_player_in_room(target_uid, key, iv):
    try:
        status_packet = await GeT_Status(int(target_uid), key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
        return True
    except Exception as e:
        return False

async def ArohiAccepted(uid, code, K, V):
    fields = {
        1: 4,
        2: {
            1: uid,
            3: uid,
            8: 1,
            9: {
                2: 161,
                4: "y[WW",
                6: 11,
                8: "1.114.18",
                9: 3,
                10: 1
            },
            10: str(code),
        }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0515', K, V)

async def get_nickname_from_api(uid):
    url = f"https://infoooooo-v6v5.vercel.app/accinfo?uid={uid}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as res:
                data = await res.json(content_type=None)
                return data.get("basicInfo", {}).get("nickname", "User")
    except Exception as e:
        return "User"

async def detect_and_hijack_emote(data_hex, key, iv, bot_uid, region):
    try:
        emote_info = await extract_emote_info(data_hex, key, iv)
        if not emote_info or not emote_info.get('sender_uid'):
            return False
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        if int(sender_uid) == bot_uid:
            return False
        hijack_packet = await Emote_k(int(bot_uid), int(emote_id), key, iv, region)
        if hijack_packet and online_writer:
            online_writer.write(hijack_packet)
            await online_writer.drain()
            return True
        return False
    except Exception as e:
        return False

async def create_hijacked_emote(hijacker_uid, emote_id, key, iv, region):
    try:
        fields = {
            1: 21,
            2: {
                1: 804266360,
                2: 909000001,
                5: {
                    1: int(hijacker_uid),
                    3: int(emote_id),
                }
            }
        }
        if region.lower() == "ind":
            packet = '0514'
        elif region.lower() == "bd":
            packet = "0519"
        else:
            packet = "0515"
        return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet, key, iv)
    except Exception as e:
        return None

async def hijack_squad_emote(data_hex, key, iv, bot_uid, region, in_squad):
    if not in_squad:
        return False
    try:
        emote_info = await extract_emote_info(data_hex, key, iv)
        if not emote_info:
            return False
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        hijack_packet = await create_hijacked_emote(bot_uid, emote_id, key, iv, region)
        if hijack_packet and online_writer:
            online_writer.write(hijack_packet)
            await online_writer.drain()
            await asyncio.sleep(0.3)
            original_packet = await Emote_k(int(sender_uid), int(emote_id), key, iv, region)
            online_writer.write(original_packet)
            await online_writer.drain()
            return True
    except Exception as e:
        return False

def extract_type_5(packet_json):
    if packet_json.get('1') == 5:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('4', {}).get('data')
                if sender:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id or 909000063,
                        'packet_type': 5,
                        'confidence': 'medium'
                    }
        except:
            pass
    return None

async def extract_emote_info(data_hex, key, iv):
    try:
        packet = await DeCode_PackEt(data_hex[10:])
        packet_json = json.loads(packet)
        structures = [
            lambda: extract_type_21(packet_json),
            lambda: extract_type_26(packet_json),
            lambda: extract_type_5(packet_json),
            lambda: generic_extract(packet_json)
        ]
        for extractor in structures:
            info = extractor()
            if info and info.get('sender_uid'):
                return info
        return None
    except Exception as e:
        return None

def extract_type_21(packet_json):
    if packet_json.get('1') == 21:
        try:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '5' in packet_json['2']['data'] and 'data' in packet_json['2']['data']['5']):
                data = packet_json['2']['data']
                nested = data['5']['data']
                sender = nested.get('1', {}).get('data')
                emote_id = nested.get('3', {}).get('data')
                if sender and emote_id:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id,
                        'packet_type': 21,
                        'confidence': 'high'
                    }
        except:
            pass
    return None

def extract_type_26(packet_json):
    if packet_json.get('1') == 26:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('2', {}).get('data')
                if sender and emote_id:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id,
                        'packet_type': 26,
                        'confidence': 'high'
                    }
        except:
            pass
    return None

def generic_extract(packet_json):
    uid = None
    emote_id = None
    def search(obj):
        nonlocal uid, emote_id
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'data' and isinstance(v, (int, str)) and str(v).isdigit():
                    num = int(v)
                    if 1000000 < num < 99999999999 and uid is None:
                        uid = num
                    if str(v).startswith('909') and len(str(v)) >= 9:
                        emote_id = num
                elif isinstance(v, dict):
                    search(v)
                elif isinstance(v, list):
                    for item in v:
                        search(item)
    search(packet_json)
    if uid:
        return {
            'sender_uid': uid,
            'emote_id': emote_id if emote_id else get_random_evo_emote(),
            'packet_type': 'generic',
            'confidence': 'medium'
        }
    return None

async def get_account_token(uid, password):
    try:
        url = "https://100067.connect.garena.com/oauth/guest/token/grant"
        headers = {
            "Host": "100067.connect.garena.com",
            "User-Agent": await Ua(),
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "close"
        }
        data = {
            "uid": uid,
            "password": password,
            "response_type": "token",
            "client_type": "2",
            "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
            "client_id": "100067"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=data) as response:
                if response.status == 200:
                    data = await response.json()
                    open_id = data.get("open_id")
                    access_token = data.get("access_token")
                    return open_id, access_token
        return None, None
    except Exception as e:
        return None, None

async def send_join_from_account(target_uid, account_uid, password, key, iv, region):
    try:
        open_id, access_token = await get_account_token(account_uid, password)
        if not open_id or not access_token:
            return False
        join_packet = await create_account_join_packet(target_uid, account_uid, open_id, access_token, key, iv, region)
        if join_packet:
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            return True
        return False
    except Exception as e:
        return False

async def SEnd_InV_with_Cosmetics(Nu, Uid, K, V, region):
    region = "ind"
    fields = {
        1: 2,
        2: {
            1: int(Uid),
            2: region,
            4: int(Nu),
            5: {
                1: "BOT",
                2: int(get_random_avatar()),
                5: random.choice([1048576, 32768, 2048]),
            }
        }
    }
    if region.lower() == "ind":
        packet = '0514'
    elif region.lower() == "bd":
        packet = "0519"
    else:
        packet = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet, K, V)

async def leave_squad(key, iv, region):
    fields = {
        1: 7,
        2: {
            1: 12480598706
        }
    }
    packet = (await CrEaTe_ProTo(fields)).hex()
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk(packet, packet_type, key, iv)

async def RedZed_SendInv(bot_uid, uid, key, iv):
    try:
        fields = {
            1: 33,
            2: {
                1: int(uid),
                2: "IND",
                3: 1,
                4: 1,
                6: "RedZedKing!!",
                7: 330,
                8: 1000,
                9: 100,
                10: "DZ",
                12: 1,
                13: int(uid),
                16: 1,
                17: {
                    2: 159,
                    4: "y[WW",
                    6: 11,
                    8: "1.120.1",
                    9: 3,
                    10: 1
                },
                18: 306,
                19: 18,
                24: 902000306,
                26: {},
                27: {
                    1: 11,
                    2: int(bot_uid),
                    3: 99999999999
                },
                28: {},
                31: {
                    1: 1,
                    2: 32768
                },
                32: 32768,
                34: {
                    1: bot_uid,
                    2: 8,
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                }
            }
        }
        if isinstance(fields[2][34][3], str):
            fields[2][34][3] = b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
        packet = await CrEaTe_ProTo(fields)
        packet_hex = packet.hex()
        final_packet = await GeneRaTePk(packet_hex, '0515', key, iv)
        return final_packet
    except Exception as e:
        return None

async def request_join_with_badge(target_uid, badge_value, key, iv, region):
    fields = {
        1: 33,
        2: {
            1: int(target_uid),
            2: region.upper(),
            3: 1,
            4: 1,
            5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
            6: "iG:[C][B][FF0000] starzzff08",
            7: 330,
            8: 1000,
            10: region.upper(),
            11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                       97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
            12: 1,
            13: int(target_uid),
            14: {
                1: 2203434355,
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            16: 1,
            17: 1,
            18: 312,
            19: 46,
            23: bytes([16, 1, 24, 1]),
            24: int(get_random_avatar()),
            26: "",
            28: "",
            31: {
                1: 1,
                2: int(badge_value)
            },
            32: int(badge_value),
            34: {
                1: int(target_uid),
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        },
        10: "en",
        13: {
            2: 1,
            3: 1
        }
    }
    packet = (await CrEaTe_ProTo(fields)).hex()
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk(packet, packet_type, key, iv)

async def start_auto_packet(key, iv, region):
    fields = {
        1: 9,
        2: {
            1: 12480598706,
        },
    }
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def leave_squad_packet(key, iv, region):
    fields = {
        1: 7,
        2: {
            1: 12480598706,
        },
    }
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def join_teamcode_packet(team_code, key, iv, region):
    fields = {
        1: 4,
        2: {
            4: bytes.fromhex("01090a0b121920"),
            5: str(team_code),
            6: 6,
            8: 1,
            9: {
                2: 800,
                6: 11,
                8: "1.111.1",
                9: 5,
                10: 1
            }
        }
    }
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def auto_start_loop(team_code, uid, chat_id, chat_type, key, iv, region):
    global auto_start_running, stop_auto
    while not stop_auto:
        try:
            status_msg = f"[B][C][FFA500]🤖 Auto Start Bot\n🎯 Team: {team_code}\n⚡ Joining team..."
            await dl_send_message(chat_type, status_msg, uid, chat_id, key, iv)
            join_packet = await join_teamcode_packet(team_code, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            await asyncio.sleep(2)
            start_msg = f"[B][C][00FF00]✅ Joined team {team_code}\n🎯 Starting match for {start_spam_duration} seconds..."
            await dl_send_message(chat_type, start_msg, uid, chat_id, key, iv)
            start_packet = await start_auto_packet(key, iv, region)
            end_time = time.time() + start_spam_duration
            while time.time() < end_time and not stop_auto:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                await asyncio.sleep(start_spam_delay)
            if stop_auto:
                break
            wait_msg = f"[B][C][FFFF00]⏳ Match started! Bot in lobby waiting {wait_after_match} seconds..."
            await dl_send_message(chat_type, wait_msg, uid, chat_id, key, iv)
            waited = 0
            while waited < wait_after_match and not stop_auto:
                await asyncio.sleep(1)
                waited += 1
            if stop_auto:
                break
            leave_msg = f"[B][C][FF0000]🔄 Leaving team {team_code} to rejoin and start again..."
            await dl_send_message(chat_type, leave_msg, uid, chat_id, key, iv)
            leave_packet = await leave_squad_packet(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            await asyncio.sleep(2)
        except Exception as e:
            error_msg = f"[B][C][FF0000]❌ Auto start error: {str(e)}\n"
            await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            break
    auto_start_running = False
    stop_auto = False

async def reset_bot_state(key, iv, region):
    try:
        leave_packet = await leave_squad(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.5)
        return True
    except Exception as e:
        return False

async def handle_badge_command(cmd, inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    parts = inPuTMsG.strip().split()
    if len(parts) < 2:
        error_msg = f"[B][C][FF0000]❌ Usage: /{cmd} (uid)\nExample: /{cmd} 123456789\n"
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    target_uid = parts[1]
    badge_value = BADGE_VALUES.get(cmd, 1048576)
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF0000]❌ Please write a valid player ID!\n"
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    total_requests = BADGE_REQUESTS
    packet_delay = PACKET_DELAY_ULTRA_FAST
    badge_names = {
        's1': 'Craftland Badge 🏆',
        's2': 'New V-Badge 🔥',
        's3': 'Moderator Badge 👮',
        's4': 'Small V-Badge ⚡',
        's5': 'Pro Badge 💎'
    }
    badge_name = badge_names.get(cmd, 'Unknown Badge')
    initial_msg = f"[B][C][1E90FF]🌀 {badge_name}\n🎯 Target: {target_uid}\n📦 Requests: {total_requests}\n⚡ Speed: {packet_delay}s\n"
    await dl_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    try:
        await reset_bot_state(key, iv, region)
        await asyncio.sleep(0.3)
        join_packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
        for i in range(total_requests):
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            await asyncio.sleep(packet_delay)
        success_msg = f"[B][C][00FF00]✅ {badge_name} COMPLETE!\n🎯 Target: {target_uid}\n📦 Sent: {total_requests} requests\n⚡ Speed: {packet_delay}s\n"
        await dl_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        await reset_bot_state(key, iv, region)
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error in /{cmd}: {str(e)}\n"
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_emote_list_command(uid, chat_id, chat_type, key, iv):
    part1 = """[B][C][00FF00]Emotes List - Part 1/8:
[FFFFFF]p90 , m60 , mp5 , groza , thompson_evo
[FFFFFF]m10_red , mp40_blue , m10_green , xm8 , ak
[FFFFFF]mp40 , m4a1 , famas , scar , ump , m18
[FFFFFF]fist , g18 , an94 , woodpecker , money , heart
[FFFFFF]rose , throne , pirate , car , cobra , ghost
[FFFFFF]sholay , blade , hello , dab , chicken , dance
[FFFFFF]babyshark , pushup , dragon , highfive , selfie
[FFFFFF]breakdance , kungfu , thor , rasengan , ninja"""
    part2 = """[B][C][00FF00]Emotes List - Part 2/8:
[FFFFFF]clone , fireball , hammer , valentineheart , rampagebook
[FFFFFF]guildflag , fish , inosuke , mummydance , shuffling
[FFFFFF]dangerousgame , jaguardance , threaten , shakewithme
[FFFFFF]devilsmove , furiousslam , moonflip , wigglewalk
[FFFFFF]battledance , shakeitup , gloriousspin , cranekick
[FFFFFF]partydance , jigdance , soulshaking , healingdance
[FFFFFF]topdj , deathglare , powerofmoney , eatmydust
[FFFFFF]bonappetit , aimfire , swan , teatime , bringiton
[FFFFFF]whyohwhy , fancyhands , shimmy , doggie , challengeon"""
    part3 = """[B][C][00FF00]Emotes List - Part 3/8:
[FFFFFF]lasso , imrich , morepractice , ffws2021 , dracossoul
[FFFFFF]goodgame , greetings , walker , bornoflight , mythosfour
[FFFFFF]championgrab , winandchill , hadouken , bloodwraith
[FFFFFF]bigsmash , fancysteps , allincontrol , debugging , waggorwave
[FFFFFF]crazyguitar , poof , chosenvictor , challenger , partygame5
[FFFFFF]partygame6 , partygame3 , partygame4 , partygame7
[FFFFFF]partygame1 , partygame8 , partygame2 , dribbleking
[FFFFFF]ffwsguitar , mindit , goldencombo , sickmoves , rapswag
[FFFFFF]battleinstyle , rulersflag , moneythrow , endlessbullets"""
    part4 = """[B][C][00FF00]Emotes List - Part 4/8:
[FFFFFF]smoothsway , number1 , fireslam , heartbroken
[FFFFFF]rockpaperscissors , shatteredreality , haloofmusic
[FFFFFF]burntbbq , switchingsteps , creedslay , leapoffail
[FFFFFF]rhythmgirl , helicoptership , kungfutigers , possessedwarrior
[FFFFFF]raiseyourthumb , fireborn , goldenfeather , comeanddance
[FFFFFF]dropkick , sitdown , booyahsparks , ffwsdance , easypeasy
[FFFFFF]winnerthrow , weightofvictory , chronicle , collapse
[FFFFFF]flaminggroove , energetic , ridicule , teasewaggor
[FFFFFF]greatconductor , fakedeath , twerk , brheroic , brmaster
[FFFFFF]csheroic , csmaster , yesido , freemoney , singersb03"""
    part5 = """[B][C][00FF00]Emotes List - Part 5/8:
[FFFFFF]singersb0203 , singersb010203 , victoriouseagle , flyingsaucer
[FFFFFF]weaponmagician , bobbledance , weighttraining , beautifullove
[FFFFFF]groovemoves , howlersrage , louderplease , ninjastand
[FFFFFF]creatorinaction , ghostfloat , shibasurf , waiterwalk
[FFFFFF]grafficameraman , agileboxer , sunbathing , skateboardswag
[FFFFFF]phantomtamer , signal , eternaldescent , swaggydance , admire
[FFFFFF]reindeerfloat , bamboodance , constellationdance , trophygrab
[FFFFFF]starryhands , yum , happydancing , juggle , neonsign
[FFFFFF]beasttease , drachentear , clapdance , influencer , macarena
[FFFFFF]technoblast , valentine , angrywalk , makesomenoise , crocohooray"""
    part6 = """[B][C][00FF00]Emotes List - Part 6/8:
[FFFFFF]scorpionspin , cindersummon , shallwedance , spinmaster
[FFFFFF]festival , artisticdance , forwardbackward , scorpionfriend
[FFFFFF]achingpower , earthlyforce , grenademagic , ohyeah
[FFFFFF]graceonwheels , flex , firebeasttamer , crimsontunes
[FFFFFF]swaggyvsteps , chromaticfinish , smashthefeather , sonoroussteps
[FFFFFF]chromaticpop , chromatwist , birthofjustice , spidersense
[FFFFFF]chromasonicshot , playwiththunderbolt , anniversary , wisdomswing
[FFFFFF]thunderflash , whirlpool , flyinginksword , dancepuppet
[FFFFFF]highknees , feeltheelectricity , whacacotton , honorablemention
[FFFFFF]brgrandmaster , csgm , monsterclubbing , basudaradance"""
    part7 = """[B][C][00FF00]Emotes List - Part 7/8:
[FFFFFF]stirfryfrostfire , moneyrain , frostfirecalling , stompingfoot
[FFFFFF]thisway , excellentservice , lvl100 , realtiger , celebrationschuss
[FFFFFF]dawnvoyage , lamborghiniride , toiletman , handgrooves , kemusan
[FFFFFF]ribbitrider , innerself , emperortreasure , whysochaos , hugefeast
[FFFFFF]colorburst , dragonswipe , samba , speedsummon , whatamatch
[FFFFFF]whatapair , bytemounting , unicyclist , basketrafting , happylamb
[FFFFFF]paradox , harmoniousparadox , raiseyourthumb2 , claphands
[FFFFFF]donedeal , starcatcher , paradoxwings , zombified , honkup
[FFFFFF]cyclone , springrocker , giddyup , goosydance , captainvictor
[FFFFFF]youknowimgood , stepstep , superyay , moonwalk , flowersalute"""
    part8 = """[B][C][00FF00]Emotes List - Part 8/8:
[FFFFFF]foxyrun , waggorsseesaw , floatingmeditation , naatunaatu
[FFFFFF]championswalk , auraboarder , booyahchamp , controlledcombustion
[FFFFFF]cheerstovictory , shoeshining , gunspinning , crowdpleaser
[FFFFFF]nosweat , magmaquake , maxfirepower , canttouchthis , firestarter
[FFFFFF]ffwsflag , beatdrop , spatialawareness , trapping , soaringup
[FFFFFF]wontbowdown , aurora , couchfortwo , flutterdash , slipperythrone
[FFFFFF]acceptancespeech , lovemelovemenot , scissorsavvy , thinker
[FFFFFF]matchcountdown , hiptwists , jkt48 , stormyascent , thousandyears
[FFFFFF]ninjasign , ninjarun , clonejutsu , rescue , midnightperuse
[FFFFFF]guitargroove , keyboardplayer , ondrums , chacchac , pillowfight
[FFFFFF]targetpractice , goofycamel , hitasix , flagsummon , swiftsteps
[FFFFFF]carnivalfunk , slurp , paint , halftime , throwin , bailalorocky
[FFFFFF]bigdill , handraise , owl , slapandtwist , sidewiggle , creationdays
[FFFFFF]rainingcoins , clapclaphooray , infiniteloops , p90surfer , boxingmachine
[FFFFFF]flyingguns , comicbarf , driveby , pedalmetal , spearspin , guildflag
[FFFFFF]discodazzle , squatchallenge , winninggoal , headhigh , ninjasummon
[FFFFFF]finalbattle , foreheadpoke , fireballjutsu , flyingraijin , thor
[FFFFFF]circle , drumtwirl , bunnyaction , broomswoosh , bladefromheart
[FFFFFF]mapread , tomato , tacticalmoveout , bunnywiggle , flamingheart
[FFFFFF]rainorshine , sholay , peakpoints , dream , angelic , shower
[FFFFFF]motorbike , bow , petals , puffyride"""
    await dl_send_message(chat_type, part1, uid, chat_id, key, iv)
    await asyncio.sleep(0.2)
    await dl_send_message(chat_type, part2, uid, chat_id, key, iv)
    await asyncio.sleep(0.2)
    await dl_send_message(chat_type, part3, uid, chat_id, key, iv)
    await asyncio.sleep(0.2)
    await dl_send_message(chat_type, part4, uid, chat_id, key, iv)
    await asyncio.sleep(0.2)
    await dl_send_message(chat_type, part5, uid, chat_id, key, iv)
    await asyncio.sleep(0.2)
    await dl_send_message(chat_type, part6, uid, chat_id, key, iv)
    await asyncio.sleep(0.2)
    await dl_send_message(chat_type, part7, uid, chat_id, key, iv)
    await asyncio.sleep(0.2)
    await dl_send_message(chat_type, part8, uid, chat_id, key, iv)

async def create_authenticated_join(target_uid, account_uid, key, iv, region):
    try:
        join_packet = await SEnd_InV(5, int(target_uid), key, iv, region)
        return join_packet
    except Exception as e:
        return None

async def create_account_join_packet(target_uid, account_uid, open_id, access_token, key, iv, region):
    try:
        fields = {
            1: 33,
            2: {
                1: int(target_uid),
                2: region.upper(),
                3: 1,
                4: 1,
                5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
                6: f"BOT:[C][B][FF0000] ACCOUNT_{account_uid[-4:]}",
                7: 330,
                8: 1000,
                10: region.upper(),
                11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                           97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
                12: 1,
                13: int(account_uid),
                14: {
                    1: 2203434355,
                    2: 8,
                    3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
                },
                16: 1,
                17: 1,
                18: 312,
                19: 46,
                23: bytes([16, 1, 24, 1]),
                24: int(get_random_avatar()),
                26: "",
                28: "",
                31: {
                    1: 1,
                    2: 32768
                },
                32: 32768,
                34: {
                    1: int(account_uid),
                    2: 8,
                    3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
                }
            },
            10: "en",
            13: {
                2: 1,
                3: 1
            }
        }
        packet = (await CrEaTe_ProTo(fields)).hex()
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
        return await GeneRaTePk(packet, packet_type, key, iv)
    except Exception as e:
        return None

async def auto_hammer_slam_emote_dual(sender_uid, key, iv, region):
    try:
        hammer_slam_emote_id = 909050008
        bot_uid = 14572471551
        emote_to_sender = await Emote_k(int(sender_uid), hammer_slam_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
        await asyncio.sleep(0.5)
        emote_to_bot = await Emote_k(int(bot_uid), hammer_slam_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_bot)
    except Exception as e:
        pass

async def Room_Spam(Uid, Rm, Nm, K, V):
    badge_sequence = [1048576, 32768, 2048, 64, 262144]
    badge_index = 0
    for i in range(SPAM_REQUESTS):
        try:
            current_badge_value = badge_sequence[badge_index % 5]
            fields = {
                1: 78,
                2: {
                    1: int(Rm),
                    2: "iG:[C][B][FF0000]STAR GAMER",
                    3: {2: 1, 3: 1},
                    4: 330,
                    5: 6000,
                    6: 201,
                    10: int(get_random_avatar()),
                    11: int(Uid),
                    12: 1,
                    15: {1: 1, 2: current_badge_value},
                    16: current_badge_value,
                    18: {
                        1: 11481904755,
                        2: 8,
                        3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
                    },
                    31: {1: 1, 2: current_badge_value},
                    32: current_badge_value,
                    34: {
                        1: int(Uid),
                        2: 8,
                        3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
                    }
                }
            }
            spam_packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0e15', K, V)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
            badge_index += 1
            await asyncio.sleep(PACKET_DELAY_ULTRA_FAST)
        except Exception as e:
            await asyncio.sleep(0.1)
    return True

async def evo_cycle_spam(uids, key, iv, region):
    global evo_cycle_running
    cycle_count = 0
    emote_numbers = list(evo_emotes.keys())
    while evo_cycle_running:
        cycle_count += 1
        uid_emote_mapping = {}
        for uid in uids:
            shuffled = emote_numbers.copy()
            random.shuffle(shuffled)
            uid_emote_mapping[uid] = shuffled
        for idx in range(len(emote_numbers)):
            if not evo_cycle_running:
                break
            for uid in uids:
                try:
                    uid_int = int(uid)
                    emote_number = uid_emote_mapping[uid][idx]
                    emote_id = evo_emotes[emote_number]
                    H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                except Exception as e:
                    pass
            if evo_cycle_running:
                for i in range(5):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
        if evo_cycle_running:
            await asyncio.sleep(2)

async def legendry_emote_cycle(uids, key, iv, region):
    global legendry_cycle_running
    cycle_count = 0
    emote_numbers = list(LEGENDRY_EMOTE.keys())
    while legendry_cycle_running:
        cycle_count += 1
        uid_emote_mapping = {}
        for uid in uids:
            shuffled = emote_numbers.copy()
            random.shuffle(shuffled)
            uid_emote_mapping[uid] = shuffled
        for idx in range(len(emote_numbers)):
            if not legendry_cycle_running:
                break
            for uid in uids:
                try:
                    uid_int = int(uid)
                    emote_number = uid_emote_mapping[uid][idx]
                    emote_id = LEGENDRY_EMOTE[emote_number]
                    H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                except Exception as e:
                    pass
            if legendry_cycle_running:
                for _ in range(5):
                    if not legendry_cycle_running:
                        break
                    await asyncio.sleep(1)
        if legendry_cycle_running:
            await asyncio.sleep(2)

async def reject_spam_loop(target_uid, key, iv):
    global reject_spam_running
    count = 0
    max_spam = 150
    while reject_spam_running and count < max_spam:
        try:
            packet1 = await DEVIL1(target_uid, key, iv)
            packet2 = await DEVIL(target_uid, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet1)
            await asyncio.sleep(0.1)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet2)
            count += 1
            await asyncio.sleep(0.2)
        except Exception as e:
            break
    return count

async def handle_reject_completion(spam_task, target_uid, sender_uid, chat_id, chat_type, key, iv):
    try:
        spam_count = await spam_task
        if spam_count >= 150:
            completion_msg = f"[B][C][00FF00]✅ Reject Spam Completed Successfully for ID {target_uid}\n✅ Total packets sent: {spam_count * 2}\n"
        else:
            completion_msg = f"[B][C][FFFF00]⚠️ Reject Spam Partially Completed for ID {target_uid}\n⚠️ Total packets sent: {spam_count * 2}\n"
        await dl_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
    except asyncio.CancelledError:
        pass
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ ERROR in reject spam: {str(e)}\n"
        await dl_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)

async def base_to_hex(number):
    hex_str = hex(number)[2:]
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
    return hex_str.upper()

async def DEVIL(client_id, key, iv):
    banner_text = f""" 
.
.
.










    
[B][C][00FF00]★ H U S S N A I N    SK★
[FF0000]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][FF9900]D O N E   H A C K I N G
[B][C][E75480]Y O U R   A C C O U N T
[81DACA]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][FF0000]F U C K   Y O U
[CCFFCC]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][81DACA]P O W E R E D   B Y   HUSSNAIN  SK
[FFFF00]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][00FF00]F O L L O W   M E   O N   T I K T O K
[B][C][FFFFFF]@dark_reality
[00008B]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][81DACA]I F   Y O U   D O N T   F O L L O W   M E
[B][C][FF0000]I   W I L L   B A N   Y O U R   A C C O U N T
        """
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    return bytes.fromhex(final_packet)

async def DEVIL1(client_id, key, iv):
    gay_text = f""" 
.
.
.










    
[B][C][00FF00]★ H U S S N A I N   SK★
[FF0000]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][FF9900]D O N E   H A C K I N G
[B][C][E75480]Y O U R   A C C O U N T
[81DACA]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][FF0000]F U C K   Y O U
[CCFFCC]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][81DACA]P O W E R E D   B Y     H U S S N A I N   SK
[FFFF00]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][00FF00]F O L L O W   M E   O N   I N S T A G R A M
[B][C][FFFFFF]@dark_reality
[00008B]━━━━━━━━━━━━━━━━━━━━━━━━━━
[B][C][81DACA]I F   Y O U   D O N T   F O L L O W   M E
[B][C][FF0000]I   W I L L   B A N   Y O U R   A C C O U N T
        """
    fields = {
        1: int(client_id),
        2: 5,
        4: 50,
        5: {
            1: int(client_id),
            2: gay_text,
        }
    }
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    return bytes.fromhex(final_packet)

async def lag_team_loop(team_code, key, iv, region):
    global lag_running
    count = 0
    MAX_CYCLES = 800
    while lag_running and count < MAX_CYCLES:
        try:
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            await asyncio.sleep(0.01)
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            count += 1
            await asyncio.sleep(0.01)
        except Exception as e:
            await asyncio.sleep(0.1)
    lag_running = False

def get_ghost_api(team_code, ghost_name):
    try:
        if not ghost_name:
            return "❌ Error: Ghost name required!"
        url = f"http://n4.nexcloud.in:2036/kx?teamcode={team_code}&ghostname={ghost_name}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            return data if data else "No response from server."
        else:
            return f"Failed! Status code: {res.status_code}"
    except Exception as e:
        return f"Error: {e}"

def send_like(target_uid):
    try:
        url = f"https://stargvhuuvjpy.vercel.app/like?uid={uid}&server_name=ind"
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return "[C][B][FF0000]Failed to send like (API error)."
        data = res.json()
        likes_given = int(data.get("LikesGivenByAPI", 0))
        raw_uid = str(data.get("UID", target_uid))
        styled_uid = fixnum(raw_uid)
        if likes_given <= 0:
            return (
                f"[C][B][FFA500]Max likes already sent today.\n"
                f"[C][B][FFFFFF]🆔 UID: {styled_uid}"
            )
        return (
            f"[C][B]-┌ [FFD700]Like Sent Successfully:\n"
            f"[FFFFFF]-├─ Name: {data.get('PlayerNickname', 'N/A')}\n"
            f"- ├─ UID: {styled_uid}\n"
            f"- ├─ Likes Before: {data.get('LikesbeforeCommand', 'N/A')}\n"
            f"- ├─ Likes Given: {data.get('LikesGivenByAPI', '0')}\n"
            f"- └─ Likes After: {data.get('LikesafterCommand', 'N/A')}"
        )
    except Exception as e:
        return f"[C][B][FF0000]Error: {e}"

async def fetch_player_info(session, uid):
    url = f"https://infoooooo-v6v5.vercel.app/accinfo?uid={uid}&region=ind"
    async with session.get(url) as resp:
        if resp.status != 200:
            return None
        return await resp.json()

async def fetch_guild_info(session, guild_id, region="ind"):
    url = f"https://guild-info-danger.vercel.app/guild?guild_id={guild_id}&region={region}"
    async with session.get(url) as resp:
        if resp.status != 200:
            return None
        return await resp.json()

def _fmt_ts(ts):
    try:
        d = datetime.fromtimestamp(int(ts))
        return f"{fixnum(str(d.day))} {d.strftime('%B')} {fixnum(str(d.year))}"
    except:
        return "Unknown"

def _fmt_dt(dt):
    try:
        d = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
        return f"{fixnum(str(d.day))} {d.strftime('%B')} {fixnum(str(d.year))}"
    except:
        return dt

def format_player_info(data):
    b = data.get("basicInfo", {})
    s = data.get("socialInfo", {})
    return (
        f"[C][B]-┌ [FFD700]📱 Player Info:\n"
        f"[FFFFFF]-├─ Name: [00FF00]{b.get('nickname','N/A')}\n"
        f"[FFFFFF]-├─ UID: [00FF00]{fixnum(b.get('accountId','N/A'))}\n"
        f"[FFFFFF]-├─ Level: [00FF00]{fixnum(str(b.get('level','N/A')))}\n"
        f"[FFFFFF]-├─ Likes: [00FF00]{fixnum(str(b.get('liked','N/A')))}\n"
        f"[FFFFFF]-├─ Bio: [00FF00]{s.get('socialHighlight','N/A')}\n"
        f"[FFFFFF]-├─ Created: [00FF00]{_fmt_ts(b.get('createAt'))}\n"
        f"[FFFFFF]-└─ Last Login: [00FF00]{_fmt_ts(b.get('lastLoginAt'))}"
    )

def format_guild_basic_info(g):
    if not g or g.get("status") != "success":
        return None
    return (
        f"[C][B]-┌ [00FF00]🏰 Guild Info:\n"
        f"[FFFFFF]-├─ Name: [00FF00]{g.get('guild_name','N/A')}\n"
        f"[FFFFFF]-├─ ID: [00FF00]{fixnum(str(g.get('guild_id','N/A')))}\n"
        f"[FFFFFF]-├─ Region: [00FF00]{g.get('guild_region','N/A')}\n"
        f"[FFFFFF]-├─ Level: [00FF00]{fixnum(str(g.get('guild_level','N/A')))}\n"
        f"[FFFFFF]-├─ Members: [00FF00]{fixnum(str(g.get('current_members','0')))}"
        f"/{fixnum(str(g.get('max_members','0')))}\n"
        f"[FFFFFF]-├─ Slogan: [00FF00]{g.get('guild_slogan','N/A')}\n"
        f"[FFFFFF]-├─ Created: [00FF00]{_fmt_dt(g.get('creation_time','N/A'))}\n"
        f"[FFFFFF]-├─ Last Updated: [00FF00]{_fmt_dt(g.get('last_updated','N/A'))}\n"
        f"[FFFFFF]-├─ Total Activity: [00FF00]{fixnum(str(g.get('total_activity_points','0')))}\n"
        f"[FFFFFF]-└─ Weekly Activity: [00FF00]{fixnum(str(g.get('weekly_activity_points','0')))}"
    )

def format_guild_leader_info(g):
    l = g.get("guild_leader")
    if not l:
        return None
    return (
        f"[C][B]-┌ [FF69B4]👑 Guild Leader:\n"
        f"[FFFFFF]-├─ Name: [FFD700]{l.get('name','N/A')}\n"
        f"[FFFFFF]-├─ UID: [FFD700]{fixnum(l.get('uid','N/A'))}\n"
        f"[FFFFFF]-├─ Level: [FFD700]{fixnum(str(l.get('level','N/A')))}\n"
        f"[FFFFFF]-└─ Likes: [FFD700]{fixnum(str(l.get('likes','N/A')))}"
    )

def format_single_officer(officer):
    return (
        f"[C][B]-┌ [FFFF00]👮 Guild Officer:\n"
        f"[FFFFFF]-├─ Name: [00FF00]{officer.get('name','N/A')}\n"
        f"[FFFFFF]-├─ UID: [00FF00]{fixnum(officer.get('uid','N/A'))}\n"
        f"[FFFFFF]-├─ Level: [00FF00]{fixnum(str(officer.get('level','N/A')))}\n"
        f"[FFFFFF]-└─ Likes: [00FF00]{fixnum(str(officer.get('likes','N/A')))}"
    )

def format_guild_notice_info(g):
    if not g.get("last_notice_change"):
        return None
    return (
        f"[C][B]-┌ [00FFFF]📢 Guild Notice:\n"
        f"[FFFFFF]-└─ Notice updated (content not available)"
    )

def add_friend(target_uid):
    try:
        url = f"https://kallu-friend-management.vercel.app/adding_friend?uid={GUEST_UID}&password={GUEST_PASSWORD}&friend_uid={target_uid}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            if data.get("status") == "success":
                return f"✅ Friend request sent successfully !"
            else:
                return f"❌ Failed to send friend request: {data.get('message', 'Unknown error')}"
        else:
            return f"❌ Failed to call API. Status code: {res.status_code}"
    except Exception as e:
        return f"❌ Error occurred: {e}"

def join_guild(guild_id):
    try:
        url = f"https://guild-info-danger.vercel.app/join?guild_id={guild_id}&uid={GUEST_UID}&password={GUEST_PASSWORD}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            message = data.get("message", "")
            if data.get("status") == "success" or "sent successfully" in message.lower():
                return f"✅ Guild join request sent successfully!"
            else:
                return f"❌ Failed to join guild: {message or 'Unknown error'}"
        else:
            return f"❌ Failed to call API. Status code: {res.status_code}"
    except Exception as e:
        return f"❌ Error occurred: {e}"

def leave_guild(guild_id):
    try:
        url = f"https://guild-info-danger.vercel.app/leave?guild_id={guild_id}&uid={GUEST_UID}&password={GUEST_PASSWORD}"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            message = data.get("message", "").lower()
            if data.get("status") == "success" or "success" in message or "left" in message:
                return "✅ Guild leaved successfully!"
            else:
                return f"❌ Failed to leave guild: {message or 'Unknown error'}"
        else:
            return f"❌ API Error | Status Code: {res.status_code}"
    except requests.exceptions.Timeout:
        return "✅ Guild leaved successfully! (API response delayed)"
    except Exception as e:
        return f"❌ Error occurred: {e}"

def remove_friend(target_uid):
    try:
        url = f"https://kallu-friend-management.vercel.app/remove_friend?uid={GUEST_UID}&password={GUEST_PASSWORD}&friend_uid={target_uid}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            if data.get("status") == "success":
                return "✅ Friend removed successfully !"
            else:
                return f"❌ Failed to remove friend: {data.get('message', 'Unknown error')}"
        else:
            return f"❌ Failed to call API. Status code: {res.status_code}"
    except Exception as e:
        return f"❌ Error occurred: {e}"

def get_player_bio(uid):
    try:
        url = f"https://infoooooo-v6v5.vercel.app/accinfo?uid={uid}"
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return f"Failed to fetch bio. Status code: {res.status_code}"
        data = res.json()
        bio = data.get("socialInfo", {}).get("socialHighlight")
        if bio:
            return bio
        else:
            return "No bio available"
    except Exception as e:
        return f"Error occurred: {e}"

def talk_with_ai(question):
    try:
        encoded_question = requests.utils.quote(question)
        url = f"https://text.pollinations.ai/{encoded_question}"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            answer = res.text.strip()
            return answer
        else:
            return f"Failed to fetch answer. Status code: {res.status_code}"
    except Exception as e:
        return f"Error occurred: {e}"

def get_friend_list_from_api():
    try:
        url = "https://danger-friend-manager.vercel.app/get_friends_list"
        params = {
            "uid": GUEST_UID,
            "password": GUEST_PASSWORD
        }
        for attempt in range(2):
            try:
                response = requests.get(url, params=params, timeout=15)
                if response.status_code == 200:
                    data = response.json()
                    if data and data.get("success") is not False:
                        return data
                return None
            except requests.exceptions.Timeout:
                if attempt == 0:
                    continue
                else:
                    return None
            except Exception as e:
                return None
    except Exception as e:
        return None

async def handle_friend_list_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    if str(uid) != ADMIN_UID:
        error_msg = "[B][C][FF0000]❌ ERROR! Only admin can use this command."
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    try:
        status_msg = f"[B][C][FFFF00]📞 Fetching friend list for Bot UID: {GUEST_UID}..."
        await dl_send_message(chat_type, status_msg, uid, chat_id, key, iv)
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            friend_data = await loop.run_in_executor(executor, get_friend_list_from_api)
        if friend_data:
            nickname = friend_data.get("nickname", "Unknown")
            total_friends = friend_data.get("total_friends", 0)
            your_uid = friend_data.get("your_uid", "Unknown")
            friends = friend_data.get("friends", [])
            bot_info_msg = f"""[C][B][00FF00]👤 Account: [FFFFFF]{nickname}
[C][B][00FF00]🆔 Bot UID: [FFFFFF]{fixnum(str(your_uid))}
[C][B][00FF00]👥 Total Friends: [FFFFFF]{fixnum(str(total_friends))}
"""
            await dl_send_message(chat_type, bot_info_msg, uid, chat_id, key, iv)
            await asyncio.sleep(0.3)
            if friends:
                for idx, friend in enumerate(friends, 1):
                    friend_nickname = friend.get("nickname", "Unknown")
                    friend_uid = friend.get("uid", "Unknown")
                    try:
                        player_data = await fetch_player_info(friend_uid)
                        if player_data:
                            player_info_msg = format_player_info(player_data)
                            await dl_send_message(chat_type, player_info_msg, uid, chat_id, key, iv)
                        else:
                            basic_info = f"""[C][B][FF0000]❌ Failed to fetch info for friend {idx}
[C][B][FFFFFF]Name: [00FF00]{friend_nickname}
[C][B][FFFFFF]UID: [00FF00]{fixnum(str(friend_uid))}
"""
                            await dl_send_message(chat_type, basic_info, uid, chat_id, key, iv)
                    except Exception as e:
                        basic_info = f"""[C][B][FF0000]❌ Error fetching friend {idx}
[C][B][FFFFFF]Name: [00FF00]{friend_nickname}
[C][B][FFFFFF]UID: [00FF00]{fixnum(str(friend_uid))}
"""
                        await dl_send_message(chat_type, basic_info, uid, chat_id, key, iv)
                    await asyncio.sleep(0.3)
            else:
                error_msg = "\n[C][B][FF0000]❌ Friend list empty!\n"
                await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        else:
            error_msg = "[B][C][FF0000]❌ API timeout! Friend list server is slow or down.\nTry again later."
            await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}"
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)

def send_insta_info(username):
    try:
        response = requests.get(
            f"https://kallu-insta-info-api.vercel.app/api/insta/{username}",
            timeout=15
        )
        if response.status_code != 200:
            return f"[B][C][FF0000]❌ Instagram API Error! Status Code: {response.status_code}"
        user = response.json()
        full_name = user.get("full_name", "Unknown")
        followers = user.get("edge_followed_by", {}).get("count") or user.get("followers_count", 0)
        following = user.get("edge_follow", {}).get("count") or user.get("following_count", 0)
        posts = user.get("media_count") or user.get("edge_owner_to_timeline_media", {}).get("count", 0)
        private_status = user.get("is_private", False)
        verified_status = user.get("is_verified", False)
        return f"""
[B][C][FB0364]╭[D21A92]─[BC26AB]╮[FFFF00]╔═══════╗
[C][B][FF7244]│[FE4250]◯[C81F9C]֯│[FFFF00]║[FFFFFF]INSTAGRAM INFO[FFFF00]║
[C][B][FDC92B]╰[FF7640]─[F5066B]╯[FFFF00]╚═══════╝
[C][B][FFFF00]━━━━━━━━━━━━
[C][B][FFFFFF]Name: [66FF00]{full_name}
[C][B][FFFFFF]Username: [66FF00]@{username}
[C][B][FFFFFF]Followers: [66FF00]{fixnum(followers)}
[C][B][FFFFFF]Following: [66FF00]{fixnum(following)}
[C][B][FFFFFF]Posts: [66FF00]{fixnum(posts)}
[C][B][FFFFFF]Private: [66FF00]{private_status}
[C][B][FFFFFF]Verified: [66FF00]{verified_status}
[C][B][FFFF00]━━━━━━━━━━━━
"""
    except requests.exceptions.RequestException:
        return "[B][C][FF0000]❌ Instagram API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF0000]❌ Unexpected Error: {str(e)}"

def get_youtube_info(channel):
    try:
        url = f"https://kallu-youtube-info-api.vercel.app/api/yt?channel={channel}"
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return f"[B][C][FF0000]❌ YouTube API Error! Status Code: {response.status_code}"
        data = response.json()
        channel_name = data.get("channel_name", "Unknown")
        subscribers = data.get("subscribers", "0")
        total_views = data.get("views", "0")
        total_videos = data.get("videos", "0")
        country = data.get("country", "N/A")
        created_date = data.get("created_at", "N/A")
        formatted_date = created_date
        try:
            for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
                try:
                    date_obj = datetime.strptime(created_date, fmt)
                    formatted_date = date_obj.strftime("%d %B %Y")
                    break
                except ValueError:
                    continue
        except:
            pass
        return f"""
[B][C][FF0000]╭[FFFFFF]─[FF0000]╮[FFFF00]╔════════╗
[C][B][FF0000]│[FFFFFF]▶[FF0000]│[FFFF00]║[FFFFFF]YOUTUBE INFO[FFFF00]║
[C][B][FF0000]╰[FFFFFF]─[FF0000]╯[FFFF00]╚════════╝
[C][B][FFFF00]━━━━━━━━━━━━
[C][B][FFFFFF]Channel: [00FF00]{channel_name}
[C][B][FFFFFF]Subscribers: [00FF00]{fixnum(subscribers)}
[C][B][FFFFFF]Total Views: [00FF00]{fixnum(total_views)}
[C][B][FFFFFF]Total Videos: [00FF00]{fixnum(total_videos)}
[C][B][FFFFFF]Country: [00FF00]{country}
[C][B][FFFFFF]Created: [00FF00]{formatted_date}
[C][B][FFFF00]━━━━━━━━━━━━
"""
    except requests.exceptions.RequestException:
        return "[B][C][FF0000]❌ YouTube API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF0000]❌ Unexpected Error: {str(e)}"

def send_tiktok_info(username):
    try:
        url = f"https://tiktok-api-mafia-ayan.vercel.app/tkinfo?username={username}"
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return f"[B][C][FF0000]❌ TikTok API Error! Status Code: {response.status_code}"
        data = response.json()
        if not data.get("status", False):
            return "[B][C][FF0000]❌ TikTok User Not Found!"
        name = data.get("name", "Unknown")
        username = data.get("username", "Unknown")
        followers = data.get("followers", 0)
        following = data.get("following", 0)
        likes = data.get("hearts", 0)
        videos = data.get("videos", 0)
        private_status = data.get("is_private", False)
        verified_status = data.get("open_favorite", False)
        user_id = data.get("user_id", "N/A")
        bio = data.get("signature", "N/A")
        return f"""
[B][C][00FFFF]╭[FF0050]─[00E5FF]╮[FFFF00]╔═══════╗
[C][B][FF0050]│[00FFFF]♪[FF0050]│[FFFF00]║[FFFFFF]TIKTOK INFO[FFFF00]║
[C][B][00FFFF]╰[FF0050]─[00E5FF]╯[FFFF00]╚═══════╝
[C][B][FFFF00]━━━━━━━━━━━━
[C][B][FFFFFF]Name: [00FFAB]{name}
[C][B][FFFFFF]Username: [00FFAB]@{username}
[C][B][FFFFFF]User ID: [66FF00]{fixnum(user_id)}
[C][B][FFFFFF]Followers: [66FF00]{fixnum(followers)}
[C][B][FFFFFF]Following: [66FF00]{fixnum(following)}
[C][B][FFFFFF]Likes: [66FF00]{fixnum(likes)}
[C][B][FFFFFF]Videos: [66FF00]{fixnum(videos)}
[C][B][FFFFFF]Private: [66FF00]{private_status}
[C][B][FFFFFF]Verified: [66FF00]{verified_status}
[C][B][FFFFFF]Bio: [00FFAB]{bio}
[C][B][FFFF00]━━━━━━━━━━━━
"""
    except requests.exceptions.RequestException:
        return "[B][C][FF0000]❌ TikTok API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF0000]❌ Unexpected Error: {str(e)}"

def get_pincode_info(pincode):
    try:
        url = f"https://pincode-ng.vercel.app/lookup?pincode={pincode}"
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return f"[B][C][FF0000]❌ API Error! Status Code: {response.status_code}"
        data = response.json()
        if data.get("Status") != "Success" or not data.get("PostOffice"):
            return f"[B][C][FF0000]❌ No data found for PIN code: {pincode}"
        return data
    except requests.exceptions.RequestException:
        return "[B][C][FF0000]❌ Internet connection failed."
    except Exception as e:
        return f"[B][C][FF0000]❌ Error: {str(e)}"

def format_pincode_summary(data, pincode):
    try:
        post_offices = data.get("PostOffice", [])
        count = len(post_offices)
        first = post_offices[0]
        result = f"[C][B]-┌ [FFD700]📮 PIN CODE SUMMARY\n"
        result += f"[FFFFFF]-├─ Pincode: [00FF00]{fixnum(pincode)}\n"
        result += f"[FFFFFF]-├─ Total Offices: [00FF00]{fixnum(str(count))}\n"
        result += f"[FFFFFF]-├─ First Office: [00FF00]{fixnum(first.get('Name','N/A'))}\n"
        result += f"[FFFFFF]-├─ District: [00FF00]{fixnum(first.get('District','N/A'))}\n"
        result += f"[FFFFFF]-├─ State: [00FF00]{fixnum(first.get('State','N/A'))}\n"
        result += f"[FFFFFF]-├─ Delivery: [00FF00]{fixnum(first.get('DeliveryStatus','N/A'))}\n"
        result += f"[FFFFFF]-└─ Country: [00FF00]{fixnum(first.get('Country','N/A'))}"
        return result
    except Exception as e:
        return f"[C][B][FF0000]Error formatting summary: {str(e)}"

def format_office_details(office, index):
    try:
        result = f"[C][B]-┌ [00FF00]🏢 OFFICE #{index}\n"
        result += f"[FFFFFF]-├─ Name: {fixnum(office.get('Name','N/A'))}\n"
        result += f"[FFFFFF]-├─ Type: {fixnum(office.get('BranchType','N/A'))}\n"
        result += f"[FFFFFF]-├─ Delivery: {fixnum(office.get('DeliveryStatus','N/A'))}\n"
        result += f"[FFFFFF]-├─ District: {fixnum(office.get('District','N/A'))}\n"
        result += f"[FFFFFF]-├─ State: {fixnum(office.get('State','N/A'))}\n"
        result += f"[FFFFFF]-├─ Circle: {fixnum(office.get('Circle','N/A'))}\n"
        result += f"[FFFFFF]-├─ Division: {fixnum(office.get('Division','N/A'))}\n"
        result += f"[FFFFFF]-├─ Region: {fixnum(office.get('Region','N/A'))}\n"
        result += f"[FFFFFF]-├─ Block: {fixnum(office.get('Block','N/A'))}\n"
        result += f"[FFFFFF]-└─ Country: {fixnum(office.get('Country','N/A'))}"
        return result
    except Exception as e:
        return f"[C][B][FF0000]Error formatting office: {str(e)}"

async def handle_pincode_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    parts = inPuTMsG.strip().split()
    if len(parts) != 2:
        await dl_send_message(
            chat_type,
            "[B][C][FF0000]❌ Usage: /pincode <6-digit_pincode>\n"
            "[FFFFFF]Example: /pincode 110001",
            uid, chat_id, key, iv
        )
        return
    pincode = parts[1]
    if not pincode.isdigit() or len(pincode) != 6:
        await dl_send_message(
            chat_type,
            "[B][C][FF0000]❌ Invalid PIN code!\n"
            "[FFFFFF]PIN must be exactly 6 digits.",
            uid, chat_id, key, iv
        )
        return
    await dl_send_message(
        chat_type,
        f"[B][C][FFFFFF]📮 Looking up PIN: [00FF00]{fixnum(pincode)}",
        uid, chat_id, key, iv
    )
    try:
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            pincode_data = await loop.run_in_executor(executor, get_pincode_info, pincode)
        if isinstance(pincode_data, str):
            await dl_send_message(chat_type, pincode_data, uid, chat_id, key, iv)
            return
        post_offices = pincode_data.get("PostOffice", [])
        if not post_offices:
            await dl_send_message(
                chat_type,
                "[B][C][FF0000]❌ No offices found",
                uid, chat_id, key, iv
            )
            return
        await dl_send_message(
            chat_type,
            format_pincode_summary(pincode_data, pincode),
            uid, chat_id, key, iv
        )
        await asyncio.sleep(0.05)
        max_offices = min(len(post_offices), 10)
        for i in range(max_offices):
            await dl_send_message(
                chat_type,
                format_office_details(post_offices[i], i + 1),
                uid, chat_id, key, iv
            )
            await asyncio.sleep(0.05)
        if len(post_offices) > 10:
            await dl_send_message(
                chat_type,
                f"[B][C][FFFF00]📊 Total Offices: {len(post_offices)}\n"
                f"[FFFFFF]📋 Showing first 10 only",
                uid, chat_id, key, iv
            )
    except Exception as e:
        await dl_send_message(
            chat_type,
            f"[B][C][FF0000]❌ Error: {str(e)}",
            uid, chat_id, key, iv
        )

def get_phone_info(phone_number):
    try:
        url = f"https://ph-ng-pi.vercel.app/?number={phone_number}"
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None
        data = response.json()
        if not data.get("success", False):
            return None
        return data
    except Exception:
        return None

async def handle_phone_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    parts = inPuTMsG.strip().split()
    if len(parts) != 2:
        await dl_send_message(
            chat_type,
            "[B][C][FF0000]❌ Usage: /num <phone_number>\nExample: /num 7395083124",
            uid, chat_id, key, iv
        )
        return
    phone_number = parts[1]
    if not phone_number.isdigit() or len(phone_number) != 10:
        await dl_send_message(
            chat_type,
            "[B][C][FF0000]❌ Invalid! 10 digits only\nExample: /num 9876543210",
            uid, chat_id, key, iv
        )
        return
    await dl_send_message(
        chat_type,
        f"[B][C][FFFFFF]🔍 Searching: [00FF00]{phone_number}",
        uid, chat_id, key, iv
    )
    try:
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            phone_data = await loop.run_in_executor(executor, get_phone_info, phone_number)
        if not phone_data:
            await dl_send_message(
                chat_type,
                "[B][C][FF0000]❌ Number not found",
                uid, chat_id, key, iv
            )
            return
        fields = phone_data.get("fields", {})
        result = "[C][B]-┌ [FFD700]📱 PHONE INFO\n"
        result += f"[FFFFFF]-├─ Number: [00FF00]{fixnum(phone_number)}\n"
        result += f"[FFFFFF]-├─ Country: [00FF00]{fields.get('Country', 'India')}\n"
        result += f"[FFFFFF]-├─ SIM: [00FF00]{fields.get('SIM card', 'N/A')}\n"
        result += f"[FFFFFF]-├─ Connection: [00FF00]{fields.get('Connection', ['N/A'])[0]}\n"
        result += f"[FFFFFF]-├─ State: [00FF00]{fields.get('Mobile State', 'N/A')}\n"
        result += f"[FFFFFF]-├─ City: [00FF00]{fields.get('Refrence City', 'N/A')}\n"
        result += f"[FFFFFF]-├─ Language: [00FF00]{fields.get('Language', 'N/A')}\n"
        result += f"[FFFFFF]-├─ Owner: [00FF00]{fields.get('Owner Name', 'Hidden')}\n"
        result += f"[FFFFFF]-└─ Complaints: [00FF00]{fields.get('Complaints', '0 reports')}"
        await dl_send_message(
            chat_type,
            result,
            uid, chat_id, key, iv
        )
    except Exception as e:
        await dl_send_message(
            chat_type,
            f"[B][C][FF0000]❌ Error: {str(e)[:50]}",
            uid, chat_id, key, iv
        )

async def handle_jwt_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    if str(uid) != ADMIN_UID:
        error_msg = "[B][C][FF0000]❌ ERROR! Only admin can update JWT token."
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    try:
        initial_msg = "[B][C][FFFF00]⏳ Fetching JWT token using Guest account...\n📁 Guest UID: " + GUEST_UID
        await dl_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
        access_token_url = "https://100067.connect.garena.com/oauth/guest/token/grant"
        headers = {
            "Host": "100067.connect.garena.com",
            "User-Agent": "GarenaMSDK/4.0.19P4 (Vivo Y15c; Android 12; en;IN;)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "close"
        }
        data = {
            "uid": GUEST_UID,
            "password": GUEST_PASSWORD,
            "response_type": "token",
            "client_type": "2",
            "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
            "client_id": "100067"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(access_token_url, headers=headers, data=data, ssl=False) as response:
                if response.status != 200:
                    error_msg = f"[B][C][FF0000]❌ Failed to get access token. Status: {response.status}"
                    await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
                    return
                token_data = await response.json()
                open_id = token_data.get("open_id")
                access_token = token_data.get("access_token")
                if not open_id or not access_token:
                    error_msg = "[B][C][FF0000]❌ Invalid response from Garena API"
                    await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
                    return
        update_msg = "[B][C][FFFF00]✅ Got access token!\n⏳ Now getting JWT from MajorLogin..."
        await dl_send_message(chat_type, update_msg, uid, chat_id, key, iv)
        jwt_result = await get_jwt_from_major_login(open_id, access_token)
        if jwt_result and 'BearerAuth' in jwt_result:
            jwt_token = jwt_result['BearerAuth']
            token_data = {
                'jwt_token': jwt_token,
                'token_access': access_token,
                'timestamp': time.time(),
                'guest_uid': GUEST_UID,
                'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            with open('token.json', 'w') as f:
                json.dump(token_data, f, indent=2)
            success_msg = f"""[B][C][00FF00]✅ JWT TOKEN UPDATED!

📁 File: token.json
👤 Guest UID: {GUEST_UID}
✅ Tokens saved:
🔐 JWT: {jwt_token[:30]}...
🔑 Access: {access_token[:20]}...

⏰ Generated: {datetime.now().strftime("%H:%M:%S")}
📅 Date: {datetime.now().strftime("%d-%m-%Y")}

✅ Old data replaced with new tokens!"""
            await dl_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        else:
            error_msg = f"[B][C][FF0000]❌ Failed to get JWT token from MajorLogin"
            await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Command error: {str(e)[:80]}"
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def get_jwt_from_major_login(open_id, access_token):
    try:
        PyL = await EncRypTMajoRLoGin(open_id, access_token)
        MajoRLoGinResPonsE = await MajorLogin(PyL)
        if MajoRLoGinResPonsE:
            MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
            token = MajoRLoGinauTh.token
            return {
                'success': True,
                'BearerAuth': token,
                'region': MajoRLoGinauTh.region,
                'url': MajoRLoGinauTh.url
            }
    except Exception as e:
        pass
    return None

def auto_rejoin_exploit(token, uid):
    import requests
    import json
    import time
    import hashlib
    import threading
    class Exploit:
        def __init__(self, t, u):
            self.tok = t
            self.id = u
            self.sq = None
            self.run = True
        def hdrs(self):
            return {
                'Authorization': f'Bearer {self.tok}',
                'X-Unity-Version': '2018.4.11f1',
                'Content-Type': 'application/json'
            }
        def get_sq(self):
            try:
                r = requests.post(
                    'https://clientbp.common.ggbluefox.com/GetSquadInfo',
                    headers=self.hdrs(),
                    data=json.dumps({'uid': self.id}),
                    timeout=5
                )
                if r.status_code == 200:
                    d = json.loads(r.text)
                    self.sq = d.get('squad_code')
                    return True
            except:
                pass
            return False
        def join_sq(self, code=None):
            c = code or self.sq
            if not c:
                return False
            try:
                p = {
                    'action': 'join',
                    'uid': self.id,
                    'squad_code': c,
                    'silent': 'true'
                }
                r = requests.post(
                    'https://clientbp.common.ggbluefox.com/JoinSquad',
                    headers=self.hdrs(),
                    data=json.dumps(p),
                    timeout=5
                )
                if r.status_code == 200:
                    d = json.loads(r.text)
                    if d.get('status') in ['success', 'joined']:
                        return True
            except:
                pass
            return False
        def chk_kick(self):
            try:
                r = requests.post(
                    'https://clientbp.common.ggbluefox.com/CheckSquad',
                    headers=self.hdrs(),
                    data=json.dumps({'uid': self.id}),
                    timeout=3
                )
                if r.status_code == 200:
                    d = json.loads(r.text)
                    if d.get('error') in ['not_in_squad', 'kicked', 'removed']:
                        return True
                    if d.get('status') == 'error' and 'kick' in d.get('message', '').lower():
                        return True
            except:
                pass
            return False
        def force_join(self):
            if not self.sq:
                return False
            if self.join_sq():
                return True
            try:
                p = {
                    'action': 'ghost',
                    'real_uid': self.id,
                    'ghost_uid': f'{self.id}_{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}',
                    'squad_code': self.sq
                }
                r = requests.post(
                    'https://clientbp.common.ggbluefox.com/GhostJoin',
                    headers=self.hdrs(),
                    data=json.dumps(p),
                    timeout=5
                )
                if r.status_code == 200:
                    return True
            except:
                pass
            return False
        def mon(self):
            self.get_sq()
            while self.run:
                try:
                    if self.chk_kick():
                        if not self.join_sq():
                            if not self.force_join():
                                self.crt_sq()
                        time.sleep(0.5)
                except Exception as e:
                    pass
                time.sleep(1)
        def crt_sq(self):
            try:
                p = {'action': 'create', 'uid': self.id, 'type': 'private'}
                r = requests.post(
                    'https://clientbp.common.ggbluefox.com/CreateSquad',
                    headers=self.hdrs(),
                    data=json.dumps(p),
                    timeout=5
                )
                if r.status_code == 200:
                    d = json.loads(r.text)
                    self.sq = d.get('squad_code')
                    return True
            except:
                pass
            return False
        def start(self):
            thread = threading.Thread(target=self.mon, daemon=True)
            thread.start()
            return thread
        def stop(self):
            self.run = False
    exp = Exploit(token, uid)
    exp.start()
    return exp

async def handle_exploit_start(uid, chat_id, chat_type, key, iv):
    global exploit_running, exploit_instance
    if str(uid) != ADMIN_UID:
        error_msg = "[B][C][FF0000]❌ ERROR! Only admin can use this command."
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    if exploit_running:
        error_msg = "[B][C][FF0000]❌ Exploit already running!"
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    try:
        with open('token.json', 'r') as f:
            token_data = json.load(f)
            jwt_token = token_data.get('jwt_token')
            if not jwt_token:
                error_msg = "[B][C][FF0000]❌ No JWT token found! Use /jwt first."
                await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
                return
    except FileNotFoundError:
        error_msg = "[B][C][FF0000]❌ token.json not found! Use /jwt first."
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error reading token: {str(e)}"
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    exploit_instance = auto_rejoin_exploit(jwt_token, GUEST_UID)
    exploit_running = True
    success_msg = f"""
[B][C][00FF00]✅ AUTO-REJOIN EXPLOIT STARTED!

👤 Target UID: {GUEST_UID}
🛡️ Protection: Active
🔄 Auto-rejoin: Enabled
🔒 Immune to kicks

💡 The bot will automatically rejoin
   if kicked from any squad!
"""
    await dl_send_message(chat_type, success_msg, uid, chat_id, key, iv)

async def handle_exploit_stop(uid, chat_id, chat_type, key, iv):
    global exploit_running, exploit_instance
    if str(uid) != ADMIN_UID:
        error_msg = "[B][C][FF0000]❌ ERROR! Only admin can use this command."
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    if not exploit_running:
        error_msg = "[B][C][FF0000]❌ No exploit running!"
        await dl_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    if exploit_instance:
        exploit_instance.stop()
    exploit_running = False
    exploit_instance = None
    success_msg = """
[B][C][00FF00]✅ AUTO-REJOIN EXPLOIT STOPPED!

🛡️ Protection: Disabled
🔄 Auto-rejoin: Disabled

💡 Bot can now be kicked normally.
"""
    await dl_send_message(chat_type, success_msg, uid, chat_id, key, iv)

async def handle_exploit_status(uid, chat_id, chat_type, key, iv):
    global exploit_running
    status_msg = f"""
[B][C][FFFF00]🛡️ AUTO-REJOIN EXPLOIT STATUS

Status: {'[00FF00]ACTIVE ✅' if exploit_running else '[FF0000]INACTIVE ❌'}
Target UID: {GUEST_UID}
Owner UID: {ADMIN_UID}

💡 Commands:
/exploit_start - Start protection
/exploit_stop  - Stop protection
/exploit_status - Check status

⚠️ Only owner can control this feature!
"""
    await dl_send_message(chat_type, status_msg, uid, chat_id, key, iv)

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB54"}

def kx_random_colour():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

def get_random_sticker():
    sticker_packs = [
        ("1200000001", 1, 24),
        ("1200000002", 1, 15),
        ("1200000004", 1, 13),
    ]
    pack_id, start, end = random.choice(sticker_packs)
    sticker_no = random.randint(start, end)
    return f"[1={pack_id}-{sticker_no}]"

async def ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region):
    try:
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        await asyncio.sleep(0.5)
        emote_packet = await Emote_k(int(target_uid), int(emote_id), key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
        await asyncio.sleep(0.3)
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        return True, f"Quick emote attack completed! Sent emote to UID {target_uid}"
    except Exception as e:
        return False, f"Quick emote attack failed: {str(e)}"

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload

async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = "2026-07-09 12:44:05"
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.126.9"
    major_login.system_software = "Android OS 13 / API-33 (TP1A.220905.001/R.206769c-2)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "45403"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1280
    major_login.screen_height = 720
    major_login.screen_dpi = "320"
    major_login.processor_details = "ARM64 FP ASIMD AES | 2352 | 8"
    major_login.memory = 128
    major_login.gpu_renderer = "Mali-G610"
    major_login.gpu_version = "OpenGL ES 3.2 v1.g18p0-01eac0.2d5e200a1514bdef1a4909db66e37e28"
    major_login.unique_device_id = "Google|7a9732a4-2549-4edc-840e-d61263d128f5"
    major_login.client_ip = "162.128.224.168"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    major_login.device_model = "OPPO CPH2217"
    major_login.region = "IND"
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "45403"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "1ac4b80ecf0478a44203bf8fac6120f5"
    major_login.external_storage_total = 20660
    major_login.external_storage_available = 17445
    major_login.internal_storage_total = 2663
    major_login.internal_storage_available = 1500
    major_login.game_disk_storage_available = 17573
    major_login.game_disk_storage_total = 20660
    major_login.external_sdcard_avail_storage = 17573
    major_login.external_sdcard_total_storage = 20660
    major_login.login_by = 3
    major_login.library_path = "/data/app/~~xHaSHUdUBlxvhJaRWh018A==/com.dts.freefireth-4OBn7-sLMoPuswIfmgixhA==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "4c322aeb56444feaa151d1ea91a8f7f2|/data/app/~~xHaSHUdUBlxvhJaRWh018A==/com.dts.freefireth-4OBn7-sLMoPuswIfmgixhA==/base.apk"
    major_login.channel_type = 6
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019120816"
    major_login.unknown_int85 = 3
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 25777
    major_login.release_channel = "3rd_party"
    major_login.extra_info = "KqsHTz+zAigQ0BOzKhQHN8ae/IefLXcroDjaj4QY+OF71nTuiQh+myDUqCZFPJQ5gyC9LfEeKoon9d461764VIGguRHcIyKfExGAh4bvxFZRgp2X"
    major_login.extra_json = '{"cur_rate":null,"support_etc2":false}'
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    major_login.unknown_bytes102 = b"E1JMTwcJXjA2"
    
    string = major_login.SerializeToString()
    return await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization'] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto

async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto

async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9:
        headers = '0000000'
    elif uid_length == 8:
        headers = '00000000'
    elif uid_length == 10:
        headers = '000000'
    elif uid_length == 7:
        headers = '000000000'
    else:
        headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"

async def cHTypE(H):
    if not H:
        return 'Squid'
    elif H == 1:
        return 'CLan'
    elif H == 2:
        return 'PrivaTe'

async def SEndMsG(H, message, Uid, chat_id, key, iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid':
        msg_packet = await xSEndMsgsQ(message, chat_id, key, iv)
    elif TypE == 'CLan':
        msg_packet = await xSEndMsg(message, 1, chat_id, chat_id, key, iv)
    elif TypE == 'PrivaTe':
        msg_packet = await xSEndMsg(message, 2, Uid, Uid, key, iv)
    return msg_packet

async def SEndPacKeT(OnLinE, ChaT, TypE, PacKeT):
    if TypE == 'ChaT' and ChaT:
        whisper_writer.write(PacKeT)
        await whisper_writer.drain()
    elif TypE == 'OnLine':
        online_writer.write(PacKeT)
        await online_writer.drain()
    else:
        return 'UnsoPorTed TypE ! >> ErrrroR (:():)'

async def dl_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3):
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
            return True
        except Exception as e:
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)
    return False

async def fast_emote_spam(uids, emote_id, key, iv, region):
    global fast_spam_running
    count = 0
    max_count = 25
    while fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                pass
        count += 1
        await asyncio.sleep(0.1)

async def custom_emote_spam(uid, emote_id, times, key, iv, region):
    global custom_spam_running
    count = 0
    while custom_spam_running and count < times:
        try:
            uid_int = int(uid)
            H = await Emote_k(uid_int, int(emote_id), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            count += 1
            await asyncio.sleep(0.1)
        except Exception as e:
            break

async def evo_emote_spam(uids, number, key, iv, region):
    try:
        emote_id = EMOTE_MAP.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-21 only."
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                pass
        return True, f"Sent evolution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    except Exception as e:
        return False, f"Error in evo_emote_spam: {str(e)}"

async def evo_fast_emote_spam(uids, number, key, iv, region):
    global evo_fast_spam_running
    count = 0
    max_count = 25
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    while evo_fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                pass
        count += 1
        await asyncio.sleep(0.1)
    return True, f"Completed fast evolution emote spam {count} times"

async def evo_custom_emote_spam(uids, number, times, key, iv, region):
    global evo_custom_spam_running
    count = 0
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    while evo_custom_spam_running and count < times:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                pass
        count += 1
        await asyncio.sleep(0.1)
    return True, f"Completed custom evolution emote spam {count} times"

async def convert_kyro_to_your_system(target_uid, chat_id, key, iv, nickname="DEVIL", title_id=904990072):
    try:
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: 902000306,
                    4: 330,
                    5: 1001000004,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: "\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        return final_packet
    except Exception as e:
        return None

async def send_kyro_title_adapted(chat_id, key, iv, target_uid, nickname="DEVIL", title_id=905190079):
    try:
        from Pb2.kyro_title_pb2 import GenTeamTitle
        root = GenTeamTitle()
        root.type = 1
        nested_object = root.data
        nested_object.uid = int(target_uid)
        nested_object.chat_id = int(chat_id)
        nested_object.title = f'{{"TitleID":{title_id},"type":"Title"}}'
        nested_object.timestamp = int(datetime.now().timestamp())
        nested_object.language = "en"
        nested_details = nested_object.field9
        nested_details.Nickname = f"[C][B][FF0000]{nickname}"
        nested_details.avatar_id = 902000306
        nested_details.rank = 330
        nested_details.badge = 102000015
        nested_details.Clan_Name = "BOT TEAM"
        nested_details.field10 = 1
        nested_details.global_rank_pos = 1
        nested_details.badge_info.value = 2
        nested_details.prime_info.prime_uid = 1158053040
        nested_details.prime_info.prime_level = 8
        nested_details.prime_info.prime_hex = b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
        nested_options = nested_object.field13
        nested_options.url_type = 2
        nested_options.curl_platform = 1
        nested_object.empty_field.SetInParent()
        packet = root.SerializeToString().hex()
        encrypted_packet = await encrypt_packet(packet, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
    except Exception as e:
        return None

async def send_all_titles_once(chat_id, key, iv, target_uid, whisper_writer, nickname="DEVIL"):
    titles = [
        904090014, 904090015, 904090024, 904090025, 904090026, 904090027,
        904790062, 904890068, 904990069, 904990070, 904990071, 904990072,
        905090075, 905190079
    ]
    for title_id in titles:
        try:
            title_packet = await send_kyro_title_adapted(chat_id, key, iv, target_uid, nickname, title_id)
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                await asyncio.sleep(0.3)
        except Exception:
            pass

async def handle_title_sm_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    parts = inPuTMsG.strip().split()
    if len(parts) == 1:
        target_uid = uid
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
    else:
        return
    try:
        if not whisper_writer:
            return
        await send_all_titles_once(chat_id, key, iv, target_uid, whisper_writer)
    except Exception:
        pass

async def handle_title_final(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    parts = inPuTMsG.strip().split()
    if len(parts) == 1:
        target_uid = uid
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
    else:
        return
    all_titles = [
        904090023, 904090026, 904090027, 904290048, 904590058, 904590059,
        904790062, 904890068, 904990069, 904990070, 904990071, 904990072,
        905090075, 905190079
    ]
    selected_title = random.choice(all_titles)
    try:
        if not whisper_writer:
            return
        title_packet = await convert_kyro_to_your_system(target_uid, chat_id, key, iv, "DEVIL", selected_title)
        if title_packet and whisper_writer:
            whisper_writer.write(title_packet)
            await whisper_writer.drain()
    except Exception:
        pass

async def send_sticker(target_uid, chat_id, key, iv, nickname="DEVILxBOT"):
    try:
        sticker_value = get_random_sticker()
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"StickerStr" : "{sticker_value}", "type":"Sticker"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(get_random_avatar()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {1: 2},
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        return final_packet
    except Exception as e:
        return None

def get_random_evo_emote():
    return int(random.choice([evo_emotes[str(i)] for i in range(1, 19)]))

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer, whisper_writer, spammer_uid, spam_chat_id, spam_uid, XX, uid, Spy, data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task, spm_inv_running, spm_inv_task, last_status_packet, status_response_cache, insquad, joining_team, whisper_writer, region, exploit_running, exploit_instance
    bot_uid = 14572471551
    if insquad is not None:
        insquad = None
    if joining_team is True:
        joining_team = False
    online_writer = None
    whisper_writer = None
    available_bundles = {
        "rampage": 914000002,
        "cannibal": 914000003,
        "devil": 914038001,
        "scorpio": 914039001,
        "frostfire": 914042001,
        "paradox": 914044001,
        "naruto": 914047001,
        "aurora": 914047002,
        "midnight": 914048001,
        "itachi": 914050001,
        "dreamspace": 914051001
    }
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2:
                    break
                data_hex = data2.hex()
                if data_hex.startswith('0500') and insquad is not None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        if packet_json.get('1') in [6, 7]:
                            insquad = None
                            joining_team = False
                            continue
                    except Exception as e:
                        pass
                if data_hex.startswith("0500") and insquad is None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        uid = packet_json['5']['data']['1']['data']
                        invite_uid = packet_json['5']['data']['2']['data']['1']['data']
                        squad_owner = packet_json['5']['data']['1']['data']
                        code = packet_json['5']['data']['8']['data']
                        emote_id = 909050008
                        bot_uid = 14572471551
                        SendInv = await RedZed_SendInv(bot_uid, invite_uid, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', SendInv)
                        inv_packet = await RejectMSGtaxt(squad_owner, uid, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)
                        Join = await ArohiAccepted(squad_owner, code, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', Join)
                        await asyncio.sleep(2)
                        emote_to_sender = await Emote_k(int(uid), emote_id, key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
                        bot_emote = await Emote_k(int(bot_uid), emote_id, key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_emote)
                        insquad = True
                        try:
                            welcome_message = """[B][C][FFFFFF]Welcome to 𝐒ᴛᴀʀ Bot

[B][C][FFFFFF]Available Features:
[B][C][FFFFFF]• Dance & Emote Commands
[B][C][FFFFFF]• Team & Squad Management
[B][C][FFFFFF]• Player Info & Status 
[B][C][FFFFFF]• Smart Spam Protection
[B][C][FFFFFF]• AI Chat Assistance

[B][C][FFFFFF]Use /help to see all commands

[B][C][FFFFFF]Tiktok : @DARK_REALITY.EXE
[B][C][FFFFFF]Contact : @HUSSNAINSK

[B][C][FFFFFF]Status: Online & Active"""
                            P = await SEndMsG(0, welcome_message, squad_owner, squad_owner, key, iv)
                            if whisper_writer:
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        except Exception as msg_error:
                            pass
                    except Exception as e:
                        insquad = None
                        joining_team = False
                        continue
                if data_hex.startswith('0500') and len(data_hex) > 1000 and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                        JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    except Exception as e:
                        pass
                if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                    try:
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        packet = json.loads(packet)
                        OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet)
                        JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                        def kx_random_colour(): return "_"
                        message = """[B][C][FFFFFF]Welcome to STAR Bot

[B][C][FFFFFF]Available Features:
[B][C][FFFFFF]• Dance & Emote Commands
[B][C][FFFFFF]• Team & Squad Management
[B][C][FFFFFF]• Player Info & Status 
[B][C][FFFFFF]• Smart Spam Protection
[B][C][FFFFFF]• AI Chat Assistance

[B][C][FFFFFF]Use /help to see all commands

[B][C][FFFFFF]Tiktok : @DARK_REALITY.EXE
[B][C][FFFFFF]Contact : @HUSSNAINSK

[B][C][FFFFFF]Status: Online & Active"""
                        P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv)
                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        bundle_names = list(available_bundles.keys())
                        selected_bundle = random.choice(bundle_names)
                        bundle_id = available_bundles[selected_bundle]
                        bundle_packet = await Look_Changer(bundle_id, key, iv, region)
                        if bundle_packet and online_writer:
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_packet)
                            bundle_msg = f'[B][C][00FF00]🎁 Auto Bundle Activated!\n📦 {selected_bundle.upper()}\n🆔 ID: {bundle_id}'
                            P = await SEndMsG(0, bundle_msg, OwNer_UiD, OwNer_UiD, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        try:
                            await auto_hammer_slam_emote_dual(OwNer_UiD, key, iv, region)
                        except Exception as emote_error:
                            pass
                    except Exception as e:
                        pass
                if data_hex.startswith("0500") and emote_hijack == True:
                    try:
                        emote_info = await extract_emote_info(data_hex, key, iv)
                        in_squad = insquad is not None
                        if emote_info and emote_info.get('sender_uid'):
                            sender_uid = emote_info['sender_uid']
                            emote_id = emote_info['emote_id']
                            if int(sender_uid) != bot_uid:
                                fixed_emote_packet = await Emote_k(int(sender_uid), 909035003, key, iv, region)
                                if fixed_emote_packet and online_writer:
                                    online_writer.write(fixed_emote_packet)
                                    await online_writer.drain()
                                    await asyncio.sleep(0.5)
                                bot_self_emote = await Emote_k(bot_uid, int(emote_id), key, iv, region)
                                if bot_self_emote and online_writer:
                                    online_writer.write(bot_self_emote)
                                    await online_writer.drain()
                                    await asyncio.sleep(0.5)
                                mirror_emote = await Emote_k(int(sender_uid), int(emote_id), key, iv, region)
                                if mirror_emote and online_writer:
                                    online_writer.write(mirror_emote)
                                    await online_writer.drain()
                    except Exception as e:
                        continue
            online_writer.close()
            await online_writer.wait_closed()
            online_writer = None
        except Exception as e:
            online_writer = None
        await asyncio.sleep(reconnect_delay)

async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region, reconnect_delay=0.5):
    global whisper_writer, spammer_uid, spam_chat_id, spam_uid, online_writer, chat_id, XX, uid, Spy, data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task, evo_cycle_running, evo_cycle_task, reject_spam_running, reject_spam_task, legendry_cycle_task, legendry_cycle_running
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                pK = await AuthClan(clan_id, clan_compiled_data, key, iv)
                if whisper_writer:
                    whisper_writer.write(pK)
                    await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data:
                    break
                if data.hex().startswith("120000"):
                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                    except:
                        response = None
                        continue
                    if response:
                    
                        if inPuTMsG.strip().startswith('/jwt'):
                            await handle_jwt_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        if inPuTMsG.strip().lower().startswith('/ai '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = "[B][C][FF0000]❌ ERROR! Usage: /ai <question>\nExample: /ai Who is Elon Musk?\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                question = " ".join(parts[1:])
                                initial_message = f"[B][C]{kx_random_colour()}\nPreparing the best response…\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    ai_result = await loop.run_in_executor(executor, talk_with_ai, question)
                                final_msg = f"[B][C]{kx_random_colour()}\n{ai_result}"
                                await dl_send_message(response.Data.chat_type, final_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().lower().startswith('/ms '):
                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)
                                if len(parts) < 2:
                                    error_msg = "[B][C][FF0000]❌ ERROR! Usage:\n/ms <single_word>\nExample: /ms STAR"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    words = parts[1].strip().split()
                                    if len(words) != 1:
                                        error_msg = "[B][C][FF0000]❌ ERROR! Only one word allowed after /ms."
                                        await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        user_message = words[0].upper()
                                        for i in range(1, len(user_message) + 1):
                                            partial_message = user_message[:i]
                                            color = kx_random_colour()
                                            colored_message = f"[B][C]{color} {partial_message}"
                                            await dl_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                            await asyncio.sleep(0.3)
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/gali '):
                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)
                                if len(parts) < 2:
                                    error_msg = "[B][C][FF0000]❌ ERROR! Usage:\n/gali <name>\nExample: /gali hater"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    input_name = parts[1].strip().lower()
                                    if input_name == "devil":
                                        target_name = await get_nickname_from_api(uid)
                                    else:
                                        target_name = input_name
                                    sender_name = await get_nickname_from_api(uid)
                                    special_name = convert_to_special_font(target_name.upper())
                                    messages = [
                f"{special_name} ᴛƐʀɪ ꜱƐxʏ ʙʜᴇɴ ᴋɪ ᴄʜxᴛ ᴍᴇ ᴍᴇ ʟ0ᴅᴀ ᴅᴀᴀʟ ᴋᴀʀ ʀᴀᴀᴛ ʙʜᴀʀ ᴊᴏʀ ᴊᴏʀ ꜱᴇ ᴄʜ0ᴅᴜɴɢᴀ",
                f"{special_name} ᴍᴀᴅʜᴇʀxʜᴏᴅ ᴛƐʀɪ ᴍᴀ́ᴀ ᴋɪ ᴋᴀʟɪ ɢ4ɴᴅ ᴍƐ ʟᴀɴᴅ ᴍᴀʀᴜ",
                f"{special_name} ᴛƐʀɪ ʙʜƐɴ ᴋɪ ᴛɪɢʜᴛ ᴄʜxᴛ ᴋᴏ 5ɢ ᴋɪ ꜱᴘᴇᴇᴅ ꜱᴇ ᴄʜ0ᴅ ᴅᴜ",
                f"{special_name} ᴛƐʀɪ ʙᴇʜᴇɴ ᴋɪ ᴄʜxᴛ ᴍᴇ ʟ4ɴᴅ ᴍᴀʀᴜ",
                f"{special_name} ᴛƐʀɪ ᴍᴀ́ᴀ ᴋɪ ᴄʜxᴛ 360 ʙᴀʀ",
                f"{special_name} ᴛƐʀɪ ʙƐʜƐɴ ᴋɪ ᴄʜxᴛ 720 ʙᴀʀ",
                f"{special_name} ʙᴇʜᴇɴ ᴋᴇ ʟ0ᴅᴇ",
                f"{special_name} ᴍᴀᴅᴀʀᴄʜxᴅ",
                f"{special_name} ʙᴇᴛᴇ ᴛƐʀᴀ ʙᴀᴀᴘ ʜᴜɴ ᴍᴇ",
                f"{special_name} ɢ4ɴᴅᴜ ᴀᴘɴᴇ ʙᴀᴀᴘ ᴋᴏ ʜ8 ᴅᴇɢᴀ",
                f"{special_name} ᴋɪ ᴍᴀ̀ᴀ ᴋɪ ᴄʜxᴛ ᴘᴇʀ ɴɪɢʜᴛ 4000",
                f"{special_name} ᴋɪ ʙƐʜƐɴ ᴋɪ ᴄʜxᴛ ᴘᴇʀ ɴɪɢʜᴛ 8000",
                f"{special_name} ʀ4ɴᴅɪ ᴋᴇ ʙᴀᴄʜʜƐ ᴀᴘɴᴇ ʙᴀᴘ ᴋᴏ ʜ8 ᴅᴇɢᴀ",
                f"ɪɴᴅɪᴀ ᴋᴀ ɴᴏ-1 ɢ4ɴᴅᴜ {special_name}",
                f"ᴄʜᴀᴘᴀʟ ᴄʜ0ʀ {special_name}",
                f"{special_name} ᴛƐʀɪ ᴍᴀ̀ᴀ ᴋᴏ ɢʙ ʀᴏᴀᴅ ᴘᴇ ʙᴇᴛʜᴀ ᴋᴇ ᴄʜxᴅᴜɴɢᴀ",
                f"{special_name} ʙᴇᴛᴀ ᴊʜᴜʟᴀ ᴊʜᴜʟ ᴀᴘɴᴇ ʙᴀᴀᴘ ᴋᴏ ᴍᴀᴛ ʙʜᴜʟ"
                                    ]
                                    for msg in messages:
                                        colored_message = f"[B][C]{kx_random_colour()} {msg}"
                                        await dl_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(0.5)
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/ig '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /ig <username>\nExample: /ig virat.kohli\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_username = parts[1]
                                initial_message = f"[B][C]{kx_random_colour()}\nFetching Instagram info for {target_username}...\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    insta_result = await loop.run_in_executor(executor, send_insta_info, target_username)
                                await dl_send_message(response.Data.chat_type, insta_result, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/yt '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = "[B][C][FF0000]❌ ERROR! Usage: /yt <channel_name>\nExample: /yt CarryMinati\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                channel_name = parts[1]
                                initial_message = f"[B][C]{kx_random_colour()}\nFetching YouTube info for {channel_name}...\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    yt_result = await loop.run_in_executor(executor, get_youtube_info, channel_name)
                                await dl_send_message(response.Data.chat_type, yt_result, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/tk '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = "[B][C][FF0000]❌ ERROR! Usage: /tk <username>\nExample: /tk mrbeast\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_username = parts[1]
                                initial_message = f"[B][C]{kx_random_colour()}\nFetching TikTok info for {target_username}...\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    tiktok_result = await loop.run_in_executor(executor, send_tiktok_info, target_username)
                                await dl_send_message(response.Data.chat_type, tiktok_result, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/num '):
                            await handle_phone_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        if inPuTMsG.strip().startswith('/guild_join '):
                            if str(uid) != ADMIN_UID:
                                error_msg = "[B][C][FF0000]❌ ERROR! Only the admin can use this command."
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                parts = inPuTMsG.strip().split()
                                if len(parts) < 2:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /guildjoin <guild_id>\nExample: /guildjoin 123456789\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    guild_id = parts[1]
                                    initial_message = f"[B][C]{kx_random_colour()}\nJoining the guild...\n"
                                    await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                    loop = asyncio.get_event_loop()
                                    with ThreadPoolExecutor() as executor:
                                        guildjoin_result = await loop.run_in_executor(executor, join_guild, guild_id)
                                    await dl_send_message(response.Data.chat_type, f"[B][C]{kx_random_colour()}\n{guildjoin_result}", uid, chat_id, key, iv)
                                    
                        if inPuTMsG.strip().startswith('/guild_leave '):
                            if str(uid) != ADMIN_UID:
                                error_msg = "[B][C][FF0000]❌ ERROR! Only the admin can use this command."
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                parts = inPuTMsG.strip().split()
                                if len(parts) < 2:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /guild_leave <guild_id>\nExample: /guild_leave 123456789\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    guild_id = parts[1]
                                    initial_message = f"[B][C]{kx_random_colour()}\nLeaving the guild...\n"
                                    await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                    loop = asyncio.get_event_loop()
                                    with ThreadPoolExecutor() as executor:
                                        guildleave_result = await loop.run_in_executor(executor, leave_guild, guild_id)
                                    await dl_send_message(response.Data.chat_type, f"[B][C]{kx_random_colour()}\n{guildleave_result}", uid, chat_id, key, iv)
                                    
                        if inPuTMsG.strip().startswith('/like '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = "[B][C][FF0000]❌ ERROR! Usage: /like <uid>\nExample: /like 4368569733"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                styled_uid = fixnum(target_uid)
                                processing_message = f"[C][B][FFFFFF]🆔 UID: {styled_uid}\n[C][B][FFFF00]⏳ Sending like...\n[C][B][00FF00]⚡ STAR BOT"
                                await dl_send_message(response.Data.chat_type, processing_message, uid, chat_id, key, iv)
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    like_result = await loop.run_in_executor(executor, send_like, target_uid)
                                final_message = f"[C][B][FFFF00]{like_result}\n[C][B][00FF00]⚡ STAR BOT"
                                await dl_send_message(response.Data.chat_type, final_message, uid, chat_id, key, iv)
                                
                        if inPuTMsG.startswith("/info "):
                            parts = inPuTMsG.strip().split()
                            if len(parts) != 2 or not parts[1].isdigit():
                                await dl_send_message(response.Data.chat_type, "[C][B][FF0000]Usage: /info <uid>", uid, chat_id, key, iv)
                                return
                            target_uid = parts[1]
                            await dl_send_message(response.Data.chat_type, "[C][B][FFFFFF]Please wait, fetching info...", uid, chat_id, key, iv)
                            try:
                                async with aiohttp.ClientSession() as session:
                                    player_data = await fetch_player_info(session, target_uid)
                                    if not player_data or "basicInfo" not in player_data:
                                        await dl_send_message(response.Data.chat_type, "[C][B][FF0000]Player not found or API error.", uid, chat_id, key, iv)
                                        return
                                    await dl_send_message(response.Data.chat_type, format_player_info(player_data), uid, chat_id, key, iv)
                                    await asyncio.sleep(0.1)
                                    clan = player_data.get("clanBasicInfo", {})
                                    guild_id = clan.get("clanId")
                                    if not guild_id:
                                        await dl_send_message(response.Data.chat_type, "[C][B][FFFF00]👤 This player is not in any guild.", uid, chat_id, key, iv)
                                        return
                                    guild_data = await fetch_guild_info(session, guild_id, region)
                                    if not guild_data or guild_data.get("status") != "success":
                                        return
                                    await dl_send_message(response.Data.chat_type, format_guild_basic_info(guild_data), uid, chat_id, key, iv)
                                    await asyncio.sleep(0.1)
                                    await dl_send_message(response.Data.chat_type, format_guild_leader_info(guild_data), uid, chat_id, key, iv)
                                    await asyncio.sleep(0.1)
                                    for officer in guild_data.get("officers", [])[:3]:
                                        await dl_send_message(response.Data.chat_type, format_single_officer(officer), uid, chat_id, key, iv)
                                        await asyncio.sleep(0.1)
                                    notice = format_guild_notice_info(guild_data)
                                    if notice:
                                        await dl_send_message(response.Data.chat_type, notice, uid, chat_id, key, iv)
                            except Exception as e:
                                await dl_send_message(response.Data.chat_type, f"[C][B][FF0000]Error: {str(e)}", uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/pincode'):
                            await handle_pincode_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        if inPuTMsG.strip().startswith('/bundle'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                bundle_list = """[B][C][00FF00]Available bundles:

[FFFFFF]• rampage • cannibal • devil
[FFFFFF]• scorpio • frostfire • paradox
[FFFFFF]• naruto • aurora • midnight
[FFFFFF]• itachi • dreamspace

[00FF00]Use:
[FFFFFF]/bundle <bundle_name>
[FFFFFF]/bundle <bundle_name> 2
"""
                                await dl_send_message(response.Data.chat_type, bundle_list, uid, chat_id, key, iv)
                                continue
                            bundle_name = parts[1].lower()
                            look_type = 1
                            if len(parts) >= 3 and parts[2] == "2":
                                look_type = 2
                            bundle_ids = {
        "rampage": 914000002,
        "cannibal": 914000003,
        "devil": 914038001,
        "scorpio": 914039001,
        "frostfire": 914042001,
        "paradox": 914044001,
        "naruto": 914047001,
        "aurora": 914047002,
        "midnight": 914048001,
        "itachi": 914050001,
        "dreamspace": 914051001
                            }
                            if bundle_name not in bundle_ids:
                                error_msg = f"""[B][C][FF0000]❌ Bundle '{bundle_name}' not found!

[00FF00]Available bundles:
[FFFFFF]• rampage • cannibal • devil
[FFFFFF]• scorpio • frostfire • paradox
[FFFFFF]• naruto • aurora • midnight
[FFFFFF]• itachi • dreamspace

[00FF00]Use:
[FFFFFF]/bundle name
[FFFFFF]/bundle name 2
"""
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            bundle_id = bundle_ids[bundle_name]
                            initial_msg = f"[B][C][00FF00]🎁 Sending Bundle...\n📦 Name: {bundle_name}\n🆔 ID: {bundle_id}\n🎭 Look Type: {look_type}"
                            await dl_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                            try:
                                bundle_packet = await Look_Changer(bundle_id, key, iv, look_type, region)
                                if bundle_packet and online_writer:
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_packet)
                                    success_msg = f"[B][C][00FF00]✅ BUNDLE SENT SUCCESSFULLY!\n📦 Name: {bundle_name}\n🎭 Look: {look_type}\n👤 Target: {uid}"
                                    await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                else:
                                    await dl_send_message(response.Data.chat_type, "[B][C][FF0000]❌ Failed to create bundle packet!", uid, chat_id, key, iv)
                            except Exception as e:
                                await dl_send_message(response.Data.chat_type, f"[B][C][FF0000]❌ Error: {str(e)[:60]}", uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/add '):
                            if str(uid) != ADMIN_UID:
                                error_msg = "[B][C][FF0000]❌ ERROR! Only the admin can use this command."
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                parts = inPuTMsG.strip().split()
                                if len(parts) < 2:
                                    error_msg = "[B][C][FF0000]❌ ERROR! Usage: /add <uid>\nExample: /add 4368569733"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    target_uid = parts[1]
                                    styled_uid = fixnum(target_uid)
                                    processing_message = f"[C][B][FFFFFF]🆔 UID: {styled_uid}\n[C][B][FFFF00]⏳ Friend Request sending...\n[C][B][00FF00]⚡ STAR BOT"
                                    await dl_send_message(response.Data.chat_type, processing_message, uid, chat_id, key, iv)
                                    loop = asyncio.get_event_loop()
                                    with ThreadPoolExecutor() as executor:
                                        add_result = await loop.run_in_executor(executor, add_friend, target_uid)
                                    final_message = f"[C][B][FFFFFF]🆔 UID: {styled_uid}\n[C][B][FFFF00]{add_result}\n[C][B][00FF00]⚡ STAR BOT"
                                    await dl_send_message(response.Data.chat_type, final_message, uid, chat_id, key, iv)
                                    
                        if inPuTMsG.strip().startswith('/remove '):
                            if str(uid) != ADMIN_UID:
                                error_msg = "[B][C][FF0000]❌ ERROR! Only the admin can use this command."
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                parts = inPuTMsG.strip().split()
                                if len(parts) < 2:
                                    error_msg = "[B][C][FF0000]❌ ERROR! Usage: /remove <uid>\nExample: /remove 4368569733"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    target_uid = parts[1]
                                    styled_uid = fixnum(target_uid)
                                    processing_message = f"[C][B][FFFFFF]🆔 UID: {styled_uid}\n[C][B][FFFF00]⏳ Removing from friend list...\n[C][B][00FF00]⚡ STAR BOT"
                                    await dl_send_message(response.Data.chat_type, processing_message, uid, chat_id, key, iv)
                                    loop = asyncio.get_event_loop()
                                    with ThreadPoolExecutor() as executor:
                                        remove_result = await loop.run_in_executor(executor, remove_friend, target_uid)
                                    final_message = f"[C][B][FFFFFF]🆔 UID: {styled_uid}\n[C][B][FFFF00]{remove_result}\n[C][B][00FF00]⚡ STAR BOT"
                                    await dl_send_message(response.Data.chat_type, final_message, uid, chat_id, key, iv)
                                    
                        if inPuTMsG.strip().startswith('/friend_list'):
                            await handle_friend_list_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            continue
                            
                        if inPuTMsG.strip().startswith('/bio '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /bio <uid>\nExample: /bio 4368569733\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{kx_random_colour()}\nFetching the player bio...\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    bio_result = await loop.run_in_executor(executor, get_player_bio, target_uid)
                                await dl_send_message(response.Data.chat_type, f"\n{bio_result}", uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().lower().startswith('/ghost '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = "[B][C][FF0000]❌ ERROR! Usage: /Ghost <teamcode> <ghostname>\nExample: /Ghost 123456 STAR\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                ghost_name = " ".join(parts[2:]).upper()
                                initial_message = f"[B][C]{kx_random_colour()}⚡ Generating Ghost Join...\n👻 Name: {ghost_name}\n🔢 TeamCode: {team_code}\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    ghost_result = await loop.run_in_executor(executor, get_ghost_api, team_code, ghost_name)
                                final_msg = f"[B][C]{kx_random_colour()}\n{ghost_result}"
                                await dl_send_message(response.Data.chat_type, final_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/quick'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /quick (team_code) [emote_id] [target_uid]\n\n[FFFFFF]Examples:\n[00FF00]/quick ABC123[FFFFFF] - Join, send hammer_slam emote, leave\n[00FF00]/ghostquick ABC123[FFFFFF] - Ghost join, send emote, leave\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                emote_id = parts[0]
                                target_uid = str(response.Data.uid)
                                if len(parts) >= 3:
                                    emote_id = parts[2]
                                if len(parts) >= 4:
                                    target_uid = parts[3]
                                if target_uid == str(response.Data.uid):
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {target_uid}"
                                initial_message = f"[B][C][FFFF00]⚡ QUICK EMOTE ATTACK!\n\n[FFFFFF]🎯 Team: [00FF00]{team_code}\n[FFFFFF]🎭 Emote: [00FF00]{emote_id}\n[FFFFFF]👤 Target: [00FF00]{target_name}\n[FFFFFF]⏱️ Estimated: [00FF00]2 seconds\n\n[FFFF00]Executing sequence...\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                try:
                                    success, result = await ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region)
                                    if success:
                                        success_message = f"[B][C][00FF00]✅ QUICK ATTACK SUCCESS!\n\n[FFFFFF]🏷️ Team: [00FF00]{team_code}\n[FFFFFF]🎭 Emote: [00FF00]{emote_id}\n[FFFFFF]👤 Target: [00FF00]{target_name}\n\n[00FF00]Bot joined → emoted → left! ✅\n"
                                    else:
                                        success_message = f"[B][C][FF0000]❌ Regular attack failed: {result}\n"
                                    await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                except Exception as e:
                                    pass
                                    
                        if inPuTMsG.strip().startswith('/inv '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /inv (uid)\nExample: /inv 123456789\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{kx_random_colour()}\nCreating 5-Player Group and sending request to {target_uid}...\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                try:
                                    PAc = await OpEnSq(key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                    C = await cHSq(5, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                    await asyncio.sleep(0.3)
                                    V = await SEnd_InV(5, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.3)
                                    E = await ExiT(None, key, iv)
                                    await asyncio.sleep(2)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                                    success_message = f"[B][C][00FF00]✅ SUCCESS! 5-Player Group invitation sent successfully to {target_uid}!\n"
                                    await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending invite: {str(e)}\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                        if inPuTMsG.startswith(("/6")):
                            initial_message = f"[B][C][00FF00]6 MEMBERS GROUP CREATED! \nAccept Invite Fast!\n"
                            await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            C = await cHSq(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            V = await SEnd_InV(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            success_message = f"[B][C][00FF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                            
                        if inPuTMsG.startswith(("/3")):
                            initial_message = f"[B][C][00FF00]3 MEMBERS GROUP CREATED! \nAccept Invite Fast!\n"
                            await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            C = await cHSq(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            V = await SEnd_InV(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            success_message = f"[B][C][00FF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                            
                        if inPuTMsG.startswith(("/5")):
                            initial_message = f"[B][C][00FF00]5 MEMBERS GROUP CREATED! \nAccept Invite Fast!\n"
                            await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            C = await cHSq(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            V = await SEnd_InV(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            success_message = f"[B][C][00FF00]✅ SUCCESS! Group invitation sent successfully to {uid}!\n"
                            await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                            
                        if inPuTMsG.strip() == "/admin":
                            admin_message = """
[C][B][FFD700]    ✦─────────✦
       💧 STAR BOT ADMIN
    ✦─────────✦

[C][B][00FF00]👑 BOT DEVELOPER: 
[C][B][FFFFFF] HUSSNAIN  SK

[B][C][FFFFFF]TikTok : @DARK_REALITY.EXE
[B][C][FFFFFF]Contact : @HUSSNAINSK

[C][B][00FF00]🆔 OWNER UIDs:
[FFFFFF]
4[C]3[C]6[C]8[C]5[C]6[C]9[C]7[C]3[C]3[C] & 1[C]3[C]6[C]9[C]9[C]7[C]7[C]6[C]6[C]6[C]6[C]

[C][B][00FF00]💼 BUSINESS:
[C][B][FFFFFF]Want to buy this bot?
[C][B][FFFFFF]DM me for cheapest price!

✦ ──PREMIUM QUALITY── ✦
"""
                            await dl_send_message(response.Data.chat_type, admin_message, uid, chat_id, key, iv)
                            
                        if inPuTMsG.strip().startswith('/reject'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /reject (target_uid)\nExample: /reject 123456789\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                if reject_spam_task and not reject_spam_task.done():
                                    reject_spam_running = False
                                    reject_spam_task.cancel()
                                    await asyncio.sleep(0.5)
                                start_msg = f"[B][C][1E90FF]🌀 Started Reject Spam on: {target_uid}\n🌀 Packets: 150 each type\n🌀 Interval: 0.2 seconds\n"
                                await dl_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
                                reject_spam_running = True
                                reject_spam_task = asyncio.create_task(reject_spam_loop(target_uid, key, iv))
                                asyncio.create_task(handle_reject_completion(reject_spam_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv))
                                
                        if inPuTMsG.strip() == '/reject_stop':
                            if reject_spam_task and not reject_spam_task.done():
                                reject_spam_running = False
                                reject_spam_task.cancel()
                                stop_msg = f"[B][C][00FF00]✅ Reject spam stopped successfully!\n"
                                await dl_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ No active reject spam to stop!\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/rmjoin '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /rmjoin [room_id] [password]\nExample: /rmjoin 12345678\nExample: /rmjoin 12345678 123\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]
                                password = parts[2] if len(parts) > 2 else ""
                                initial_msg = f"[B][C][00FF00]🎮 Joining custom room...\nRoom ID: {room_id}\nPassword: {'Yes' if password else 'No'}\n"
                                await dl_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                try:
                                    await reset_bot_state(key, iv, region)
                                    await asyncio.sleep(1)
                                    join_packet = await RoomJoin(room_id, password, key, iv)
                                    if join_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                        success_msg = f"[B][C][00FF00]✅ Successfully joined room {room_id}!\n"
                                        await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ Failed to join room {room_id}\n"
                                        await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Error joining room: {str(e)}\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                        if inPuTMsG.strip() == '/rmleave' or inPuTMsG.strip().startswith('/rmleave '):
                            parts = inPuTMsG.strip().split()
                            target_uid = uid
                            if len(parts) > 1:
                                target_uid = parts[1]
                            initial_msg = f"[B][C][00FF00]🚪 Leaving room...\nTarget UID: {target_uid}\n"
                            await dl_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                            try:
                                leave_packet = await XRLeaveRoom(target_uid, key, iv)
                                if leave_packet:
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
                                    success_msg = f"[B][C][00FF00]✅ Successfully left room!\n"
                                    await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                else:
                                    error_msg = f"[B][C][FF0000]❌ Failed to create leave packet\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ Error leaving room: {str(e)}\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        elif inPuTMsG.startswith('/rmlag '):
                            try:
                                parts = inPuTMsG.strip().split()
                                if len(parts) < 3:
                                    msg = f"[B][C][FF0000]❌ Usage: /rmlag <room_id> <password>"
                                    await dl_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                    return
                                room_id = parts[1]
                                password = parts[2]
                                async def run_simple_lag():
                                    start_time = time.time()
                                    while time.time() - start_time < 10:
                                        join_pkt = await RoomJoin(int(room_id), password, key, iv)
                                        if online_writer and join_pkt:
                                            online_writer.write(join_pkt)
                                            await online_writer.drain()
                                        leave_pkt = await XRLeaveRoom(int(uid), key, iv)
                                        if online_writer and leave_pkt:
                                            online_writer.write(leave_pkt)
                                            await online_writer.drain()
                                        await asyncio.sleep(0.10)
                                msg = f"[B][C][00FF00]✅ Room lag started for 10 seconds!"
                                await dl_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                asyncio.create_task(run_simple_lag())
                            except Exception as e:
                                pass
                                
                        if inPuTMsG.strip().startswith('/room'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ Usage: /room [uid] [room_id]\nExample: /room 123456789 987654321\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                room_id = parts[2]
                                initial_msg = f"[B][C][00FF00]🌀 ROOM SPAM: 99 requests\n🎯 Target: {target_uid}\n🏠 Room: {room_id}\n🔄 s1→s5 rotation\n⚡ 0.02s delay\n"
                                await dl_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                try:
                                    success = await Room_Spam(target_uid, room_id, "STAR GAMER", key, iv)
                                    if success:
                                        success_msg = f"[B][C][00FF00]✅ ROOM SPAM COMPLETE!\n🎯 Target: {target_uid}\n🏠 Room: {room_id}\n📦 99 packets\n⚡ 0.02s delay\n"
                                        await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Room spam error: {str(e)}\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                        if inPuTMsG.strip().startswith('/s1'):
                            await handle_badge_command('s1', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                        if inPuTMsG.strip().startswith('/s2'):
                            await handle_badge_command('s2', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                        if inPuTMsG.strip().startswith('/s3'):
                            await handle_badge_command('s3', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                        if inPuTMsG.strip().startswith('/s4'):
                            await handle_badge_command('s4', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                        if inPuTMsG.strip().startswith('/s5'):
                            await handle_badge_command('s5', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                        if inPuTMsG.strip().startswith('/spam'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = "[B][C][FF0000]❌ Usage: /spam <uid>\nExample: /spam 123456789\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                total_requests = SPAM_REQUESTS
                                badge_sequence = ['s1', 's2', 's3', 's4', 's5']
                                try:
                                    await reset_bot_state(key, iv, region)
                                    count = 0
                                    while count < total_requests:
                                        current_badge = badge_sequence[count % len(badge_sequence)]
                                        badge_value = BADGE_VALUES[current_badge]
                                        join_packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                                        count += 1
                                        await asyncio.sleep(PACKET_DELAY_ULTRA_FAST)
                                    await reset_bot_state(key, iv, region)
                                    success_msg = f"[B][C][00FF00]✅ SPAM SUCCESS!\n🎯 Target: {target_uid}\n📦 Requests: {count}\n🔄 Badges: s1 → s5\n"
                                    await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Spam error: {str(e)}\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                        if inPuTMsG.startswith('/join'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /join (team_code)\nExample: /join ABC123\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                sender_uid = response.Data.uid
                                initial_message = f"[C][B][00FF00]🤖 Joining Team \n[C][B][FFFF00]Team Code:[00FFFF] {CodE}\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                try:
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
                                    await asyncio.sleep(2)
                                    try:
                                        await auto_hammer_slam_emote_dual(sender_uid, key, iv, region)
                                    except Exception as emote_error:
                                        pass
                                    success_message = f"[B][C][00FF00]✅ SUCCESS! Joined squad: {CodE}!\n💍 Dual hammer_slam emote activated!\n🤖 Bot + You = 💕\n"
                                    await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Failed to join squad: {str(e)}\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                        if inPuTMsG.strip().startswith('/exploit_start'):
                            await handle_exploit_start(uid, chat_id, response.Data.chat_type, key, iv)
                            continue
                        if inPuTMsG.strip().startswith('/exploit_stop'):
                            await handle_exploit_stop(uid, chat_id, response.Data.chat_type, key, iv)
                            continue
                        if inPuTMsG.strip().startswith('/exploit_status'):
                            await handle_exploit_status(uid, chat_id, response.Data.chat_type, key, iv)
                            continue
                            
                        if inPuTMsG.strip().lower() == '/emote_list':
                            await handle_emote_list_command(uid, chat_id, response.Data.chat_type, key, iv)
                            continue
                            
                        if inPuTMsG.strip().startswith('/dance'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) == 2:
                                target_uids = [int(uid)]
                                emote_identifier = parts[1].strip().lower()
                                initial_message = f'[B][C]{kx_random_colour()}\nSending emote to yourself...\n'
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            elif len(parts) >= 3:
                                target_uids = []
                                emote_identifier = parts[-1].strip().lower()
                                for part in parts[1:-1]:
                                    if part.isdigit() and len(part) >= 7:
                                        target_uids.append(int(part))
                                if not target_uids:
                                    error_msg = "[B][C][FF0000]❌ ERROR! No valid UIDs found.\n[00FF00]Usage: /dance [uid] [emote_number/name]\n[00FF00]Example: /dance 123456789 1\n[00FF00]Example: /dance 123456789 hello\n[00FF00]Example: /dance 1 (for yourself)\n[00FF00]Example: /dance hello (for yourself)"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                                initial_message = f'[B][C]{kx_random_colour()}\nSending emote to target(s)...\n'
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            else:
                                error_msg = "[B][C][FF0000]❌ ERROR! Usage:\n[00FF00]For yourself:\n[FFFFFF]  /dance [emote_number]\n[FFFFFF]  /dance [emote_name]\n\n[00FF00]For others:\n[FFFFFF]  /dance [uid] [emote_number]\n[FFFFFF]  /dance [uid] [emote_name]\n\n[00FF00]Examples:\n[FFFFFF]  /dance 1           (send emote 1 to yourself)\n[FFFFFF]  /dance hello       (send 'hello' emote to yourself)\n[FFFFFF]  /dance 123456789 1 (send emote 1 to UID 123456789)\n[FFFFFF]  /dance 123456789 hello (send 'hello' to UID 123456789)"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            import os
                            emote_map_by_number = {}
                            emote_map_by_name = {}
                            emote_names_list = []
                            try:
                                script_dir = os.path.dirname(os.path.abspath(__file__))
                                emotes_path = os.path.join(script_dir, 'emotes.json')
                                with open(emotes_path, 'r', encoding='utf-8') as f:
                                    emotes_data = json.load(f)
                                    for entry in emotes_data:
                                        num = str(entry['Number']).strip()
                                        emote_id = str(entry['Id']).strip()
                                        emote_name = entry.get('Name', '').strip().lower()
                                        emote_map_by_number[num] = emote_id
                                        if emote_name:
                                            emote_map_by_name[emote_name] = emote_id
                                        if emote_name:
                                            emote_names_list.append(emote_name)
                            except FileNotFoundError:
                                error_msg = "[C][B][FF0000]Error: emotes.json file not found.\nPlease contact admin to add the file."
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            except (json.JSONDecodeError, KeyError) as e:
                                error_msg = f"[C][B][FF0000]Error: emotes.json format incorrect.\n{str(e)}"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            except Exception as e:
                                error_msg = f"[C][B][FF0000]Error loading emotes: {str(e)}"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            emote_id_to_send = None
                            emote_name_display = None
                            if emote_identifier.isdigit():
                                if emote_identifier in emote_map_by_number:
                                    emote_id_to_send = emote_map_by_number[emote_identifier]
                                    for entry in emotes_data:
                                        if str(entry['Number']) == emote_identifier:
                                            emote_name_display = entry.get('Name', f"Emote {emote_identifier}")
                                            break
                                    if not emote_name_display:
                                        emote_name_display = f"Emote {emote_identifier}"
                                else:
                                    max_emote = len(emote_map_by_number)
                                    error_msg = f"[B][C][FF0000]Invalid emote number: {emote_identifier}\n[00FF00]Available numbers: 1-{max_emote}\n[00FF00]Try: /dance [1-{max_emote}]"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                            else:
                                if emote_identifier in emote_map_by_name:
                                    emote_id_to_send = emote_map_by_name[emote_identifier]
                                    emote_name_display = emote_identifier.title()
                                else:
                                    similar = [name for name in emote_names_list if emote_identifier in name]
                                    if similar:
                                        error_msg = f"[B][C][FF0000]Emote '{emote_identifier}' not found.\n[00FF00]Similar names: {', '.join(similar[:5])}\n[FFFFFF]Try one of these."
                                    else:
                                        popular_names = ['hello', 'dance', 'ak', 'scar', 'p90', 'm60', 'breakdance', 'kungfu']
                                        available = [name for name in popular_names if name in emote_names_list]
                                        if available:
                                            error_msg = f"[B][C][FF0000]Emote '{emote_identifier}' not found.\n[00FF00]Popular names: {', '.join(available)}\n[FFFFFF]Use /emote_list to see all names."
                                        else:
                                            error_msg = f"[B][C][FF0000]Emote '{emote_identifier}' not found.\n[FFFFFF]Use /emote_list to see all available emotes."
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                            try:
                                sent_count = 0
                                for target in target_uids:
                                    H = await Emote_k(target, int(emote_id_to_send), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                    sent_count += 1
                                    await asyncio.sleep(0.1)
                                if len(target_uids) == 1 and target_uids[0] == int(uid):
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS!\n🎭 Emote: {emote_name_display} (ID: {emote_id_to_send})\n🎯 Sent to: Yourself\n😊 Enjoy your emote!"
                                else:
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS!\n🎭 Emote: {emote_name_display} (ID: {emote_id_to_send})\n🎯 Sent to: {sent_count} player(s)\n👥 Targets: {', '.join(map(str, target_uids))}\n"
                                await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR sending emote: {str(e)}\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/lag '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /lag (team_code)\nExample: /lag ABC123\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)
                                lag_running = True
                                lag_task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Lag attack started!\nTeam: {team_code}\nAction: Rapid join/leave\nSpeed: Ultra fast (milliseconds)\n"
                                await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip() == '/stop lag':
                            if lag_task and not lag_task.done():
                                lag_running = False
                                lag_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Lag attack stopped successfully!\n"
                                await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active lag attack to stop!\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/lagx'):
                            initial_message = f"[B][C]{kx_random_colour()}\nStarting new lag attack...\n"
                            await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            try:
                                for i in range(2111):
                                    C = await new_lag(key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                    await asyncio.sleep(0.003)
                                success_message = f"[B][C][00FF00]✅ SUCCESS! new lag attack completed!\n"
                                await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR in lagx command: {str(e)}\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/kick'):
                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)
                                if len(parts) < 2:
                                    return
                                target_uid = parts[1]
                                C = await KickTarget(target_uid, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            except Exception as e:
                                pass
                        if inPuTMsG.startswith('/exit'):
                            initial_message = f"[B][C]{kx_random_colour()}\nLeaving current squad...\n"
                            await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            leave = await ExiT(uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave)
                            success_message = f"[C][B][FF0000]╔═════════╗[C][B][FFFFFF]                  LEAVING GROUP [C][B][00FF00]╚═════════╝     \n[C][B][FFFF00]🚪 Bot is leaving...[84D4F1]            \n[C][B][FF00FF]👋 Goodbye![FFA500]\n"
                            await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/title_sm'):
                            await handle_title_sm_command(inPuTMsG, uid, chat_id, key, iv, region, 0)
                        if inPuTMsG.strip().startswith('/title'):
                            await handle_title_final(inPuTMsG, uid, chat_id, key, iv, region, 0)
                        if inPuTMsG.strip().startswith('/'):
                            await handle_title_final(inPuTMsG, uid, chat_id, key, iv, region, 0)
                        if inPuTMsG.strip().startswith('/sticker'):
                            packet = await send_sticker(uid, chat_id, key, iv, nickname="DEVILxBOT")
                            if packet:
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', packet)
                        if inPuTMsG.strip().startswith('/e'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /e (uid) (emote_id)\nExample: /e 123456789 909000001\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            initial_message = f'[B][C]{kx_random_colour()}\nSending emote to target...\n'
                            await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            uid2 = uid3 = uid4 = uid5 = None
                            s = False
                            target_uids = []
                            try:
                                target_uid = int(parts[1])
                                target_uids.append(target_uid)
                                uid2 = int(parts[2]) if len(parts) > 2 else None
                                if uid2:
                                    target_uids.append(uid2)
                                uid3 = int(parts[3]) if len(parts) > 3 else None
                                if uid3:
                                    target_uids.append(uid3)
                                uid4 = int(parts[4]) if len(parts) > 4 else None
                                if uid4:
                                    target_uids.append(uid4)
                                uid5 = int(parts[5]) if len(parts) > 5 else None
                                if uid5:
                                    target_uids.append(uid5)
                                idT = int(parts[-1])
                            except ValueError as ve:
                                s = True
                            except Exception as e:
                                s = True
                            if not s:
                                try:
                                    for target in target_uids:
                                        H = await Emote_k(target, idT, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        await asyncio.sleep(0.1)
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS! Emote {idT} sent to {len(target_uids)} player(s)!\nTargets: {', '.join(map(str, target_uids))}\n"
                                    await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending emote: {str(e)}\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Invalid UID format. Usage: /e (uid) (emote_id)\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/lw'):
                            global auto_start_running, auto_start_teamcode, stop_auto, auto_start_task
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /lw (team_code)\nExample: /lw 123456\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                if not team_code.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Team code must be numbers only!\nExample: /lw 123456\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                                if auto_start_running:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Auto start already running for team {auto_start_teamcode}!\nUse /stop_auto to stop first.\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
                                global auto_start_task, stop_auto
                                stop_auto = False
                                auto_start_running = True
                                auto_start_teamcode = team_code
                                initial_msg = f"""
[B][C][00FFFF]🤖 AUTO START BOT ACTIVATED!

🎯 Team Code: {team_code}
⚡ Action: Join → Start → Wait → Leave → Repeat
⏰ Start Spam: {start_spam_duration} seconds
⏳ Wait Time: {wait_after_match} seconds
🔄 Loop: Continuous 24x7

💡 To stop: /stop_auto
"""
                                await dl_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                auto_start_task = asyncio.create_task(auto_start_loop(team_code, uid, chat_id, response.Data.chat_type, key, iv, region))
                        if inPuTMsG.strip().startswith('/random'):
                            parts = inPuTMsG.strip().split()
                            uids = []
                            sender_uid = str(response.Data.uid)
                            if len(parts) == 1:
                                uids.append(sender_uid)
                            else:
                                for part in parts[1:]:
                                    if part.isdigit() and len(part) >= 7:
                                        uids.append(part)
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(evo_cycle_spam(uids, key, iv, region))
                            if len(parts) == 1:
                                success_msg = "[B][C][00FF00]✅ SUCCESS!\n🎯 Target: Yourself\n🎭 Emotes: All 18 evolution emotes\n⏰ Delay: 5 seconds\n🔄 Loop: Until /ruk bhai\n"
                            else:
                                success_msg = f"[B][C][00FF00]✅ SUCCESS!\n🎯 Targets: {len(uids)} player(s)\n🎭 Emotes: All 18 evolution emotes\n⏰ Delay: 5 seconds\n🔄 Loop: Until /ruk bhai\n"
                            await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/legendary_emote'):
                            parts = inPuTMsG.strip().split()
                            uids = []
                            sender_uid = str(response.Data.uid)
                            if len(parts) == 1:
                                uids.append(sender_uid)
                            else:
                                for part in parts[1:]:
                                    if part.isdigit() and len(part) >= 7:
                                        uids.append(part)
                            if legendry_cycle_task and not legendry_cycle_task.done():
                                legendry_cycle_running = False
                                legendry_cycle_task.cancel()
                                await asyncio.sleep(0.5)
                            legendry_cycle_running = True
                            legendry_cycle_task = asyncio.create_task(legendry_emote_cycle(uids, key, iv, region))
                            if len(parts) == 1:
                                success_msg = "[B][C][00FF00]✅ SUCCESS!\n🎯 Target: Yourself\n🎭 Emotes: All 22 legendry emotes\n⏰ Delay: 5 seconds\n🔄 Loop: Until /ruk bhai\n"
                            else:
                                success_msg = f"[B][C][00FF00]✅ SUCCESS!\n🎯 Targets: {len(uids)} player(s)\n🎭 Emotes: All 22 legendry emotes\n⏰ Delay: 5 seconds\n🔄 Loop: Until /ruk bhai\n"
                            await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip() == '/ruk bhai':
                            stopped_any = False
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                stopped_any = True
                            if legendry_cycle_task and not legendry_cycle_task.done():
                                legendry_cycle_running = False
                                legendry_cycle_task.cancel()
                                stopped_any = True
                            if stopped_any:
                                success_msg = "[B][C][00FF00]✅ SUCCESS!\n🛑 All active emote cycles stopped successfully!\n"
                                await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = "[B][C][FF0000]❌ ERROR!\n🚫 No active emote cycle is running!\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip() == '/ruk bhai':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution emote cycle stopped successfully!\n"
                                await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution emote cycle to stop!\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/fast'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /fast uid1 [uid2] [uid3] [uid4] emoteid\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                uids = []
                                emote_id = None
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) > 3:
                                            uids.append(part)
                                        else:
                                            emote_id = part
                                    else:
                                        break
                                if not emote_id and parts[-1].isdigit():
                                    emote_id = parts[-1]
                                if not uids or not emote_id:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /fast uid1 [uid2] [uid3] [uid4] emoteid\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    if fast_spam_task and not fast_spam_task.done():
                                        fast_spam_running = False
                                        fast_spam_task.cancel()
                                    fast_spam_running = True
                                    fast_spam_task = asyncio.create_task(fast_emote_spam(uids, emote_id, key, iv, region))
                                    success_msg = f"[B][C][00FF00]✅ SUCCESS! Fast emote spam started!\nTargets: {len(uids)} players\nEmote: {emote_id}\nSpam count: 25 times\n"
                                    await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/p'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 4:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /p (uid) (emote_id) (times)\nExample: /p 123456789 909000001 10\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    target_uid = parts[1]
                                    emote_id = parts[2]
                                    times = int(parts[3])
                                    if times <= 0:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Times must be greater than 0!\n"
                                        await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif times > 100:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Maximum 100 times allowed for safety!\n"
                                        await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        if custom_spam_task and not custom_spam_task.done():
                                            custom_spam_running = False
                                            custom_spam_task.cancel()
                                            await asyncio.sleep(0.5)
                                        custom_spam_running = True
                                        custom_spam_task = asyncio.create_task(custom_emote_spam(target_uid, emote_id, times, key, iv, region))
                                        success_msg = f"[B][C][00FF00]✅ SUCCESS! Custom emote spam started!\nTarget: {target_uid}\nEmote: {emote_id}\nTimes: {times}\n"
                                        await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Usage: /p (uid) (emote_id) (times)\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! {str(e)}\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/spm_inv '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /spm_inv (uid)\nExample: /spm_inv 123456789\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{kx_random_colour()}\nStarting spam invite: sending invites in batches of 7...\n"
                                await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                spm_inv_running = True
                                total_invites = 57
                                batch_size = 7
                                count = 0
                                try:
                                    while count < total_invites and spm_inv_running:
                                        current_batch = min(batch_size, total_invites - count)
                                        for _ in range(current_batch):
                                            if not spm_inv_running:
                                                break
                                            PAc = await OpEnSq(key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                            await asyncio.sleep(0.1)
                                            C = await cHSq(5, int(target_uid), key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                            await asyncio.sleep(0.1)
                                            V = await SEnd_InV(5, int(target_uid), key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                            await asyncio.sleep(0.1)
                                            E = await ExiT(None, key, iv)
                                            await asyncio.sleep(0.1)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                                            count += 1
                                        if count % batch_size == 0 and spm_inv_running:
                                            pause_message = f"[B][C][FFFF00]⏳ Pausing 10 seconds after 3 invites...\n"
                                            await dl_send_message(response.Data.chat_type, pause_message, uid, chat_id, key, iv)
                                            await asyncio.sleep(10)
                                    success_message = f"[B][C][00FF00]✅ SUCCESS! Finished spamming 30 invites to {target_uid}!\n"
                                    await dl_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending invite: {str(e)}\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/evo '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo 123456789 1\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                uids = []
                                number = None
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{kx_random_colour()}\nSending evolution emote {number_int}...\n"
                                            await dl_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            success, result_msg = await evo_emote_spam(uids, number_int, key, iv, region)
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ SUCCESS! {result_msg}\n"
                                                await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/evo_fast '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo_fast 123456789 1\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                uids = []
                                number = None
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                                evo_fast_spam_running = False
                                                evo_fast_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            evo_fast_spam_running = True
                                            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam(uids, number_int, key, iv, region))
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][00FF00]✅ SUCCESS! Fast evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nSpam count: 25 times\nInterval: 0.1 seconds\n"
                                            await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/evo_c '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\nExample: /evo_c 123456789 1 10\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                uids = []
                                number = None
                                time_val = None
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:
                                            if number is None:
                                                number = part
                                            elif time_val is None:
                                                time_val = part
                                            else:
                                                uids.append(part)
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                if not time_val and len(parts) >= 3:
                                    last_part = parts[-1]
                                    if last_part.isdigit() and len(last_part) <= 3:
                                        time_val = last_part
                                        if time_val in uids:
                                            uids.remove(time_val)
                                if not uids or not number or not time_val:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\n"
                                    await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        time_int = int(time_val)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        elif time_int < 1 or time_int > 100:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Time must be between 1-100 only!\n"
                                            await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                                evo_custom_spam_running = False
                                                evo_custom_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            evo_custom_spam_running = True
                                            evo_custom_spam_task = asyncio.create_task(evo_custom_emote_spam(uids, number_int, time_int, key, iv, region))
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][00FF00]✅ SUCCESS! Custom evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nRepeat: {time_int} times\nInterval: 0.1 seconds\n"
                                            await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number/time format! Use numbers only.\n"
                                        await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip() == '/stop evo_fast':
                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                evo_fast_spam_running = False
                                evo_fast_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution fast spam stopped successfully!\n"
                                await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution fast spam to stop!\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip() == '/stop evo_c':
                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                evo_custom_spam_running = False
                                evo_custom_spam_task.cancel()
                                success_msg = f"[B][C][00FF00]✅ SUCCESS! Evolution custom spam stopped successfully!\n"
                                await dl_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution custom spam to stop!\n"
                                await dl_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.strip().lower() == "star bhai mera uid do":
                            styled_uid = fixnum(str(uid))
                            reply_text = f"[B][C][FFFFFF]Le bhai tera uid : {styled_uid}"
                            await dl_send_message(response.Data.chat_type, reply_text, uid, chat_id, key, iv)
                        if inPuTMsG.strip().lower() == "hi":
                            nickname = await get_nickname_from_api(uid)
                            greeting_message = f"[B][C][FFFFFF]Hello {nickname}!"
                            await dl_send_message(response.Data.chat_type, greeting_message, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/4368569733'):
                            parts = inPuTMsG.strip().split(maxsplit=1)
                            if len(parts) < 2:
                                await dl_send_message(response.Data.chat_type, "[B][C][FF0000]Usage: /4368569733 (message)", uid, chat_id, key, iv)
                            else:
                                raw_text = parts[1]
                                message_text = f"[B][C][FFFFFF]{raw_text}"
                                packet = await SEndMsG(0, message_text, None, chat_id, key, iv)
                                if packet:
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', packet)
                    if inPuTMsG.strip() == '/restart':
                        restart_msg = f"[B][C][FFFF00]🔄 Bot restarting...\n⏳ Please wait 10 seconds...\n"
                        await dl_send_message(response.Data.chat_type, restart_msg, uid, chat_id, key, iv)
                        if online_writer:
                            online_writer.close()
                        if whisper_writer:
                            whisper_writer.close()
                        await asyncio.sleep(2)
                        os._exit(0)
                    if inPuTMsG.strip().lower() in ("help", "/help", "menu", "/menu", "commands"):
                        uid = getattr(response.Data, 'uid', None)
                        if not uid:
                            uid = "UnknownUID"
                        nickname = await get_nickname_from_api(uid)
                        header = f"[C][B][FFD700]Hey {nickname} Welcome to 𝐒ᴛᴀʀ ɢᴜɪʟᴅᴮᴼᵀ!\n\n[C][B][FFFFFF]Type commands to interact with me.\n[C][B][00FF00]Below are all available commands:"
                        await dl_send_message(response.Data.chat_type, header, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        group_commands = """[C][B][FFD700]╭──────────╮
│    GROUP CMDS                     │
╰──────────╯
[C][B][FFFFFF]┌─ /3 [00FF00]- Create 3 Player Group
[C][B][FFFFFF]├─ /5 [00FF00]- Create 5 Player Group
[C][B][FFFFFF]├─ /6 [00FF00]- Create 6 Player Group
[C][B][FFFFFF]├─ /inv [uid] [00FF00]- Invite Player to Current Group
[C][B][FFFFFF]├─ /join [team_code] [00FF00]- Join Team Using Team Code
[C][B][FFFFFF]└─ /exit [00FF00]- Leave Current Group"""
                        await dl_send_message(response.Data.chat_type, group_commands, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        player_info = """[C][B][FFD700]╭──────────╮
│    INFO CMDS                           │
╰──────────╯
[C][B][FFFFFF]┌─ /info [uid] [00FF00]- Full Player Information
[C][B][FFFFFF]├─ /bio [uid] [00FF00]- Get Player Bio
[C][B][FFFFFF]├─ /ig [username]     [00FF00]- Fetch Instagram User Info
[C][B][FFFFFF]├─ /tk [username]     [00FF00]- Fetch TikTok User Info
[C][B][FFFFFF]├─ /yt [channel_name] [00FF00]- Fetch YouTube Channel Info
[C][B][FFFFFF]├─ /num [phone_number] [00FF00]- Phone To Information
[C][B][FFFFFF]└─/pincode [pincode] [00FF00]- Pincode To Area Information"""
                        await dl_send_message(response.Data.chat_type, player_info, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        advanced_commands = """[C][B][FFD700]╭──────────╮
│  ADVANCED CMDS               │
╰──────────╯
[C][B][FFFFFF]┌─ /lw [team_code] [00FF00]- Start Level Up Bot (24×7) for Team
[C][B][FFFFFF]├─ /stop_auto [00FF00]- Stop Level Up Bot
[C][B][FFFFFF]├─ /spm_inv [uid] [00FF00]- Spam Invites (30x) to Player
[C][B][FFFFFF]├─ /ghost [team_code] [name] [00FF00]- Ghost Join Team Using Code
[C][B][FFFFFF]├─ /lag [team_code] [00FF00]- Start Lag Attack on Team
[C][B][FFFFFF]├─ /lagx [00FF00]- Start Lag Attack (Without TC)
[C][B][FFFFFF]├─ /reject [uid] [00FF00]- Reject Incoming Spam Requests"""
                        await dl_send_message(response.Data.chat_type, advanced_commands, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        room_commands = """[C][B][FFD700]╭──────────╮
│    ROOM CMDS                        │
╰──────────╯
[C][B][FFFFFF]┌─ /rmjoin [room_id] [password] [00FF00]- Join Custom Room
[C][B][FFFFFF]├─ /rmleave [uid] [00FF00]- Leave Custom Room
[C][B][FFFFFF]├─ /rmlag [room_id] [password] [00FF00]- Room Lag Attack (10 seconds)
[C][B][FFFFFF]└─ /room [uid] [room_id] [00FF00]- Join Request With New V-Badge In Room"""
                        await dl_send_message(response.Data.chat_type, room_commands, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        emote_commands = """[C][B][FFD700]╭──────────╮
│    EMOTE CMDS                       │
╰──────────╯
[C][B][FFFFFF]┌─ /e [uid] [emote_id] [00FF00]- Send Single Emote to Player
[C][B][FFFFFF]├─ /dance [uid] [1-384] [00FF00]- Play emote by number (1-384)
[C][B][FFFFFF]├─ /dance [uid] [name] [00FF00]- Play emote by name (ex: hello, ak)
[C][B][FFFFFF]├─ /fast [uid] [emote_id] [00FF00]- Fast Emote (25x) to Player
[C][B][FFFFFF]├─ /p [uid] [emote_id] [x] [00FF00]- Custom Emote X Times to Player
[C][B][FFFFFF]└─ /quick [team_code] [emote_id] [target_uid] [00FF00]- Quick Emote And Solo"""
                        await dl_send_message(response.Data.chat_type, emote_commands, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        evo_commands = """[C][B][FFD700]╭──────────╮
│ EVOLUTION CMDS               │
╰──────────╯
[C][B][FFFFFF]┌─ /evo [uid] [1-21] [00FF00]- Send Evolution Emote to Player
[C][B][FFFFFF]├─ /evo_fast [uid] [1-21] [00FF00]- Fast Evolution Emote (25x) to Player
[C][B][FFFFFF]├─ /evo_c [uid] [1-21] [x] [00FF00]- Custom Evolution Emote X Times to Player
[C][B][FFFFFF]├─ /random [uid] [00FF00]- Auto Cycle All Evolution Emotes for Player
[C][B][FFFFFF]└─ /ruk bhai [00FF00]- Stop Evolution Emote Cycle"""
                        await dl_send_message(response.Data.chat_type, evo_commands, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        ai_commands = """[C][B][FFD700]╭──────────╮
│    FUNNY CMDS                      │
╰──────────╯
[C][B][FFFFFF]┌─ /ms <text> [00FF00]- Send Custom Spam Message
[C][B][FFFFFF]├─ /sticker [00FF00]- Sends sticker via bot
[C][B][FFFFFF]├─ /title [00FF00]- Sends title via bot
[C][B][FFFFFF]├─ /bundle [name] [00FF00]- Bundle Send To Bot
[C][B][FFFFFF]├─ /kick [uid] [00FF00]- Kick Specified Player (Works only when bot is Squad Owner)
[C][B][FFFFFF]├─ /ai [question] [00FF00]- Ask AI Anything
[C][B][FFFFFF]└─ /admin [00FF00]- Admin Information"""
                        await dl_send_message(response.Data.chat_type, ai_commands, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        badge_commands = """[C][B][FFD700]╭──────────╮
│    BADGE CMDS                      │
╰──────────╯
[C][B][FFFFFF]┌─ /s1 [uid] [00FF00]- Join Request With Craftland Badge
[C][B][FFFFFF]├─ /s2 [uid] [00FF00]- Join Request With New V-Badge
[C][B][FFFFFF]├─ /s3 [uid] [00FF00]- Join Request With Moderator Badge
[C][B][FFFFFF]├─ /s4 [uid] [00FF00]- Join Request With Small V-Badge
[C][B][FFFFFF]├─ /s5 [uid] [00FF00]- Join Request With Pro Badge
[C][B][FFFFFF]└─ /spam [uid] [00FF00]- Join Requests With All Badges"""
                        await dl_send_message(response.Data.chat_type, badge_commands, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        admin_commands = """[C][B][FFD700]╭──────────╮
│    ADMIN CMDS                       │
╰──────────╯
[C][B][FFFFFF]┌─ /add [uid] [00FF00]- Send Friend to Specified User
[C][B][FFFFFF]├─ /remove [uid] [00FF00]- Remove Friend from List
[C][B][FFFFFF]├─ /guild_join [guild_id] [00FF00]- Join the Specified Guild
[C][B][FFFFFF]├─ /guild_leave [guild_id] [00FF00]- Leave the Specified Guild"""
                        await dl_send_message(response.Data.chat_type, admin_commands, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        
                        dev = f"""[FFFFFF]┌────────────┐
[00CED1]   BOT INFORMATION
[FFFFFF]├──────────┤
[FFFFFF] Developer  → DR.EXE
[FFFFFF] Status     → ONLINE
[FFFFFF] Version    → ENHANCED V2
[FFFFFF]└───────────┘"""
                            
                        await dl_send_message(response.Data.chat_type, dev, uid, chat_id, key, iv)
                        await asyncio.sleep(0.2)
                        
                    response = None
            whisper_writer.close()
            await whisper_writer.wait_closed()
            whisper_writer = None
        except Exception as e:
            whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    import json
    import time
    from datetime import datetime

    Uid, Pw = '6903498825', 'EB68D89D121F400350F0391832D0FDEB2F80638E2CCFDDE9D260F9ECD4C95035'
    print("📁 Loading credentials...")
    print("✅ Using hardcoded UID/Password")

    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token:
        print("❌ Error - Invalid Account (Check UID/Password)")
        return None

    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE:
        print("❌ Target Account => Banned / Not Registered!")
        return None

    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)

    token = MajoRLoGinauTh.token
    if not token:
        print("❌ No authentication token received!")
        return None

    try:
        region = getattr(MajoRLoGinauTh, 'region', 'IND')
        token_data = {
            "token": token,
            "saved_at": time.time(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "bot_uid": str(Uid),
            "region": region,
            "source": "main.py_hardcoded_login"
        }
        with open("token.json", "w") as f:
            json.dump(token_data, f, indent=2)
        print("✅ Token saved to token.json")
        print(f"📝 Token info: Region={region}, UID={Uid}")
    except Exception as e:
        print(f"⚠️ Warning: Could not save token to file: {e}")

    UrL = MajoRLoGinauTh.url
    os.system('clear')
    print("=" * 50)
    print("🤖 STAR BOT - INITIALIZING")
    print("=" * 50)
    print("🔄 Starting TCP Connections...")
    print("📡 Connecting to Free Fire servers...")
    print("🌐 Server connection established")

    region = getattr(MajoRLoGinauTh, 'region', 'IND')
    ToKen = token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp

    print(f"🔐 Authentication successful")
    print(f"👤 Account UID: {TarGeT}")
    print(f"🌍 Region: {region}")
    print(f"🔑 Token: {ToKen[:30]}...")

    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa:
        print("❌ Error - Getting Ports From Login Data!")
        return None

    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)

    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port

    print(f"📡 Online Server: {OnLinePorTs}")
    print(f"💬 Chat Server: {ChaTPorTs}")

    OnLineiP, OnLineporT = OnLinePorTs.split(":")
    ChaTiP, ChaTporT = ChaTPorTs.split(":")

    acc_name = LoGinDaTaUncRypTinG.AccountName
    print(f"👋 Welcome, {acc_name}!")
    
    equie_emote(ToKen, UrL)

    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)

    ready_event = asyncio.Event()

    print("\n🚀 Starting bot services...")

    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region))
    task2 = asyncio.create_task(TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen))

    # ---------- 加载动画（模仿第二个版本）----------
    os.system('clear')
    print("🤖 DARK BOT - STARTING")
    print("=" * 50)
    for i in range(1, 4):
        dots = "." * i
        print(f"🔄 Loading{dots}")
        time.sleep(0.3)

    os.system('clear')
    print("🤖 DARK BOT - CONNECTING")
    print("=" * 50)
    print("┌────────────────────────────────────┐")
    print("│ ██████████████████████████████████ │")
    print("└────────────────────────────────────┘")

    print("\n⏳ Waiting for chat connection...")
    try:
        await asyncio.wait_for(ready_event.wait(), timeout=10)
        print("✅ Chat connection established!")
    except asyncio.TimeoutError:
        print("⚠️ Chat connection timeout, continuing...")

    os.system('clear')
    print(render('STAR', colors=['white', 'green'], align='center'))
    print('')
    print("🤖 DARK BOT - ONLINE")
    print("=" * 50)
    print(f"🔹 UID: {TarGeT}")
    print(f"🔹 Name: {acc_name}")
    print(f"🔹 Region: {region}")
    print(f"🔹 Status: 🟢 READY")
    print(f"🔹 Chat Server: {ChaTiP}:{ChaTporT}")
    print(f"🔹 Online Server: {OnLineiP}:{OnLineporT}")
    print("=" * 50)
    print("💡 Commands available in squad/guild chat")
    print("💡 Type /help for command list")
    print("=" * 50)

    print("\n📊 System Check:")
    print(f"📁 Working directory: {os.getcwd()}")
    try:
        CACHE_FILE
    except NameError:
        CACHE_FILE = "cache.pkl"
    try:
        test_data = {'test': 'ok', 'timestamp': time.time()}
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(test_data, f)
        print("✅ Cache file write test: PASSED")
    except Exception as e:
        print(f"⚠️ Cache file write test: {e}")

    if os.path.exists("token.json"):
        print("✅ token.json file exists")
        try:
            with open("token.json", "r") as f:
                token_info = json.load(f)
            age = time.time() - token_info.get('saved_at', 0)
            print(f"✅ Token age: {age:.1f} seconds")
        except:
            print("⚠️ Could not read token.json")
    else:
        print("❌ token.json not found!")

    print("\n🎯 Bot is now running...")
    print("📡 Listening for commands and invitations")

    try:
        await asyncio.wait_for(asyncio.gather(task1, task2), timeout=30 * 60)
    except asyncio.TimeoutError:
        print("Auto restart after 7 hours")
        raise RestartBot()
    except RestartBot:
        raise
    except asyncio.CancelledError:
        print("\n🛑 Bot tasks cancelled")
    except Exception as e:
        print(f"\n❌ Error in bot tasks: {e}")
        import traceback
        traceback.print_exc()

    return None
    
async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout=7 * 60 * 60)
        except KeyboardInterrupt:
            break
        except asyncio.TimeoutError:
            pass
        except Exception as e:
            pass

if __name__ == '__main__':
    asyncio.run(StarTinG())