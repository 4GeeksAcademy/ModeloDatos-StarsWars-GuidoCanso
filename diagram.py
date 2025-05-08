from eralchemy2 import render_er
from src.models import Base


render_er(Base, 'diagram.png')
