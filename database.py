from os import path

from sqlalchemy import (create_engine,
                        Column,
                        String,
                        Integer,
                        Boolean,
                        Table,
                        ForeignKey)

from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

database_filename = 'twitter.sqlites3'

directory = path.abspath(path.dirname(__file__))
database_filepath = path.join(directory, database_filename)

engine_url = 'sqlite:///{}'.format(database_filepath)

engine = create_engine(engine_url)

# Out database class object are going to inherite form this class
Base = declarative_base(bind=engine)

# create a configured 'session' class
Session = sessionmaker(bind=engine, autoflush=False)

#  create a session
session = Sessioin()




hashtag_tweet = Table('hashtag_tweet', Base.metadata,
            Column('hashtag_id', Integer, ForeignKey('hastags.id'), nullable=False),
            Column('tweet_id', Integer, ForeignKey('tweets.id'), nullable=False))

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    tid = Column(String(100), nullable=False)
    tweet = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    coordinates = Column(String(50), nullable=True)
    user = relationship('User', backref='tweets')
    created_at = Column(String(100), nullable=False)
    favorite_count = Column(Integer)
    in_reply_to_screen_name = Column(String)
    in_reply_to_status_id = Column(Integer)
    lang = Column(String)
    quoted_status_id = Column(Integer)
    retweet_count = Column(Integer)
    source = Column(String)
    is_retweet = Column(Boolean)
    hashtags = relationship('Hashtag',
                            secondary='hastag_tweet',
                            back_populates='tweets')

    def __repr__(self):
        return '<Tweet {}>'.format(self.id)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    uid = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    screen_name = Column(String)
    #nullable
    description = Column(String)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    statuses_count = Column(Integer)
    favorite_count = Column(Integer)
    listed_count = Column(Integer)
    geo_enabled = Column(Boolean)
    lang = Column(String)

    def __repr__(self):
        return '<USer {}>'.format(self.id)

class Hastag(Base):
    __tablename__ = 'hastags'
    id = Column(Integer, primary_key=True)
    text = Column(String(200), nullable=False)
    tweets = relationship('Tweet',
                           secondary='hastag_tweet',
                           back_populates='hashtags')

    def __repr__(self):
        return '<Hastag {}>'.format(self.text)
