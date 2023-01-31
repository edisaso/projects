from PIL import Image, ImageSequence

# Output (max) size
size = 320, 240

# Open source
im = Image.open("masta.gif")

frames = ImageSequence.Iterator(im)

def thumbnails(frames):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.ANTIALIAS)
        yield thumbnail

frames = thumbnails(frames)

# Save output
om = next(frames) # Handle first frame separately
om.info = im.info # Copy sequence info
om.save("out.gif", save_all=True, append_images=list(frames))