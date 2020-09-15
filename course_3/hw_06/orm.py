import os
from contextlib import contextmanager

from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey,
    MetaData
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, validates

BASE_DIR = os.path.dirname(__file__)
engine = create_engine(
    f'sqlite:///orm.sqlite', echo=False, pool_recycle=7200
)
Base = declarative_base(metadata=MetaData(bind=engine))
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Database connection context manager."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    goods = relationship('Good', back_populates='category')

    def __repr__(self):
        return f'Category - {self.name}'


class Unit(Base):
    __tablename__ = 'units'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    goods = relationship('Good', back_populates='unit')

    def __repr__(self):
        return f'Unit - {self.name}'


class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    employees = relationship('Employee', back_populates='position')

    def __repr__(self):
        return f'Position - {self.name}'


class Good(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    unit_id = Column(Integer, ForeignKey('units.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    unit = relationship('Unit', back_populates='goods')
    category = relationship('Category', back_populates='goods')

    def __repr__(self):
        return f'Good - {self.name}'


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    position_id = Column(Integer, ForeignKey('positions.id'), nullable=False)

    position = relationship('Position', back_populates='employees')

    def __repr__(self):
        return f'Employee - {self.fullname}'


class Vendor(Base):
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    ownerchipform = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

    @validates('email')
    def validate_email(self, key, vendors):
        assert '@' in vendors
        return vendors

    def __repr__(self):
        return f'Vendor - {self.name}'


if __name__ == '__main__':
    Base.metadata.create_all(engine, checkfirst=True)

    with session_scope() as session:
        unit = Unit(name='pc.')
        category = Category(
            name='fruits',
            description='good fruits'
        )

        session.add(unit)
        session.add(category)

        good = Good(
            name='good#1',
            unit=unit,
            category=category
        )
        session.add(good)

        print('unit:', unit)
        print('category:', category)
        print('good:', good)
        print('good.unit:', good.unit)
        print('good.category:', good.category)
        print('unit.goods:', unit.goods)
        print('category.goods:', category.goods)
