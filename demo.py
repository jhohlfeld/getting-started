import os
import io

import riseml.server
from PIL import Image

def transform(in_bytes):
  in_img = Image.open(io.BytesIO(in_bytes))
  out_img = in_img.rotate(180)
  out_bytes = io.BytesIO()
  out_img.save(out_bytes, 'JPEG')
  return out_bytes.getvalue()

riseml.server.serve(transform)
