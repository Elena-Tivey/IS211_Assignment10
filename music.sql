-- music.sql
-- Relational model for artists, albums, and songs.


CREATE DATABASE IF NOT EXISTS music;   
USE music;

 
PRAGMA foreign_keys = ON;
 
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY,
    name      TEXT NOT NULL
);
 
CREATE TABLE albums (
    album_id  INTEGER PRIMARY KEY,
    name      TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);
 
CREATE TABLE songs (
    song_id      INTEGER PRIMARY KEY,
    name         TEXT NOT NULL,
    album_id     INTEGER NOT NULL,
    track_number INTEGER NOT NULL CHECK (track_number > 0),
    length       INTEGER NOT NULL CHECK (length > 0),  -- length in seconds
    FOREIGN KEY (album_id) REFERENCES albums(album_id),
    UNIQUE (album_id, track_number)  -- one song per track slot on an album
);
 