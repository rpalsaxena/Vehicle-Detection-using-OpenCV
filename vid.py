import glob, os
from moviepy.editor import ImageSequenceClip
vid_imgs = glob.glob('proc_vid/*.jpg')
files = []
for i in range(len(vid_imgs)):
    files.append('proc_vid/'+str(i)+'.jpg')
	
outvid = "abc.mp4"
images = files
fps = 5
clip = ImageSequenceClip(images, fps = fps)
clip.write_videofile(outvid)