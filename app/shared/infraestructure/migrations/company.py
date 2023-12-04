from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper


def createTable(metadata):
    company = Table(
        "company",
        metadata,
        Column("id", String(255), primary_key=True),
        Column("name", String(255), nullable=True)
    )

    return company
