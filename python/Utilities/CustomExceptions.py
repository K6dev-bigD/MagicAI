_author_ = 'kundan kumar'


class EmptyTweetsException(Exception):
   # Constructor or Initializer
   def __init__(self, message):
       self.message = "[SentiBoxException][EmptyTweetsException] : " + message

   def __str__(self):
       return self.message


class TweetException(Exception):
    # Constructor or Initializer
   def __init__(self, message):
       self.message = "[SentiBoxException][TweetException] : " + message

   def __str__(self):
       return self.message


class EmptyObjectException(Exception):
    # Constructor or Initializer
   def __init__(self, message):
       self.message = "[SentiBoxException][EmptyObjectException] : " + message

   def __str__(self):
       return self.message


class TypeMismatchException(Exception):
    # Constructor or Initializer
    def __init__(self, message):
        self.message = "[SentiBoxException][TypeMismatchException] : " + message

    def __str__(self):
        return self.message
