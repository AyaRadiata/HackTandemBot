from app.database.models import async_session
from app.database.models import User, Appointments
from sqlalchemy import select

async def set_user(tg_id: int, name, surname, number) -> None:
  async with async_session() as session:
    user = await session.scalar(select(User).where(User.tg_id == tg_id))

    if not user:
      session.add(User(tg_id=tg_id, name=name, surname=surname, number=number))
      await session.commit()

# async def get_categories():
#   async with async_session() as session:
#     return await session.scalars(select(Category))
  
# async def get_category_item(category_id):
#   async with async_session() as session:
#     return await session.scalars(select(Item).where(Item.category == category_id))

async def get_appointment_name(appointment_id):
  async with async_session() as session:
    return await session.scalars(select(Appointments.name).where(Appointments.id == appointment_id))
  
async def get_appointments_str():
  async with async_session() as session:
    return await session.scalars(select(Appointments))