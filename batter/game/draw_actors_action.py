from game.action import Action

class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller
    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """


    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """

        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """


        self._output_service.clear_screen()
        for i in cast.keys():
            actors = cast[i]
            self._output_service.draw_actors(actors)
        self._output_service.flush_buffer()