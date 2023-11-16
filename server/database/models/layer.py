from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, DateTime, ForeignKey, Float

from .base import Model

class Layer(Model):
    __tablename__ = "layers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source: Mapped[int] = mapped_column(Integer)
    start: Mapped[DateTime] = mapped_column(DateTime)
    end: Mapped[DateTime] = mapped_column(DateTime)
    cadence: Mapped[int] = mapped_column(Integer)
    scale: Mapped[float] = mapped_column(Float)
    scene_id = mapped_column(ForeignKey("scenes.id"))
    scene: Mapped["Scene"] = relationship(back_populates="layers")
    def __repr__(self) -> str:
        return f"Layer(scene={self.scene_id!r}, id={self.id!r}, source={self.source!r}, dates: {self.start!r} to {self.end!r})"

    settable = (
        'source',
        'start',
        'end',
        'cadence',
        'scale'
    )

class LayerData(BaseModel):
    id: Optional[int] = None
    scene_id: Optional[int] = None
    source: int
    start: datetime
    end: datetime
    cadence: int
    scale: float