# 
from echo.src.echo import (
  _tick_
)

#
from aiohttp import web

#
app_tick = web.Application()

#
app_tick.add_routes([

  web.get('/',   _tick_),
  
])
