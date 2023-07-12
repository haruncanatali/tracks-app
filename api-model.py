from enum import Enum
from typing import List, Union
from datetime import datetime


class AlbumTypeEnum(Enum):
    ALBUM = "album"


class ExternalUrls:
    spotify: str

    def __init__(self, spotify: str) -> None:
        self.spotify = spotify


class ID(Enum):
    THE_36_Q_JP_DE2_GO2_KGA_RLE_HCD_TP = "36QJpDe2go2KgaRleHCDTp"


class Name(Enum):
    LED_ZEPPELIN = "Led Zeppelin"


class ArtistType(Enum):
    ARTIST = "artist"


class URI(Enum):
    SPOTIFY_ARTIST_36_Q_JP_DE2_GO2_KGA_RLE_HCD_TP = "spotify:artist:36QJpDe2go2KgaRleHCDTp"


class Artist:
    external_urls: ExternalUrls
    href: str
    id: ID
    name: Name
    type: ArtistType
    uri: URI

    def __init__(self, external_urls: ExternalUrls, href: str, id: ID, name: Name, type: ArtistType, uri: URI) -> None:
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.name = name
        self.type = type
        self.uri = uri


class Image:
    height: int
    url: str
    width: int

    def __init__(self, height: int, url: str, width: int) -> None:
        self.height = height
        self.url = url
        self.width = width


class ReleaseDatePrecision(Enum):
    DAY = "day"
    YEAR = "year"


class Album:
    album_type: AlbumTypeEnum
    artists: List[Artist]
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: Union[datetime, int]
    release_date_precision: ReleaseDatePrecision
    total_tracks: int
    type: AlbumTypeEnum
    uri: str

    def __init__(self, album_type: AlbumTypeEnum, artists: List[Artist], available_markets: List[str], external_urls: ExternalUrls, href: str, id: str, images: List[Image], name: str, release_date: Union[datetime, int], release_date_precision: ReleaseDatePrecision, total_tracks: int, type: AlbumTypeEnum, uri: str) -> None:
        self.album_type = album_type
        self.artists = artists
        self.available_markets = available_markets
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.images = images
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.total_tracks = total_tracks
        self.type = type
        self.uri = uri


class ExternalIDS:
    isrc: str

    def __init__(self, isrc: str) -> None:
        self.isrc = isrc


class ItemType(Enum):
    TRACK = "track"


class Item:
    album: Album
    artists: List[Artist]
    available_markets: List[str]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIDS
    external_urls: ExternalUrls
    href: str
    id: str
    is_local: bool
    name: str
    popularity: int
    preview_url: str
    track_number: int
    type: ItemType
    uri: str

    def __init__(self, album: Album, artists: List[Artist], available_markets: List[str], disc_number: int, duration_ms: int, explicit: bool, external_ids: ExternalIDS, external_urls: ExternalUrls, href: str, id: str, is_local: bool, name: str, popularity: int, preview_url: str, track_number: int, type: ItemType, uri: str) -> None:
        self.album = album
        self.artists = artists
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.is_local = is_local
        self.name = name
        self.popularity = popularity
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = type
        self.uri = uri


class Tracks:
    href: str
    items: List[Item]
    limit: int
    next: str
    offset: int
    previous: None
    total: int

    def __init__(self, href: str, items: List[Item], limit: int, next: str, offset: int, previous: None, total: int) -> None:
        self.href = href
        self.items = items
        self.limit = limit
        self.next = next
        self.offset = offset
        self.previous = previous
        self.total = total


class ApiResponseModel:
    tracks: Tracks

    def __init__(self, tracks: Tracks) -> None:
        self.tracks = tracks