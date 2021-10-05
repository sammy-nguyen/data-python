
# strawberry = 0
# chocolate = 0
# vanilla = 0


# for line in open_file:
#   value = line.split(',')
#   quality = int(value[3])
#   price = float(value[4])
#   total = (quality * price)
#   if value[2] ==  "Strawberry":
#     strawberry = strawberry + total
#   if value[2] == "Chocolate":
#     chocolate = chocolate + total
#   if value[2] == "Vanilla":
#     vanilla = vanilla + total

# print(strawberry, chocolate, vanilla)



# cupcakes_type = ['Straberry','Chocolate','Vanilla']
# total_sale = [160, 267, 389]

# plt.bar(cupcakes_type, total_sale)
# plt.title('Total Sales of Cupcakes')
# plt.xlabel('Cupcake Types')
# plt.ylabel('Total Sales')
# plt.show()



import numpy as np
import matplotlib.pyplot as plt

y_axis = np.array([160, 267, 389])

x_labels = np.array(['Straberry','Chocolate','Vanilla'])

w = 3
nitems = len(y_axis)
x_axis = np.arange(0, nitems*w, w)    # set up a array of x-coordinates

fig, ax = plt.subplots(1)
ax.bar(x_axis, y_axis, width=w, align='center')
ax.set_xticks(x_axis);
ax.set_xticklabels(x_labels, rotation=90);
plt.show()
