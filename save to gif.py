import imageio

ims = [ ]
for i in range(1, 387):
    ims.append(imageio.imread('png/{}.png'.format(i)))

imageio.mimsave('life.gif', ims, duration=0.3)


# from PIL import Image

# gif = Image.open('png/1.png')
# ims = [ ]
# for i in range(1, 387):
#     ims.append(Image.open('png/{}.png'.format(i)))
# gif.save('life5.gif', save_all=True, append_images=ims, loop=1, duration=0.5)