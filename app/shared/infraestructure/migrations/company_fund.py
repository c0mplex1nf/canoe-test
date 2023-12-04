from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper


def createTable(metadata):
    company_fund = Table(
        "company_fund",
        metadata,
        Column('company_id', String(255), ForeignKey('company.id')),
        Column('fund_id', String(255), ForeignKey('fund.id'))
    )

    return company_fund
