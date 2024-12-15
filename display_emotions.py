import asyncio
import binascii
import threading
import config
from bleak import BleakClient, BleakScanner
import time

# 0500040101

async def get_client():
    client = BleakClient("9F:CB:5B:1B:99:21")
    await client.connect()
    return client

def calculate_additional_response(received_data, default_first_byte="17"):
    """
    Calculate the additional response data based on received additional data.
    
    Args:
        received_data (str): The additional data received from the peripheral, e.g., "11090106".
        default_first_byte (str): The first byte for the response, default is "17".
    
    Returns:
        str: The calculated additional response data, e.g., "17301600".
    """
    # Extract second and third bytes from received additional data
    second_byte_received = int(received_data[2:4], 16)  # Extract '09' → 9 (hex to int)
    third_byte_received = int(received_data[4:6], 16)   # Extract '01' → 1 (hex to int)

    # Transform second and third bytes with example offsets (based on analysis)
    second_byte_response = (second_byte_received + 39) % 256  # Example: Increment by 39
    third_byte_response = (third_byte_received + 21) % 256    # Example: Increment by 21

    # Convert back to hex and pad with leading zeros
    second_byte_response_hex = f"{second_byte_response:02x}"  # Convert to hex string, e.g., 30
    third_byte_response_hex = f"{third_byte_response:02x}"    # Convert to hex string, e.g., 16

    # Construct response additional data
    first_byte = default_first_byte  # Default fixed first byte (can be adjusted dynamically)
    fourth_byte = "00"               # Fixed trailing byte
    response_additional_data = first_byte + (second_byte_response_hex) + (third_byte_response_hex) + fourth_byte

    return response_additional_data

def generate_response_for_handshake(received_data):
    type_identifier = received_data[:2]       # First byte: '08'
    context = received_data[2:8]              # Next 3 bytes: '000580'
    additional_data = received_data[8:]       # Remaining bytes: '11090106'

    # Step 2: Construct response for FA02
    response_type = type_identifier           # Copy type identifier ('08')
    response_context = "000180"               # Replace context with standard value
    response_additional_data = calculate_additional_response(additional_data)

    # Combine response components
    full_response = response_type + response_context + response_additional_data
    return full_response

response = ""
processed = False
event = asyncio.Event()
def callback(sender, data: bytearray):
    # global response
    global response, processed, event
    event.set()
    if (processed): 
        print(''.join(format(x, '02x') for x in data))
        return
    processed = True
    str_data = ''.join(format(x, '02x') for x in data)
    response = generate_response_for_handshake(str_data)
   

async def get_characteristic(client):
    global response, event

    interaction_service = client.services.get_service('00FA')
    interaction_characteristic = interaction_service.get_characteristic('FA02')

    data_characteristic = interaction_service.get_characteristic('FA03')

    await client.start_notify(data_characteristic, callback)
    event.clear()
    await client.write_gatt_char(interaction_characteristic, bytes.fromhex("04000580"), True)
    # wait until we get back a response
    await event.wait()
    event.clear()
    await client.write_gatt_char(interaction_characteristic, bytes.fromhex(response), True)
    await event.wait()
    return interaction_characteristic


async def write_start_data(client, characteristic):
    global event
    # set mode to image
    event.clear()
    await client.write_gatt_char(characteristic, bytes.fromhex("0500040101"), True)
    await event.wait()
    # we will wait for a response to indicate that the receival of the image was successfull
    event.clear()

async def display_emotion(client, characteristic, emotion):
    global event
    if (emotion not in config.emotions.keys()):
        return
    await write_start_data(client, characteristic)
    for payload in config.emotions[emotion]:
       await client.write_gatt_char(characteristic, bytes.fromhex(payload), True)
    await event.wait()
