from sqlalchemy import Table, Column, String, DateTime, func, JSON


def createTable(metadata):
    log = Table(
        "log",
        metadata,
        Column("id", String(255), primary_key=True, nullable=False),
        Column("data", JSON, primary_key=True, nullable=False),
        Column("created_at", DateTime, default=func.now())
    )

    return log
