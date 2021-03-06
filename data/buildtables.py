from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime


class BuildTables:
    def __init__(self, metadata):
        self._metadata = metadata
        self._build_tables()

    def _build_tables(self):
        Table(
            'logs', self._metadata,
            Column('id', Integer, primary_key=True),
            Column('timestamp', DateTime),
            Column('text', String(500))
        )
        Table(
            'triggers', self._metadata,
            Column('id', Integer, primary_key=True),
            Column('parent_id', Integer, nullable=False),
            Column('is_group', Boolean),
            Column('name', String(250)),
            Column('search_text', String(500)),
            Column('alert_text', String(500)),
            Column('use_audio', Boolean),
            Column('audio_file', String(50))
        )



