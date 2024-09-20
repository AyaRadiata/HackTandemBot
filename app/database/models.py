from sqlalchemy import BigInteger, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
  pass

class User(Base):
  __tablename__ = 'users'

  id: Mapped[int] = mapped_column(primary_key=True)
  tg_id = mapped_column(BigInteger)
  name: Mapped[str] = mapped_column(String(25))
  surname: Mapped[str] = mapped_column(String(25))
  number: Mapped[str] = mapped_column(String(20))

class Appointments(Base):
  __tablename__ = 'appointments'

  id: Mapped[int] = mapped_column(primary_key=True)
  date: Mapped[str] = mapped_column(String(5))
  booked: Mapped[int] = mapped_column(Integer())


async def async_main():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)