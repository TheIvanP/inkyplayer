#%%
from soco import SoCo, discover

my_zone = SoCo("192.168.0.21")
song = "spotify:track:52yEkn1b6BiOZad3x7x6PP"

my_zone.clear_queue()
my_zone.add_spotify_uri_to_queue(song)
my_zone.play_from_queue(0)

#%%