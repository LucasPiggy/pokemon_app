def get_sprite(pokemon):
    url = f"https://play.pokemonshowdown.com/sprites/xyani/{pokemon}.gif"
    response = r.get(url)

    with open("spriteGIF.gif","wb") as f:
        f.write(response.content)

def get_audio(pokemon):
    url = f'https://play.pokemonshowdown.com/audio/cries/{pokemon}.mp3'
    resp = r.get(url, allow_redirects=True)
    open('crie.mp3', 'wb').write(resp.content)

def get_tipo(pokemon):
    tipos = []
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    resp = r.get(url)
    result = json.loads(resp.content)
    res_tipos = result["types"]
    tipos.append(res_tipos[0]["type"]["name"])
    if len(res_tipos) == 2:
        tipos.append(res_tipos[1]["type"]["name"])
    return tipos
