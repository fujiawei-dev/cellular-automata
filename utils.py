import imageio


def synthetic_gif(num):
    ims = []
    for i in range(1, num+1):
        ims.append(imageio.imread('png/{}.png'.format(i)))
    imageio.mimsave('life.gif', ims, duration=0.3)


if __name__ == '__main__':
    synthetic_gif(2063)