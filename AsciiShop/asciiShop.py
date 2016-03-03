import os
import time
import urllib3
import uuid
from PIL import Image
import math
import re


url = 'http://thecatapi.com/api/images/get'


def get_cat(directory=None, filename=None, format='png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile = os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()
    return savefile


class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image
        self.img = None         # Pillow var to hold image

    """
    @Description:
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location
    @Returns:
    """
    def get_image(self):
        """Gets a cat image
        :Description:
        Gets a random cat image and saves to file system. Uses get_time_stamp for naming of file.
        :param: none
        :return: none

        """

        self.name = self.get_time_stamp()
        get_cat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)

        self.width, self.height = self.img.size

    def save_image(self):
        pass

    def name_image(self):
        pass

    """
    Gets time stamp from local system
    """
    def get_time_stamp(self):
        """Gets time in seconds
        :description:
        Grabs current time in seconds from nuclear clock.
        :returns: current time in seconds

        """

        seconds, milli = str(time.time()).split('.')
        return seconds


"""
The ascii character set we use to replace pixels.
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""


class AsciiImage(RandomCat):

    def __init__(self, new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0

        self.asciiChars = ['#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None

        self.newImage = None
        self.grayScale = None

    def convert_to_gray_scale(self):
        if self.grayScale is None:
            if self.newWidth == "not_set":
                self.newWidth = self.width

            self.newHeight = int((self.height * self.newWidth) / self.width)

            if self.newWidth is None:
                self.newWidth = self.width
                self.newHeight = self.height

            self.newImage = self.img.resize((self.newWidth, self.newHeight))
            self.newImage = self.newImage.convert("L")  # convert to gray scale

    """
    Your comments here
    """
    def convert_to_ascii(self):
        """

        :return:
        :rtype:

        """
        self.convert_to_gray_scale()
        all_pixels = list(self.newImage.getdata())
        self.matrix = list_to_matrix(all_pixels,self.newWidth)

        for pixel_value in all_pixels:
            index = pixel_value // 25  # 0 - 10
            self.imageAsAscii.append(self.asciiChars[index])

    def print_image(self):
        self.imageAsAscii = ''.join(ch for ch in self.imageAsAscii)
        for c in range(0, len(self.imageAsAscii), self.newWidth):
            print(self.imageAsAscii[c:c+self.newWidth])
        print('')

    def scale_img(self, x, y):
        """
        :param x:
        :type x:
        :param y:
        :type y:
        :return:
        :rtype:
         :todo: make comments

        """

        rf = self.newHeight/y
        cf = self.newWidth/x

        #print(len(self.matrix[1]))

        tempmatrix = [[0 for foo in range(x)] for boo in range(y)]
        for i in range(y):
            for j in range(x):
                it1 = 0
                it2 = 0
                it3 = 0
                xoffest = j * cf
                yoffest = i * rf

                xfloor = math.floor(xoffest)
                yfloor = math.floor(yoffest)

                xceiling = xfloor + 1
                yceiling = yfloor + 1

                if xceiling >= self.newWidth:
                        xceiling = self.newHeight-1

                if yceiling >= self.newHeight:
                    yceiling = self.newHeight - 1

                it1 = ((xceiling - xoffest) * (self.matrix[yfloor][xceiling])) + ((xoffest - xfloor) * (
                    self.matrix[yfloor][xfloor]))
                it2 = ((xceiling - xoffest) * (self.matrix[yceiling][xceiling])) + ((xoffest - xfloor) * (
                    self.matrix[yceiling][xfloor]))
                it3 = ((yceiling - yoffest) * it1) + ((yoffest - yfloor) * it2)

                tempmatrix[i][j] = self.asciiChars[int(it3//25)]
                print(tempmatrix[i][j], end="")

            print("")
        print('')

    def flipit(self, direction):
        """

        :return:

 :rtype:
        """

        if direction == 'up':
            self.imageAsAscii = self.imageAsAscii[::-1]
            self.print_image()
            self.imageAsAscii = self.imageAsAscii[::-1]

        else:
            count = 0
            while count < 2:
                tempstring = ""
                retstring = []
                div = self.newWidth
                for x in range(self.newHeight):
                    tempstring = self.imageAsAscii[div-self.newWidth:div]

                    div += self.newWidth
                    retstring.append(tempstring[::-1])
                self.imageAsAscii = ''.join(retstring)
                if count == 0:
                    self.print_image()
                count += 1


def list_to_matrix(l, n):
    """
    Convert to 2D list of lists to help with manipulating the ascii image.
    Example:

        L = [0,1,2,3,4,5,6,7,8]

        L = to_matrix(L,3)

        L becomes:
        [[0,1,2],
        [3,4,5],
        [6,7,8]]

    """
    return [l[i:i+n] for i in range(0, len(l), n)]

if __name__ == '__main__':
    awesomeCat = AsciiImage(150)
    awesomeCat.get_image()

    awesomeCat.convert_to_ascii()
    awesomeCat.print_image()
    awesomeCat.scale_img(50, 20)
    awesomeCat.flipit('up')
