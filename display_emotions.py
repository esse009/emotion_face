import asyncio
import binascii
import threading
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
event = threading.Event()
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
    event.wait()
    event.clear()
    await client.write_gatt_char(interaction_characteristic, bytes.fromhex(response), True)
    event.wait()
    await display_angry(client, interaction_characteristic)
    return interaction_characteristic


async def write_start_data(client, characteristic):
    global event
    # set mode to image
    event.clear()
    await client.write_gatt_char(characteristic, bytes.fromhex("0500040101"), True)
    event.wait()
    # this seems to represent the image index, as this gets incremented, hardcoded for now
    await client.write_gatt_char(characteristic, bytes.fromhex("07000880010011"), True)


async def display_neutral(client, characteristic):
    await write_start_data(client, characteristic)
    await client.write_gatt_char(characteristic, bytes.fromhex("c903020000ba030000c7a64404001289504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000001af09c79e6a0000017b49444154381162501617a52962c061ba88b23810116f374ef5681688288b8a28cac8c82b2a2bcaca83ed20688d88a284b8a2bca2a2bcb2a29404a6b3902d1051949717f5cde4aedec8de7e90bb6187486c83bc9a2ea61e98cf40ae96317112c89eced1ba97a3f5205fd142296b7f657171642d700b4494a5a404537a5866dde7aedbcc973e91b76021fbc4cb7cd5ebe595359035c04c1755161594b1f0649f709ebdef2c6fde4cbeccc91ccd7bd8a75e91728b531615822b835aa0222428ee99c032eba160741dd0d5e0505211770a67ef3921983e41590423a044858061c2d57e90ab619b94859ba2aca2a28cbc8cae195f"), True)
    await client.write_gatt_char(characteristic, bytes.fromhex("e654a095b25a26ca22821067c17c2022c857b298bdfdb0ac862e540e68848cac40422b47cf29a07e744f880848597932cd7922ea9b0e762f28f2800c293337f68917c57d33958578219e8059202ac45bb391ab723d301a94c5e11e1417092a609f705111144a704170d212e193720c03fa58ca3608ec20b02030d0b4cdd83b8f898495ab08422d00000000ffff31d710660000012c49444154635016170522151101c1941ef69e335226f6cae22210a4a8acc1973d93bb61aba294145804a4128a440465f5ad59a6df108aac519491816a9192127789649f7851ca3e4445840fa29201aa41544856c390ab753f47c33651cf04191327095b7f81ccc91c3da7a46c839445041146c3ed101711896d609f785930b649c2c25bcacc45c43f8fa3fdb060f6746407c12c00691391b1f0e02b590cb486ab610757d32edeea35e21e09c8aa51ac11159157561389ae03aa04a1861ddc4dbb0493bae435f49545816100f52bc402714509085f44515e51c6c451c23e48c6c2535e5903ea77986ab83630031c925212b25ac652b6be408fcaea5a28ca000313168c6006b20fa076805448882b83ac8444068a0634fd303540f5e2305b51d4635a80228d611cc9b243df020014d3ea47b74de8b60000000049454e44ae426082"), True)

