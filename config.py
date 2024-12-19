VERTICAL = 7
HORIZONTAL = 15

emotions = {
    "neutral": [
        "c903020000ba030000c7a64404001289504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000001af09c79e6a0000017b49444154381162501617a52962c061ba88b23810116f374ef5681688288b8a28cac8c82b2a2bcaca83ed20688d88a284b8a2bca2a2bcb2a29404a6b3902d1051949717f5cde4aedec8de7e90bb6187486c83bc9a2ea61e98cf40ae96317112c89eced1ba97a3f5205fd142296b7f657171642d700b4494a5a404537a5866dde7aedbcc973e91b76021fbc4cb7cd5ebe595359035c04c1755161594b1f0649f709ebdef2c6fde4cbeccc91ccd7bd8a75e91728b531615822b835aa0222428ee99c032eba160741dd0d5e0505211770a67ef3921983e41590423a044858061c2d57e90ab619b94859ba2aca2a28cbc8cae195f",
        "e654a095b25a26ca22821067c17c2022c857b298bdfdb0ac862e540e68848cac40422b47cf29a07e744f880848597932cd7922ea9b0e762f28f2800c293337f68917c57d33958578219e8059202ac45bb391ab723d301a94c5e11e1417092a609f705111144a704170d212e193720c03fa58ca3608ec20b02030d0b4cdd83b8f898495ab08422d00000000ffff31d710660000012c49444154635016170522151101c1941ef69e335226f6cae22210a4a8acc1973d93bb61aba294145804a4128a440465f5ad59a6df108aac519491816a9192127789649f7851ca3e4445840fa29201aa41544856c390ab753f47c33651cf04191327095b7f81ccc91c3da7a46c839445041146c3ed101711896d609f785930b649c2c25bcacc45c43f8fa3fdb060f6746407c12c00691391b1f0e02b590cb486ab610757d32edeea35e21e09c8aa51ac11159157561389ae03aa04a1861ddc4dbb0493bae435f49545816100f52bc402714509085f44515e51c6c451c23e48c6c2535e5903ea77986ab83630031c925212b25ac652b6be408fcaea5a28ca000313168c6006b20fa076805448882b83ac8444068a0634fd303540f5e2305b51d4635a80228d611cc9b243df020014d3ea47b74de8b60000000049454e44ae426082"
    ],
    "angry": [
        "7302020000640200000a75bad6000f89504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000000f19c0fd3d8000000bd49444154381162501617a52512675019b5007f08630b2245711108223e6e706b41b500a84e4d464a5f45d950434d5b511e68015004bf3510a3b5e46581ba749515d5a42450b52059009400aa488a8eec6c6e9adad7d7505d19e4e9a1252fa3288ad30ea0160d59295f17a7caa2829ed6d6a69a9ab8b010a04d48762059202f22e46265d15c53d35a570754bd74c1bcfd7b76cd993ad544430dab1d4041a05993fbfaf6eedab562e9e2c93d3d7deded3dedadfe6e2ef22282307f8b03000000ffffae8c59dd0000009449444154635011175586210d59192d7959352909351929132d8da4e8c8c5f3e604797ac80b09c2d5c0",
        "19f222829ef6b60b66cd4a4f88b3d2d7d59297016ad75751d655565414178129136740b600260ab212a84851544457591ea84119a101e11aa0026d45902c50191041d48074a128c66d01c4320c0d080ba08e40310e45166c02210b20d650408e5a8019e86822340f225100b562c2ee051fac800000000049454e44ae426082"
    ],
    "happy": [
        "7302020000640200000a75bad6000f89504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000000f19c0fd3d8000000bd49444154381162501617a52512675019b5007f08630b2245711108223e6e706b41b500a84e4d464a5f45d950434d5b511e68015004bf3510a3b5e46581ba749515d5a42450b52059009400aa488a8eec6c6e9adad7d7505d19e4e9a1252fa3288ad30ea0160d59295f17a7caa2829ed6d6a69a9ab8b010a04d48762059202f22e46265d15c53d35a570754bd74c1bcfd7b76cd993ad544430dab1d4041a05993fbfaf6eedab562e9e2c93d3d7deded3dedadfe6e2ef22282307f8b03000000ffffae8c59dd0000009449444154635011175586210d59192d7959352909351929132d8da4e8c8c5f3e604797ac80b09c2d5c0",
        "19f222829ef6b60b66cd4a4f88b3d2d7d59297016ad75751d655565414178129136740b600260ab212a84851544457591ea84119a101e11aa0026d45902c50191041d48074a128c66d01c4320c0d080ba08e40310e45166c02210b20d650408e5a8019e86822340f225100b562c2ee051fac800000000049454e44ae426082"
    ],
    "surprise": [
        "6d030200005e030000e4be6ff5001089504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000001873c72369000000153494441543811b491c14ac3401086fb0aca2e09cb2ec3b0210445bc4828f6201e4b1045040925a5945009016f458a454a24483c941611cfe223f4059d24ad49b43d0a4308936fe6ffff4c4b1bfc5fabb56b3b1a6cd7a7663fc73077b99ddf2240f411f08e235ddbb0052b8677a6444eb0d171846b9b8ee0c87fcb340468d7a132220f96915e46163dd3015eb862e3b12153c1b15ec6d6a280bd02ae476c0858269bfa388ff4e456a50348fa402fefb1be6a4bf863cd36f9b4878b08d7704030bcc5fab22d8055392a01eafa67727ea7d32166431c75d5a30f5f633df5d56ba88fc1a85f0518f7cf15c12f43a41a75e5c487cf",
        "078be08c6024781db712508c3df5f42c808f7b4d3f4aee33aaf14daef1dc07ca5ef755c058c2078a6f60cce1017aaefc812b016acd022b0b210950ece51969cc3b91abc4a145d7a73453dd8060c2b2109340134c7e73d815abc42e6172505ee21b0000ffff645ee689000000f849444154d5d0318bc23014c0713f44424a501e8f57444e8208ae525c0e8e0e2e2e22771c1290221607671141a422c71d72084e7e54d3a8b16a055721c31b7ee9bf790512fc7880b1b80d491fb631b594ac48510331ffc4fd8416df18280ff8491a5f3a61dcc67ea064d9e2d9d71957a5c3051740ce1b24967d5a6bf81fd1cfc037a5dd98120d83101c3b0e29f60dc6b5c60cc644e30dbe04ec4df65e97b31efe46f437c4cd10571aa3b0544381e787664a299e5a6ce4263298a2102c668edd04d22528e01f0dd90d8a9d66b1f926caf2b21977cd0d0a44067bf73827905ef6b86f8f19f2fefd3ae9b060f7f841206721d71f7d1abc7ee000cc10f1a0b0316e5d0000000049454e44ae426082"
    ],
    "sad": [
        "c903020000ba030000c7a64404001289504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000001af09c79e6a0000017b49444154381162501617a52962c061ba88b23810116f374ef5681688288b8a28cac8c82b2a2bcaca83ed20688d88a284b8a2bca2a2bcb2a29404a6b3902d1051949717f5cde4aedec8de7e90bb6187486c83bc9a2ea61e98cf40ae96317112c89eced1ba97a3f5205fd142296b7f657171642d700b4494a5a404537a5866dde7aedbcc973e91b76021fbc4cb7cd5ebe595359035c04c1755161594b1f0649f709ebdef2c6fde4cbeccc91ccd7bd8a75e91728b531615822b835aa0222428ee99c032eba160741dd0d5e0505211770a67ef3921983e41590423a044858061c2d57e90ab619b94859ba2aca2a28cbc8cae195f",
        "e654a095b25a26ca22821067c17c2022c857b298bdfdb0ac862e540e68848cac40422b47cf29a07e744f880848597932cd7922ea9b0e762f28f2800c293337f68917c57d33958578219e8059202ac45bb391ab723d301a94c5e11e1417092a609f705111144a704170d212e193720c03fa58ca3608ec20b02030d0b4cdd83b8f898495ab08422d00000000ffff31d710660000012c49444154635016170522151101c1941ef69e335226f6cae22210a4a8acc1973d93bb61aba294145804a4128a440465f5ad59a6df108aac519491816a9192127789649f7851ca3e4445840fa29201aa41544856c390ab753f47c33651cf04191327095b7f81ccc91c3da7a46c839445041146c3ed101711896d609f785930b649c2c25bcacc45c43f8fa3fdb060f6746407c12c00691391b1f0e02b590cb486ab610757d32edeea35e21e09c8aa51ac11159157561389ae03aa04a1861ddc4dbb0493bae435f49545816100f52bc402714509085f44515e51c6c451c23e48c6c2535e5903ea77986ab83630031c925212b25ac652b6be408fcaea5a28ca000313168c6006b20fa076805448882b83ac8444068a0634fd303540f5e2305b51d4635a80228d611cc9b243df020014d3ea47b74de8b60000000049454e44ae426082"
    ],
    "fear":[
        "7302020000640200000a75bad6000f89504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000000f19c0fd3d8000000bd49444154381162501617a52512675019b5007f08630b2245711108223e6e706b41b500a84e4d464a5f45d950434d5b511e68015004bf3510a3b5e46581ba749515d5a42450b52059009400aa488a8eec6c6e9adad7d7505d19e4e9a1252fa3288ad30ea0160d59295f17a7caa2829ed6d6a69a9ab8b010a04d48762059202f22e46265d15c53d35a570754bd74c1bcfd7b76cd993ad544430dab1d4041a05993fbfaf6eedab562e9e2c93d3d7deded3dedadfe6e2ef22282307f8b03000000ffffae8c59dd0000009449444154635011175586210d59192d7959352909351929132d8da4e8c8c5f3e604797ac80b09c2d5c0",
        "19f222829ef6b60b66cd4a4f88b3d2d7d59297016ad75751d655565414178129136740b600260ab212a84851544457591ea84119a101e11aa0026d45902c50191041d48074a128c66d01c4320c0d080ba08e40310e45166c02210b20d650408e5a8019e86822340f225100b562c2ee051fac800000000049454e44ae426082"
    ],
    "disgust":[
         "c903020000ba030000c7a64404001289504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000001af09c79e6a0000017b49444154381162501617a52962c061ba88b23810116f374ef5681688288b8a28cac8c82b2a2bcaca83ed20688d88a284b8a2bca2a2bcb2a29404a6b3902d1051949717f5cde4aedec8de7e90bb6187486c83bc9a2ea61e98cf40ae96317112c89eced1ba97a3f5205fd142296b7f657171642d700b4494a5a404537a5866dde7aedbcc973e91b76021fbc4cb7cd5ebe595359035c04c1755161594b1f0649f709ebdef2c6fde4cbeccc91ccd7bd8a75e91728b531615822b835aa0222428ee99c032eba160741dd0d5e0505211770a67ef3921983e41590423a044858061c2d57e90ab619b94859ba2aca2a28cbc8cae195f",
        "e654a095b25a26ca22821067c17c2022c857b298bdfdb0ac862e540e68848cac40422b47cf29a07e744f880848597932cd7922ea9b0e762f28f2800c293337f68917c57d33958578219e8059202ac45bb391ab723d301a94c5e11e1417092a609f705111144a704170d212e193720c03fa58ca3608ec20b02030d0b4cdd83b8f898495ab08422d00000000ffff31d710660000012c49444154635016170522151101c1941ef69e335226f6cae22210a4a8acc1973d93bb61aba294145804a4128a440465f5ad59a6df108aac519491816a9192127789649f7851ca3e4445840fa29201aa41544856c390ab753f47c33651cf04191327095b7f81ccc91c3da7a46c839445041146c3ed101711896d609f785930b649c2c25bcacc45c43f8fa3fdb060f6746407c12c00691391b1f0e02b590cb486ab610757d32edeea35e21e09c8aa51ac11159157561389ae03aa04a1861ddc4dbb0493bae435f49545816100f52bc402714509085f44515e51c6c451c23e48c6c2535e5903ea77986ab83630031c925212b25ac652b6be408fcaea5a28ca000313168c6006b20fa076805448882b83ac8444068a0634fd303540f5e2305b51d4635a80228d611cc9b243df020014d3ea47b74de8b60000000049454e44ae426082"
    ],
    "exciting":[
        "17030200000803000022cb8657000189504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f540000000200000000000000080000002800000008000000080000013d17c66c020000010949444154381162501617a52962a0a9e940c31116288a8b50c532a039c846c12d10579112579610479326de4a9846118839708d200b1445450c35d432931212c2c2dcecad0dd5d494a5c481827045f81910a3b5e4656d4d0c43bcbdb39392fcdd5ce0dac116888b6829cae7a5a72d9e3767ddaa157d9dedd14141c61a6aca44041ad0740d5919375bebcaa282c50be6ad59b1a2bda9c9c5ca42515408e22c681001d5c908f269c9cbc48604ad5abaf4cae58b73a64f75b230833b04ab2780ba800e2fc9cb3d71ecd8b1c307ebca4bad0df5e545048108ae1e1e07a0c40ad4202f2428232830a1abf3ffffff0be7cc01b2e14a",
        "3119b28202c0d0f8f6eddbfdbb774db434804ec47410000000ffffdcdd07bc000000ec4944415463501617454222b2428216faba9bd7afbb72f9724a6cb4bc8820922cb24a105b5144c84c5b6bfd9a550fefdf4f8a0c571417018aa0a96780f38166a949491465671edcb367fae4c94e1666cae22270595c0c4551115d65c582ccf4bd7b76cd9b39ddd6d85046900f5931d402a0cdd6868693fbfae6cd9a95161d6da8a106d4498c0540b3802a3564a43c9dec3b9b9b162f5890141d89dd020f7bdb84f030a01380fe009b8e1e20c8dad0d8a0c0111731545309f070031a02b40fc885a8410491b2843810c125d08c20860bd1ab22258eac18c90294d826c1f9c8c601d9684ea4be0568f6d1dc02003a96e598153e54000000000049454e44ae426082"
    ],
    "sadness":[
        "760202000067020000e76656e6001389504e470d0a1a0a0000000d4948445200000020000000100802000000f862ea0e000000017352474200aece1ce900000078655849664d4d002a000000080005011200030000000100010000011a0005000000010000004a011b0005000000010000005201280003000000010002000087690004000000010000005a00000000000000480000000100000048000000010002a00200040000000100000020a0030004000000010000001000000000b1553fc4000000097048597300000b1300000b1301009a9c180000001c69444f54000000020000000000000008000000280000000800000008000000ee1107de2d000000ba49444154381162501617a52962a0a9e940c387bd058ae222f8c390a0029c41a4280a32da504d594d4a0aa71d12e2fa2aca2a52e28a2242709b800c381b250ed4a4c4d5a4242066a94849e82a2bfabbb935d7d5186aa8412cc3b04604a8a5bca0203a24c8584d4d4d464a59421c883464a4346465e08aa13e90171174b3b56e6f6a009ad8545333b9af67f3faf5870f1eac292d0169c39194e545845262a3f7ecdab167c7b639d3a777b53677b5b64eece98a0b0b014a417401000000ffff1c973a5d0000009a494441546350161705224511215b13c3bef6f68d6bd6ecddb36bff9e3d2b962ece4e49d2909551141581a8c1",
        "2415c541529141fef3664edfb363db9e5d3b36af5f3fb5afcfd7c5096820443d035c1b50b5868c9489968695a1be99b69696bc2c500462045c0d5606d005408d861a6a66ba5a40524346065917c202a0669089a23004761d56133105f16844b1005327e522a316100c439a0711004240cbd22c04cd390000000049454e44ae426082"
    ],
}

