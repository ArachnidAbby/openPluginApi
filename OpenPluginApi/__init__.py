import OpenPluginApi.async
import OpenPluginApi.ApiTemplates
import OpenPluginApi.PluginLoader
import OpenPluginApi.Schedule

def help():
    message = """
REQUIREMENTS:
  aiofiles
  asyncio
  aiohttp
OPA:
  ApiTemplates
  PluginLoader
  Schedule
"""
    print(message)
    return message