async def display_angry(client, characteristic):
    await write_start_data(client, characteristic)
    await client.write_gatt_char(characteristic, bytes.fromhex("7704020000680400005f0dedec000d89504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000001e8e17f4a59000001b44944415438119452c14a2341109d4342c0e0303d74d34dd34d53f420434208e2206290b0735856641006090411820c48102488c18b84208804422e92c3c25e3c2cf8031e170f5e16d9652f7bf073aca8091e440cf4a1baabde7bf5bacab19c3e1f360b8073cbf13aef419e17c82ce001630ebe823266a96282122835939956cf2583d41c0c98b06a6c68a54012c72a29a39834cfc86e5f6c6c4f12629298da9a430094d4e5886d66defe802607d8b415ccc1c6fdb453b8bccf8dfe15bb3ffdf45855d7a7563ec94eade00056d612a45ee8dfe6aefe174f6f442d01a51db35c73db57b9f1a3978d78dcf4da63371b49b4024b"), True)
    await client.write_gatt_char(characteristic, bytes.fromhex("e8f7333e400a5d5a61497bf1e807d9edf12f8dc2c5affce0374dda0081a3d7be2e76aef3c33f2a8aadefa22fdae8ba87df316dc20a823fd600ad6554277be7eee198c70db41e5097ecf5f3a3bf74e7440725c7acc6c5ce75e1e24e8755cb88653e48293652b4451ba7aa5a7bf7bb008724b88140d4532f1ba2802a47af0b4289bfd3cd0f1f68dad141e89872e4ee0f50402dd72d25d3f1520478ad4bd21ac8b52d5c0ca47bbb5720b90e2b6c2b9bf4b17d3429e0fe2b9611d2ec2121ffd602639f000000ffff0fd98898000001a149444154ad51dd4b423114f72d6124f7cac6c6d8658c494822228a08971025221131420a8940421491242409292282f0257c91de7c284288e82d82febcceeef58681d44bb01d0e9cf3fbda4252695a6eaddd7e461b979a4435c59a12530996f154f47064b526ccad2a470623a2198511ae9d46ba53566a28e1c0b287221adb52c7d1c51beacf78b6a4390bc115c9bcd51c87af3f58a16e58b06d94a0324a0b753478c67b7d802d28401e209962a433b55af74e3c65360d04aaa5a4b69a77e1ab77523e512aa6190901a3129c678b76738c46aff6d115cfed88545e640a78ff0cd8adf684bb1525210124f30e24d848904a1b0d1e239d092d3544ca85c38af548f7018dde70ad6784190572103018258493c8e16a1752a3f3391abe18eace94d47a22bde5bd4f"), True)
    await client.write_gatt_char(characteristic, bytes.fromhex("c0ee6b702a6371b6b56f1fdfac9fcdd01020f3f5c113b864c50319dbd41cd80112089897a154492537d33cb7cddd2acfef3a892c44d69c2f8cfbd441559e2d9001071091bb6568e446d27c49b003cd2281afe6c978df05e94c4063c13b3fed2ff0fee88ffd65816f160fb3e462d9d1aafeb7fd9502df4affd07c015fa8f6995df651a70000000049454e44ae426082"), True)

async def display_happy(client, characteristic):
    await write_start_data(client, characteristic)
    await client.write_gatt_char(characteristic, bytes.fromhex("7302020000640200000a75bad6000f89504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000000f19c0fd3d8000000bd49444154381162501617a52512675019b5007f08630b2245711108223e6e706b41b500a84e4d464a5f45d950434d5b511e68015004bf3510a3b5e46581ba749515d5a42450b52059009400aa488a8eec6c6e9adad7d7505d19e4e9a1252fa3288ad30ea0160d59295f17a7caa2829ed6d6a69a9ab8b010a04d48762059202f22e46265d15c53d35a570754bd74c1bcfd7b76cd993ad544430dab1d4041a05993fbfaf6eedab562e9e2c93d3d7deded3dedadfe6e2ef22282307f8b03000000ffffae8c59dd0000009449444154635011175586210d59192d7959352909351929132d8da4e8c8c5f3e604797ac80b09c2d5c0"), True)
    await client.write_gatt_char(characteristic, bytes.fromhex("19f222829ef6b60b66cd4a4f88b3d2d7d59297016ad75751d655565414178129136740b600260ab212a84851544457591ea84119a101e11aa0026d45902c50191041d48074a128c66d01c4320c0d080ba08e40310e45166c02210b20d650408e5a8019e86822340f225100b562c2ee051fac800000000049454e44ae426082"), True)
	
