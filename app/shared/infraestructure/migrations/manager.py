from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper


def createTable(metadata):
    manager = Table(
        "manager",
        metadata,
        Column("id", String(255), primary_key=True),
        Column("name", String(255), nullable=True)
    )

    return manager
