import cv2
from sklearn.cluster import KMeans


def convert_rgb2hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_rgb_img(img_path):
    img = cv2.imread(img_path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return rgb_img


def get_color(img, numb_of_colors, shor_chart):
    clf = KMeans(n_clusters=numb_of_colors)
    labels = clf.fit_predict(modified_img)
    #
    counts = Counter(labels)
    center_colors = clf.cluster_centers_
    #
    ordered_colors = [center_colors[i] for i in counts.keys()]
    