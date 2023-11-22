from PIL import Image
from itertools import product
import os
import numpy as np

WHITE=(255, 255, 255, 255)

def tile(filename, dir_in, dir_out, d):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)

colors = []
# tile('IMG_0186.PNG', '/Users/dkullas/Documents/Python_Scripts/Game Pics', '/Users/dkullas/Documents/Python_Scripts/Game Pics/pics', 20)

directory = 'pics'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        img = Image.open(f)

        tes =img.load()
        for i in range(img.size[0]): # for every pixel:
            for j in range(img.size[1]):
                print(tes[i,j])
                if tes[i,j] != (255, 255, 255, 255):
                    # change to black if not white
                    tes[i,j] = (0, 0 ,0, 255)
        img.save("my.png")
        # for ea in tes:
        #     print(ea[0])


        # image = Image.open("test.png")
        # count=0
        # input_array = np.asarray(img)
        # for l1 in input_array:
        #     for l2 in l1:
        #         for l3 in l2:
        #             if(count==3):
        #                 count=0
        #             else:
        #                 l3 = 0
        #                 print(l3)
        #                 count+=1
        # print(input_array)

# output_array = do_my_stuff(input_array)

# output_image = Image.fromarray(np.uint8(output_array))
# output_image.save("test_result.png")
        exit()
#         tmp = img.getcolors(100)
#         # print(tmp[0][1][0])

#         # if(tmp):
#         tlist = []
        
#         tlist.append(tmp[0][1][0])
#         tlist.append(tmp[0][1][1])
#         tlist.append(tmp[0][1][2])

#         colors.append(tlist)
        
# print(len(colors))

# grid = []
# for x in range(96):
#     help = []
#     for y in range(96):
#         help.append(colors[x*96+y])
#     grid.append(help)

# change = []
# for x in range(len(grid)):
#     for y in range(len(grid[0])):        
#         if(grid[x][y] == WHITE):
#             if(y>1):
#                 # Check Left
#                 if(grid[x][y-1] == WHITE and grid[x][y-2] == WHITE):
#                     change.append([x,y])

#             if(y<94):
#                 # Check Right
#                 if(grid[x][y+1] == WHITE and grid[x][y+2] == WHITE):
#                     change.append([x,y])
#             if(x>1):
#                 # Check Up
#                 if(grid[x-1][y] == WHITE and grid[x-2][y] == WHITE):
#                     change.append([x,y])
#             if(x<94):
#                 # Check Down
#                 if(grid[x+1][y] == WHITE and grid[x+2][y] == WHITE):
#                     change.append([x,y])


# for block in change:
#     grid[block[0]][block[1]] = [0, 0, 0]

# print(grid)



# list1 = np.array(grid).reshape(-1, 3)

# np.array(list1).reshape(96, 96, 3)

# img = Image.fromarray(list1, "I")
# img.save("my.png")