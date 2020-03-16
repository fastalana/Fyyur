#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask_sqlalchemy import SQLAlchemy

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

db = SQLAlchemy(app)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
  __tablename__ = 'venues'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  address = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  genres = db.Column(db.String(120))
  website = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, nullable = False, default = False)
  seeking_description = db.Column(db.String(500))
  shows = db.relationship('Show', backref='Venue', lazy=True) #Show and Venue are the name of the model class, not the name of the table

  def __repr__(self):
    return f'<Venue Id: {self.id}, Name: {self.name}>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate - DONE

class Artist(db.Model):
  __tablename__ = 'artists'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  facebook_link = db.Column(db.String(120))
  website = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, nullable = False, default = False)
  seeking_description = db.Column(db.String(500))
  shows = db.relationship('Show', backref = 'Artist', lazy = True) #Show and Artist are the name of the model class, not the name of the table

    # TODO: implement any missing fields, as a database migration using Flask-Migrate - DONE

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration. - DONE
class Show(db.Model):
  __tablename__ = 'shows'

  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), primary_key = True) #venues is the table name, not the name of the class
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), primary_key = True) #artists is the table name, not the name of the class
  start_time = db.Column(db.String(120))