async def display_surprise(client, characteristic):
    await write_start_data(client, characteristic)
    await client.write_gatt_char(characteristic, bytes.fromhex("6d030200005e030000e4be6ff5001089504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000001873c72369000000153494441543811b491c14ac3401086fb0aca2e09cb2ec3b0210445bc4828f6201e4b1045040925a5945009016f458a454a24483c941611cfe223f4059d24ad49b43d0a4308936fe6ffff4c4b1bfc5fabb56b3b1a6cd7a7663fc73077b99ddf2240f411f08e235ddbb0052b8677a6444eb0d171846b9b8ee0c87fcb340468d7a132220f96915e46163dd3015eb862e3b12153c1b15ec6d6a280bd02ae476c0858269bfa388ff4e456a50348fa402fefb1be6a4bf863cd36f9b4878b08d7704030bcc5fab22d8055392a01eafa67727ea7d32166431c75d5a30f5f633df5d56ba88fc1a85f0518f7cf15c12f43a41a75e5c487cf"), True)
    await client.write_gatt_char(characteristic, bytes.fromhex("078be08c6024781db712508c3df5f42c808f7b4d3f4aee33aaf14daef1dc07ca5ef755c058c2078a6f60cce1017aaefc812b016acd022b0b210950ece51969cc3b91abc4a145d7a73453dd8060c2b2109340134c7e73d815abc42e6172505ee21b0000ffff645ee689000000f849444154d5d0318bc23014c0713f44424a501e8f57444e8208ae525c0e8e0e2e2e22771c1290221607671141a422c71d72084e7e54d3a8b16a055721c31b7ee9bf790512fc7880b1b80d491fb631b594ac48510331ffc4fd8416df18280ff8491a5f3a61dcc67ea064d9e2d9d71957a5c3051740ce1b24967d5a6bf81fd1cfc037a5dd98120d83101c3b0e29f60dc6b5c60cc644e30dbe04ec4df65e97b31efe46f437c4cd10571aa3b0544381e787664a299e5a6ce4263298a2102c668edd04d22528e01f0dd90d8a9d66b1f926caf2b21977cd0d0a44067bf73827905ef6b86f8f19f2fefd3ae9b060f7f841206721d71f7d1abc7ee000cc10f1a0b0316e5d0000000049454e44ae426082"), True)
	
async def display_sad(client, characteristic):
    await write_start_data(client, characteristic)
    await client.write_gatt_char(characteristic, bytes.fromhex("760202000067020000e76656e6001389504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000000ee1107de2d000000ba49444154381162501617a52962a0a9e940c387bd058ae222f8c390a0029c41a4280a32da504d594d4a0aa71d12e2fa2aca2a52e28a2242709b800c381b250ed4a4c4d5a4242066a94849e82a2bfabbb935d7d5186aa8412cc3b04604a8a5bca0203a24c8584d4d4d464a59421c883464a4346465e08aa13e90171174b3b56e6f6a009ad8545333b9af67f3faf5870f1eac292d0169c39194e545845262a3f7ecdab167c7b639d3a777b53677b5b64eece98a0b0b014a417401000000ffff1c973a5d0000009a494441546350161705224511215b13c3bef6f68d6bd6ecddb36bff9e3d2b962ece4e49d2909551141581a8c1"), True)
    await client.write_gatt_char(characteristic, bytes.fromhex("2415c541529141fef3664edfb363db9e5d3b36af5f3fb5afcfd7c5096820443d035c1b50b5868c9489968695a1be99b69696bc2c500462045c0d5606d005408d861a6a66ba5a40524346065917c202a0669089a23004761d56133105f16844b1005327e522a316100c439a0711004240cbd22c04cd390000000049454e44ae426082"), True)

		

async def display_emotion(client, characteristic, emotion):
    match emotion:
        case "angry":
            return await display_angry(client, characteristic)
        # case "fear":
        #     return await display_fear(client, characteristic)
        case "sad":
            return await display_sad(client, characteristic)
        # case "disgust":
        #     return await display_disgust(client, characteristic)
        case "happy":
            return await display_happy(client, characteristic)
        case "surprise":
            return await display_surprise(client, characteristic)
        case "neutral":
            return await display_neutral(client, characteristic)