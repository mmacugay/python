class Television: 
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        self.status:bool = False
        self.muted:bool = False
        self.volume:int = Television.MIN_VOLUME
        self.channel:int = Television.MIN_CHANNEL

    def power(self):
        if self.status == False:
            self.status = True
        else: 
            self.status = False

    def mute(self):
        if self.muted == True:
            self.muted = False
        else: 
            self.muted = True

    def channel_up(self):
        if self.channel < Television.MAX_CHANNEL:
            self.channel += 1
        else:
            self.channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.channel > Television.MIN_CHANNEL:
            self.channel -= 1
        else:
            self.channel = Television.MAX_CHANNEL
        
    def volume_up(self):
        self.mute = False
        if self.volume < Television.MAX_VOLUME:
            self.volume += 1
    
    def volume_down(self):
        self.mute = False
        if self.volume > Television.MIN_VOLUME:
            self.volume -= 1

    def __str__(self):
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume if (self.muted) else Television.MIN_VOLUME}"