def get_sprite(pokemon):
    url = f"https://play.pokemonshowdown.com/sprites/xyani/{pokemon}.gif"
    response = r.get(url)

    with open("spriteGIF.gif","wb") as f:
        f.write(response.content)

def get_audio(pokemon):
    url = f'https://play.pokemonshowdown.com/audio/cries/{pokemon}.mp3'
    resp = r.get(url, allow_redirects=True)
    open('crie.mp3', 'wb').write(resp.content)
