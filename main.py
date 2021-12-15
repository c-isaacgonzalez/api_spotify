import base64
import pandas as pd 
import requests
import IPython.display as ipd


def get_token(client_id, client_secret):
  encoded = base64.b64encode(bytes(client_id+':'+client_secret,'utf-8'))
  params = {'grant_type':'client_credentials'}
  header = {'Authorization': 'Basic '+str(encoded,'utf-8')}
  r = requests.post('https://accounts.spotify.com/api/token',data=params,headers=header)
  if r.status_code !=200:
    print('Error en la request.'+r.json())
    return None
  else:
    print('Token válid por {} sgundos'.format(r.json()['expires_in']))
    return r.json()['access_token']
  
  
 def get_albums(id_artist,token):
    header = {'Authorization': 'Bearer {}'.format(token)}
    url_busqueda = 'https://api.spotify.com/v1/artists/{}/albums'.format(id_artist)
    params = {'country':'MX'}
    busqueda_albums = requests.get(url_busqueda,headers=header,params=params)
    lista_albums = [(album['id'],album['name']) for album in busqueda_albums.json()['items']]
    return lista_albums
  
  
 
def get_song_in_album(id_album,token):
    header = {'Authorization': 'Bearer {}'.format(token)}
    url_busqueda = 'https://api.spotify.com/v1/albums/{}/tracks'.format(id_album)
    params = {'country':'MX'}
    busqueda_songs = requests.get(url_busqueda,headers=header,params=params)
    lista_tracks = [(track['id'],track['name']) for track in busqueda_songs.json()['items']]
    return lista_tracks
  
  
client_id = '5ede3667b7ad409d91cf6df8c1b3d738'
client_secret = '08138f434f20E8e7aw75ddbf5b866ef8'
token = get_token(client_id, client_secret)



for album in get_albums('5KNNVgR6LBIABRIomyCwKJ',token):
  print(album[1])
  for song in get_song_in_album(album[0],token):
    print('\t',song[1])

 def get_song_in_album_play(id_album,token):
    header = {'Authorization': 'Bearer {}'.format(token)}
    url_busqueda = 'https://api.spotify.com/v1/albums/{}/tracks'.format(id_album)
    params = {'country':'MX'}
    busqueda_songs = requests.get(url_busqueda,headers=header,params=params)
    lista_tracks = [(track['preview_url'],track['name'],track['id']) for track in busqueda_songs.json()['items']]
    return lista_tracks
  
 
df = pd.DataFrame(get_song_in_album_play('3T4tUhGYeRNVUGevb0wThu',token))

pd.DataFrame(get_song_in_album_play('3T4tUhGYeRNVUGevb0wThu',token))[0][1]


preview_url = 'https://p.scdn.co/mp3-preview/beb4ed48cca5d2a792e877c7efe92d54046eac67?cid=5ede3667b7ad409d91cf6df8c1b3d738'
preview = requests.get(preview_url) 
ipd.Audio(preview.content)

  
  
  
  
  
