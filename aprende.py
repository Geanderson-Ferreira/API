from sqlalchemy import Column, Integer, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, index=True)
    image_data = Column(LargeBinary)

from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/upload/")
async def upload_image(image: UploadFile):
    # Aqui você pode salvar a imagem no banco de dados usando SQLAlchemy
    # image.file contém os dados binários da imagem
    return {"filename": image.filename}


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Substitua pelo seu URL do banco de dados
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def save_image(image_data):
    db_image = Image(image_data=image_data)
    db = SessionLocal()
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    db.close()

@app.post("/upload/")
async def upload_image(image: UploadFile):
    image_data = image.file.read()
    save_image(image_data)
    return {"filename": image.filename}
