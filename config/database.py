import os
from sqlalchemy import orm, create_engine
from app.shared.infraestructure.migrations.company import createTable as createCompanyTable
from app.shared.infraestructure.migrations.manager import createTable as createManagerTable
from app.shared.infraestructure.migrations.fund import createTable as createFundTable
from app.shared.infraestructure.migrations.log import createTable as createLogTable
from app.shared.infraestructure.migrations.company_fund import createTable as createCompanyFundTable
from app.shared.domain.models.company import Company
from app.shared.domain.models.manager import Manager
from app.shared.domain.models.fund import Fund
from app.shared.domain.models.log import Log


registry = orm.registry()


def start_mappers():
    db_manager = createManagerTable(registry.metadata)
    db_fund = createFundTable(registry.metadata)
    db_log = createLogTable(registry.metadata)
    db_company = createCompanyTable(registry.metadata)
    db_company_fund = createCompanyFundTable(registry.metadata)

    registry.map_imperatively(Company, db_company, properties={
        'funds': orm.relationship(Fund, secondary=db_company_fund, back_populates='companies', order_by=db_fund.c.id)
    })

    registry.map_imperatively(Manager, db_manager, properties={
        'funds': orm.relationship(Fund, backref='manager', order_by=db_fund.c.id)
    })

    registry.map_imperatively(Fund, db_fund, properties={
        'companies': orm.relationship(Company, secondary=db_company_fund, back_populates='funds', order_by=db_company.c.id)
    })

    registry.map_imperatively(Log, db_log)

    return registry.metadata


def get_session():
    engine = create_engine(os.environ.get("DATABASE_URL"))
    session = orm.sessionmaker(bind=engine)
    return session()