movements = {
"happy": 
    [
        {"direction": HORIZONTAL, "angle": 60, "speed": 0.5},
        {"direction": HORIZONTAL, "angle": -60, "speed": 0.5}
    ],
    

"surprise": 
    [
        {"direction": VERTICAL, "angle": -50, "speed": 0.5},
        {"direction": HORIZONTAL, "angle": 60, "speed": 0.5},
        {"direction": HORIZONTAL, "angle": -60, "speed": 0.5},
        {"direction": VERTICAL, "angle": 50, "speed": 0.5}
    ],
    

"sad":
     [
        {"direction": VERTICAL, "angle": 50, "speed": 0.5},
        {"direction": VERTICAL, "angle": -50, "speed": 0.5},
    ],
    
"angry": 
     [
        {"direction": HORIZONTAL, "angle": 60, "speed": 0.5},
        {"direction": HORIZONTAL, "angle": -60, "speed": 0.5}
    ],
    
"fear": 
    [
        {"direction": HORIZONTAL, "angle": 60, "speed": 0.5},
        {"direction": HORIZONTAL, "angle": -60, "speed": 0.5}
    ],

}

dialogue = {
    "happy": "./audio/dhappy.wav",
    "surprise": "./audio/dsurprise.wav",
    "sad": "./audio/dsad.wav",
    "angry": "./audio/dangry.wav",
    "fear": "./audio/dfear.wav",
    "disgust": "./audio/ddisgust.wav",
}