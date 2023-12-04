from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper


def createTable(metadata):
    fund = Table(
        "fund",
        metadata,
        Column("id", String(255), primary_key=True),
        Column("name", String(255)),
        Column("start_year", String(255)),
        Column("nationality", String(255)),
        Column("alias", String(255), nullable=True),
        Column('manager_id', String(255), ForeignKey('manager.id'))
    )

    return fund
