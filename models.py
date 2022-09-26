import peewee


db = peewee.SqliteDatabase('music_app_data.sqlite3')


class Artist(peewee.Model):
    name = peewee.CharField()
    pseudonim = peewee.CharField()

    class Meta:
        database = db


class Music(peewee.Model):
    name = peewee.CharField()
    duration = peewee.FloatField()
    author = peewee.ForeignKeyField(Artist)

    class Meta:
        database = db


if __name__ == '__main__':
    db.create_tables([Artist, Music])
