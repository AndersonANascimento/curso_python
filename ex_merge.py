#-*- encoding=UTF-8 -*-
import pandas as pd
from db import DemoDB

database = DemoDB()

database.tables

album = database.tables.Album.all()
print album.head()

artista = database.tables.Artist.all()
print artista.head()

artista_album = pd.merge(artista, album)
print artista_album.head()

artista_album = pd.merge(artista, album, on='ArtistId')
print artista_album.head()

album.rename(columns={'ArtistId':'Artist_Id'}, inplace=True)
print album.head()

artista_album = pd.merge(artista, album, left_on='ArtistId', right_on='Artist_Id')
print artista_album.head()

artista_album = pd.merge(artista, album, left_on='ArtistId', right_on='Artist_Id').drop('Artist_Id', axis=1)
print artista_album.head()
