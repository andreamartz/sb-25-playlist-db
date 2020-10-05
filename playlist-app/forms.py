"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField("Playlist Name",
                       validators=[InputRequired(message="Playlist name cannot be blank.")])

    description = StringField("Playlist Description")


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField("Song Title",
                        validators=[InputRequired(message="Song title cannot be blank.")])

    artist = StringField("Artist", validators=[
                         InputRequired(message="Artist cannot be blank.")])

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
