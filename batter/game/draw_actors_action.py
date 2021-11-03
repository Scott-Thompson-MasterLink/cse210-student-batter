from game.action import Action

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        self._output_service.clear_screen()
        for i in cast.keys():
            actors = cast[i]
            self._output_service.draw_actors(actors)
        self._output_service.flush_buffer()