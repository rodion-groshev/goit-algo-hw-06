import networkx as nx
import matplotlib.pyplot as plt


def main_roads():
    roads = [("Lviv", "Rivne"), ("Rivne", "Zhytomyr"), ("Zhytomyr", "Kyiv"), ("Kyiv", "Uman"), ("Uman", "Odesa"),
             ("Kyiv", "Poltava"), ("Poltava", "Kharkiv"), ("Kharkiv", "Dnipro"), ("Dnipro", "Zaporizhzhya"),
             ("Dnipro", "Kryvyi Rih"), ("Kryvyi Rih", "Mykolayiv"), ("Mykolayiv", "Kherson"), ("Mykolayiv", "Odesa"),
             ("Uman", "Vinnytsya"), ("Vinnytsya", "Khmelnytskyi"), ("Khmelnytskyi", "Ternopil"), ("Ternopil", "Lviv")]

    pos = {
        "Uman": (0, 0), "Kyiv": (0.2, 2), "Odesa": (0.2, -2), "Poltava": (3, 1.7), "Kharkiv": (4, 2),
        "Dnipro": (3.5, 0),
        "Kryvyi Rih": (2.2, -0.8), "Mykolayiv": (1.5, -1.8), "Kherson": (2, -1.9), "Zaporizhzhya": (3.8, -0.5),
        "Vinnytsya": (-1.5, 0.5), "Khmelnytskyi": (-3, 0.7), "Ternopil": (-4, 0.8), "Lviv": (-5, 1), "Rivne": (-3.5, 2),
        "Zhytomyr": (-1.5, 1.7)
    }

    options = {
        "node_color": "yellow",
        "edge_color": "blue",
        "node_size": 500,
        "width": 3,
        "with_labels": True
    }

    G = nx.Graph()
    G.add_edges_from(roads)
    nx.draw(G, pos, **options)
    plt.title("Main roads of Ukraine")
    plt.show()

    num_nodes = G.number_of_nodes()
    print(f"Number of nodes {num_nodes}")

    num_edges = G.number_of_edges()
    print(f"Number of edges {num_edges}")

    return G


if __name__ == '__main__':
    main_roads()
