class Timer:
    def __init__(self, get_delta_time: callable, target_time: float = 1, repeat: bool = True, trigger: callable = None):
        self.get_delta_time = get_delta_time
        self.trigger = trigger
        self.time = 0.0
        self.target_time = target_time
        self.repeat = repeat
        self.ended = False

    def start(self) -> None:
        """Reinicia el timer"""
        if self.ended:
            self.time = 0.0
            self.ended = False

    def update(self) -> bool:
        """Actualiza el timer, dispara trigger si corresponde"""
        if self.ended:
            return False

        self.time += self.get_delta_time()
        if self.time >= self.target_time:
            if self.trigger:
                self.trigger()

            if self.repeat:
                self.time -= self.target_time  # reinicia para el siguiente tick
            else:
                self.ended = True

            return True
        return False
