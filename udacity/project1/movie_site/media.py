
class Video:
  def __init__(self, title, description, image):
    self.title = title
    self.storyline = description
    self.poster_image_url = image

class Movie(Video):
  """Movie is an object which extends Video

     Attributes:
      title(str): title from Video
      storyline(str): plot from Video
      image url(str): image url to use, from Video
      youtube url(str): url to use for bootstrap video modal
  """
  def __init__(self, title, description, image, link):
    Video.__init__(self, title, description, image)
    self.trailer_youtube_url = link
