"""Run river simulation"""

__author__ = "730766896"
from ex07.river import River

my_river: River = River(10, 2)
my_river.view_river()
my_river.one_river_week()
